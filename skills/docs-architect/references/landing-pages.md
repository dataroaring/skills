# Landing Page Design

Load this file when designing the docs home page, a section landing page (like "Payments" or "Observe"), or any page whose primary job is **routing readers to the right detail page** rather than teaching content.

Landing pages follow different rules than detail pages. The principles in `SKILL.md` and `writing-style.md` still apply, but the structural logic is inverted: a landing page that's optimized like a how-to will fail at its real job.

---

## The core distinction

**Detail pages teach.** A how-to, tutorial, or reference page exists to transfer knowledge. Readers arrive with a specific need and leave with that need met.

**Landing pages route.** A landing page exists to send the reader somewhere else. Readers arrive without a clear destination (they're at "/docs" or "/payments") and leave by clicking through. The landing page's success metric is **whether the click was the right one**, not whether the page itself was informative.

This produces a different design surface. A great landing page is mostly white space, headers, and short link descriptions. It's not where content lives.

---

## Pattern 1 — The docs home page is a path selector, not a product directory

The most common mistake: docs home pages list products. ("Here's our 12 products, click one.") This puts the burden on the reader to map their goal to a product name they may not recognize.

**Stripe's docs home page does the opposite.** The first thing you see is three columns of **user scenarios**, organized by business model:

| Column | Items |
|---|---|
| Payment scenarios | Accept online payments / Collect via invoices / Accept in-person |
| Revenue models | Sell subscriptions / Usage-based pricing / Customer portal |
| Developer entry points | Set up environment / Build with AI / Quickstarts |

**"Browse by product" appears further down the page**, not at the top. The reader who knows exactly which product they want can still find it; the reader who doesn't gets routed by what they're trying to do.

**The principle**: at the top of the docs home page, the reader should see verbs and outcomes, not product names. Products live below the fold or in a secondary section.

**Apply to VeloDB Cloud**:
- ❌ Top of home: "Clusters / Workspaces / SQL Editor / Workload Groups / Audit / Alerts..."
- ✅ Top of home: "Ingest real-time data / Run analytics queries / Migrate from Doris OSS / Monitor production workloads"
- Below the fold: the product-feature directory

**Check questions**:
- Does the first thing a reader sees on the home page require them to know your product names?
- Could a reader with a goal (not a product) find the right next click in 5 seconds?
- Are the top-level items verbs/scenarios, or are they nouns/products?

---

## Pattern 2 — Section landing pages are curated, not exhaustive

A section landing page (the page at, e.g., `/observe` or `/payments`) is the entry into a section. Two failure modes:

1. **It's an auto-generated TOC** — every page in the section listed in alphabetical order. The reader has to scan everything.
2. **It's a marketing page** — lots of prose about why this section matters, no clear entries.

**Stripe's section landing pages do this**:

- **A 1-2 sentence intro** ("Use Stripe to start accepting payments.")
- **A "Get started" link** prominently placed, going to the most common entry point
- **Curated subsection groups with H3/H4 headers** — "Most popular", "Online", "In-person", "Subscriptions", "Invoicing"
- **Each entry is a link + one-phrase description**: "[Accept online payments]: Build a payment form or use a prebuilt payment page."
- **"More guides" at the bottom**: a denser list for advanced/edge-case content

**Notice what's not there**:
- No long marketing paragraphs.
- No section overview that has to be read.
- No comprehensive list of every page.

**The principle**: a section landing page surfaces the **top 5-15 most-used entry points**, grouped by sub-task. Everything else is reachable via the sidebar or via "More" links. Curation is the value.

**Check questions**:
- If you removed your section landing page entirely, would readers be lost or would they just use the sidebar?
- (If the answer is "just use the sidebar," the landing page isn't earning its place.)
- Are entries grouped by sub-task ("Online", "In-person"), or just dumped in a list?
- Does each entry have a one-phrase description of what's on the other side?

---

## Pattern 3 — "Next steps" sections at the end of pages

Detail pages end with "Next steps", but this isn't a generic "see also" list. Stripe formats next steps as **mini-landing-page entries**:

```markdown
## Next steps

#### [Fulfill orders](url)

Set up an event destination to fulfill orders after a payment succeeds and to handle other critical events.

#### [Receive payouts](url)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refund and cancel payments](url)

Handle requests for refunds by using the Stripe API or Dashboard.
```

Each next step is:
- An **H4-level link** (visible, not buried in prose)
- Followed by a **one-sentence description** of what the reader will learn or do

This makes the end of every page a routing surface—the reader is never stranded.

**Why H4 and not bullets**: H4 gives each entry visual weight equal to a section heading, signaling "this is a real next destination," not a tertiary reference. Bullet lists of links look like footnotes; H4 cards look like CTAs.

**Apply to VeloDB Cloud**: every how-to and tutorial ends with 2-4 next-step cards. Generic "See the API reference for details" footers don't count.

**Check questions**:
- Does this page have a "Next steps" section, or does it end mid-thought?
- Are the next steps **routing options** (different directions the reader might go) or just **related reading** (similar topics)? Routing options are better.
- Is each next step a heading-styled card with a description, or a flat link?

---

## Pattern 4 — "Get started" gets visual prominence

On Stripe's section landing pages, "Get started" is not just another link in the list. It usually gets:

- Its own H2 or H3 heading
- A short framing sentence ("Integrate a Stripe product to start accepting payments online and in person, embed financial services, power custom revenue models, and more.")
- A single prominent CTA link

This implements Principle 5 (docs as product funnel) at the structural level: the path from "I just arrived" to "I started doing something" is the most visible thing on the page.

**For VeloDB Cloud**: every section landing should have a clear "Start here if you're new" path, distinct from the "I'm looking up something specific" path.

---

## A note on visual design

The patterns above are about structure, not visuals. But landing pages also benefit from:

- **Card grids over bullet lists** for top entries (more scannable)
- **Icons or illustrations** for the top categories (faster recognition)
- **Generous white space** (landing pages should feel sparse, not dense)

These are implementation choices, not principles—but if the docs platform supports them, use them on landing pages and reserve dense layouts for detail pages.

---

## Anti-patterns to avoid

- **TOC-as-landing**: an alphabetical or sidebar-mirrored list. Adds no value over the sidebar itself.
- **Marketing-as-landing**: paragraphs of "why this matters" before any entry point. The reader didn't come here to be sold.
- **Everything-flat landing**: 30 links with no grouping. Forces the reader to scan all.
- **No-next-steps detail pages**: pages that end without routing the reader anywhere. Dead ends.
- **"Learn more" as the only CTA**: vague, low-information. Users don't click vague links.
