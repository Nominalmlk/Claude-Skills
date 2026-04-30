#!/usr/bin/env python3
"""
Readability analyzer: Flesch Reading Ease, Flesch-Kincaid Grade Level,
sentence length, passive voice ratio, and composite grade (A-F).
"""

import argparse
import json
import re
import sys


# ---------------------------------------------------------------------------
# Syllable counting (pure stdlib, no ML)
# ---------------------------------------------------------------------------

def count_syllables(word: str) -> int:
    word = word.lower().strip(".,!?;:\"'()-")
    if not word:
        return 0
    # Special short words
    if len(word) <= 3:
        return 1

    # Remove silent trailing e
    word = re.sub(r"(?<=[^aeiou])e$", "", word)

    # Count vowel groups
    count = len(re.findall(r"[aeiouy]+", word))
    return max(1, count)


# ---------------------------------------------------------------------------
# Text segmentation
# ---------------------------------------------------------------------------

SENTENCE_END = re.compile(r"[.!?]+")
WORD_RE = re.compile(r"\b[a-zA-Z']+\b")
PASSIVE_PATTERNS = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+\w+ed\b",
    re.IGNORECASE,
)


def tokenize_sentences(text: str) -> list[str]:
    raw = SENTENCE_END.split(text)
    return [s.strip() for s in raw if s.strip()]


def tokenize_words(text: str) -> list[str]:
    return WORD_RE.findall(text)


# ---------------------------------------------------------------------------
# Readability formulas
# ---------------------------------------------------------------------------

def flesch_reading_ease(words: list[str], sentences: list[str]) -> float:
    """Higher = easier. 60-70 is plain English."""
    if not sentences or not words:
        return 0.0
    asl = len(words) / len(sentences)  # average sentence length
    asw = sum(count_syllables(w) for w in words) / len(words)  # avg syllables/word
    return 206.835 - 1.015 * asl - 84.6 * asw


def flesch_kincaid_grade(words: list[str], sentences: list[str]) -> float:
    """US grade level required to understand the text. Target ≤8."""
    if not sentences or not words:
        return 0.0
    asl = len(words) / len(sentences)
    asw = sum(count_syllables(w) for w in words) / len(words)
    return 0.39 * asl + 11.8 * asw - 15.59


def passive_voice_ratio(sentences: list[str]) -> float:
    """Fraction of sentences containing a passive construction."""
    if not sentences:
        return 0.0
    passive_count = sum(1 for s in sentences if PASSIVE_PATTERNS.search(s))
    return passive_count / len(sentences)


def avg_sentence_length(words: list[str], sentences: list[str]) -> float:
    if not sentences:
        return 0.0
    return len(words) / len(sentences)


# ---------------------------------------------------------------------------
# Jargon density (lightweight — full scan in jargon_detector.py)
# ---------------------------------------------------------------------------

COMMON_JARGON = {
    "leverage", "utilize", "synergy", "synergies", "paradigm", "robust",
    "scalable", "ecosystem", "bandwidth", "ideate", "actionable",
    "stakeholder", "deliverable", "onboard", "sunset", "iterate",
    "surface", "unpack", "evangelize", "frictionless", "seamless",
    "boilerplate", "granular", "holistic", "proactive", "reactive",
    "agile", "pivot", "disrupt", "disruptive", "innovation",
    "bleeding-edge", "cutting-edge", "best-in-class", "world-class",
    "thought-leader", "thought-leadership", "empower", "empowering",
    "streamline", "streamlined", "optimize", "optimization",
    "visibility", "transparency", "alignment", "deep-dive",
}


def jargon_density(words: list[str]) -> float:
    if not words:
        return 0.0
    hits = sum(1 for w in words if w.lower() in COMMON_JARGON)
    return hits / len(words)


# ---------------------------------------------------------------------------
# Composite grade
# ---------------------------------------------------------------------------

def composite_grade(fre: float, fk: float, passive: float, jargon: float) -> tuple[str, int]:
    score = 100

    # Flesch Reading Ease: ideal 60-70
    if fre >= 70:
        score -= 0
    elif fre >= 60:
        score -= 5
    elif fre >= 50:
        score -= 15
    elif fre >= 40:
        score -= 25
    else:
        score -= 40

    # FK grade: ideal ≤8
    if fk <= 8:
        score -= 0
    elif fk <= 10:
        score -= 10
    elif fk <= 12:
        score -= 20
    else:
        score -= 30

    # Passive voice: ideal ≤10%
    if passive <= 0.10:
        score -= 0
    elif passive <= 0.20:
        score -= 5
    else:
        score -= 15

    # Jargon density: ideal ≤2%
    if jargon <= 0.02:
        score -= 0
    elif jargon <= 0.05:
        score -= 5
    else:
        score -= 15

    score = max(0, min(100, score))

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 45:
        grade = "D"
    else:
        grade = "F"

    return grade, score


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyze(text: str) -> dict:
    sentences = tokenize_sentences(text)
    words = tokenize_words(text)

    fre = flesch_reading_ease(words, sentences)
    fk = flesch_kincaid_grade(words, sentences)
    passive = passive_voice_ratio(sentences)
    jargon = jargon_density(words)
    asl = avg_sentence_length(words, sentences)
    grade, score = composite_grade(fre, fk, passive, jargon)

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(asl, 1),
        "flesch_reading_ease": round(fre, 1),
        "flesch_kincaid_grade": round(fk, 1),
        "passive_voice_ratio": round(passive * 100, 1),
        "jargon_density": round(jargon * 100, 1),
        "composite_score": score,
        "grade": grade,
    }


def human_report(result: dict) -> str:
    grade = result["grade"]
    grade_labels = {
        "A": "Anyone can read it. Caveman approved.",
        "B": "Clear with minor rough patches.",
        "C": "Readable but dense in places.",
        "D": "Needs work. Many readers will struggle.",
        "F": "Jargon swamp. Rewrite required.",
    }

    fre = result["flesch_reading_ease"]
    fre_label = (
        "Very easy" if fre >= 80 else
        "Easy" if fre >= 70 else
        "Plain English" if fre >= 60 else
        "Fairly difficult" if fre >= 50 else
        "Difficult" if fre >= 30 else
        "Very difficult"
    )

    lines = [
        "=" * 52,
        f"  READABILITY REPORT",
        "=" * 52,
        f"  Words            : {result['word_count']}",
        f"  Sentences         : {result['sentence_count']}",
        f"  Avg sentence len  : {result['avg_sentence_length']} words  (target ≤20)",
        f"  Flesch Ease       : {result['flesch_reading_ease']}  ({fre_label})  (target 60-70)",
        f"  FK Grade Level    : {result['flesch_kincaid_grade']}  (target ≤8)",
        f"  Passive voice     : {result['passive_voice_ratio']}%  (target ≤10%)",
        f"  Jargon density    : {result['jargon_density']}%  (target ≤2%)",
        "-" * 52,
        f"  Grade  : {grade}  ({result['composite_score']}/100)",
        f"  Verdict: {grade_labels.get(grade, '')}",
        "=" * 52,
    ]

    # Improvement hints
    hints = []
    if result["avg_sentence_length"] > 20:
        hints.append(f"  • Break long sentences (avg {result['avg_sentence_length']} words, target ≤20)")
    if result["flesch_reading_ease"] < 60:
        hints.append("  • Shorter words + shorter sentences raise the Flesch score")
    if result["flesch_kincaid_grade"] > 8:
        hints.append(f"  • Text reads at grade {result['flesch_kincaid_grade']}; aim for grade 8 or below")
    if result["passive_voice_ratio"] > 10:
        hints.append(f"  • {result['passive_voice_ratio']}% passive voice — flip sentences to active")
    if result["jargon_density"] > 2:
        hints.append(f"  • {result['jargon_density']}% jargon — run /caveman:smash to replace flagged terms")

    if hints:
        lines.append("\n  Suggestions:")
        lines.extend(hints)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Readability analyzer — score any text for plain-language compliance."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="-",
        help="File to analyze, or '-' to read from stdin (default: stdin)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON metrics instead of the human report",
    )
    args = parser.parse_args()

    if args.file == "-":
        text = sys.stdin.read()
    else:
        try:
            with open(args.file, encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    if not text.strip():
        print("Error: no text to analyze.", file=sys.stderr)
        sys.exit(1)

    result = analyze(text)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(human_report(result))


if __name__ == "__main__":
    main()
