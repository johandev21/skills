---
name: readable-react
description: Write or refactor React components whose top-level JSX has become difficult to scan because it mixes rendering with branches, iteration, event logic, or data transformation. Use for `.jsx` and `.tsx` implementation work where composition or component readability is in scope.
---

# Readable React

Make the main component read as an outline of the UI. A reader should be able to identify its states, sections, and interactions without first tracing implementation details.

## Workflow

1. Read the component and its local collaborators before choosing extractions. Identify the page or feature story the main component should tell.
2. Keep the main component near the top of the module, after imports and any declarations that must precede it. Arrange its JSX around named UI sections and visible state branches.
3. Move a detail below the main component when naming it removes nested reasoning from the outline:
   - Rendered entities or sections become focused components such as `TaskRow` or `UserActions`.
   - Meaningful UI branches become components such as `EmptyState` or `ErrorState`.
   - Transforms and derived presentation values become named variables or helpers such as `visiblePosts` or `getStatusClassName`.
   - Event sequences become named handlers such as `handleDelete`.
4. Keep cohesive details together. Leave simple one-use JSX, direct state setters, and obvious expressions inline when extracting them would make the reader jump between locations without clarifying the parent.
5. Re-read only the main component. The refactor is complete when it communicates the UI's structure and behavior at a glance, every extraction has a semantic name, and no abstraction exists solely to reduce line count.

## Composition rules

- Prefer domain names (`PostList`, `RoleBadge`) over mechanical names (`PostListComponent`, `renderPosts`).
- Give components a focused responsibility and a small, direct prop surface.
- Keep hooks at the top level and in stable order. Extract a custom hook only when a cohesive group of state and effects obscures the component outline.
- Choose the smallest clear construct: a variable can beat a helper, a ternary can beat a component, and a local component can beat a configurable framework.
- Preserve behavior, state ownership, accessibility, styling conventions, and public APIs unless the task explicitly includes changing them.

For an existing refactor, summarize the meaningful extractions and the resulting readability improvement in the handoff.
