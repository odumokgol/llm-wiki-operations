# Retrieval Rules

These rules are shared by Hermes and ChatGPT. They describe how to answer questions from an LLM Wiki without loading or copying the entire vault.

## Retrieval order

```text
Operating rules
  -> Home / Hot Context
  -> index.md
  -> topic map
  -> Context Bundle
  -> project hub or decision
  -> concept / entity / query
  -> raw evidence when verification is needed
```

Use the smallest context that can answer the question. Do not inject the entire Wiki into every prompt.

## Before answering

1. Identify the requested system and profile.
2. Confirm whether the question is about operating rules, project state, or source facts.
3. Search existing pages before creating a new answer or page.
4. Check dates, `updated`, `review_state`, `confidence`, and `evidence_status`.
5. Distinguish direct source evidence from interpretation.

## Answer format

When evidence is incomplete, separate the answer into:

- **Fact:** directly supported by the available source.
- **Interpretation:** reasoned meaning based on those facts.
- **Hypothesis:** plausible but unconfirmed explanation or forecast.
- **Confirmation needed:** exact next source or action required.

Cite the relevant page or source path. Do not invent missing details, fill gaps from memory, or silently merge conflicting pages.

## Cross-system rule

- Hermes normally reads the OneDrive canonical Wiki.
- ChatGPT normally reads the approved Google Drive copy.
- GitHub provides the shared operating rules only.
- A Google Drive page must not override a newer or conflicting OneDrive canonical page without review.
- Do not copy raw private sources into Google Drive merely to improve retrieval.

## When to file an answer

- One-time lookup: answer inline.
- Reusable research: create or update a Query page in the appropriate canonical system.
- Repeated concept: promote to an existing Concept or Entity.
- Confirmed choice: record in a Decision page.
- Actionable work: connect to a Project Hub or backlog.

Promotion preserves the original query and source evidence.
