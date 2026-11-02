---
name: backend-feature-architecture
description: Organize backend features, dependencies, and responsibility boundaries when creating or extending features, moving backend code, or reviewing backend structure.
---

# Backend Feature Architecture

Give each behavior a clear owner and make dependencies between capabilities explicit. For a new backend, start feature-first and add internal layers only where they help. In an existing backend, follow its established structure and improve boundaries within the requested scope.

## Workflow

1. **Trace the change.** Read project guidance and nearby code; follow a representative request, job, or event through its behavior, dependencies, persistence, and tests. Identify existing composition and public boundaries before deciding where new code belongs.
2. **Choose ownership.** Place behavior and its supporting contracts, persistence operations, and entry points with the capability that owns them, using the project's conventions. Keep cross-cutting infrastructure in its established home; share domain behavior through its owner rather than moving it into a generic shared bucket.
3. **Shape the boundary.** Use the project's public interface and composition mechanisms for cross-feature access. Keep dependencies visible and avoid cycles. Assign transaction and data ownership to the behavior that coordinates the invariant; preserve existing consistency and authorization guarantees.
4. **Separate responsibilities.** Keep transport parsing and response mapping at the entry point, business decisions with their owner, and external-system details at the integration boundary when this separation clarifies the change. Use direct code for simple flows; introduce a layer, interface, or subfolder when it addresses a concrete complexity, dependency, or testing need. For placement and cross-feature tradeoffs, consult [boundaries.md](boundaries.md).
5. **Verify the touched path.** Check that changed code follows the chosen ownership and public interfaces, composition resolves dependencies, and relevant behavior and project checks still pass. For a review or design request, report evidence and tradeoffs without moving code unless the user requested changes.

Preserve existing behavior, public contracts, and local naming unless the task calls for a change. Do not turn a local feature into an unrelated restructuring. A directory alone is not a boundary: check its imports and runtime wiring.
