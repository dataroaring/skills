---
name: Release Notes from Commits
description: This skill should be used when the user asks to "generate release notes", "write release notes", "update release notes", "create changelog", "summarize a release", "what changed in version X", or to document new versions/tags of VeloDB Core (or Apache Doris based products) for end users. Generates user-facing release notes derived from git commits between tags, with the upstream release page used only as a completeness cross-check. Emphasizes user impact: what changed, who is affected, and whether it is in the product.
---

# Release Notes from Commits

Generate end-user release notes for a database/data-platform product (default context: **VeloDB Core**, a cloud product based on **Apache Doris**) by summarizing the git commits between two release tags. The commits are the source of truth; any upstream vendor release page is only a completeness check.

## Core principle

**Generate from commits, not from the upstream release page.** Read the actual commits between the previous tag and the new tag, then summarize the user-facing ones. Use the upstream page (for example the matching Apache Doris release note) only to verify you did not miss anything, never as the primary source. If you start from the upstream page you will both miss product-specific work and include items that are not in the product.

## Workflow

1. **Find the gap.** Compare the tags in the code repo against the versions already documented.
   - List tags: `git tag | grep -E "<series>" | sort -V`
   - Find where the docs stop, and generate notes for every missing tag.

2. **For each new tag, gather facts:**
   - **Release date** = the tag's commit date: `git log -1 --format=%ci <tag>`. Convert to a readable date (for example "April 12, 2026"). Do not invent dates.
   - **Upstream base version** (for Doris-based products): read the build version at that tag, for example `git show <tag>:gensrc/script/gen_build_version.sh` and read the `DORIS_BUILD_VERSION_MAJOR/MINOR/PATCH` defaults. This tells you which upstream patch was merged.
   - **Commits** in range: `git log --format="%s" <prev-tag>..<tag>`. For large ranges, also pull bodies for non-obvious fixes: `git show -s --format="%s%n%b" <hash>`.

3. **Classify each commit** into one of: keep (user-facing), drop (internal/out-of-product), or fold (merge into a grouped line). See "What to include vs exclude".

4. **Write the section** grouped as **New Features / Improvements / Bug Fixes** (omit empty groups). Newest version first. Keep a one-line note of the upstream base, for example: "This release incorporates Apache Doris v4.0.5 along with VeloDB-specific enhancements."

5. **Cross-check** against the upstream release page for that base version. If the page lists a user-facing item you dropped, reconsider and add it back. The page is a checklist, not the source.

6. **Verify and apply** to all relevant doc copies (see "Doc mechanics").

## What to include vs exclude

The bar is **user-observable impact**. A user reading the note should be able to tell whether it affects them.

**Include (user-facing):**
- SQL syntax, functions, and behavior changes (for example ASOF JOIN, ORDER BY/LIMIT on UPDATE/DELETE, a new hash function).
- Catalogs, connectors, and integrations users configure (Paimon, Iceberg, JDBC, Elasticsearch).
- Full-text search / index capabilities.
- Observable performance gains (faster queries, lower load memory, better read performance after scaling). Describe the **user benefit**, even if the mechanism is internal.
- Correctness fixes (wrong results), crashes, and failures users hit during normal operations (failed loads, failed queries, failed restore, cancelled jobs).
- Default and limit changes (for example raising a default partition limit).

**Exclude (internal implementation / plumbing):**
- File cache internals, peer read, warm-up internals, recycler, meta-service RPC counts, FoundationDB, bthread, segment footer, memtable/segment memory internals, LRU mechanics.
- Logging verbosity, internal-only metrics, and observability that requires no user action.
- Pure refactors, test/CI/build/docker/regression/compile changes, dependency bumps, chores.
- Capabilities present in the upstream **core** but **not exposed in the product**. When unsure, ask the user or flag it; do not assume a core feature ships in the product.

**Product-availability filtering (critical for VeloDB Cloud):** some upstream features are not enabled in the cloud product. Past reviewer guidance on this project:
- Do **not** mention **TLS / mTLS / certificate-based authentication / LDAPS** (not supported in the product). The LDAP injection-hardening *fix* can stay as a bug fix, but drop "LDAPS support".
- Do **not** mention the **enterprise license module** or other enterprise-only machinery.
- Drop vendor-specific storage that is not the product's cloud (for example **Aliyun KMS**, **Apache Ozone**, and **DLF over OSS-HDFS** are Alibaba/OSS-oriented and not shown for the AWS-based product). Keep the generic part of such a line (for example Paimon REST catalog and partition data types).
- When the upstream page lists something you must exclude (such as LDAPS), say so to the user rather than silently keeping it.

## Bug fixes must answer "Am I affected?"

This is the most important quality bar. Every bug-fix line must name the **operation and the triggering condition** so a user can self-assess. Do not write "Fixed incorrect results from SUM and AVG" with no context.

- Bad: "Fixed incorrect results from the SUM and AVG functions caused by improper type coercion."
- Good: "Fixed SUM and AVG failing with a type error when given JSON input, such as SUM over a json_extract result."

Other patterns:
- "Fixed the query cache returning incorrect results ... You are affected only if the query cache is enabled and you query more than one subcolumn of a Variant column."
- "Fixed JDBC catalog issues ... You are affected if you query PostgreSQL or SQL Server through a JDBC catalog."
- "Fixed ALTER VIEW not propagating ... You are affected only in multi-frontend deployments."

When the commit subject is too terse to state the condition, **read the upstream PR** (for example `https://github.com/apache/doris/pull/<n>`) to learn the real trigger. Verify rather than guess: in one case a "wrong result" fix was actually a query *failure*, and the note had to be corrected. If the trigger truly cannot be pinned down, state it at the feature level (for example "if you extract string values from JSON") rather than inventing specifics.

## Writing style

- **Whole sentences** in prose and bullets; not keyword fragments or `(a, b, c)` term dumps. Reference tables may stay terse.
- **No em dashes or en dashes** (— –). Rewrite with a colon, comma, parentheses, or two sentences.
- **English only** for these docs. Skip translations (for example `i18n/ja/`) and do not block on them.
- Group related fixes into one line when there are many similar ones (for example "several query planner issues that could return incorrect results, including ...").
- Keep the upstream-base note per version, without hyperlinking unpublished upstream pages (3.1.5/3.1.6 may not exist publicly even when merged); link only pages you verified return 200.

## Doc mechanics (VeloDB docs repo)

- Core release notes live at `cloud_versioned_docs/version-<X>.x/release-notes/core-release-notes/<file>.md` (for example `v41.md`, `v260.md`). Newest version section goes at the top.
- The **v4.1** notes appear in **both** `version-4.x` and `version-26.x`; keep the two `v41.md` copies **identical** (write one, copy to the other, then `diff` to confirm).
- After writing, verify: `grep` for forbidden terms (`tls`, `mtls`, `ldaps`, `enterprise`, `license`, `aliyun`, `ozone`, and internal-plumbing terms) and for em/en dashes; both should return nothing.
- Open a PR against `master`. End the PR body with the Claude Code attribution line.

See `examples/sample-version.md` for a fully worked version section.

## Quick command reference

```bash
# tags in a series, sorted
git tag | grep -E "4\.1|26\.0" | sort -V

# release date for a tag
git log -1 --format=%ci <tag>

# upstream base version merged at a tag (Doris-based products)
git show <tag>:gensrc/script/gen_build_version.sh | sed -n '30,42p'

# user-facing commit subjects between tags
git log --format="%s" <prev-tag>..<tag>

# full message for a non-obvious fix
git show -s --format="%s%n%b" <hash>
```
