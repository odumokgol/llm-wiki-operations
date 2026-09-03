# GitHub Review Process

Review GitHub repositories monthly for useful Wiki, Hermes, and active-project operating ideas.

## Review order

1. Official README.
2. VISION, ROADMAP, architecture, and application README files.
3. Package manifests and tests when implementation claims matter.
4. License, activity, security, and data-boundary notes.

## Classification

- `adopt-now`: small, low-risk, reversible, and clearly compatible.
- `validate-first`: promising but needs a local read-only experiment.
- `defer`: useful later but current scale or maintenance cost is not justified.
- `do-not-adopt`: conflicts with privacy, profile separation, raw immutability, or Markdown-first policy.

## Current decision pattern

Prefer selective adoption of ideas such as ingest disposition, provenance, cascade checks, hot context, deterministic linting, and approval-separated edits. Do not automatically adopt Graph DBs, embeddings, full product migrations, or plugin-heavy structures merely because a repository is popular.

## Recordkeeping

Save research and decisions in the canonical Wiki, not in this repository's issue tracker by default. This repository should contain only generalized operating guidance and changes to that guidance.
