# VeloDB Cloud — Documentation Context

Load this file when the documentation task involves VeloDB Cloud specifically. It contains the project-specific conventions that override or specialize the general principles.

## Sidebar / Top-level structure

The current top-level taxonomy (use these exact labels):

- **INGEST** — data ingestion paths (Stream Load, Routine Load, Spark/Flink connectors, S3 import, CDC)
- **COMPUTE** — clusters, warehouses, workload management, scaling
- **OBSERVE** — metrics, alerts, query audit, query profile
- **PROTECT** — security, access control, audit log, compliance

These four are the NA SaaS–aligned categories. Do not invent new top-level categories without a strong reason; if a new feature doesn't fit cleanly into one of the four, consider whether it belongs as a sub-page of an existing category.

**Rationale**: This taxonomy mirrors Snowflake/Databricks/MongoDB Atlas patterns (action-verb categories at the top), not Apache Doris's internal team structure.

## Terminology rules

### Use these terms

| Use | Not | Why |
|---|---|---|
| Cluster | Instance, Warehouse, Group | "Cluster" matches NA enterprise DBaaS conventions (Snowflake, MongoDB, CockroachDB). "Warehouse" is Snowflake-specific and confusing. "Instance" is too generic. |
| Workspace | Project, Organization | "Workspace" is the NA SaaS convention for the top-level tenancy unit (Databricks, Notion, Linear). |
| SQL Editor | Query Console, SQL IDE | "SQL Editor" matches Snowflake/Databricks. Avoid "console" because it conflicts with the cloud management console. |
| Query Audit | Query History, Query Log | "Audit" emphasizes the security/compliance use case; "history" suggests ephemeral. |
| Metrics | Monitoring data, Stats | "Metrics" is precise; "monitoring" is the section name, not the data type. |
| Alerts | Notifications, Warnings | "Alerts" is the standard observability term. |

### Doris vs. VeloDB terminology

When the underlying Apache Doris feature uses a different name than the VeloDB Cloud UI surface:

- **Document the VeloDB Cloud name as primary.** Mention the Doris equivalent once, parenthetically, for users coming from the OSS docs.
- Example: "Workload Groups (Apache Doris: `WORKLOAD GROUP`) let you assign compute resources..."
- Do not maintain two parallel naming systems. Pick one (the VeloDB UI name) and stick to it.

## English / 中文 alignment rules

VeloDB Cloud docs ship in both English and Chinese. Follow these rules:

### Structural alignment
- Section structure (URL paths, section names) **must be identical** across EN and 中文.
- If a section is split or merged in one language, do the same in the other in the same release.
- Page titles translate the *meaning*, not the words. "Get Started" → "快速开始", not "获取开始".

### Terminology consistency
- Maintain a glossary mapping for every technical term. Examples:
  - Cluster → 集群
  - Workspace → 工作空间
  - SQL Editor → SQL 编辑器
  - Workload Group → 工作负载组
  - Query Audit → 查询审计
  - Routine Load → 例行导入 (do NOT translate as "常规加载")
- Apache Doris–origin terms keep their established 中文 translation where one exists in the Doris community; don't reinvent.

### Code, error messages, and UI strings
- Code examples stay in English in both versions.
- Error messages in the UI are bilingual (English first, 中文 in parentheses or via locale toggle).
- Doc references to UI labels match the user's locale: in 中文 docs, refer to the 中文 UI label.

## Monitoring section structure (current restructure)

The Monitoring section is being restructured. The target structure is:

```
OBSERVE/
├── Overview                 (landing page — what's in this section)
├── Metrics                  (data: what metrics exist, how to read them)
├── Alerts                   (data: rules, channels, alert history)
├── Query Audit              (data: query log, slow queries, audit trail)
└── Query Profile            (tool: deep-dive performance analysis per query)
```

**Design notes**:
- These are **parallel sub-pages**, not nested. Following Stripe/Snowflake convention.
- Each sub-page is its own Diátaxis cluster (a Metrics overview + how-to + reference triad, etc.).
- "Overview" is a landing page that explains *when to use each sub-page*, not a TOC.

## Empty state ↔ docs linking

VeloDB Cloud is investing in empty states for Clusters / Data Ingestion / SQL Editor / Monitoring. These should bidirectionally link with docs:

- **Empty state → Docs**: every empty state has a "Learn more" link pointing to the relevant Get Started or Quickstart page.
- **Docs → Product**: every Quickstart and major how-to ends with a CTA like "Open in Console" or "Try in SQL Editor" with a deep link.

This implements Principle 5 (docs as product funnel) for the VeloDB context.

## Internal vs. external audience

VeloDB docs serve two primary audiences:

1. **NA enterprise evaluators** — comparing against Snowflake, Databricks, ClickHouse Cloud. They care about: enterprise security, pricing transparency, integrations, SLAs. Language: formal, precise, NA SaaS conventions.
2. **Existing Doris/OSS users** migrating to managed** — they know the engine, need to learn the control plane. Language: assumes Doris knowledge, focuses on what's *different* in Cloud.

When writing, ask which audience the page primarily serves. Don't try to serve both in one page; cross-link instead.

## What NOT to do

- Don't import Apache Doris docs structure wholesale. The OSS docs are reference-heavy and engineer-organized; VeloDB Cloud docs need to be task-organized for NA enterprise buyers.
- Don't use Chinese-localized SaaS terminology that doesn't have NA traction (e.g., avoid "实例" when the NA convention is "cluster").
- Don't put release notes inside feature docs. Release notes are their own section.
- Don't write internal product strategy into docs ("our differentiation vs. Snowflake is..."). That belongs in marketing, not docs.
