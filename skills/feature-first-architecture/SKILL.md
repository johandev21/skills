---
name: feature-first-architecture
description: Enforce feature-first architecture for React/TypeScript frontends - organize code by domain (app/pages/features/shared), direct dependency flow, promote to shared only after reuse, keep .tsx composition-focused. Use when scaffolding features, reviewing structure, moving code between feature/shared, or auditing imports and layering.
---

# Feature-First Architecture

Keep business code by feature, not by technical type. `features/` owns domain behavior; `shared/` holds only genuinely cross-domain reuse. Dependency flows one way: `app → pages → features → shared`.

## Workflow

1. **Inventory against canonical layout.** Map current `src/` to the layout in [structure.md](structure.md). List global buckets (`components/`, `hooks/`, `utils/` at root), feature code in `shared/`, and inverted imports.
2. **Place code by ownership.** Default to feature-local. Promote to `shared/` only when reused across ≥2 features and free of domain ownership - see placement rules in [structure.md](structure.md).
3. **Fix dependency direction.** Enforce `app → pages → features → shared`. Forbid `shared → features`, `shared → pages`, `features → pages`. Use feature `index.ts` as public API; forbid deep reaches into `features/<x>/hooks/internal/*` - see layering rules in [structure.md](structure.md).
4. **Separate composition from behavior.** Make `.tsx` read as composition in 30 seconds. Move fetches, transforms, and meaningful state to `.ts` outside JSX - see [component-state.md](component-state.md). For JSX extraction inside the component, delegate to `readable-react`.
5. **Apply naming, colocation, and state ownership, then verify.** Use predictable filenames and moderate barrels from [structure.md](structure.md); apply state-ownership table and colocation option from [component-state.md](component-state.md). Verify every import respects the layer arrow, every feature is self-contained, and no `shared/` item carries domain ownership.

## Reference

Load only what the current branch needs:

- **[structure.md](structure.md)** - canonical `src/` tree, placement (feature vs shared), dependency direction, API split (`shared/api` client vs `features/*/api` endpoints), naming and barrel rules.
- **[component-state.md](component-state.md)** - `.tsx` vs `.ts` split, what to extract vs keep inline, state-ownership categories, and colocation option.

Do not load both disclosed files preemptively. The workflow states which file each step needs.

## Completion

The work is complete when:

- Every domain file (components, hooks, api, types, utils, schemas for that domain) lives under its `features/<domain>/` - no scattering across global type folders.
- Every `shared/` item is cross-domain and reused or clearly generic (`button`, `format-date`, `use-debounce`); no `order-status` in shared.
- Every import respects `app → pages → features → shared` with no cycles; cross-feature access goes through the feature's `index.ts`.
- Every `.tsx` communicates structure at a glance per [component-state.md](component-state.md) and `readable-react`; every transform/fetch lives outside JSX.

In the handoff, name structure violations fixed, items promoted to or kept out of `shared/`, and import/barrel changes made.

