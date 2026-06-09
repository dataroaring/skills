# Page Templates by Document Type

Load this file when writing a new page from scratch, or when designing a section landing page. The templates below are skeletons—they're starting points, not prescriptions. Adapt to the specific content.

## When to use which template

Match the user's intent to the template:

- "I want users to learn how to use X" → **Tutorial template**
- "I want users to accomplish Y" → **How-to template**
- "I want users to look up Z" → **Reference template**
- "I want users to understand W" → **Explanation template**
- "I want users to find their way around" → **Landing page template**
- "I want users to work through a multi-visit checklist" → **Checklist template**
- "I want users to handle a category of problems (errors, statuses, limits)" → **Problem catalog template**
- "I want to teach a broad technical topic with multiple techniques and detail levels" → **Topic survey template**

If the user's request doesn't match exactly one, ask which type they mean. Don't mix types in a single page (with one exception: see "Topic survey" below, which is intentionally multi-type).

---

## Tutorial template

A tutorial teaches by doing. The reader follows along, gets a working result, and feels successful. It's not optimized for reference—it's optimized for learning.

```markdown
# [Verb-based title: "Get started with X" or "Build your first Y"]

[1-2 sentence framing: what the reader will build/achieve, and roughly how long it will take. Be honest about time.]

## Before you begin

[Prerequisites as a short list. Each item links to setup docs if needed.]
- Account / access requirement
- Tools to install
- Sample data or credentials

## Step 1 — [First concrete action]

[Brief context, then the action. Show the exact command or UI step.]

[Code block or screenshot]

[1-2 sentences explaining what just happened and what to look for.]

## Step 2 — [Next action]

[Same pattern.]

## Step 3 — [...]

## What you built

[Recap what the reader now has. Reinforce the success.]

## Next steps

[2-3 links to related how-tos or the next tutorial in a series. NOT a generic "see also."]
- [Specific next action]
- [Specific next action]
```

**Rules**:
- One linear path. No "if you want to do X instead..." branches—those belong in how-tos.
- Every step has a visible, verifiable outcome.
- The first step happens within the first 90 seconds of reading.
- Keep prerequisites short. If they're long, that's a sign the tutorial is too ambitious.

---

## How-to template

A how-to solves a specific problem for someone who already knows the basics. It's task-focused, scannable, and assumes context.

```markdown
# How to [specific task, verb-first]

[1-2 sentence statement of when you'd want to do this. The reader is here because they have this exact problem—don't re-sell the feature.]

## Prerequisites

[Only what's strictly required. Often just a sentence.]

## Steps

1. [First action]
   ```
   [Code or command]
   ```
2. [Second action]
3. [...]

## Verify

[How to confirm it worked. Often a query or UI check.]

## Common issues

[2-4 likely failure modes with brief solutions. NOT an exhaustive troubleshooting guide.]

**Issue**: [Symptom]
**Solution**: [Fix]

## See also

[1-3 closely related how-tos. Don't dump the entire section index here.]
```

**Rules**:
- Assume the reader knows the basics. Don't explain what a cluster is in a how-to about scaling clusters.
- Skip the motivational prose. Get to the steps within the first 100 words.
- "Common issues" is more useful than a separate troubleshooting page for most users.

---

## Reference template

Reference is a lookup, not a read. Optimize for fast scanning, completeness, and consistency across pages.

```markdown
# [Exact name of the thing: function name, parameter, API endpoint]

[One-sentence definition. The reader is here to look up details, not to be sold.]

## Syntax

```
[Exact syntax, formatted consistently]
```

## Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | What this parameter does. |
| `option` | int | No (default: 10) | What this controls. Valid range: 1–100. |

## Return value

[What it returns. Types, structure, edge cases.]

## Examples

### Basic usage
```sql
[Minimal working example]
```

### [Specific scenario]
```sql
[More involved example]
```

## Errors

[Common errors this can produce, with the exact error message text and meaning.]

## Related

[Tightly related reference entries only. No marketing links.]
```

**Rules**:
- Consistent structure across every reference page. If 90% have an "Errors" section, the other 10% should too (even if "None known").
- No motivational prose. No "this powerful feature lets you..."
- Examples are minimal and self-contained. Each example shows one thing.
- Use the same formatting for syntax everywhere. Pick a convention and apply it ruthlessly.

---

## Explanation template

Explanation builds understanding. It's for the reader who wants to know *why*, not *how*. These pages are read end-to-end, not scanned.

```markdown
# [Concept name, often a noun phrase]

[1-2 sentence overview: what this concept is and why it matters.]

## The problem

[What problem does this concept solve? Why was it needed?]

## How it works

[The mental model. Diagrams welcome. Avoid implementation details unless they affect user-visible behavior.]

[Diagram or architecture figure]

## Tradeoffs

[Honest discussion of what this approach trades away. Not all concepts are perfect for all situations.]

## When to use this

[Concrete scenarios. Help the reader map their situation to whether this applies.]

## Further reading

[Links to deeper material: papers, blog posts, related concepts. NOT how-tos.]
```

**Rules**:
- No procedural steps. If the reader wants to *do* something, link to a how-to.
- Use diagrams generously. Concepts are spatial.
- Be willing to say "this is a tradeoff, not a free lunch."
- It's OK to be opinionated about when to use this. That's the point of explanation.

---

## Landing page template

A landing page is a navigation aid, not content. Its job is to route the reader to the right next page within 5 seconds.

```markdown
# [Section name]

[1-2 sentence framing of what this section covers. Position it within the broader docs.]

## Get started

[The 1-2 most common entry points for this section, with brief descriptions. These are bigger than the rest—visually or with prominent links.]

- **[Quickstart name]** — What you'll do, who it's for.
- **[Most-used how-to]** — Common task most users do.

## By task

[The how-to landscape, organized by user goal. 4-8 items maximum at this level. If more, group further.]

- **[Goal cluster 1]**
  - [Task 1]
  - [Task 2]
- **[Goal cluster 2]**
  - [Task 1]

## Concepts

[Links to explanation pages. Short list.]

- [Concept 1] — Brief framing
- [Concept 2] — Brief framing

## Reference

[Link to the reference section, not a list of every reference page.]

→ [Section name] reference
```

**Rules**:
- A landing page is not a table of contents. It's a curated list with framing.
- Lead with the 80% paths. Don't try to surface every page.
- Use brief descriptions (one phrase, not a paragraph) for each link.
- If you need to scroll past the fold, the landing page is too long.

---

## Checklist template (interactive go-live / readiness pages)

A specialized template for pages whose purpose is **a multi-step checklist the reader works through over multiple visits**. Examples: "go-live checklist", "production readiness checklist", "security review checklist".

The defining feature: the reader is not consuming this page once and moving on. They return repeatedly to mark off items as their integration matures. The page should support that workflow.

```markdown
# [Checklist name]

[1-2 sentence framing: when to use this checklist, and what completion means.]

> As you check off each item, the state is saved in your browser cache. 
> You can return to this page any time to see what you've completed.

## Before you begin

[Prerequisites the reader needs before this checklist applies.]

## [Section 1 — e.g., "Before going live"]

- [ ] **[Item title]** — [1-2 sentence explanation. Link to deeper docs if needed.]
- [ ] **[Item title]** — [Explanation with link to the relevant feature page.]
- [ ] **[Item title]** — [Explanation.]

## [Section 2 — e.g., "Security"]

- [ ] **[Item title]** — [Explanation.]
- [ ] **[Item title]** — [Explanation.]

## [Section 3 — e.g., "Monitoring and operations"]

- [ ] **[Item title]** — [Explanation.]
- [ ] **[Item title]** — [Explanation.]

## After you launch

[1-2 sentences on what to monitor, where to get help, how to escalate.]
```

**Rules specific to checklists**:

- Use Markdown task list syntax (`- [ ]`). Most modern doc platforms render this as a real checkbox; some persist state across sessions, which is the high-value version.
- Each item is **one specific verifiable action**, not a vague concept. "Configure your VPC subnets correctly" is bad; "Verify each VPC subnet has at least 16 free IP addresses" is good.
- **Bold the item title**, then dash, then explanation. The reader scans bold titles to see what's on the list; reads the explanation only for items they're uncertain about.
- Link aggressively from each item to the detail page for that step. Checklists are routing surfaces, like landing pages.
- Group items by lifecycle phase ("Before you begin" / "During build" / "Before launch" / "Ongoing"). Don't dump everything into one flat list.
- Aim for 10-30 items total. Fewer than 10 is a how-to in disguise; more than 30 won't get completed.

**Why this is its own template**: checklists violate several rules of normal docs. They're long. They use bullets heavily. They mix concepts with actions. They're meant to be skimmed and partially read. None of this is wrong for a checklist—but applying normal doc rules to one produces a bad checklist.

---

## Problem catalog template

For pages that enumerate a known set of problems—errors, status codes, decline reasons, limits, known issues, troubleshooting categories. The defining feature: there's a **fixed set of items**, each with the same kind of metadata (an identifier, a cause, a fix). Examples: error code reference, HTTP status code guide, troubleshooting page, declines and refusals page.

```markdown
# [Catalog name: e.g., "Error handling", "Decline codes"]

[1-2 sentence framing: when this catalog is relevant, and how the reader uses it.]

## Parse [the structure]

[Brief explanation of the data structure the reader will receive. 
Often a table listing every field with type and description. This is 
the reader's mental model for everything that follows.]

| Property   | Description                                  |
|------------|----------------------------------------------|
| `code`     | The error code.                              |
| `doc_url`  | A link to the documentation for this error.  |
| `message`  | A human-readable description.                |
| ...        | ...                                          |

## [Handling techniques overview]

[A preview table that lists the main ways to deal with this category. 
Each row maps to a section below. The "When needed" column gives the 
reader frequency guidance up front.]

| Technique             | Purpose                              | When needed |
|-----------------------|--------------------------------------|-------------|
| [Technique A]         | What it solves                       | Always      |
| [Technique B]         | What it solves                       | Sometimes   |
| [Technique C]         | What it solves                       | Rarely      |

## [Technique A]

[Detailed explanation of one approach. Code example.]

## [Technique B]

[Same.]

## [Technique C]

[Same.]

## Types of [problem]

[A table mapping each type/code/category to a class or identifier 
the reader will see in their integration. Each row links to its 
detailed section below.]

| Name              | Class / Code              | Description                       |
|-------------------|---------------------------|-----------------------------------|
| [Problem type 1]  | `ErrorClassName`          | One-sentence description.         |
| [Problem type 2]  | `ErrorClassName`          | One-sentence description.         |
| ...               | ...                       | ...                               |

## [Problem type 1]

[Detailed entry using the Type/Problem/Solutions card below.]

| **Type**      | `ErrorClassName`                                         |
| **Codes**     | `error.code == 'specific_code'` (when applicable)        |
| **Problem**   | One-sentence explanation of what went wrong.             |
| **Solutions** | - Concrete action 1 with link.                           |
|               | - Concrete action 2 with link.                           |
|               | - "This error can occur when your integration is        |
|                  working correctly" if applicable—reassure the reader  |
|                  that not every error indicates a bug.                   |

## [Problem type 2]

[Same card format.]

## [...repeat for each type]
```

**Rules specific to problem catalogs**:

- **Use the four-section spine**: Parse the structure → Handling techniques → Types overview → Each type in detail. This is the order a reader actually needs.
- **Use the Type/Problem/Solutions card consistently**. Every entry has the same fields, in the same order. Inconsistent entries force readers to scan each one.
- **"Codes" field is optional**—only include when there's a programmatic way to match this case. Don't omit the row inconsistently; use "N/A" or skip the row schema-wide.
- **In Solutions, lead with concrete actions, then explanations**. Bullets, each starting with a verb.
- **Add "This error can occur when your integration is working correctly" when applicable**. Many readers see an error and assume they've broken something. Be explicit about which errors are expected behavior vs. true bugs.
- **Link aggressively in Solutions**. Each solution should link to the doc that explains it in detail.
- **Use consistent type names across multiple language sections**. If the page covers Ruby/Python/Node, the same conceptual error has different class names per language; keep the structure parallel and only the class names change.

---

## Topic survey template

For pages that teach a broad technical topic spanning multiple Diátaxis types—how something works, how to use it, common cases, and edge details. Examples: a "Webhooks" guide, a "Workload Management" guide, a "Replication" guide. Unlike how-to pages, topic surveys are intentionally long and intentionally multi-type.

**Use this template only when**: the topic is foundational to the product, the reader needs to read most of it once before being productive, and splitting into smaller pages would force annoying navigation. Otherwise use multiple smaller pages.

```markdown
# [Topic name]

[1-2 sentence framing of what this topic covers and why it exists.]

[Optional: A "Start here" callout for AI agents or new readers, pointing 
to the most important sub-section or external resource.]

## Get started

[Tutorial section: 3-5 numbered steps that get the reader to a working 
first result. This is the only tutorial-style section on the page.]

1. [Action]
2. [Action]
3. [Action]
4. [Action]

[1-2 sentences: what they just achieved and where to go next.]

## [Main concept]

[Explanation section: how the thing works conceptually. Diagrams welcome. 
This is the only explanation-style section here.]

## [Primary how-to: e.g., "Create a handler"]

[How-to section: the main task readers will do, with code per language.]

## [Secondary how-to: e.g., "Test your handler"]

[How-to section: the next task in the natural sequence.]

## [Setup or registration step]

[How-to section: any final setup the reader needs.]

## [Reference subsection: e.g., "Status codes" or "Event types"]

[Reference section: a table, a parameter list, or an enumerated catalog. 
Pure reference style—no motivational prose, just data.]

## [Behavior or operational details]

[Explanation section: how the system actually behaves in edge cases 
(ordering, retries, versioning, error recovery). Multiple H3s as needed.]

## Best practices

[Checklist-style: a list of recommendations with brief explanations. 
Different from how-to: principles and patterns, not steps.]

## See also

[Next-step cards, H4 + one-sentence description format. 
See landing-pages.md.]
```

**Rules specific to topic surveys**:

- **The order matters**: tutorial → explanation → how-tos → reference → operational behavior → best practices. This matches the reader's natural progression: do it first, then understand it, then handle edges, then improve.
- **Each H2 is internally pure**. Mixing within a section is what breaks readability; mixing across sections is fine if the page is well-marked.
- **Anchor TOC is required**. A topic survey only works if readers can jump to the section they need on a return visit. Without an anchor TOC, this template fails.
- **Cap at ~5000-8000 words**. If you're going past this, split into multiple pages with a landing page.
- **"Get started" never branches**. The tutorial section is linear—no "if you want to do X instead". Branches belong in a separate how-to.
- **The reference subsection should be short**. If the reference content is more than a screen, split it to a dedicated reference page and link to it. Embedding a 200-row table inside a topic survey breaks the survey.

**When NOT to use this template**:
- If you can split into 4-5 smaller pages with a section landing page—do that instead.
- If the reader will mostly look things up, not read end-to-end—use the Problem catalog or Reference template.
- If the topic is genuinely a single task—use the How-to template.

---

## A note on length

These templates are guides, not contracts. A 200-word how-to is fine. A 3000-word explanation is fine. What matters is that each section serves its purpose. If a section in the template would be empty or trivial, drop it.

The exception: **reference pages should be uniformly structured**. Consistency is the value-add of reference docs. If you skip the "Errors" section on some reference pages but not others, the user has to read every page to find out whether errors are documented. That defeats the purpose.
