# LLM Wiki Operations

A version-controlled operating handbook for a Markdown-first LLM Wiki.

This repository documents **how to build, manage, retrieve, validate, and improve** an LLM Wiki. It is not the user's personal knowledge vault and must not contain private Wiki pages, raw sources, conversation archives, company material, credentials, or personal data.

## Canonical data boundary

- **Canonical knowledge vault:** a private/local Markdown Wiki managed separately.
- **This repository:** reusable operating rules, templates, examples, and safe validation scripts.
- **Never publish here:** `raw/`, conversation exports, CHAT/SUM archives, emails, customer data, API keys, `.env` files, or relationship records.

## Operating model

```text
raw source -> refined knowledge -> project / decision -> index / log
                    ^                         |
                    +------ evidence --------+
```

The human directs scope, interpretation, approval, and sensitive decisions. The agent captures sources, synthesizes pages, maintains links, performs bounded validation, and reports uncertainty.

## Core principles

1. Raw before synthesis.
2. Raw sources are immutable.
3. Every meaningful page has provenance and an evidence boundary.
4. Existing pages are checked before new pages are created.
5. Ingest is classified before editing: `new`, `update`, `disputed`, or `no-material`.
6. Impact is classified as `none`, `local`, or `cascade`.
7. Automated checks observe first; large edits require approval.
8. `index.md` and append-only `log.md` remain navigational and auditable.
9. The Wiki is read selectively through Home, Hot Context, Topic Maps, and Context Bundles.
10. Knowledge quality is measured by retrieval accuracy and traceability, not by page count.

## Documentation map

- [Operating Rules](OPERATING_RULES.md)
- [Retrieval Rules](RETRIEVAL_RULES.md)
- [Memory Rules](MEMORY_RULES.md)
- [Hermes Workflow](hermes/HERMES_WORKFLOW.md)
- [ChatGPT Google Drive Workflow](chatgpt/CHATGPT_GOOGLE_DRIVE_WORKFLOW.md)
- [Google Drive LLM Wiki Skill](chatgpt/skills/google-drive-llm-wiki/SKILL.md)
- [Architecture](docs/architecture.md)
- [Schema and metadata](docs/schema-and-metadata.md)
- [Source ingestion](docs/source-ingestion.md)
- [Retrieval and promotion](docs/retrieval-and-promotion.md)
- [Maintenance and health checks](docs/maintenance-and-health-check.md)
- [Projects and decisions](docs/projects-and-decisions.md)
- [Security and privacy](docs/security-and-privacy.md)
- [GitHub review process](docs/github-review-process.md)
- [Raw source template](templates/raw-source-template.md)
- [Project hub template](templates/project-hub-template.md)
- [Safe filename scan](scripts/safe_filename_scan.py)

## What this repository is not

- Not a backup or mirror of the personal Wiki.
- Not a replacement for OneDrive's canonical vault.
- Not an automatic sync target.
- Not a place for private source material.
- Not a promise that every experimental tool or graph database should be adopted.

## Status

Initial handbook based on the current Markdown-first, OneDrive-separated operating model. Revisit monthly and record changes in [CHANGELOG.md](CHANGELOG.md).
