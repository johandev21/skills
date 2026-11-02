# Backend boundary decisions

Use these decisions when ownership or dependencies are unclear; adapt names and wiring to the project.

## Placement

- A feature owns its business rules and the data access needed to enforce them. Keep its request or event schemas, handlers, and tests nearby when that matches local conventions.
- Application composition assembles features and infrastructure. Shared code serves multiple capabilities without owning one capability's business rules; an existing platform facility can be shared even before multiple features use it.
- A new backend can start with feature directories and an application entry point. Add subfolders for transport, behavior, or persistence only when they make that feature easier to navigate. A tiny feature can remain a few files.

## Collaboration and data

- A caller uses another feature's intended public capability rather than importing private storage or implementation details. If no public surface exists, follow local conventions to create the smallest useful one; do not assume an index file alone enforces a boundary.
- When a workflow spans features, locate the coordinator where the business operation belongs. Make dependencies and transaction boundaries explicit; choose synchronous calls, events, or a shared transaction according to the project's consistency needs. Avoid introducing messaging or distributed transactions solely for architectural symmetry.
- Keep a single owner for each business invariant. A shared database or common types do not automatically imply shared ownership; avoid copying rules or reaching around the owner to update its data.

## Seams

- Isolate a dependency behind a contract when a concrete domain, test, or integration need justifies it. A one-use pass-through interface or repository adds little on its own.
- Validate input at the relevant trust boundary, enforce business invariants with the behavior that owns them, and preserve the existing error and authorization semantics across boundaries.
