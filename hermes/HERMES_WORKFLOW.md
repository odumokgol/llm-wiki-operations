# Hermes Workflow

Hermes uses the OneDrive Markdown Wiki as its canonical personal/work knowledge vault. This document connects Hermes operations to the shared rules in the repository root.

## Session start

1. Read the applicable operating rules.
2. Read `SCHEMA.md`, `index.md`, and `00_Hot.md` when the task is Wiki-grounded.
3. Route through the topic map and Context Bundle before opening many detail pages.
4. Keep default and wife profiles separate.
5. Check whether the task touches sensitive, company, or approval-controlled material.

## Ingest

1. Capture the raw source in the canonical Wiki.
2. Compute or record provenance and extraction status.
3. Search existing pages.
4. Classify `new / update / disputed / no-material`.
5. Assess `none / local / cascade` impact.
6. Update refined pages only; keep raw evidence immutable.
7. Update navigation and append the log.
8. Run health and link checks.

## Maintenance cadence

- Daily: read-only archive/structure/watchdog checks.
- Weekly: review candidates, active projects, decisions, and cascade impact.
- Monthly: retrieval test, project-state review, and GitHub operating-pattern review.

Automation detects candidates and structural defects. It must not silently settle sensitive meaning, delete evidence, or perform large merges.

## GitHub relationship

This repository contains generalized rules and safe tools. It must not receive the OneDrive Wiki, raw sources, CHAT/SUM archives, company files, or secrets. Changes to Hermes-specific operational behavior should be reviewed against the canonical Wiki policy before implementation.

## Google Drive relationship

Hermes may prepare an approved, sanitized export for ChatGPT's Google Drive copy only when the user explicitly approves the scope. The export is not an automatic mirror and must not overwrite the OneDrive canonical source.

## Completion report

For Wiki-related work, report separately:

- source and evidence status;
- files/pages created or updated;
- structural validation result;
- approval status;
- unresolved uncertainty or remaining manual action.
