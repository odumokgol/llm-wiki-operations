# Google Drive LLM Wiki Skill

## Purpose

Use this skill when ChatGPT needs to retrieve, summarize, maintain, or propose updates to the user's Google Drive `Master LLM_Wiki` reference copy.

This skill implements the repository-level rules in:

- `OPERATING_RULES.md`
- `MEMORY_RULES.md`
- `RETRIEVAL_RULES.md`
- `chatgpt/CHATGPT_GOOGLE_DRIVE_WORKFLOW.md`

The GitHub repository defines the operating method. The Google Drive Wiki contains only approved, non-sensitive, reusable knowledge for ChatGPT retrieval.

## Trigger conditions

Apply this skill when the user asks to:

- recall or continue a previous project, decision, research topic, or durable preference;
- search the Google Drive LLM Wiki;
- save reusable knowledge to the Google Drive LLM Wiki;
- update an existing Wiki page;
- create or refresh a project hub, decision page, query page, concept, entity, context bundle, Home, Hot Context, index, or log;
- check Wiki consistency, staleness, duplicate pages, or retrieval quality.

Do not use the Wiki merely to personalize an answer when the current conversation already contains everything needed.

## Authority and storage boundary

1. GitHub `llm-wiki-operations` is the source of truth for operating rules.
2. The canonical private Wiki remains outside this repository.
3. Google Drive `Master LLM_Wiki` is the ChatGPT-facing reference copy.
4. A Google Drive page that conflicts with a newer canonical source must be marked stale or disputed and must not silently override the canonical source.
5. Never place private Wiki content, raw company/customer material, credentials, private relationship records, complete email archives, or sensitive personal data in this GitHub repository.

## Retrieval workflow

Use the smallest context that can answer the request.

Preferred order:

```text
GitHub operating rules
  -> 00_Home / 00_Hot
  -> index
  -> topic map
  -> context bundle
  -> project hub / decision
  -> concept / entity / comparison / query
  -> raw evidence only when verification is necessary and approved
```

Before answering:

1. Identify the requested system, project, profile, and time scope.
2. Check whether the question concerns operating rules, project state, a confirmed decision, or source facts.
3. Search existing pages before creating a new page or relying on memory.
4. Check `updated`, `review_state`, `confidence`, and `evidence_status` when present.
5. Prefer the newest approved page when multiple non-conflicting versions exist.
6. If pages conflict, preserve the conflict and state what requires confirmation.
7. Cite or name the relevant Wiki page/source path in the response when possible.

## Answer discipline

When evidence is incomplete, distinguish:

- **Fact** — directly supported by the available source.
- **Interpretation** — reasoned meaning based on facts.
- **Hypothesis** — plausible but unconfirmed explanation.
- **Confirmation needed** — the exact source or action needed next.

Never invent missing details or silently merge incompatible claims.

## Save and promotion workflow

Before writing:

1. Search for an existing page covering the same durable knowledge.
2. Classify the ingest as `new`, `update`, `disputed`, or `no-material`.
3. Classify impact as `none`, `local`, or `cascade`.
4. Decide whether the content is safe and useful for the Google Drive reference copy.
5. Prefer updating the canonical existing topic page over creating a duplicate.

Promote content only when it has durable reuse value:

- repeated idea -> Concept or Entity;
- reusable research -> Query;
- confirmed choice -> Decision;
- actionable work -> Project Hub;
- compact restart context -> Context Bundle or `00_Hot`;
- navigation change -> `index` and, when relevant, `00_Home`.

One-time lookups, temporary drafts, unconfirmed hypotheses, and transient progress should normally stay in the current conversation.

## Page metadata

For refined pages, use the shared schema when the storage format supports it:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | entity | comparison | query | project | decision | summary
tags: [controlled, tags]
sources: [source references]
confidence: high | medium | low
ingest_disposition: new | update | disputed | no-material
evidence_status: grounded | partial | inferred | mixed
review_state: current | needs-review | disputed | archived
---
```

Google Docs that cannot use literal Markdown frontmatter should preserve the same fields in a compact metadata block at the top.

## Google Drive safety rules

Allowed in the ChatGPT-facing copy:

- generalized concepts and research summaries;
- approved non-confidential project plans;
- approved decisions and rationale;
- reusable operating guidance;
- sanitized Home, index, topic maps, and Context Bundles.

Do not place in the ChatGPT-facing copy:

- company-confidential or customer material;
- raw emails or full conversation/session exports;
- credentials, tokens, API keys, OAuth data, or secrets;
- private relationship records;
- sensitive personal data;
- material whose sharing or approval status is unclear.

If a requested save crosses this boundary, do not save it; explain the boundary and keep it local unless the user explicitly changes the operating policy.

## Change control

Explicit user approval is required before:

- large folder moves, merges, deletions, or bulk rewrites;
- changing the canonical storage system;
- publishing or sharing private knowledge;
- copying sensitive/company material across services;
- enabling an external integration that transmits Wiki content.

Small additive changes such as creating a safe guide, template, index entry, or non-sensitive reusable page may be performed when the user's request clearly authorizes the write.

## Navigation and audit

For meaningful new or renamed pages:

- update the relevant index or routing page;
- preserve stable links;
- append an audit/log entry when the Google Drive Wiki provides a log page;
- never rewrite historical log entries;
- avoid duplicate pages with near-identical scope.

## Health check

A periodic Wiki health check should look for:

- duplicate or overlapping pages;
- missing or broken navigation links;
- stale `00_Hot` or project hubs;
- pages with `needs-review` or `disputed` state;
- low-confidence pages being treated as facts;
- decisions lacking rationale or evidence;
- index entries pointing to missing pages;
- unsafe content that should not be in the ChatGPT-facing copy.

Report findings before large automatic fixes.

## Completion standard

A successful Wiki-assisted task should make it possible to answer:

1. Which page or source supported the answer?
2. Is the information current, approved, and within the correct profile/project?
3. What is fact versus interpretation?
4. Was an existing page reused instead of duplicating knowledge?
5. If something changed, was the change bounded, traceable, and safe?
