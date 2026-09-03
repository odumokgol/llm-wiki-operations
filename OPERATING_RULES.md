# Operating Rules

## Purpose

This document is the shared operating baseline for Hermes and ChatGPT when maintaining an LLM Wiki. It defines **how the Wiki is operated**, not where private knowledge is stored.

## Storage roles

| System | Role | Authority |
|---|---|---|
| GitHub `llm-wiki-operations` | Shared operating rules, templates, safe scripts, and change history | Source of truth for operating method |
| OneDrive `100_LLM Wiki` | Hermes-managed canonical personal/work knowledge vault and sensitive raw evidence | Canonical source for Hermes knowledge |
| Google Drive `Master LLM_Wiki` | ChatGPT-facing copy containing only approved, non-sensitive knowledge | Read/reference copy, not a second editable master |

Do not treat OneDrive and Google Drive as equal editable masters. If both contain a page, OneDrive remains authoritative and Google Drive is refreshed only through an intentional, reviewed export/copy process.

## Wiki structure

```text
raw/                  immutable source captures
concepts/             reusable ideas and topics
entities/             people, tools, products, organizations
comparisons/          structured alternatives
queries/              durable research answers
10_Projects/          actionable project hubs
40_Decisions/         confirmed decisions and rationale
_context-bundles/     compact retrieval routes
_meta/topic-map.md    topic routing map
00_Home.md            living dashboard
00_Hot.md             restart context
index.md              catalog
log.md                append-only audit trail
```

## Source and evidence rules

1. Preserve source material before synthesis.
2. Never rewrite or edit an immutable raw source to correct an interpretation.
3. Keep facts, interpretations, hypotheses, and confirmation items separate.
4. Record provenance, extraction status, confidence, and review state where applicable.
5. Never turn a forecast, search snippet, MOU, consultation, or cooperation statement into a confirmed contract, revenue event, or approved decision.

## Change classifications

Every meaningful ingest is classified as one of:

- `new`
- `update`
- `disputed`
- `no-material`

Potential effect on existing knowledge is classified as:

- `none`
- `local`
- `cascade`

Automated checks may identify candidates. A human reviews semantic meaning, sensitive content, and large changes.

## Navigation and audit

- Check existing pages before creating duplicates.
- Update `index.md` for meaningful new or renamed knowledge pages.
- Append changes to `log.md`; do not rewrite historical entries.
- Use stable, resolvable links.
- Keep the operating repository free of real private Wiki content.

## Approval boundary

Explicit approval is required before:

- publishing or sharing private knowledge;
- copying sensitive or company material to another service;
- changing the canonical storage system;
- large moves, merges, deletions, or automatic rewrites;
- adding external integrations that transmit Wiki content.
