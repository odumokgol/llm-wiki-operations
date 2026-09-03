# Source Ingestion

## Standard workflow

1. Identify the source and sensitivity boundary.
2. Preserve the extractable original under `raw/` before interpretation.
3. Record URL/path, date, extraction status, and body hash where possible.
4. Search `index.md` and relevant folders for existing entities, concepts, projects, and decisions.
5. Classify `new / update / disputed / no-material`.
6. Write or update the smallest appropriate refined page.
7. Add provenance and confidence; separate facts, interpretation, hypotheses, and confirmation items.
8. Check `none / local / cascade` impact.
9. Update index/navigation and append `log.md`.
10. Re-run link and metadata checks.

## Evidence boundary

Do not convert a headline, forecast, MOU, consultation, cooperation statement, or search snippet into a confirmed contract, revenue event, or decision. If extraction is incomplete, label it `partial` and preserve the original source for later review.

## Re-ingestion

For the same source, recompute the body hash. If unchanged, do not duplicate the page. If changed, record source drift, compare dates, and update the refined page only after checking whether the new material contradicts existing knowledge.

## Promotion threshold

- One-time observation: retain in a dated Query page.
- Repeated two or three times: consider updating an existing Concept or Entity.
- Confirmed choice: update a Decision page.
- Reusable comparison: create or update a Comparison page.
- Actionable work: connect to a Project Hub or backlog.

Always retain the original raw source and dated query after promotion.
