#!/usr/bin/env python3
"""check_vocab.py — Vocabulary check for English documentation drafts.

Checks four categories of issues:

1. Banned "formal English" verbs and phrases (utilize, initiate, leverage,
   commence, subsequently, in order to, etc.). These have higher-frequency
   replacements that always work in technical docs.

2. Low-frequency action verbs (Zipf < 4.0). These signal "thesaurus-style"
   writing where a more common verb may work.

3. Contractual adjectives (stable, production-ready, backward-compatible,
   etc.) that need concrete definitions on the page.

4. Mixed modal strength (must, should, recommend, can, may) that may signal
   inconsistent obligation levels.

Technical nouns (webhook, payload, asynchronous, etc.) are NOT flagged
even when low-frequency. Only words tagged as verbs (or known formal-verb
strings) are flagged.

USAGE:
    python scripts/check_vocab.py <file.md>
    python scripts/check_vocab.py - < draft.md         # read from stdin
    echo "Please utilize the API" | python scripts/check_vocab.py -

REQUIREMENTS:
    pip install wordfreq

EXIT CODES:
    0 — no hard violations found; soft warnings may still print
    1 — banned phrases found
    2 — usage error
"""

import sys
import re

try:
    from wordfreq import zipf_frequency
except ImportError:
    print("ERROR: wordfreq not installed. Run: pip install wordfreq", file=sys.stderr)
    sys.exit(2)

# --- Configuration ---

ZIPF_THRESHOLD = 4.0  # Threshold for flagging verbs as possibly too formal.
# Note: 4.5 is where Stripe's *most-used* verbs cluster, but normal docs
# routinely use 4.0-4.5 verbs (route, prevent, guarantee, validate). We
# flag below 4.0 to catch real outliers without drowning in false positives.

# Banned formal verbs/phrases with suggested replacements.
# Keys are matched case-insensitively as whole words/phrases.
BANNED_PHRASES = {
    "utilize": "use",
    "utilizes": "uses",
    "utilized": "used",
    "utilizing": "using",
    "initiate": "start, create",
    "initiates": "starts, creates",
    "initiated": "started, created",
    "initiating": "starting, creating",
    "facilitate": "help, allow",
    "facilitates": "helps, allows",
    "facilitated": "helped, allowed",
    "facilitating": "helping, allowing",
    "leverage": "use",
    "leverages": "uses",
    "leveraged": "used",
    "leveraging": "using",
    "commence": "begin, start",
    "commences": "begins, starts",
    "commenced": "began, started",
    "commencing": "beginning, starting",
    "subsequently": "then, next",
    "in order to": "to",
    "ascertain": "check, find out",
    "endeavor": "try",
    "endeavors": "tries",
    "endeavored": "tried",
    "terminate": "end, stop",
    "terminates": "ends, stops",
    "terminated": "ended, stopped",
    "furnish": "provide, give",
    "furnishes": "provides, gives",
    "demonstrate": "show",
    "demonstrates": "shows",
    "demonstrated": "showed",
    "necessitate": "require, need",
    "necessitates": "requires, needs",
    "obtain": "get",
    "obtains": "gets",
    "obtained": "got",
    # Filler that should be cut, not replaced
    "simply": "(cut)",
    "easily": "(cut)",
    "just": "(cut, unless contrast: 'just one' is fine)",
    "please note that": "(cut, or use a Note callout)",
    "it is important to": "(cut, just state the thing)",
    "it should be noted that": "(cut)",
    "as you can see": "(cut)",
    "unfortunately": "(cut, just state the fact)",
    # Rule 16 — page-opening fluff
    "welcome to": "(Rule 16: cut, open with a one-sentence purpose statement)",
    "this page covers": "(Rule 16: state the reader's outcome, not the page contents)",
    "this page describes": "(Rule 16: state the reader's outcome, not the page contents)",
    "this guide will": "(Rule 16: state the outcome directly without 'this guide')",
    "in this guide, you will": "(Rule 16: state the outcome directly)",
    "in this guide, we will": "(Rule 16: state the outcome directly)",
    "in this section, we": "(Rule 16: state the outcome directly)",
    "in this article": "(Rule 16: cut, redundant)",
}

# Soft-warning terms: contractual adjectives that need concrete definition.
# These aren't wrong to use—but each occurrence should be paired with a concrete
# definition on the page (a list, a number, a specific criterion). The script
# flags them so the writer can verify they did define them. Maps term to the
# question the writer should be able to answer.
CONTRACTUAL_ADJECTIVES = {
    "stable": "What changes are allowed without breaking this contract?",
    "production-ready": "What are the specific criteria for production-ready?",
    "production ready": "What are the specific criteria for production-ready?",
    "backward-compatible": "What changes count as backward-compatible?",
    "backwards-compatible": "What changes count as backward-compatible?",
    "backward compatible": "What changes count as backward-compatible?",
    "breaking change": "What changes count as breaking? Give a list.",
    "deprecated": "What's the deprecation timeline and support guarantee?",
    "deprecation": "What's the deprecation timeline?",
    "low-latency": "What's the actual latency number/ceiling?",
    "low latency": "What's the actual latency number/ceiling?",
    "real-time": "What's the actual time window?",
    "near real-time": "What's the actual time window?",
    "high-throughput": "What's the actual throughput number?",
    "high throughput": "What's the actual throughput number?",
    "scalable": "Scales to what number? Linear or sublinear?",
    "highly available": "What's the SLA number? What windows are excluded?",
    "secure": "Secure against what threat model?",
    "compliant": "Compliant with which specific standards?",
    "best practice": "Whose best practice? Documented where?",
    "best practices": "Whose best practices? Documented where?",
}

# Rule 20 — Modal verb strength levels.
# These don't trigger warnings on their own; the script counts occurrences per
# level and warns only if mixed strengths appear (suggesting inconsistent
# obligation signaling on the same page).
MODAL_VERB_LEVELS = {
    "hard": [
        r"\bmust\b",
        r"\brequires?\b",
        r"\brequired\b",
        r"\bcannot\b",
    ],
    "strong": [
        r"\byou should\b",
        r"\bit's a best practice\b",
        r"\bit is a best practice\b",
        r"\bbe sure to\b",
        r"\bmake sure\b",
    ],
    "soft": [
        r"\bwe recommend\b",
        r"\brecommended\b",
        r"\bconsider\b",
        r"\bencouraged\b",
    ],
    "capability": [
        r"\byou can\b",
        r"\boptional\b",
        r"\boptionally\b",
    ],
    "hint": [
        r"\byou might\b",
        r"\byou may\b",
        r"\bperhaps\b",
    ],
}

# Words to NEVER flag as low-frequency, because they are clearly
# technical nouns or domain terms (not verbs we'd want to swap).
# This list catches false positives from the verb detector.
TECHNICAL_TERMS_ALLOWLIST = {
    "webhook", "webhooks", "endpoint", "endpoints", "payload", "payloads",
    "asynchronous", "asynchronously", "idempotent", "idempotency",
    "fulfillment", "callback", "callbacks", "throttling", "throttle",
    "deserialize", "serialize", "serialization", "tokenize", "tokenization",
    "redirect", "redirects", "auth", "authentication", "authorization",
    "oauth", "jwt", "tls", "ssl", "json", "yaml", "csv", "tsv", "xml",
    "api", "apis", "sdk", "cli", "url", "uri", "https", "http",
    "kubernetes", "kafka", "flink", "spark", "doris", "velodb",
    "cluster", "clusters", "workspace", "workspaces", "namespace",
    "polling", "poll", "retries", "backoff", "subnet", "vpc",
    "schema", "schemas", "subscription", "subscriptions", "checkout",
    # Domain/product nouns common in data platform docs — not action verbs
    "cloud", "queries", "query", "metrics", "alerts", "logs", "audit",
    "ingest", "ingestion", "compute", "observe", "protect", "monitor",
    "monitoring", "warehouse", "warehouses", "pipeline", "pipelines",
    "shard", "shards", "replica", "replicas", "tablet", "tablets",
    "partition", "partitions", "rollup", "rollups", "materialized",
    # Common safe verbs that fall just under threshold but are fine in docs
    "navigate", "assign", "specify", "retrieve", "notify", "configure",
    "trigger", "validate", "validates", "validated", "verify", "verifies",
    "verified", "trigger", "triggers", "triggered", "register", "registered",
    "submit", "submits", "submitted", "expose", "exposed",
    "pause", "pauses", "paused", "pausing", "resume", "resumes", "resumed",
    "resuming", "deploy", "deploys", "deployed", "deploying",
    "rollback", "scale", "scales", "scaled", "scaling",
}

# Heuristic verb endings — words ending in these patterns are *likely* verbs
# (gerunds, past tense, third-person singular). Used as a quick filter
# before checking Zipf frequency.
VERB_ENDINGS = ("ing", "ed", "es", "s", "ize", "ise", "ate", "fy")

# Common words that look verb-like but aren't, used to suppress noise.
NOT_VERBS = {
    "settings", "things", "things", "during", "string", "strings",
    "billing", "during", "starting", "following", "matching", "containing",
    "is", "was", "has", "does", "this", "yes", "its",
    "address", "process", "access", "success", "business",
    "headers", "filters", "parameters", "users", "events",
    # Common nouns that get false-flagged as verbs by ending heuristic
    "analytics", "deployments", "deployment", "upgrades", "upgrade",
    "latency", "throughput", "metrics", "alerts", "policies",
    "permissions", "constraints", "dependencies", "guarantees",
    "limits", "limitations", "operations", "configurations",
    "resources", "components", "instances", "containers",
    "responses", "requests", "queries", "errors", "warnings",
    "nodes", "node", "tablets", "tablet", "buckets", "bucket",
    "indexes", "indices", "tables", "fields", "rows", "columns",
    "exceptions", "exception", "techniques", "technique",
    "integrations", "integration", "endpoints", "endpoint",
    "parse", "parses", "parsed", "parsing", "docs", "doc",
    "declines", "decline", "invalid", "failures", "failure",
    "stripe", "velodb", "doris", "snowflake", "databricks",
    "json", "yaml", "csv", "xml", "sql", "api",
    "signals", "signal", "handlers", "handler", "consumers", "consumer",
}


def is_likely_verb(word):
    """Cheap heuristic: word ends in a verb-typical suffix and isn't in noun list."""
    w = word.lower()
    if w in NOT_VERBS:
        return False
    if w in TECHNICAL_TERMS_ALLOWLIST:
        return False
    return any(w.endswith(suf) for suf in VERB_ENDINGS)


def read_input(arg):
    if arg == "-":
        return sys.stdin.read()
    try:
        with open(arg, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"ERROR: file not found: {arg}", file=sys.stderr)
        sys.exit(2)


def strip_code_blocks(text):
    """Remove fenced code blocks and inline code so we don't lint code identifiers."""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", "", text)
    return text


def find_banned_phrases(text):
    """Find all banned formal verbs/phrases. Returns list of (line_num, phrase, suggestion)."""
    hits = []
    for line_num, line in enumerate(text.splitlines(), 1):
        lower = line.lower()
        for phrase, suggestion in BANNED_PHRASES.items():
            # Word-boundary match for single words; substring for multi-word phrases
            if " " in phrase:
                if phrase in lower:
                    hits.append((line_num, phrase, suggestion, line.strip()))
            else:
                if re.search(rf"\b{re.escape(phrase)}\b", lower):
                    hits.append((line_num, phrase, suggestion, line.strip()))
    return hits


def find_low_frequency_verbs(text):
    """Find likely verbs with Zipf < threshold. Returns list of (line_num, word, zipf, line)."""
    hits = []
    seen = set()  # don't repeat the same word on the same line
    for line_num, line in enumerate(text.splitlines(), 1):
        words = re.findall(r"\b[A-Za-z]+\b", line)
        for w in words:
            wl = w.lower()
            key = (line_num, wl)
            if key in seen:
                continue
            if wl in TECHNICAL_TERMS_ALLOWLIST:
                continue
            if wl in BANNED_PHRASES:
                continue  # already caught by banned-phrase check
            if not is_likely_verb(wl):
                continue
            z = zipf_frequency(wl, "en")
            if 0 < z < ZIPF_THRESHOLD:
                hits.append((line_num, w, z, line.strip()))
                seen.add(key)
    return hits


def find_contractual_adjectives(text):
    """Find contractual adjectives that need concrete definitions on the page.
    Returns list of (line_num, term, prompting_question, line).
    These are soft warnings: the term may be fine if the page defines it concretely.
    """
    hits = []
    # Sort terms by length descending so longer matches win (avoid "best practice" 
    # and "best practices" both firing on the same span).
    sorted_terms = sorted(CONTRACTUAL_ADJECTIVES.keys(), key=len, reverse=True)
    for line_num, line in enumerate(text.splitlines(), 1):
        lower = line.lower()
        # Track which character spans on this line are already consumed by a match
        # to prevent overlapping reports.
        consumed = [False] * len(lower)
        for term in sorted_terms:
            question = CONTRACTUAL_ADJECTIVES[term]
            if " " in term or "-" in term:
                # Substring match for multi-word terms
                start = 0
                while True:
                    idx = lower.find(term, start)
                    if idx == -1:
                        break
                    if not any(consumed[idx:idx + len(term)]):
                        hits.append((line_num, term, question, line.strip()))
                        for i in range(idx, idx + len(term)):
                            consumed[i] = True
                    start = idx + len(term)
            else:
                # Word-boundary match for single words
                for m in re.finditer(rf"\b{re.escape(term)}\b", lower):
                    idx, end = m.span()
                    if not any(consumed[idx:end]):
                        hits.append((line_num, term, question, line.strip()))
                        for i in range(idx, end):
                            consumed[i] = True
    return hits


def audit_modal_verbs(text):
    """Count modal verb occurrences by strength level across the whole document.
    Returns a dict {level: count} and a list of sample (line_num, level, snippet) hits.
    Only used to warn when 3+ strength levels appear, suggesting inconsistent
    obligation signaling.
    """
    counts = {level: 0 for level in MODAL_VERB_LEVELS}
    samples = {level: [] for level in MODAL_VERB_LEVELS}
    lower_full = text.lower()
    for line_num, line in enumerate(text.splitlines(), 1):
        lower = line.lower()
        for level, patterns in MODAL_VERB_LEVELS.items():
            for pat in patterns:
                if re.search(pat, lower):
                    counts[level] += 1
                    if len(samples[level]) < 2:
                        samples[level].append((line_num, line.strip()))
                    break  # one match per line per level is enough
    return counts, samples


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)

    text = read_input(sys.argv[1])
    text = strip_code_blocks(text)

    banned = find_banned_phrases(text)
    low_freq = find_low_frequency_verbs(text)
    contractual = find_contractual_adjectives(text)
    modal_counts, modal_samples = audit_modal_verbs(text)
    # Levels that actually appear in the document
    active_levels = [level for level, c in modal_counts.items() if c > 0]
    modal_mixed = len(active_levels) >= 3

    if not banned and not low_freq and not contractual and not modal_mixed:
        print("No vocabulary issues found.")
        sys.exit(0)

    if banned:
        print(f"\n=== Banned formal phrases ({len(banned)} found) ===")
        print("These have simpler equivalents. Replace them.\n")
        for line_num, phrase, suggestion, line in banned:
            print(f"  L{line_num}: '{phrase}' → {suggestion}")
            print(f"        {line[:100]}{'...' if len(line) > 100 else ''}")
            print()

    if low_freq:
        print(f"\n=== Possibly low-frequency verbs ({len(low_freq)} found) ===")
        print(f"Zipf < {ZIPF_THRESHOLD}. Consider whether a more common verb would work.")
        print("(Technical nouns are skipped; if this flags a noun, it's a false positive.)\n")
        for line_num, word, z, line in low_freq:
            print(f"  L{line_num}: '{word}' (zipf={z:.2f})")
            print(f"        {line[:100]}{'...' if len(line) > 100 else ''}")
            print()

    if contractual:
        print(f"\n=== Contractual terms needing concrete definition ({len(contractual)} found) ===")
        print("These adjectives are fine to use IF the page defines them concretely.")
        print("Check each one: did you give a list, a number, or specific criteria?\n")
        for line_num, term, question, line in contractual:
            print(f"  L{line_num}: '{term}' — {question}")
            print(f"        {line[:100]}{'...' if len(line) > 100 else ''}")
            print()

    if modal_mixed:
        print(f"\n=== Mixed modal verb strength (Rule 20) ===")
        print("This page uses modal verbs at 3+ different strength levels.")
        print("Verify each obligation is at the right level. Hierarchy:")
        print("  hard (must/required) > strong (should/best practice) > soft (recommend)")
        print("  > capability (can/optional) > hint (might/may)\n")
        for level in ("hard", "strong", "soft", "capability", "hint"):
            if modal_counts[level] > 0:
                ln, snippet = modal_samples[level][0]
                print(f"  {level:12s} (count={modal_counts[level]:2d})  e.g. L{ln}: {snippet[:80]}")
        print()

    print(f"\nTotal: {len(banned)} banned, {len(low_freq)} low-frequency verb(s), "
          f"{len(contractual)} contractual term(s), "
          f"modal levels mixed: {modal_mixed}.")

    # Exit 1 only for hard violations (banned phrases). Soft warnings don't fail.
    if banned:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
