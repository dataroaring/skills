# Designing Documentation for Both Humans and LLMs

Load this file when designing docs for a product whose users include AI agents, LLM-assisted developers, or AI-coding tools (Cursor, Claude Code, Copilot, etc.). This is a 2025-2026 frontier in documentation design and is becoming a competitive differentiator.

---

## Why this matters

A growing share of developers consume documentation through an AI intermediary—Cursor pulling docs into context, Claude Code reading them via web fetch, ChatGPT answering "how do I do X with VeloDB" from the docs. For these readers, the consumer of your docs is **a language model**, not a human.

LLMs have different needs than humans:

| Humans need | LLMs need |
|---|---|
| Scannable layout, visual hierarchy | Plain text, predictable structure |
| Images, diagrams, callout boxes | Text equivalents of any visual content |
| Brief, action-oriented prose | Specific, precise prose with no ambiguity |
| Curated landing pages | Predictable, fetchable file paths |
| Interactive code playgrounds | Complete, copy-pasteable code blocks |

The good news: **most of these aren't in conflict**. Docs designed well for humans are usually also well-structured for LLMs. But there are specific moves that improve LLM-readability significantly, and a few that conflict.

---

## Stripe's approach: explicit dual-audience design

Stripe is leading on this. The webhooks documentation page opens with a section titled **"Start here: Install agent skills"**:

> Stripe recommends using official skills to integrate with the API using best practices. Follow the instructions below to learn how.
> 
> **Tip: Use curl instead of Fetch tools.** Skills are detailed 10–20 KB markdown files. Fetch tools summarize them. `curl -sL` guarantees the full content.
> 
> **Using `npx skills`**: Check if `npx` is installed on the system. If `npx` is available, run `npx skills add https://docs.stripe.com --list` to list available skills, then run `npx skills add https://docs.stripe.com --yes --skill <skill-name>` to install individual skills.

What's happening:
- The instructions are **written for an LLM agent**, not a human (notice "Check if `npx` is installed on the system").
- They give the agent a precise tool-use pattern (`curl -sL` rather than the agent's default fetch).
- They point to a **machine-readable skill index** at `https://docs.stripe.com/.well-known/skills/index.json`.
- They sit at the **top of the page**, ahead of human content—because if an LLM is reading, you want it to find this first.

This is "RTFM for robots." Stripe is treating LLM-consumption as a first-class use case, not an afterthought.

---

## Concrete moves for LLM-readable docs

### 1. Publish a machine-readable structure index

Have a known URL (e.g., `https://docs.example.com/.well-known/docs/index.json` or `llms.txt`) that lists:
- All doc pages with their titles, URLs, and 1-sentence summaries
- The Diátaxis type of each page (tutorial/how-to/reference/explanation)
- The product or topic each page belongs to

This lets an LLM agent quickly find the right page without crawling. Stripe uses this format; many others (Anthropic, Cloudflare) are adopting it.

### 2. Use `.md` URLs that return raw Markdown

Stripe lets you fetch `https://docs.stripe.com/webhooks.md` and get the raw markdown directly. Humans visit `/webhooks` and get HTML; agents fetch `/webhooks.md` and get text.

This is the single highest-leverage move: it makes your entire docs site fetchable by any agent without HTML parsing.

If your docs site can't easily do this, at least make sure:
- The HTML is clean and convertible to markdown (avoid heavy framework markup).
- The page's `<main>` content is clearly identifiable.

### 3. Write specific, unambiguous prose

LLMs have a harder time with implicit references than humans. Compare:

**Ambiguous (human-friendly, LLM-fragile)**:
> Click the button to start. You'll see a confirmation. Once it's done, you can use the new endpoint.

**Explicit (works for both)**:
> Click **Create endpoint**. The system shows a confirmation message. After the endpoint reaches `active` status, you can send events to it.

The explicit version uses:
- **Named UI elements** in bold (not "the button")
- **Specific outcomes** ("confirmation message" not "a confirmation")
- **Named states** (`active` status, not "once it's done")

Humans benefit from this too. LLMs depend on it.

### 4. Include text equivalents of all visual content

Every diagram should have a paragraph describing what it shows. Every screenshot should have an alt text or caption explaining the relevant element. Every video should have a transcript or summary.

This isn't just accessibility—it's the entire content for an LLM consuming the docs.

### 5. Include complete, runnable code—not snippets

Stripe's code examples include all imports, all setup, all error handling. Why? Because an LLM that pulls one code block into a user's project needs it to actually work. Snippets that assume "you already did X" leave the user (and the LLM) guessing.

For every code example:
- Include all imports/requires
- Include all setup (client initialization, env vars referenced)
- Include error handling for non-trivial cases
- Use real, named variables (not `x = ...`)

### 6. Use predictable file/URL paths

LLM agents often guess URLs. If your docs follow a pattern—`/{product}/{topic}/{page}.md`—the agent can predict where things are. Inconsistent paths (some at `/docs/`, some at `/guides/`, some at `/learn/`) force the agent to search.

### 7. Embed structured metadata

Each page should declare:
- Its title (in the H1)
- Its Diátaxis type (in metadata or visible)
- The product/section it belongs to
- Last updated date
- A 1-2 sentence summary near the top

These help both human readers and LLMs orient.

### 8. Consider a dedicated `llms.txt` or skill manifest

A growing convention: publish an `llms.txt` at your site root listing key docs URLs and what each covers, formatted for LLM consumption. This is analogous to `robots.txt` but for AI agents wanting curated entry points.

Stripe's version is at `/.well-known/skills/index.json`, providing structured agent skills. Other companies use plain markdown `/llms.txt`.

---

## Trade-offs and tensions

A few places where human and LLM optimization diverge:

### Long context vs. short attention spans

LLMs can read a 10,000-word page in seconds. Humans skim and bail at the 30-second mark. **The fix**: design the page so the human gets value from the first 200 words (TL;DR + clear next click), and the LLM has the depth it needs lower down.

### Visual hierarchy vs. plain text

A human reads headers and skims. An LLM treats headers as structural signals but reads the prose under them. **The fix**: make headers descriptive on their own (a human can skim "Verify webhook signatures with official libraries" and know what's there; an LLM uses it as a topical signal).

### Marketing voice vs. precise voice

Marketing voice (warm, persuasive, occasionally vague) helps humans engage. LLMs propagate that voice into their answers—including the vagueness. **The fix**: keep marketing voice out of docs entirely. Use precise voice always; if marketing wants warmth, that lives on the product pages, not the docs.

---

## Check questions for LLM-readiness

- Can your docs be fetched as raw markdown by an agent without scraping?
- Is there a single URL where an agent can get a structured index of all pages?
- Are UI elements, system states, and outcomes named explicitly (not "it" or "the result")?
- Does every code example run as-is without context the LLM can't see?
- Is there a machine-readable manifest (skills, llms.txt, sitemap with summaries)?
- If you fed your docs to an LLM and asked "how do I do X with this product," does it give a correct, complete answer?

---

## A note on Stripe's specific implementation

Stripe is currently the most aggressive at this, but the patterns are imitable:

- `.md` URLs for every page (one-line server config in most static site generators)
- A `/.well-known/skills/` structured index
- "Start here" sections explicitly addressing LLM agents
- Aggressively specific prose throughout

You don't need to do all of these. Start with `.md` URLs and explicit prose—those are the highest-leverage with the lowest cost.

---

## What this means for VeloDB Cloud

This is a real opportunity. Snowflake's docs are not LLM-optimized. Databricks's docs are not LLM-optimized. ClickHouse Cloud's docs are not LLM-optimized. **No NA data platform competitor has invested here yet.**

Concrete moves to consider:
- Publish raw markdown URLs for every doc page
- Add an `llms.txt` at the docs site root with structured entry points
- Add a "For AI agents" section to high-traffic pages (cluster setup, SQL examples)
- Write code examples that are runnable without external context
- Match Stripe's level of explicit prose ("Click **Create cluster**" not "click the button")

This is a one-time investment with a long compounding payoff: every Cursor user, every Claude Code user, every developer asking ChatGPT "how do I use VeloDB" gets a better answer because the docs were designed for the LLM in the middle.
