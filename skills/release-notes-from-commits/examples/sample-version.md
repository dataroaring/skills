# Worked example: one version section

This shows the target output for a single version, derived from the commits between
`tag-selectdb-cloud-26.0.2` and `tag-selectdb-cloud-26.0.3` and cross-checked against
the Apache Doris 4.0.5 release page. Note: New Features / Improvements / Bug Fixes
groups, a one-line upstream-base note, and every bug fix stating its trigger condition.

```markdown
## v26.0.3 (April 12, 2026)

This release incorporates Apache Doris v4.0.5 along with VeloDB-specific enhancements.

New Features

- Added support for ASOF JOIN, which matches each row to the closest preceding row in time and is useful for time series analysis.
- Added ORDER BY and LIMIT clauses to UPDATE and DELETE statements.
- Enhanced full-text search with BM25 relevance scoring, including phrase-level scoring, added prefix and phrase-prefix queries, and made it possible to use a MATCH result as a projected virtual column.

Improvements

- Raised the default partition limit to 20000.
- Changed the default search function mode from standard to Lucene.
- Extended the NDV approximate distinct count function to support the decimalv2 type.
- Improved Paimon catalog performance.
- Reduced memory usage during data loading.

Bug Fixes

- Fixed the abs() function returning an incorrect result for decimalv2 values. You are affected if you call abs() on a column or expression of the legacy decimalv2 type.
- Fixed SUM and AVG failing with a type error when given JSON input, such as SUM over a json_extract result. These aggregations now work by coercing the JSON value to DOUBLE.
- Fixed array_apply failing with a type error on arrays that contain LARGEINT values.
- Fixed the query cache returning incorrect results when different subcolumns of the same Variant column were read. You are affected only if the query cache is enabled and you query more than one subcolumn of a Variant column.
- Fixed incorrect results from ORDER BY ... LIMIT (TopN) queries over an outer join when the sort key comes from the nullable side of the join.
- Fixed crashes when reading Iceberg tables that have both undergone a schema change and use equality deletes.
- Fixed query errors when reading an Elasticsearch catalog table whose keyword field contains array data.
- Hardened LDAP filter handling to prevent injection. Relevant only to deployments that use LDAP authentication.
```

## Why each choice was made

- **SUM/AVG** was first written as "incorrect results from improper type coercion." Reading upstream PR #59602 showed the real bug was a *query failure* on JSON input. The note was corrected. Always verify ambiguous fixes against the PR.
- **TLS/mTLS, the enterprise license module, Aliyun KMS, and Apache Ozone** were dropped because they are not exposed in the cloud product, even though they appear in the commits and (for LDAPS) on the upstream page.
- Internal cloud plumbing (file cache, peer read, warm-up, recycler, meta-service RPC) was excluded; where it had a user benefit, it was generalized (for example "Reduced memory usage during data loading").
- Every bug fix names the operation and condition so a user can tell whether they are affected.
