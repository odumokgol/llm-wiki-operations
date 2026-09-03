# Schema and Metadata

## Page frontmatter

Refined pages should use:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | entity | comparison | query | project | decision | summary
tags: [controlled, tags]
sources: [raw/articles/source.md]
confidence: high | medium | low
ingest_disposition: new | update | disputed | no-material
evidence_status: grounded | partial | inferred | mixed
review_state: current | needs-review | disputed | archived
---
```

Project and decision pages may additionally use `status`, `domain`, `last_verified`, `next_review`, `privacy`, `lifecycle`, and `review_cycle`.

## Raw frontmatter

```yaml
---
source_url: https://example.com/source
ingested: YYYY-MM-DD
sha256: <body hash>
extraction_status: complete | partial | failed
---
```

The SHA-256 covers only the body after the closing frontmatter delimiter. Raw content is immutable; corrections belong in refined pages.

## Controlled classifications

### Ingest disposition

- `new`: material not represented in the Wiki.
- `update`: local enrichment of an existing page.
- `disputed`: conflicts with an existing claim or decision.
- `no-material`: preserve the source, but no refined page is warranted.

### Impact

- `none`: no existing claim, decision, or project state changes.
- `local`: one page or one bounded project is affected.
- `cascade`: multiple linked pages, decisions, or active projects may change.

### Evidence status

- `grounded`: source supports the main claims.
- `partial`: only part of the source was observable or extracted.
- `inferred`: interpretation is stronger than direct evidence.
- `mixed`: multiple evidence levels are present.

## Linking rules

- Prefer stable slug links with readable aliases.
- Do not create links to pages that do not exist.
- Use fewer correct links rather than mass-linking every noun.
- New or substantially updated pages should normally have at least two meaningful outbound links.
- Preserve source links even after promoting material into a concept, entity, project, or decision.
