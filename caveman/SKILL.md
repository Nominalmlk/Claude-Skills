---
name: "caveman"
description: "Caveman communication skill — simplify complex technical language, crush jargon, and explain any concept in plain primitive terms. Use when: user wants complex docs or code explained simply, jargon removed from writing, concepts broken to first principles, or dense technical text made readable by anyone. Covers readability analysis, jargon detection, plain-language rewriting, and ELI5 explanations."
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: communication
  updated: 2026-04-30
---

# Caveman

> Ugg. Big words bad. Simple words good. Me explain.

Strip technical jargon, crush complexity, and make any concept understandable to anyone — from a five-year-old to a non-technical executive. Not a dumbing-down tool — a clarity tool. The goal is precision without pretension.

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/caveman:simplify` | Rewrite any text in plain language, cutting jargon and shortening sentences |
| `/caveman:explain` | Explain a concept, code block, or error as if the reader has never heard of it |
| `/caveman:smash` | Scan a document for jargon and replace every instance with a plain alternative |
| `/caveman:score` | Run a readability audit and score any text or file |

---

## When This Skill Activates

Recognize these patterns from the user:

- "Explain this like I'm five"
- "Make this simpler"
- "Remove the jargon from this"
- "What does this code actually do?"
- "Can you translate this error message?"
- "My non-technical team can't understand this doc"
- "Rewrite this in plain English"
- "What does [acronym/buzzword] even mean?"
- Any request containing: ELI5, plain English, dumb it down, simplify, jargon, buzzwords, readable

---

## Workflow

### `/caveman:simplify` — Plain Language Rewrite

1. **Analyze the input**
   - Identify the target audience (default: non-technical adult)
   - Scan for jargon density using `scripts/jargon_detector.py`
   - Measure readability score using `scripts/complexity_crusher.py`

2. **Apply the Plain Language Checklist**

   ```
   SENTENCES
   ├── Max 20 words per sentence (break longer ones)
   ├── One idea per sentence
   ├── Active voice over passive ("We built X" not "X was built")
   └── No nominalization ("utilize" → "use", "implementation" → "build")

   WORDS
   ├── Replace every jargon term with the simplest synonym
   ├── Spell out acronyms on first use
   ├── Delete filler words (leverage, synergy, paradigm, robust, scalable)
   ├── Replace Latin ("i.e.", "e.g.") with English ("that is", "for example")
   └── Numbers: spell out one through nine, use digits for 10+

   STRUCTURE
   ├── Lead with the main point (inverted pyramid)
   ├── Use bullet points for lists of 3+ items
   ├── Add a one-sentence summary at the top
   └── Remove any sentence that doesn't add information
   ```

3. **Output format**
   - Show: original → simplified side-by-side for short inputs
   - For documents: show full rewrite with change summary
   - Include readability score before/after

---

### `/caveman:explain` — Concept Explanation

Use this three-layer explanation framework:

```
LAYER 1 — THE TODDLER VERSION (1-2 sentences, no jargon at all)
  Explain using only concepts a 5-year-old knows: food, toys, houses, animals.

LAYER 2 — THE ADULT VERSION (3-5 sentences, minimal jargon)
  Explain using everyday analogies. One concrete example.

LAYER 3 — THE PRACTITIONER VERSION (technical detail, jargon defined inline)
  Full explanation for someone learning the field. All terms defined on first use.
```

**For code blocks:**
1. State what the code *does* in one sentence (not how)
2. Walk through what each section produces
3. Call out any gotchas, side effects, or failure modes
4. Show a minimal concrete example input/output

**For error messages:**
1. State what went wrong in plain English
2. State what the program was trying to do
3. Give the most common cause
4. Give the most common fix (with command if applicable)

---

### `/caveman:smash` — Jargon Crusher

1. **Scan the document**
   ```bash
   python scripts/jargon_detector.py path/to/file.txt
   # or pipe text:
   echo "We need to leverage our synergies..." | python scripts/jargon_detector.py -
   ```

2. **Review the hit list**
   - Every flagged term shown with line number and plain alternative
   - Severity: HIGH (blocks comprehension) / MEDIUM (slows reading) / LOW (style issue)

3. **Apply replacements**
   - Confirm each swap or use `--auto` for automatic replacement
   - Re-scan to verify jargon density dropped below 2%

4. **Output**
   - Cleaned document saved as `filename_caveman.txt` (or `.md`)
   - Change log with every replacement made

---

### `/caveman:score` — Readability Audit

```bash
# Score a file
python scripts/complexity_crusher.py path/to/document.md

# Score piped text
cat README.md | python scripts/complexity_crusher.py -

# JSON output for CI integration
python scripts/complexity_crusher.py path/to/file.md --json
```

**Metrics reported:**

| Metric | Target | Description |
|--------|--------|-------------|
| Flesch Reading Ease | 60–70 | 60+ = plain English, 30– = academic |
| Flesch-Kincaid Grade | ≤8 | US grade level to read it comfortably |
| Avg sentence length | ≤20 words | Longer = harder |
| Jargon density | ≤2% | % of flagged words in total word count |
| Passive voice ratio | ≤10% | % of sentences in passive voice |
| Readability grade | A–F | Composite score |

**Score grades:**

```
A  (90-100) — Anyone can read it. Caveman approved.
B  (75-89)  — Clear with minor rough patches.
C  (60-74)  — Readable but dense in places.
D  (45-59)  — Needs work. Many readers will struggle.
F  (<45)    — Jargon swamp. Rewrite required.
```

---

## Jargon Hit List

Common offenders and their replacements:

| Kill this | Use this instead |
|-----------|-----------------|
| leverage | use |
| utilize | use |
| synergy / synergies | working together |
| paradigm shift | big change |
| robust | strong / reliable |
| scalable | grows easily |
| ecosystem | system / community |
| bandwidth | time / capacity |
| circle back | follow up |
| deep dive | look closely |
| boil the ocean | try to do too much |
| move the needle | make a difference |
| low-hanging fruit | easy win |
| ping | message / contact |
| touch base | check in |
| at the end of the day | ultimately |
| going forward | from now on |
| ideate | think of ideas |
| socialize (an idea) | share (an idea) |
| actionable | useful / doable |
| stakeholder | person involved |
| deliverable | output / result |
| onboard | set up / train |
| sunset (a product) | retire / shut down |
| iterate | improve step by step |
| surface (an issue) | bring up |
| unpack | explain |
| evangelize | promote / champion |
| frictionless | easy |
| seamless | smooth |

---

## Reference Guides

- [Plain Language Guide](references/plain-language-guide.md) — Rules, examples, and rewrites
- [Tech Jargon Dictionary](references/tech-jargon-dictionary.md) — 200+ tech terms with plain definitions

---

## Python Tools

| Script | What it does |
|--------|-------------|
| `scripts/complexity_crusher.py` | Readability metrics: Flesch, FK grade, sentence length, passive voice |
| `scripts/jargon_detector.py` | Jargon scanner: detects flagged terms, reports density, suggests replacements |

---

## Output Principles

Every output from this skill must follow:

1. **Lead sentence** — one sentence stating the main point
2. **No unexplained acronyms** — spell it out or drop it
3. **No passive voice** — rewrite all passive constructions
4. **Short paragraphs** — max 4 sentences
5. **Plain verbs** — use, build, show, fix, find (not: utilize, implement, surface, remediate, identify)
