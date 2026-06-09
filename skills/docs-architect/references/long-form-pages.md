# Long-form Pages and Cross-referencing

Load this file when writing a long technical guide that covers multiple aspects of a feature (a "complete guide to X"), or when deciding how heavily to cross-link between docs.

These two topics are paired because they're the same problem from different angles: **how should a single page relate to the rest of the docs?**

---

## The traditional view vs. the Stripe view

**Traditional advice**: each page should be one Diátaxis type. Tutorials separate from how-tos separate from explanations. (This is what `SKILL.md` Principle 2 says.)

**Stripe's practice**: long-form pages routinely mix Diátaxis types **within a single page**, using H2 headings to separate sections that each have their own type.

For example, the page `https://docs.stripe.com/webhooks.md` is one of Stripe's most important documents. It contains:

- A 1-paragraph **explanation** (what webhooks are, why)
- A 4-step **tutorial** ("Get started")
- A multi-language **how-to** ("Create a handler" with Ruby/Python/Java/etc. code)
- A **reference** (HTTP status code table)
- More **explanations** (event ordering, API versioning)
- A **best-practices checklist**

It works because each H2 section is **internally pure**. The "Get started" section is purely tutorial. The "Create a handler" section is purely how-to. The "Fix HTTP status codes" subsection is purely reference (a table).

**The refined rule**: a single H2 section should be one Diátaxis type. A page can contain multiple H2 sections of different types if they're tightly related and the reader benefits from having them in one place.

---

## When to mix types in one page

Use a long-form mixed page when **all of the following are true**:

1. **The content forms a unit the reader thinks of as one topic.** ("Webhooks" is one topic, even though learning it involves tutorial + how-to + reference.)
2. **Splitting would create high-friction navigation.** If a reader needs to bounce between 5 pages to do one task, fold them.
3. **The page can be navigated by anchor links** (table of contents in sidebar or top of page). A 5000-word page only works with anchor navigation; without it, readers can't jump.
4. **You're willing to maintain it.** Long pages have higher maintenance cost; orphaned subsections decay faster.

If any of these is false, split into multiple pages.

**Bad reasons to mix**:
- "We don't have time to split it"
- "It's all about X, so it should be one page"
- "The team agreed to a 'comprehensive guide' format"

**Good reasons to mix**:
- The reader needs to do tutorial → how-to → reference as one continuous task
- The reference material is short and only relevant to this topic
- A separate page would have <500 words

---

## Structuring a long-form mixed page

```markdown
# [Topic name]

[1-2 sentence framing]

## Get started

[Tutorial-style: linear steps, end with working result. ~3-5 steps.]

## Create a [thing]

[How-to-style: assumes context from Get started, shows the main task.]

## Test your [thing]

[How-to-style: continues the task.]

## [Reference subsection, e.g., "HTTP status codes"]

[Pure reference: table, parameter list, error code list. No motivational prose.]

## [Explanation subsection, e.g., "Event ordering" / "Delivery behaviors"]

[Pure explanation: how the system behaves and why.]

## Best practices

[Checklist or short principles. Distinct from how-to: principles, not steps.]

## See also

[Next-step cards. See landing-pages.md for the format.]
```

**Notice the order**: tutorial → how-to → reference → explanation → best practices. This matches the reader's likely progression: first do it, then look up details, then understand it deeply.

**Anchor links matter**: long pages need a visible table of contents (auto-generated from H2/H3 is fine) so readers can jump to the section they need on a return visit.

---

## High-density cross-referencing

Even within a long page, Stripe links **aggressively** to other docs. Sample sentence from `webhooks.md`:

> Stripe sends most event types asynchronously, but waits for a response for some event types. In these cases, Stripe behaves differently based on whether or not the event destination responds. If your event destination receives [Organization](url) events, those requiring a response have the following limitations: You can't subscribe to `issuing_authorization.request` for organization destinations. Instead, set up a [webhook endpoint](url) in a Stripe account within the organization to subscribe to this event type.

**Two short sentences. Three inline links.**

The links go to:
- The concept page for "Organization"
- The how-to for setting up a webhook endpoint
- (Implicitly) other concept and reference pages elsewhere in the doc

**The philosophy**: don't try to explain everything on this page. Trust the reader to follow links for context they need. The reader's mental model is "this is the network of docs, I'll navigate it."

This is the opposite of the "self-contained README" approach, where every page tries to be readable in isolation.

### When to link inline

Link inline when:
- You mention a **concept** that has its own page (link to the concept).
- You reference a **task** the reader might need to do (link to the how-to).
- You name a **product feature** or **API resource** (link to the reference).
- You name a **dashboard area** or **product surface** ("the [Webhooks](url) tab in Workbench").

Don't link inline when:
- You're repeating a link from earlier in the same page (link once per page, usually).
- The link is to a generic concept ("Markdown", "JSON") that doesn't need explaining.
- The destination is the same page (use anchor links instead).

### What inline links should look like

Link text should be:
- **The natural noun phrase**, not a clunky insert. "Set up a [webhook endpoint](url)" not "Set up a webhook endpoint ([learn more](url))".
- **Specific**: "the [Webhooks](url) tab" not "the webhooks tab [here](url)".
- **Stable**: don't link the same noun phrase twice on the same page (the second one is visual noise).

### Density target

A rough heuristic from Stripe's docs: **a how-to or explanation paragraph typically has 1-3 inline links**. A page-level "next steps" or "see also" section has 3-6 links. A reference page may have far more (every parameter type, every related resource).

Going too sparse hurts navigation. Going too dense (every other word linked) hurts readability. Aim for "a link wherever a reader might want to dig deeper."

---

## A note on the reader's mental model

The cross-referencing philosophy assumes the reader will:
1. Skim the current page.
2. Open a few links in new tabs.
3. Read selectively.

This is how developers actually consume docs. Writing for the "linear reader who reads top to bottom" is a fiction—and writing for it produces bloated, self-contained pages that no one finishes.

Link aggressively. Trust the reader to follow what they need.

---

## Anti-patterns

- **"Comprehensive guide" pages that are just 8 chapters glued together** — these need to be split or restructured into a section with its own landing page.
- **Self-contained pages with no outbound links** — fine for a quickstart, hostile for everything else. The doc is a graph, not a tree.
- **Repeating the same link 4 times on one page** — visual noise; link once and the reader can scroll back if needed.
- **"Click here" or "learn more" instead of natural link text** — already covered in `writing-style.md` Rule 5, but worth reinforcing.
- **Long pages with no anchor TOC** — without anchors, long pages are unnavigable on a return visit.
