---
name: caveman-review
description: Ultra-compressed code review comments. One-line format with exact line numbers and concrete fixes.
---

# Caveman Review

One-line comments. Exact line numbers. Concrete fixes. No filler.

## Activation

Triggered by: "review this", "code review", `/caveman-review`. Each comment one line. No paragraphs.

## Format

`L<line>: <severity> <problem>. <fix>.`

Severity prefixes:
- 🔴 bug — incorrect behavior
- 🟡 risk — potential issue
- 🔵 nit — style or minor quality
- ❓ q — question

## Rules

Drop: "I noticed that", "perhaps", "maybe", "you might want to", restating what code does. Keep: exact line numbers, symbol names in backticks, concrete fixes, reasoning when fix is non-obvious.

## Examples

Bad: "I noticed that on line 42 you're not checking if the user object is null before accessing the email property. This could potentially cause a crash."

Good: `L42: 🔴 bug: user can be null after .find(). Add guard before .email.`

## Exception

Security vulnerabilities, architectural disputes, and onboarding contexts warrant full explanation. Resume terseness after.
