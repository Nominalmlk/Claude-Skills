---
name: caveman-commit
description: Ultra-compressed commit message generator using Conventional Commits format with ≤50 character subjects.
---

# Caveman Commit

Generate terse Conventional Commits messages. No fluff. No AI credits. No self-reference.

## Activation

Triggered by: "write a commit", "commit message", "git commit", `/caveman-commit`. Outputs message as code block. Does NOT execute git commands or stage files.

## Subject Line

Format: `<type>(<scope>): <imperative summary>`

Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, `revert`

- Imperative mood: "add", "fix", "remove" — not "added", "fixes", "removed"
- Preferred ≤50 chars, hard limit 72
- No trailing period

## Body

Include only when reasoning is non-obvious. Required for: breaking changes, migrations, non-obvious decisions. Wrap at 72 chars. Bullets with dashes. Issue refs at end.

## Prohibited

- Self-referential: "This commit does X"
- First-person or temporal markers
- AI attribution or generation credits
- Emoji unless project convention mandates
- Redundant file refs already covered by scope
