# Maintenance and Health Check

## Cadence

### Daily

Run read-only structural checks: frontmatter, links, ontology/migration validation where applicable, and the health report. Alert only on failures or meaningful metric changes.

### Weekly

Review `00_Hot.md`, active projects, recent decisions, recent CHAT/SUM promotion candidates, ingest disposition, and cascade candidates. Apply only bounded, reversible local updates.

### Monthly

Run a retrieval test and review GitHub for useful Wiki/Hermes patterns. Classify candidates as `adopt-now`, `validate-first`, `defer`, or `do-not-adopt`. Record the rationale before changing structure or policy.

## Health checks

Track metrics with explicit denominators:

- total Markdown and curated pages;
- broken wikilinks, separating raw-reference candidates;
- orphan curated pages;
- duplicate titles;
- missing or invalid frontmatter;
- quality metadata coverage;
- stale and due-review pages;
- project status/next-action coverage;
- source hash drift;
- maintenance reminder status.

A zero stale count is not proof that every page is current if valid `updated` metadata is missing.

## Safe change sequence

1. Run the health harness and save the baseline.
2. Separate structural findings from semantic decisions.
3. Present cascade candidates before editing.
4. Never mass-update, move, merge, or delete without approval.
5. Verify links, metadata, index, log, and health report after changes.
6. Append maintenance history to the end of the log.
