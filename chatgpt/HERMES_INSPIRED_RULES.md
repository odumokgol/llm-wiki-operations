# Hermes-Inspired Rules for ChatGPT Google Drive Wiki

## Purpose

Hermes has a more explicit operating system than a normal folder of notes. The following rules are useful for the iPhone GPT app's Google Drive Wiki and can be applied without copying Hermes' local paths, cron jobs, session database, or sensitive archives.

## Adopt these rules

### 1. Use a compact retrieval front door

Maintain three small navigation files:

- `00_Home.md`: current priorities and major areas;
- `00_Hot.md`: recent decisions, next actions, and restart context;
- `index.md`: page catalog and routing hints.

ChatGPT should read or search these before scanning many detailed files.

### 2. Separate evidence from synthesis

Keep source captures, refined explanations, project pages, and decisions conceptually separate. Every important synthesis should identify its source, evidence boundary, confidence, and review state.

Do not treat a ChatGPT answer as a source merely because it sounds plausible. A claim should be marked as inferred until a source supports it.

### 3. Classify before updating

Before adding or changing a page, classify the material:

- `new`
- `update`
- `disputed`
- `no-material`

Also assess impact:

- `none`
- `local`
- `cascade`

For a `cascade` candidate, list affected pages and review the implications before changing multiple documents.

### 4. Promote selectively

Do not turn every conversation into a permanent page.

- One-time answer: keep it in the conversation.
- Reusable answer: file as a Query.
- Repeated topic: update a Concept or Entity.
- Confirmed choice: update a Decision.
- Actionable work: update a Project Hub.

Preserve the original source or conversation reference when promotion occurs.

### 5. Treat Google Drive as a reviewed copy

For the current two-system model:

- OneDrive remains Hermes' canonical Wiki.
- Google Drive contains approved, non-sensitive material for ChatGPT.
- GitHub contains shared operating standards.

A Google Drive edit is not automatically authoritative over a newer OneDrive decision. Reconcile meaningful changes deliberately.

### 6. Use approval and uncertainty gates

ChatGPT should pause or label uncertainty when:

- a source is incomplete or inaccessible;
- two pages conflict;
- the request involves sensitive data;
- a large batch update is proposed;
- a decision is not explicitly confirmed;
- the requested information is absent from the connected files.

It should state what is known, what is inferred, and what needs confirmation instead of filling gaps silently.

## Do not copy these Hermes-specific mechanisms

The following are not required for an iPhone GPT Google Drive Wiki at this stage:

- Hermes' local Windows paths;
- Hermes profile or wife-profile configuration;
- Hermes cron job IDs and schedules;
- state database or session runtime details;
- complete CHAT/SUM conversation archives;
- automatic two-way synchronization with OneDrive;
- local-only health scripts that cannot run in the ChatGPT app.

## Minimal ChatGPT operating prompt

When working with the connected Google Drive Wiki, ChatGPT should:

1. identify whether the request is lookup, synthesis, project, or decision work;
2. start from Home, Hot Context, and index when available;
3. search existing pages before creating new content;
4. cite the relevant page or source;
5. separate fact, interpretation, hypothesis, and confirmation needed;
6. preserve privacy and the OneDrive/Google Drive authority boundary;
7. avoid large updates unless the user explicitly approves them.

## Adoption status

| Hermes pattern | ChatGPT Google Drive | Status |
|---|---|---|
| Home / Hot Context / index routing | Useful immediately | Adopt |
| Evidence status and provenance | Useful immediately | Adopt |
| Ingest and impact classification | Useful for edits | Adopt |
| Query promotion | Useful as the Wiki grows | Adopt |
| Hermes cron/session database | App-specific | Do not copy |
| Full session archive | Privacy-sensitive | Do not copy by default |
| Automatic OneDrive↔Drive sync | Authority risk | Defer |
