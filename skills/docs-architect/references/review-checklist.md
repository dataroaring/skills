# Documentation Review Checklist

Load this file when reviewing or diffing existing documentation—whether it's the user's own docs, a competitor's docs, or a draft for feedback.

## How to use this checklist

The review has four passes, ordered from cheapest to most expensive:

1. **Structural pass** — does the IA make sense?
2. **Page-type pass** — is each page the right Diátaxis type, done well?
3. **Content pass** — is the writing good and the code working?
4. **Details pass** — the small touches that signal professionalism.

You don't have to walk all four for every review. If the user asks "is the sidebar organized right?", do pass 1 and stop. If they ask "review this page", start at pass 2.

For each pass, the checks below are **questions to investigate**, not boxes to tick. Some will be obvious yeses or noes; others require judgment.

---

## Pass 1 — Structural pass

### Top-level navigation
- Could a first-time user, with zero product context, guess what each top-level item means in 3 seconds?
- Are top-level items verbs or user-recognizable nouns, or are they internal product names?
- Is the count of top-level items reasonable (5–9)? More than 9 is hard to scan; fewer than 5 may be over-grouped.
- Are there separate areas for **Guides / Reference / API**, or are they mixed?

### Section organization
- Does each section have a landing page that orients the reader, or is the sidebar the only navigation aid?
- Are sub-pages parallel siblings (Stripe/Snowflake style) or deeply nested? Deep nesting hurts discoverability.
- Are similar tasks grouped together, or scattered across sections?

### Multi-product / multi-plan handling
- If the product has multiple plans/editions, is it clear which docs apply to which plan?
- Are plan differences handled by URL parameter, separate sidebars, or callouts? Each works; inconsistency doesn't.

### Bilingual / multilingual (if applicable)
- Are sections structurally identical across languages?
- Does the language switcher persist across pages?
- Are terms translated consistently across pages? (Pick 3 random terms; check 3 random pages.)

---

## Pass 2 — Page-type pass

For each page sampled, identify its Diátaxis type and check against that type's standards.

### Is the type clear?
- Can you label this page as Tutorial / How-to / Reference / Explanation with confidence?
- If you can't, the page is mixing types. Note which types and suggest a split.

### Tutorials specifically
- Does the first concrete action appear within the first screen?
- Is there a linear path with no "if you want to do X instead..." branches?
- Does the reader get a verifiable working result by the end?
- Is the time estimate honest?

### How-tos specifically
- Does the page get to the steps within 100 words?
- Are prerequisites stated, or assumed?
- Is there a "verify" or "expected result" section?
- Are common issues addressed, or does the user have to hunt in a separate troubleshooting page?

### Reference specifically
- Is the structure consistent with other reference pages in the same section?
- Are parameters fully specified (type, required/optional, default, valid range)?
- Are there minimal working examples?
- Are errors documented?

### Explanation specifically
- Does it avoid procedural steps? (If steps appear, they belong in a how-to.)
- Are diagrams used where concepts are spatial?
- Are tradeoffs discussed honestly?

---

## Pass 3 — Content pass

### Code examples
- Pick 3 random code examples. Could you copy each verbatim and run it? If not, what's missing?
- Are placeholders clearly marked and consistent (`<your-cluster-id>` not a mix of styles)?
- For SQL: do queries reference real sample datasets the user can access?
- For each example, is there a one-click path to try it in the product?

### Writing
- Is the page front-loaded with the answer, or with motivational prose?
- Does the writing assume the right level of context? (Tutorial: low context. Reference: high context.)
- Are there sentences you could cut without losing meaning? (Usually yes, often many.)
- Is the voice consistent with the rest of the docs? (Formal/casual mix is jarring.)

### Cross-linking
- Does each page link to closely related pages, or is it an island?
- Are links specific ("How to scale a cluster") rather than vague ("learn more")?
- Are there dead-end pages with no next action?

### Calls to action
- Does the page have a clear next action—either another doc or a product action?
- Is there a path from this page to "first successful use in the product"?

---

## Pass 4 — Details pass

These are the small touches that compound into "professional feel." Each one alone is minor; missing them collectively is a credibility hit.

### Code blocks
- Every code block has a copy button with success feedback?
- Syntax highlighting is consistent and correct?
- For shell commands, is the prompt character (`$`) unselectable, or does it get copied with the command?

### Navigation aids
- Breadcrumbs on every page?
- Sticky sidebar that stays in view while scrolling?
- "Last updated" date visible?
- Previous/next page links at the bottom of sequential content?

### Search
- Does search return relevant results, or alphabetical/keyword-match?
- Are there search filters by section/type if the doc set is large?

### Locale and persistence
- If bilingual: does the language choice persist across pages?
- If there's a code language selector (Python/Curl/etc.): does it persist?
- If there's a plan/edition selector: does it persist?

### Visual
- Does the documentation site have its own visual identity, or does it look like a template?
- Are diagrams used and well-rendered, or is everything walls of text?
- Is the typography optimized for reading (line length, font size)?

---

## Reporting a review

When delivering a review to the user, structure it like this:

1. **Top 3 strengths** — what's working well. Be specific, not generic.
2. **Top 3 issues** — what to fix first. Each with: the issue, why it matters, a concrete fix.
3. **Smaller items** — a list of less-critical observations.
4. **Open questions** — things you couldn't determine from the docs alone (e.g., "Is this section meant to be exhaustive, or representative?").

Avoid:
- Walls of "found 47 issues" without prioritization.
- Vague feedback ("the writing could be tighter"). Show an example.
- Reviewing what isn't there (scope creep). Stick to what the user asked about.

---

## Common patterns this checklist surfaces

Things I've seen come up repeatedly when reviewing data platform / database docs:

- **Reference and tutorial mixed**: a "Getting started" page that's actually 80% parameter reference.
- **No section landing pages**: sidebars work, but new users have no orienting page.
- **Inconsistent placeholder style**: `<id>` and `{id}` and `your_id` all in the same doc set.
- **Toy SQL examples**: `SELECT * FROM t` instead of a realistic query against a documented sample dataset.
- **Dead-end pages**: pages with no "next step" link, leaving the user stranded.
- **Bilingual structural drift**: EN has 5 sub-pages, 中文 has 4, because one was added without updating the other.
- **Empty state ↔ docs gap**: empty states don't link to docs; docs don't link to product actions.
