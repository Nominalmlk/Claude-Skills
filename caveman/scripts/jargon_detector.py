#!/usr/bin/env python3
"""
Jargon detector — scans text for corporate/tech buzzwords and suggests
plain replacements. Outputs a hit list with line numbers, severity, and
optionally rewrites the document with all replacements applied.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict


# ---------------------------------------------------------------------------
# Jargon dictionary: (pattern, plain replacement, severity)
# severity: HIGH = blocks comprehension, MEDIUM = slows reading, LOW = style
# ---------------------------------------------------------------------------

JARGON_MAP: list[tuple[str, str, str]] = [
    # Business / corporate speak
    ("leverage",             "use",                        "HIGH"),
    ("leveraging",           "using",                      "HIGH"),
    ("leveraged",            "used",                       "HIGH"),
    ("utilize",              "use",                        "HIGH"),
    ("utilizing",            "using",                      "HIGH"),
    ("utilized",             "used",                       "HIGH"),
    ("synergy",              "working together",           "HIGH"),
    ("synergies",            "combined benefits",          "HIGH"),
    ("paradigm shift",       "big change",                 "HIGH"),
    ("paradigm",             "model / approach",           "MEDIUM"),
    ("ideate",               "think of ideas",             "HIGH"),
    ("ideation",             "brainstorming",              "HIGH"),
    ("evangelize",           "promote / champion",         "MEDIUM"),
    ("socialize the idea",   "share the idea",             "MEDIUM"),
    ("socialize",            "share / discuss",            "MEDIUM"),
    ("actionable",           "useful / doable",            "MEDIUM"),
    ("stakeholder",          "person involved",            "MEDIUM"),
    ("deliverable",          "output / result",            "MEDIUM"),
    ("onboard",              "set up / train",             "MEDIUM"),
    ("offboard",             "remove / exit",              "MEDIUM"),
    ("sunset",               "retire / shut down",         "MEDIUM"),
    ("iterate",              "improve step by step",       "LOW"),
    ("iteration",            "version / step",             "LOW"),
    ("surface",              "bring up / show",            "MEDIUM"),
    ("unpack",               "explain",                    "MEDIUM"),
    ("deep.?dive",           "close look / detailed look", "MEDIUM"),
    ("boil the ocean",       "try to do everything",       "HIGH"),
    ("move the needle",      "make a difference",          "MEDIUM"),
    ("low.?hanging fruit",   "easy win",                   "MEDIUM"),
    ("ping",                 "message / contact",          "LOW"),
    ("circle back",          "follow up",                  "MEDIUM"),
    ("touch base",           "check in",                   "MEDIUM"),
    ("at the end of the day","ultimately",                  "LOW"),
    ("going forward",        "from now on",                "LOW"),
    ("bandwidth",            "time / capacity",            "HIGH"),
    ("alignment",            "agreement",                  "MEDIUM"),
    ("visibility",           "awareness / view",           "MEDIUM"),
    ("transparency",         "openness",                   "LOW"),
    ("proactive",            "acting early",               "LOW"),
    ("holistic",             "complete / whole",           "MEDIUM"),
    ("granular",             "detailed",                   "MEDIUM"),
    ("robust",               "strong / reliable",          "MEDIUM"),
    ("scalable",             "grows easily",               "MEDIUM"),
    ("ecosystem",            "system / community",         "MEDIUM"),
    ("streamline",           "simplify / speed up",        "LOW"),
    ("optimize",             "improve",                    "LOW"),
    ("optimization",         "improvement",                "LOW"),
    ("empower",              "give power to / enable",     "LOW"),
    ("disruptive",           "game-changing",              "LOW"),
    ("innovation",           "new idea / improvement",     "LOW"),
    ("cutting.?edge",        "latest / modern",            "LOW"),
    ("bleeding.?edge",       "very new / experimental",    "LOW"),
    ("best.?in.?class",      "top / excellent",            "LOW"),
    ("world.?class",         "excellent",                  "LOW"),
    ("thought.?leader",      "expert",                     "MEDIUM"),
    ("thought.?leadership",  "expertise",                  "MEDIUM"),
    ("pivot",                "change direction",           "MEDIUM"),
    # Tech jargon
    ("boilerplate",          "standard template code",     "MEDIUM"),
    ("scaffolding",          "starter / template",         "MEDIUM"),
    ("refactor",             "restructure the code",       "MEDIUM"),
    ("abstraction",          "simplified layer",           "MEDIUM"),
    ("microservice",         "small independent service",  "MEDIUM"),
    ("monolith",             "single large codebase",      "MEDIUM"),
    ("containerize",         "package in a container",     "MEDIUM"),
    ("orchestrate",          "coordinate / manage",        "MEDIUM"),
    ("idempotent",           "safe to repeat",             "HIGH"),
    ("asynchronous",         "non-blocking / background",  "MEDIUM"),
    ("synchronous",          "step-by-step / blocking",    "MEDIUM"),
    ("deprecated",           "old / no longer supported",  "MEDIUM"),
    ("regression",           "newly broken feature",       "MEDIUM"),
    ("refactoring",          "restructuring the code",     "MEDIUM"),
    ("technical debt",       "shortcuts that cost later",  "MEDIUM"),
    ("legacy",               "old / outdated",             "LOW"),
]

# Pre-compile patterns for speed
COMPILED: list[tuple[re.Pattern, str, str, str]] = [
    (re.compile(r"\b" + pattern + r"\b", re.IGNORECASE), pattern, replacement, severity)
    for pattern, replacement, severity in JARGON_MAP
]


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class JargonHit:
    line_number: int
    column: int
    matched_text: str
    replacement: str
    severity: str
    context: str


# ---------------------------------------------------------------------------
# Scanner
# ---------------------------------------------------------------------------

def scan(text: str) -> list[JargonHit]:
    hits: list[JargonHit] = []
    lines = text.splitlines()

    for line_num, line in enumerate(lines, start=1):
        for compiled_re, _pattern, replacement, severity in COMPILED:
            for match in compiled_re.finditer(line):
                # 40-char context window around the match
                start = max(0, match.start() - 20)
                end = min(len(line), match.end() + 20)
                snippet = line[start:end].strip()
                hits.append(JargonHit(
                    line_number=line_num,
                    column=match.start() + 1,
                    matched_text=match.group(),
                    replacement=replacement,
                    severity=severity,
                    context=f"...{snippet}...",
                ))

    # Sort: HIGH first, then MEDIUM, then LOW, then by line number
    severity_order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    hits.sort(key=lambda h: (severity_order.get(h.severity, 9), h.line_number))
    return hits


# ---------------------------------------------------------------------------
# Auto-replace
# ---------------------------------------------------------------------------

def apply_replacements(text: str) -> tuple[str, int]:
    count = 0
    for compiled_re, _pattern, replacement, _severity in COMPILED:
        new_text, n = compiled_re.subn(replacement, text)
        count += n
        text = new_text
    return text, count


# ---------------------------------------------------------------------------
# Density calculation
# ---------------------------------------------------------------------------

def jargon_density(text: str, hits: list[JargonHit]) -> float:
    words = re.findall(r"\b[a-zA-Z']+\b", text)
    if not words:
        return 0.0
    return len(hits) / len(words) * 100


# ---------------------------------------------------------------------------
# Human report
# ---------------------------------------------------------------------------

SEVERITY_COLORS = {"HIGH": "!!!", "MEDIUM": " ! ", "LOW": "   "}


def human_report(hits: list[JargonHit], text: str, filename: str) -> str:
    density = jargon_density(text, hits)
    lines = [
        "=" * 60,
        f"  JARGON SCAN: {filename}",
        "=" * 60,
        f"  Hits found     : {len(hits)}",
        f"  Jargon density : {density:.1f}%  (target ≤2%)",
        f"  HIGH severity  : {sum(1 for h in hits if h.severity == 'HIGH')}",
        f"  MEDIUM severity: {sum(1 for h in hits if h.severity == 'MEDIUM')}",
        f"  LOW severity   : {sum(1 for h in hits if h.severity == 'LOW')}",
        "-" * 60,
    ]

    if not hits:
        lines.append("  No jargon detected. Caveman approves.")
    else:
        lines.append(f"  {'SEV':5}  {'LINE':5}  {'COL':4}  {'FOUND':25}  REPLACE WITH")
        lines.append(f"  {'-'*5}  {'-'*5}  {'-'*4}  {'-'*25}  {'-'*20}")
        for h in hits:
            sev_icon = SEVERITY_COLORS.get(h.severity, "   ")
            found = h.matched_text[:25]
            replace = h.replacement[:30]
            lines.append(f"  [{sev_icon}]  {h.line_number:5}  {h.column:4}  {found:<25}  → {replace}")

    lines.append("=" * 60)

    if density > 2:
        lines.append("\n  Run with --auto to replace all jargon automatically.")
        lines.append("  Run /caveman:simplify for a full plain-language rewrite.")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Jargon detector — find and replace corporate/tech buzzwords."
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="-",
        help="File to scan, or '-' to read from stdin (default: stdin)",
    )
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Automatically replace all jargon and print the cleaned text",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        help="Write the cleaned text to this file (requires --auto)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON hit list instead of the human report",
    )
    parser.add_argument(
        "--severity",
        choices=["HIGH", "MEDIUM", "LOW"],
        help="Only report hits at or above this severity level",
    )
    args = parser.parse_args()

    # Read input
    if args.file == "-":
        text = sys.stdin.read()
        filename = "<stdin>"
    else:
        try:
            with open(args.file, encoding="utf-8") as f:
                text = f.read()
            filename = args.file
        except FileNotFoundError:
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    if not text.strip():
        print("Error: no text to scan.", file=sys.stderr)
        sys.exit(1)

    hits = scan(text)

    # Filter by severity if requested
    if args.severity:
        order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
        cutoff = order[args.severity]
        hits = [h for h in hits if order[h.severity] <= cutoff]

    # Auto-replace mode
    if args.auto:
        cleaned, count = apply_replacements(text)
        print(f"Replaced {count} jargon term(s).", file=sys.stderr)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(cleaned)
            print(f"Saved to: {args.output}", file=sys.stderr)
        else:
            print(cleaned)
        return

    # Report mode
    if args.json:
        print(json.dumps([asdict(h) for h in hits], indent=2))
    else:
        print(human_report(hits, text, filename))


if __name__ == "__main__":
    main()
