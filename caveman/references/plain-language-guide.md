# Plain Language Guide

Rules, patterns, and rewrite examples for turning dense text into clear communication.

---

## The One Rule

If a reader has to re-read a sentence to understand it, rewrite it.

---

## Sentence Rules

### Rule 1 — One idea, one sentence

**Before:**
> The system, which was designed to handle high-throughput scenarios while maintaining data consistency across distributed nodes, leverages a consensus algorithm to ensure that all replicas are synchronized.

**After:**
> The system keeps data consistent across all copies. It does this using a consensus algorithm that syncs every node.

---

### Rule 2 — Active voice

Switch from passive (thing was done by someone) to active (someone did the thing).

| Passive | Active |
|---------|--------|
| The bug was found by the team. | The team found the bug. |
| The feature was deprecated in v3. | We deprecated the feature in v3. |
| Errors are handled by the middleware. | The middleware handles errors. |
| The report was sent to all stakeholders. | We sent the report to everyone involved. |

**Quick test:** Can you add "by zombies" after the verb? If yes, it's passive.
- "The bug was found *by zombies*" — passive. Fix it.
- "The team found the bug" — no slot for zombies. Active. Good.

---

### Rule 3 — Kill nominalization

Nominalization turns a verb into a noun, making sentences longer and weaker.

| Nominalization (noun) | Plain verb form |
|-----------------------|-----------------|
| make an assumption | assume |
| provide an explanation | explain |
| conduct an investigation | investigate |
| reach a conclusion | conclude |
| make a decision | decide |
| give consideration to | consider |
| perform an analysis | analyze |
| take into account | consider |
| conduct a review | review |
| provide support | support |

**Before:**
> We will conduct an investigation into the cause of the failure and provide an explanation to the team.

**After:**
> We will investigate the failure and explain what happened to the team.

---

### Rule 4 — Short sentences

Target: **20 words or fewer** per sentence.

Count the words. If over 20, find the natural break point (usually a conjunction: and, but, because, so, which) and split.

**Before (34 words):**
> Because the deployment pipeline was not configured to run integration tests in parallel, each push to the main branch triggered a sequential test run that increased CI time by 40%.

**After:**
> The deployment pipeline ran integration tests in order, not in parallel. Each push to main triggered a sequential run. CI time increased 40%.

---

### Rule 5 — Lead with the point

Put the main idea first. Don't make readers wade through background to find the answer.

**Before:**
> Given the increasing complexity of the distributed architecture and the need to maintain uptime during peak traffic periods while also reducing operational costs, we have decided to migrate to Kubernetes.

**After:**
> We are migrating to Kubernetes. This will cut costs and keep the system running during high traffic.

---

## Word Rules

### Replace weak verbs with strong ones

| Weak | Strong |
|------|--------|
| utilize | use |
| implement | build / add |
| leverage | use |
| facilitate | help |
| enable | let / allow |
| ensure | make sure |
| provide | give |
| demonstrate | show |
| indicate | show / mean |
| terminate | end / stop |

---

### Kill filler phrases

These add length but zero meaning. Delete them.

| Delete this | Or replace with |
|-------------|----------------|
| It is worth noting that | — (just say the thing) |
| In order to | To |
| Due to the fact that | Because |
| At this point in time | Now |
| In the event that | If |
| With regard to | About |
| For the purpose of | To |
| In close proximity to | Near |
| Prior to | Before |
| Subsequent to | After |
| In the near future | Soon |
| It should be noted | — |
| As previously mentioned | — |
| Please be advised | — |

---

### Acronym rule

Spell out every acronym on its first use. After that, use the short form.

**Before:**
> The API connects to the DB via TLS and returns JSON.

**After:**
> The API (Application Programming Interface) connects to the database using TLS (Transport Layer Security) and returns JSON (JavaScript Object Notation).

In subsequent mentions: "The API returns JSON."

---

### Numbers

- Spell out one through nine
- Use digits for 10 and above
- Always use digits with units: 5 GB, 3 ms, 2 seconds
- Approximate large numbers when precision doesn't matter: "about 2,000 users" not "1,987 users" in a summary

---

## Structure Rules

### Use bullet points for 3+ items

**Before:**
> The system supports authentication via username/password, OAuth 2.0, SAML, and API keys.

**After:**
> The system supports four authentication methods:
> - Username and password
> - OAuth 2.0
> - SAML
> - API keys

---

### Inverted pyramid

Lead with the answer. Then add context. Then add detail.

```
[MOST IMPORTANT] — What happened / What to do
[CONTEXT]        — Why it matters
[DETAIL]         — How / Technical specifics
```

**Example:**
> The login service is down. Users cannot sign in.
> The issue started at 14:32 UTC after a failed config push.
> The root cause is a misconfigured rate limiter in the auth middleware. Rollback is in progress.

---

### Parallel structure

Items in a list must follow the same grammatical pattern.

**Before (mixed forms):**
> The tool can:
> - Analyze text
> - Detection of jargon
> - It will suggest replacements

**After (all verbs):**
> The tool can:
> - Analyze text
> - Detect jargon
> - Suggest replacements

---

## Rewrite Examples

### Technical error message

**Before:**
> An unhandled exception was encountered during the execution of the request pipeline. The server was unable to process the request due to an internal error.

**After:**
> Something went wrong on the server. We could not complete your request. Please try again. If the problem continues, contact support.

---

### Pull request description

**Before:**
> This PR implements the refactoring of the authentication middleware to leverage a more robust token validation strategy utilizing the JWT library, which was necessitated by the deprecation of the legacy session-based approach.

**After:**
> This PR rewrites the authentication middleware. We switched from session cookies to JWT tokens because the old session system is being retired.

---

### README introduction

**Before:**
> This repository contains a comprehensive, enterprise-grade, highly-scalable solution for the orchestration of containerized microservices leveraging cutting-edge cloud-native paradigms to facilitate seamless deployment pipelines.

**After:**
> This repo helps you deploy and manage containers in the cloud. It automates deployments and works with major cloud providers.

---

## Checklist Before Publishing

Use this checklist on any document before sharing:

- [ ] Every sentence is ≤20 words
- [ ] All acronyms are spelled out on first use
- [ ] No passive voice (or flagged exceptions justified)
- [ ] No filler phrases
- [ ] No jargon without a plain alternative offered
- [ ] Main point comes first in every paragraph
- [ ] Lists use parallel structure
- [ ] Numbers follow the word/digit rule
- [ ] Readability score is C or better (run `/caveman:score`)
