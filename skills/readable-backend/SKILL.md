---
name: readable-backend
description: Write or refactor backend handlers and business workflows that are difficult to follow because orchestration, branches, transformations, or integration details obscure their intent.
---

# Readable Backend

Make a backend workflow read as a clear account of the operation, while keeping cohesive details close enough to follow. Work within the project's existing ownership and architecture.

## Workflow

1. Read the entry point, the behavior it invokes, and nearby collaborators. Identify the operation, important decisions, side effects, and guarantees before changing its shape.
2. Make the main flow reveal its meaningful sequence: validate or accept trusted input, make business decisions, coordinate side effects, and return or translate the outcome as appropriate. Use names from the domain and existing project vocabulary.
3. Extract a cohesive decision, transformation, or integration step when a name makes the flow easier to understand. Keep simple one-use expressions inline; choose a local helper, existing collaborator, or separate module according to ownership and complexity. Avoid pass-through wrappers and abstractions added just to shorten a function.
4. Make branching and failure paths easy to follow. Preserve execution order, authorization, validation, transaction boundaries, errors, and observable behavior; avoid hiding important side effects behind vague names.
5. Re-read the main flow and its extracted details together. The work is complete when the operation and its consequential decisions are apparent, each extraction has a clear responsibility, and appropriate existing checks confirm behavior remains intact.

When architecture changes are part of the task, apply the project's structural conventions; this skill focuses on the readability of the workflow within those boundaries. For a review, report evidence and proposed improvements without changing code unless requested.
