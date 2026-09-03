# Architecture

## Purpose

The LLM Wiki is a durable, interlinked Markdown knowledge system. It separates evidence from interpretation and execution context so that an agent can retrieve only the context needed for a question.

## Recommended layers

```text
SCHEMA.md                 operating contract
index.md                  catalog and navigation
00_Home.md                living synthesis and priorities
00_Hot.md                 short restart cache
raw/                      immutable evidence
concepts/                 reusable concepts
entities/                 people, tools, companies, products
comparisons/              structured alternatives
queries/                  filed answers and research
10_Projects/              actionable work
40_Decisions/             approved choices and rationale
_context-bundles/         compact retrieval routes
_meta/topic-map.md        topic-to-page routing
_automation/              reports, candidates, and validation state
log.md                    append-only audit trail
```

## Data flow

1. Capture the source without rewriting it.
2. Record provenance, date, and extraction status.
3. Search the existing catalog and pages.
4. Classify the ingest disposition.
5. Update or create the smallest useful refined page.
6. Check local and cascade impact.
7. Update navigation and append the audit log.
8. Run validation and report remaining uncertainty.

## Retrieval path

```text
SCHEMA -> index/Home/Hot -> topic map -> context bundle
       -> project hub or decision -> concept/entity/query -> raw evidence
```

The whole vault should not be injected into every request. Bundles are routing aids, not replacements for source evidence.

## Separation of responsibilities

| Responsibility | Human | Agent | Automated check |
|---|---:|---:|---:|
| Choose scope and sensitivity | Yes | Assist | No |
| Preserve raw source | Approve policy | Yes | Hash/format check |
| Synthesize and cross-link | Review | Yes | Link candidates |
| Confirm a decision | Yes | Draft | No |
| Detect stale/broken structure | Review exceptions | Run | Yes |
| Large move/merge/delete | Approve | Execute after approval | No |
