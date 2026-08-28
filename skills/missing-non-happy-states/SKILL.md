---
name: missing-non-happy-states
description: Audit or improve non-happy-state behavior in data-driven frontend features. Use for async views, forms, search, authentication, uploads, mutations, and similar flows that need explicit loading, empty, failure, permission, degraded-data, or recovery coverage.
---

# Missing Non-Happy States

Treat the feature as the full set of states a user can experience. Make each reachable state explicit, actionable where recovery is possible, accessible, and testable.

## Workflow

1. Trace every stateful boundary in scope, including fetches, mutations, browser APIs, authentication, and third-party calls. Inspect the state model and request lifecycle as well as the rendered markup.
2. Build a matrix for each boundary with: trigger, rendered result, allowed action, recovery path, data retained, and announcement or focus behavior. Include only reachable states, but actively check for:
   - initial load, background refresh, success with data, empty results, and partial or stale data;
   - recoverable failure, terminal failure, timeout, offline, unauthorized or forbidden access, and malformed responses;
   - mutation pending, duplicate action, cancellation, success, failure, and optimistic rollback or divergence.
3. Implement each missing state at the boundary that owns its recovery. Preserve usable data and user input when safe, make retry idempotent, prevent duplicate submissions, and translate technical failures into user-facing explanations.
4. Match the product's established state components and language. Use meaningful text, appropriate status or alert semantics, keyboard-operable actions, visible focus, and deliberate focus movement after major transitions.
5. Exercise each implemented matrix row with the narrowest effective check: component tests for rendering, fault simulation for request behavior, browser tests for complete recovery flows, and accessibility assertions for announcements and keyboard use.

The audit is complete when every reachable boundary has an accounted-for outcome, every recoverable outcome has an action proven to change the state, and the verification rules out permanent waits, dead ends, unintended input loss, and duplicate effects.

## Reporting

Report uncovered boundaries with severity, implemented recovery behavior, verification performed and its limits, and only the remaining assumptions that require product judgment.
