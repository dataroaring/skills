# Writing Style — English Developer Documentation

Load this file when writing or editing English documentation prose, headings, code comments, or link text. The principles in `SKILL.md` cover structure and organization; this file covers sentence and paragraph craft.

The rules below are extracted from Stripe's documentation as the working reference, supplemented by Google Developer Documentation Style Guide and Microsoft Writing Style Guide where they converge. When sources disagree, Stripe wins—it's the highest-trafficked developer documentation in the industry and the de facto NA standard.

This is a style guide, not a grammar checker. Apply rules with judgment. A sentence that breaks one rule but reads well is better than a sentence that follows all rules and reads stiff.

---

## The core stance

Stripe-style English documentation has one defining quality: **the reader is treated as competent and busy.** Every sentence assumes the reader can act, doesn't need motivation, and would rather read 5 words than 15.

This produces a writing style that feels:
- **Direct** — no warm-up sentences, no "in this section we will..."
- **Imperative** — instructions sound like instructions, not suggestions
- **Specific** — concrete nouns and verbs, not abstractions
- **Confident** — no hedging where the answer is known

If a sentence sounds like it's apologizing, hedging, or warming up, cut it or rewrite it.

---

## Rule 1 — Lead with the verb

Every step, instruction, or action sentence should start with the verb. The subject is implied to be the reader.

**Good** (Stripe pattern):
> Add the `{CHECKOUT_SESSION_ID}` template variable to the `success_url`.
> Retrieve the Checkout Session from the API with the `line_items` property expanded.
> Check the `payment_status` property to determine if it requires fulfillment.

**Bad** (verbose, indirect):
> You should add the `{CHECKOUT_SESSION_ID}` template variable to the `success_url`.
> The Checkout Session can be retrieved from the API.
> It is recommended that you check the `payment_status` property.

**Check questions**:
- Does the sentence start with "You should", "You can", "It is recommended", "We suggest"? Cut those words.
- Is the verb buried in the middle of the sentence? Move it to the front.
- Is the sentence in passive voice ("X is done by...")? Rewrite in active voice.

**Exception**: when explaining behavior the system does (not the user), passive or system-as-subject is fine. "When the payment succeeds, Stripe sends a `checkout.session.completed` event."

---

## Rule 2 — Action first, explanation second

When a sentence has both an instruction and a reason, put the instruction first.

**Good**:
> Add `{CHECKOUT_SESSION_ID}` to the `success_url`. This is a literal string—don't substitute it with an actual session ID. The substitution happens automatically after the customer is redirected.

**Bad**:
> Because the substitution happens automatically and the placeholder is a literal string that shouldn't be replaced, you should add `{CHECKOUT_SESSION_ID}` to the `success_url`.

The principle: the reader's brain wants the action first to know what to do, then the explanation to understand why. Reversing this order forces them to hold the rationale in memory while waiting for the verb.

**Check questions**:
- Does the sentence start with "Because", "Since", or "In order to"? Try inverting—the imperative usually wins.
- Is the main verb in a subordinate clause? Promote it to the main clause.

---

## Rule 3 — Short sentences. Aim for 15 words or fewer.

Stripe's sentences are aggressively short. Long sentences in technical docs nearly always pack two ideas that should be two sentences.

**Good**:
> Set up a webhook event handler. Stripe sends payment events directly to your server. This bypasses the client entirely.

**Bad**:
> You should set up a webhook event handler so that Stripe can send payment events directly to your server, which has the advantage of bypassing the client entirely and providing the most reliable way to confirm payment.

**Check questions**:
- Is the sentence longer than 20 words? Look for "and", "which", "so that", "because"—those are split points.
- Does the sentence make more than one point? Split it.

**Exception**: lists with parallel structure can be a single long sentence. "The API accepts `card`, `bank_account`, `card_present`, and `payment_method` as values." Don't artificially split parallel lists.

---

## Rule 4 — Headings: 5 words or fewer, verb-first when actionable

Stripe's actual section headings:
- "Create a payments form"
- "Set up a webhook"
- "Fulfill orders"
- "Customize redirect behavior"
- "Save payment details during payment"

Patterns to follow:
- **For how-to and tutorial sections**: verb + object. "Create a cluster", "Configure alerts", "Connect a workspace".
- **For reference sections**: noun phrase. "Cluster status codes", "API rate limits".
- **For explanation sections**: noun phrase or short question. "How replication works", "Compute pricing".

Patterns to avoid:
- Gerund-heavy ("Creating a cluster" instead of "Create a cluster")—use gerunds only for explanation headings, not action headings.
- "Overview" / "Introduction" / "About"—every page has these implicitly; the heading should say what the section actually covers.
- Long descriptive titles ("A comprehensive guide to setting up your first cluster")—cut to 3-5 words.
- Marketing-style titles ("Unlock the power of your data")—headings are functional, not promotional.

**Check questions**:
- Is the heading over 5 words? Find what can be cut.
- Does it start with a gerund where a verb would work? "Creating" → "Create".
- Is it functional, or is it trying to sell?

**Title case vs. sentence case**: Use **sentence case** for all headings (Stripe, Google, Microsoft all do this). "Create a payments form", not "Create A Payments Form".

---

## Rule 5 — Link text is a command or a noun, never "click here" or "learn more"

The link text should describe what the user will find on the other end, in their own scanning context.

**Good**:
> [Start building your checkout integration]
> [Explore the demo]
> [See API rate limits]
> [Configure your webhook endpoint]

**Bad**:
> Learn more [here].
> [Click here] to read about webhooks.
> For more information, [see this page].

**Check questions**:
- Can the link text be read in isolation (with no surrounding sentence) and still make sense? It should.
- Does it contain "here", "this", "more"? Rewrite.
- Is it a verb phrase (action) or a clear noun phrase (destination)? One of those two.

---

## Rule 6 — Use precise domain nouns, capitalized consistently

Stripe treats product concepts as proper nouns: **Checkout Session**, **Payment Intent**, **Customer**, **Line Items**, **Billing Portal**, **Dashboard**.

The convention:
- **Capitalize when referring to the concept** ("Create a Checkout Session.")
- **Lowercase when used generically** ("Create a session to track the user's flow.")
- **Code identifiers stay in code formatting** (`checkout_session`, `payment_intent`)

This serves two purposes: (a) signals to the reader which terms are Stripe-domain vs. generic English, (b) lets the reader build a mental glossary by visual cue.

For VeloDB Cloud, apply the same pattern to:
- **Cluster**, **Workspace**, **SQL Editor**, **Workload Group**, **Routine Load**, **Query Audit**

**Check questions**:
- Is this a domain concept? Capitalize. Is it a generic English word being used loosely? Lowercase.
- Are you using the same capitalization on this page that other pages use? Check.

---

## Rule 7 — Code examples include comments that serve as navigation

Stripe's code comment pattern is consistent and worth copying:

```text
# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<stripe-secret-key>')
```

Notice what the comments do:
1. **Warn about a common mistake** (don't hardcode keys).
2. **Link to the canonical reference** (best practices doc).
3. **Tell the reader where to do the prerequisite action** (Dashboard URL).

This makes the code block self-sufficient: a reader who copies just the code (not the surrounding prose) still has the most important guidance inline.

**Apply this pattern**:
- For every non-obvious value, add a comment with a link to where the reader gets it.
- For every common mistake, add an inline warning comment.
- Don't comment what the code obviously does. Comment what the reader can't see.

**Bad** (comments restate the code):
```text
# Create a Stripe client
client = Stripe::StripeClient.new('<stripe-secret-key>')
# Create a session
session = client.v1.checkout.sessions.create(...)
```

**Good** (comments add what the code can't show):
```text
# Find your keys at https://dashboard.stripe.com/apikeys
client = Stripe::StripeClient.new('<stripe-secret-key>')

session = client.v1.checkout.sessions.create(
    success_url='https://example.com/success',
    # `mode: subscription` is required for recurring billing
    mode='subscription',
)
```

---

## Rule 8 — Placeholders use angle brackets and kebab-case

Stripe uses two distinct patterns:
- **Literal placeholders the user replaces**: `{{PRICE_ID}}` or `<your-cluster-id>` — clearly visually distinct from real code.
- **System-generated literals the user passes through**: `{CHECKOUT_SESSION_ID}` — a literal string Stripe substitutes at runtime.

**Pick one convention per project and apply it everywhere.** For VeloDB, the recommended convention:
- User-replaced: `<your-cluster-id>`, `<your-workspace-id>`, `<your-api-key>`
- System literals (rare): document explicitly when they appear.

**Anti-patterns** to avoid:
- Mixing `<id>`, `{id}`, `YOUR_ID`, `your_id` in the same doc set.
- Realistic-looking fake IDs (`cluster_abc123`) that readers might paste verbatim without realizing they're placeholders.
- Placeholders that don't visually differ from real code (`id` in plain text).

---

## Rule 9 — Don't apologize, don't oversell

**Cut these phrases on sight**:

| Cut | Reason |
|---|---|
| "Unfortunately, ..." | The reader doesn't need your sympathy; they need the fact. |
| "Please note that..." | If it's worth saying, say it. "Note:" callout if it's important. |
| "It's important to..." | Everything in the doc is important. Just state the thing. |
| "Powerful", "robust", "seamless", "intuitive" | Marketing words; show, don't tell. |
| "Simply ..." | If it were simple, you wouldn't need to write it. Implies the reader is slow. |
| "Easily ..." | Same as "simply". |
| "Just ..." | Same. |
| "As you can see..." | The reader can already see. |
| "We will now..." | Just do the thing. |
| "In order to" | "To" is shorter. |

**Replace with**:
- "Unfortunately, the API doesn't support X." → "The API doesn't support X."
- "It's important to set the timeout to at least 30 seconds." → "Set the timeout to at least 30 seconds."
- "VeloDB Cloud provides powerful workload management." → "VeloDB Cloud routes queries by workload group." (Show the capability instead of naming it.)

---

## Rule 9.5 — Use high-frequency verbs, accept technical nouns

This is the most counter-intuitive rule, so it deserves its own number. Stripe's documentation **feels simple** but isn't written with universally simple words. The pattern, verified by analyzing actual Stripe doc text against English word-frequency data:

**Action words (verbs) should be high-frequency.** Aim for Zipf ≥ 4.5—words a 12-year-old uses comfortably. The actual top verbs in Stripe docs are exactly this kind:

| Verb used | Zipf frequency |
|---|---|
| create | 5.02 |
| use | 5.81 |
| set | 5.59 |
| add | 5.09 |
| send | 5.11 |
| check | 5.31 |
| listen | 5.06 |
| select | 4.45 |
| save | 5.14 |
| handle | 4.79 |

**Cut "thesaurus verbs"**—words that exist mainly to sound formal:

| Cut | Replace with |
|---|---|
| utilize | use |
| initiate | start, create |
| facilitate | help, allow |
| leverage | use |
| commence | begin, start |
| subsequently | then, next |
| in order to | to |
| ascertain | check, find out |
| endeavor | try |
| terminate | end, stop |
| furnish | provide, give |
| demonstrate | show |
| necessitate | require, need |
| obtain | get |

**Technical nouns can be uncommon.** Words like `webhook`, `idempotent`, `asynchronous`, `payload`, `fulfillment`, `endpoint` all score low on frequency but are perfectly fine in Stripe's docs because **no simpler word means the same thing**.

The pattern: **simple verbs operating on technical objects.** Readers process the action instantly, then absorb the technical term. "Retrieve the Checkout Session" works because `retrieve` is one familiar word doing all the lifting; the new concept (`Checkout Session`) is the only thing the reader needs to learn.

**The test**: if a higher-frequency synonym fully captures the meaning, use it. If the term is genuinely technical with no plain-English equivalent, keep it.

**Why this matters more than "use simple words" in general**: vocabulary tier matters most for the verb of the sentence, because the verb is where the reader's brain decides "what action is this telling me to take." A familiar verb means instant comprehension. An unfamiliar verb forces a lookup. The noun can be technical because the reader knows they need to learn it anyway.

**A self-check tool is available**: `scripts/check_vocab.py` in this skill takes a draft and flags verbs with Zipf < 4.5, plus all "thesaurus verbs" in the cut list above. Run it on drafts before submitting for review.

---

## Rule 10 — Numbers, units, and formatting

**Numbers**:
- Spell out one through nine in prose. Use numerals for 10+.
- Always use numerals for measurements, ports, version numbers, percentages.
- "10 GB", not "10GB". Space between number and unit.

**Capitalization**:
- Sentence case for headings (as noted in Rule 4).
- Acronyms stay uppercase: SQL, API, URL, JSON, CSV.
- File extensions lowercase in prose: `.csv`, `.json`. Tools are capitalized as the vendor capitalizes them: Kafka, Flink, Spark.

**Code formatting in prose**:
- Wrap parameter names, function names, file paths, and CLI commands in backticks: "Set `max_workers` to 4."
- Don't backtick concept nouns: "Set the cluster to active mode." Not "Set the `cluster` to `active` mode."

**Lists**:
- Use numbered lists for sequential steps only.
- Use bulleted lists for unordered items.
- Start each bullet with a capital letter; end with a period only if the bullet is a full sentence.

---

## Rule 11 — Use callouts sparingly

Stripe uses callouts (Note / Warning / Caution) for genuinely important asides, not for every other paragraph.

**Use a Note callout for**: information the reader can succeed without but will appreciate knowing.
**Use a Warning/Caution for**: information the reader will fail or lose data without.

**Don't use callouts for**:
- General information that should be in the main flow.
- Marketing ("Note: VeloDB also offers...").
- Three callouts in a row—if everything is highlighted, nothing is.

If a page has more than 2-3 callouts, most of them probably belong in the main prose.

---

## Rule 12 — Compare with tables, not paragraphs

When introducing a feature with multiple options or variants, use a comparison table with consistent columns rather than describing each option in prose.

**Stripe pattern** (Checkout UI options):

| | Stripe-hosted page | Embedded form |
|---|---|---|
| Hosting | Stripe's domain | Your domain |
| Integration effort | 2/5 | 2/5 |
| UI customization | Limited | Limited |

The reader can compare across options by scanning a single column. Prose forces them to remember each option's details.

**When to use tables**:
- Comparing 2+ alternatives across the same dimensions.
- Listing parameters or options with consistent attributes.
- Mapping values (e.g., status codes to meanings).

**When not to use tables**:
- For sequential steps (use a numbered list).
- For prose-heavy content where the cells would be long (use sections instead).
- When there's only one option ("comparison" of one thing isn't a comparison).

---

## Rule 13 — Define key terms inline on first use

Stripe's docs heavily use this pattern—a key term, on first appearance in a page, gets its definition in italics and parentheses immediately:

> Test your integration in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) by simulating transactions.

The definition appears every time the term is introduced on a new page, not just once across all docs. This serves three readers:

- **First-time visitors** who landed here from Google with no prior context.
- **Returning readers** who forget what specialized terms mean.
- **LLM agents** that fetch a single page and have no access to a separate glossary.

**The rule**: when a domain-specific term first appears on a page, give a 1-2 sentence definition in italics and parentheses inline. Don't make the reader click out to a glossary.

**Apply this when**:
- The term is product-specific and not common English ("workload group", "tablet", "MoW")
- The term is common English used in a specialized way ("cluster" means something specific in VeloDB)
- The term has multiple possible meanings and you mean a specific one ("workspace" varies by product)

**Don't apply this for**:
- Standard technical terms with widely understood meanings (SQL, JSON, API)
- Terms already defined earlier on the same page
- Terms that have their own dedicated reference page that's the natural destination

**Format**:

```markdown
Use a *workload group* (A workload group is a named pool of compute 
resources that VeloDB Cloud uses to isolate and prioritize queries. 
Each group has its own CPU, memory, and concurrency limits.) to 
control how queries compete for resources.
```

Note: this works well in Markdown but renders differently in MDX or other formats. Some doc platforms support a `<Glossary term="sandbox">` component that produces the same effect with cleaner source. Either approach is fine; consistency within the doc set matters more than the specific syntax.

**Why it matters more in 2026**: LLM agents pulling a single page into context have zero awareness of your separate glossary. Inline definitions are the only way to make a page self-sufficient for AI consumption. This connects directly to Principle 8.

---

## Rule 14 — Define contractual terms with concrete lists, not adjectives

Words like "backward-compatible", "stable", "production-ready", "deprecated", "breaking change" are not self-explanatory. Two readers can disagree on what counts. **Replace adjectives with concrete enumerated definitions.**

**Stripe's pattern** (from their versioning docs):

> Stripe considers the following changes to be backward-compatible:
> - Adding new API resources.
> - Adding new optional request parameters to existing API methods.
> - Adding new properties to existing API responses.
> - Changing the order of properties in existing API responses.
> - Changing the length or format of opaque strings, such as object IDs, error messages, and human-readable strings.
> - ...

After reading this list, no developer can disagree about whether their proposed change is backward-compatible. The contract is **machine-checkable**, not interpretive.

**Where to apply this**:
- **API stability tiers** ("What does 'GA' vs 'public preview' vs 'beta' mean? What's guaranteed at each level?")
- **Backward compatibility** (what changes can land without bumping the major version?)
- **Deprecation policy** (how long does a deprecated feature stay supported? What warnings appear?)
- **SLA terms** ("99.9% uptime" — measured how? excluded windows?)
- **Pricing terms** ("compute usage" — billed how? what counts as a unit?)
- **Performance terms** ("low-latency", "real-time" — what number is the actual ceiling?)

**Check questions**:
- Does this term appear in support tickets or sales calls with people interpreting it differently? Define it.
- Could two readers acting on this doc make different decisions and both believe they followed it? Define it.
- Is there a number, list, or specific criterion behind the word? Surface it.

**Bad** (interpretive):
> Workload groups provide stable, production-ready isolation for queries.

**Good** (concrete):
> Workload groups are generally available (GA). VeloDB Cloud commits to: (a) no breaking changes to the API for 12 months following any deprecation announcement, (b) backward-compatible additions only on the existing API surface, and (c) maintained documentation for the lifetime of the feature.

The "good" version is harder to write, harder to commit to, and infinitely more useful.

---

## Rule 15 — Tag section headings with the surface they apply to

When a feature can be used through multiple surfaces (UI / API / CLI / SDK), make each section's surface explicit in the heading. Stripe does this with bracketed tags:

```markdown
## Create a card [Dashboard]

[UI-specific steps]

## Create a card [API]

[API-specific steps]

## Create a test purchase [Dashboard]

[UI-specific steps for this same operation]
```

The bracketed tag tells the reader **at heading-scan time** whether this section applies to them. A reader who's using the API doesn't have to read the Dashboard section to discover it's not for them.

**Alternatives**:
- Tabbed UI components (one tab per surface, all surfaces on one page).
- Separate pages per surface (with cross-links).
- The bracket tag (a single page, with parallel sections).

The bracket tag works best when:
- The operations on different surfaces map closely (same outcome, different steps).
- The page would be over-fragmented if split per surface.
- The reader benefits from seeing the parallel structure.

**Apply to VeloDB Cloud**: any operation available via Console + SQL + API + CLI (e.g., creating a cluster, configuring a workload group) should use surface tags or tabbed components, not interleaved prose.

**Format options**:

```markdown
## Create a cluster [Console]
## Create a cluster [SQL]
## Create a cluster [API]
## Create a cluster [CLI]
```

Or as H3 inside one H2:

```markdown
## Create a cluster

### Using the Console
### Using SQL
### Using the API
### Using the CLI
```

The bracket form is more scannable; the H3 form integrates better with auto-generated tables of contents. Pick one convention per doc set.

---

## Rule 16 — Open every page with one short sentence stating its purpose

Every Stripe doc page follows this pattern:

```markdown
# Error handling

Catch and respond to declines, invalid data, network problems, and more.

# Testing

Simulate payments to test your integration.

# Receive Stripe events in your webhook endpoint

Listen for events from Stripe on your webhook endpoint so your 
integration can automatically trigger reactions.
```

H1, immediately followed by a single sentence (rarely two) that states what this page is for. Not "Welcome to the X documentation." Not "This page covers X, Y, and Z." A single declarative sentence describing the reader's problem or outcome.

This sentence serves four jobs:
- Helps the reader confirm they're on the right page within 2 seconds.
- Becomes the page's `<meta description>` for search results.
- Becomes the page's summary in any LLM-indexed structure.
- Forces you (the writer) to articulate the page's purpose in one sentence—if you can't, the page is unfocused.

**Check questions**:
- Is your opening one sentence, or does it sprawl?
- Does it state what the reader can do or understand, not what the page contains?
- Could you cut "This page describes..." or "Welcome to..." and lose nothing?

**Good**:
> Catch and respond to declines, invalid data, network problems, and more.

**Bad** (states the page's contents, not the reader's outcome):
> This page contains information about error handling, including types of errors, how to catch them, and best practices.

**Bad** (welcome/marketing):
> Welcome to VeloDB Cloud's error handling documentation, where you'll learn about our powerful error handling capabilities.

---

## Rule 17 — Pair abstract principles with immediate concrete translation

When you state an abstract principle, follow it immediately with a concrete restatement. Stripe pattern:

> Treat the result of the API call as indeterminate. **That is, don't assume that it succeeded or that it failed.**

> Make sure your event destination isn't dependent on receiving events in a specific order. **Be prepared to manage their delivery appropriately.**

The pattern is **abstract sentence → "That is" / "In practice" / "Specifically" → concrete sentence**. Never let an abstract directive stand alone.

**Why this matters**: abstract words like "indeterminate", "idempotent", "robust", "graceful" have technical meanings that experienced developers know but novices interpret differently. The concrete sentence binds the abstract word to a specific behavior.

**Apply when you use any of these abstract words**: indeterminate, atomic, idempotent, eventually consistent, fault-tolerant, robust, graceful, resilient, optimal, efficient.

**Bad**:
> Webhook handlers should be idempotent.

**Good**:
> Webhook handlers should be idempotent. That is, if Stripe sends the same event twice, your handler should produce the same result both times—no duplicate database rows, no double-charging, no doubled side effects.

---

## Rule 18 — Tell readers "this error can occur when your integration is working correctly"

Many errors are not bugs—they're expected outcomes of valid integrations. A `card_declined` from a real issuer isn't a code problem. A `signature_verification_failed` from a malicious third party is the system working as designed.

But readers' default assumption is "I broke something." Without an explicit signal, every error becomes a debugging session.

**Stripe's solution**: include a one-sentence reassurance in the docs for any error/state/failure that is sometimes expected behavior.

> **Solutions**: This error can occur when your integration is working correctly. Catch it and prompt the customer for a different payment method.

This single sentence saves the reader from a fruitless investigation. Cost is small (one sentence per applicable error); benefit compounds across every reader who hits the case.

**Where to apply**:
- Error code documentation
- Warning messages explained in docs
- "Why did my job fail" pages
- Status pages for non-terminal states
- Any "expected but undesirable" behavior

**Don't apply to**:
- True bugs / true configuration errors (these need fixing, not reassurance)
- Critical errors that always indicate a problem (auth failures, permission errors)

**Apply to VeloDB Cloud**: query timeouts on user error, deliberate workload group throttling, validation failures from user-supplied SQL, replication lag during high write load. Any case where a sophisticated user might wrongly assume "something is broken on my end."

---

## Rule 19 — Use frequency words (Always / Sometimes / Rarely) to set expectations early

When multiple techniques or options exist, tell the reader **how often each one is needed**, not just what each one does:

```markdown
| Technique             | Purpose                              | When needed |
|-----------------------|--------------------------------------|-------------|
| Catch exceptions      | Recover when API call can't continue | Always      |
| Monitor webhooks      | React to notifications from Stripe   | Sometimes   |
| Use stored info       | Investigate past problems            | Sometimes   |
```

The "When needed" column is the highest-value column. Without it, readers don't know which techniques are foundational versus situational and may waste time implementing optional ones.

**Frequency vocabulary** (consistent across the doc set):

| Word | Meaning |
|---|---|
| **Always** | Every integration needs this. Skipping it produces broken behavior. |
| **Often** | Most integrations need this. Some legitimate cases skip it. |
| **Sometimes** | Specific situations require this. Many integrations skip it. |
| **Rarely** | Edge cases only. Default is to skip it. |
| **Optional** | Pure convenience. No correctness implication. |

**Apply this when**:
- The page introduces multiple methods to do something.
- The reader needs to know "where do I start" vs "I can skip this for now."
- The page lists features or APIs where coverage isn't required.

**Bad** (no frequency signal):
> VeloDB Cloud offers three ways to monitor workload health: built-in metrics, alerts, and query profile.

**Good**:
> VeloDB Cloud offers three ways to monitor workload health:
> - **Built-in metrics** — always-on dashboards. Every workspace uses these.
> - **Alerts** — recommended for production. Optional in development.
> - **Query profile** — deep-dive tool. Use only when investigating specific slow queries.

---

## Rule 20 — Use precise modal verbs; don't mix strength levels

Different modal verbs signal different levels of obligation. Mixing them confuses the reader about what's required.

**The hierarchy**:

| Phrase | Strength | Meaning |
|---|---|---|
| **You must** / **X requires** | Hard requirement | Skipping breaks behavior. Non-negotiable. |
| **You need to** | Strong requirement | Same as "must" but slightly softer tone. |
| **You should** / **It's a best practice to** | Strong recommendation | Skipping degrades quality but doesn't break. |
| **We recommend** | Recommendation | Suggested default. Reasonable to skip with cause. |
| **You can** | Capability | One option among several. No obligation. |
| **You might** / **You may want to** | Hint | Suggestion for specific cases. |

**Pick the right level for each statement, then stick to it.** Don't say "you can verify webhook signatures" if you mean "you must verify webhook signatures for production traffic." Don't say "you must add a description" if it's actually optional.

**Check questions**:
- Will the reader's integration break if they skip this? Use "must" / "requires".
- Will quality degrade but not break? Use "should" / "we recommend".
- Is this one of several valid options? Use "can".
- Is this a hint for a specific edge case? Use "might" / "may want to".

**Bad** (mixed strength, reader can't tell what's required):
> You can verify webhook signatures. We recommend that you must include an idempotency key. You should always handle errors.

**Good**:
> Verify webhook signatures for all production traffic—Stripe requires it. Include an idempotency key when creating or updating objects; we recommend this for any non-idempotent operation. Handle errors gracefully (see [Error handling](url)).

The good version uses three different strength levels intentionally: "requires" (hard), "recommend" (soft), "Handle" (imperative — assumed standard practice).

---

## Rule 21 — Proactively distinguish similar-but-different concepts

Readers regularly confuse pairs of similar concepts. Don't wait for them to make the mistake—name the distinction explicitly:

> In particular, make sure you're using the correct endpoint secret. **This is different from your API key.**

> The `customer` field accepts a Customer ID. **Don't confuse this with the customer's account ID, which has a different prefix.**

The pattern is **"X. This is different from Y."** Or **"X. Don't confuse this with Y."** It's one extra sentence, and it prevents a class of bugs that would otherwise generate support tickets.

**Apply this when**:
- Two concepts have similar names (`workspace_id` vs `workspace_name`, `api_key` vs `account_id`).
- Two concepts have similar shapes (both are IDs, both are tokens).
- Two concepts have related but distinct semantics (`access_token` vs `refresh_token`, "deleting a cluster" vs "pausing a cluster").
- A concept has a common alias from another product (Snowflake's "warehouse" vs VeloDB's "cluster" — readers from Snowflake will assume they're the same).

**Apply to VeloDB Cloud**:
- "Workspace" vs "Project" (if both exist)
- "Cluster ID" vs "Cluster name"
- "Workload group" vs "Resource group" (if both terms appear)
- "Pause cluster" vs "Stop cluster" vs "Delete cluster"
- "Routine Load" vs "Stream Load" (similar names, different mechanics)

**Format**:
> [Statement about X]. **This is different from Y** — [one-sentence distinction].

---

## Rule 22 — Acknowledge naming history transparently

Some names in any mature product are awkward—they reflect history, not current best naming. Trying to pretend the names are perfect makes the docs harder to read; reality contradicts the docs. Stripe's approach:

> Payment errors—sometimes called "card errors" for historical reasons—cover a wide range of common problems.

> For historical reasons, payment errors have the type `Stripe::CardError`. But in fact, they can represent a problem with any payment, regardless of the payment method.

The pattern: **acknowledge the awkward name + give the reason + state the actual scope**. This costs one sentence and prevents readers from being confused by a class name that doesn't match its current meaning.

**Where to apply**:
- A class/type/field whose name no longer matches its scope.
- A feature whose marketing name and internal name differ.
- A term that's correct now but used to mean something else.
- A unit or limit whose value has a non-obvious origin.

**For VeloDB Cloud, candidates**:
- Any feature inherited from Apache Doris with a name that doesn't fit the cloud product (e.g., `BE` for "backend node" — historically meaningful but opaque to NA enterprise users).
- Any field whose value range is constrained by Doris internals (e.g., a limit that's a power of 2 for historical reasons).
- Any term that VeloDB renames in the UI but keeps in the SQL syntax.

**Don't** apply this to:
- Names that are simply unfamiliar to new readers (those just need definition — see Rule 13).
- Names you can still change. If you can rename it cleanly, do that and skip the historical note.

**Format**:
> [Concept], **historically called [old name]** because [brief reason], [current accurate description].

---

## A self-check loop

After writing a draft, scan for these high-frequency issues:

1. **"You should" / "You can"** in instructional sentences → cut, use imperative.
2. **Long sentences** (over 20 words) → split.
3. **"Click here" / "learn more"** links → rewrite link text.
4. **Marketing words** (powerful, robust, seamless, simply, just, easily) → cut.
5. **"In order to"** → "to".
6. **Inconsistent placeholder style** → unify.
7. **Headings over 5 words** → cut.
8. **Code with no comments, or comments that restate the code** → rewrite comments to add what the code can't show.
9. **Domain terms used without inline definition** → add `*term* (1-2 sentence definition)` on first use.
10. **Contractual terms used as adjectives** ("stable", "production-ready", "backward-compatible") → replace with concrete enumerated criteria.
11. **Multi-surface operations interleaved in one section** → split into surface-tagged sections.
12. **Page opens with "Welcome to" or "This page covers"** → replace with one-sentence purpose statement.
13. **Abstract directive ("be robust", "be idempotent") with no concrete follow-up** → add "That is, ..." sentence.
14. **Error/failure documented without "can occur when integration is working correctly" reassurance, where applicable** → add it.
15. **Multiple methods/options listed with no frequency signal** → add "Always / Sometimes / Rarely" column or label.
16. **Mixed modal verb strength on the same page** ("must" / "should" / "can" used interchangeably) → audit and align with Rule 20 hierarchy.
17. **Similar concepts mentioned without a distinguishing sentence** → add "This is different from Y" note.

If a draft has zero matches on any of these, it's already in good shape. If a draft has matches on 5+, it needs another pass before review.
