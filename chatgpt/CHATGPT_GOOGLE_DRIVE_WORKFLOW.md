# ChatGPT Google Drive Workflow

## Purpose

This workflow supports a ChatGPT app connection to a Google Drive folder named `Master LLM_Wiki`. It is a **reference copy for ChatGPT**, not a second canonical master.

## Recommended folder structure

```text
Master LLM_Wiki/
├── 00_Home.md
├── 00_Hot.md
├── index.md
├── concepts/
├── entities/
├── comparisons/
├── queries/
├── 10_Projects/
├── 40_Decisions/
└── _context-bundles/
```

Do not begin by copying the complete OneDrive vault. Start with approved, non-sensitive, reusable pages and synthetic templates.

## Safe content policy

Google Drive may contain:

- generalized concepts and research summaries;
- approved project plans without confidential details;
- approved decisions and reusable operating guidance;
- sanitized navigation pages and Context Bundles.

Google Drive must not contain:

- company-confidential or customer material;
- private relationship records;
- raw emails, complete session exports, or CHAT/SUM archives;
- tokens, passwords, API keys, or credentials;
- personal data whose sharing status is unclear.

## Update direction

```text
OneDrive canonical Wiki
        |
        | reviewed, sanitized export/copy
        v
Google Drive Master LLM_Wiki
        |
        | ChatGPT reads and answers
        v
User review / approved feedback
        |
        +--> manually reconcile into OneDrive when appropriate
```

Do not use automatic two-way synchronization initially. A page edited in Google Drive is a proposal until reconciled with the OneDrive canonical page.

## ChatGPT retrieval behavior

ChatGPT should:

1. use the Google Drive Wiki only within the user's connected scope;
2. read `00_Home.md`, `00_Hot.md`, and `index.md` first when available;
3. search the relevant project, decision, concept, or query pages;
4. state when a page is missing, stale, partial, or only a copy;
5. avoid treating Google Drive content as authoritative when it conflicts with a newer canonical decision;
6. never infer private details that are absent from the connected files.

## Maintenance

When refreshing the copy:

- use an explicit date and source reference;
- copy only approved pages;
- preserve page titles and source boundaries;
- remove secrets and unnecessary personal data;
- do not overwrite the canonical OneDrive files;
- record what was included, excluded, and still needs review.

## Initial rollout checklist

- [ ] Create a personal Google Drive folder named `Master LLM_Wiki`.
- [ ] Confirm the ChatGPT app's Google Drive connection scope.
- [ ] Add only sanitized Home, index, operating summaries, and selected project/decision pages.
- [ ] Test retrieval with known questions and source citations.
- [ ] Compare answers with Hermes against the OneDrive canonical Wiki.
- [ ] Establish a reviewed refresh cadence before adding more content.
