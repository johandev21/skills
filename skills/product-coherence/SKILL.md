---
name: product-coherence
description: Align a UI change with an existing product's design system and repeated patterns. Use when building or reviewing screens, shared components, visual tokens, interaction patterns, or microcopy where inconsistency, duplication, or a generic-looking result is a concern.
---

# Product Coherence

Make each UI change feel native to the product. Treat the repository's established components, tokens, language, and interaction behavior as the design evidence.

## Workflow

1. Find the nearest precedents before designing the change: the shared component library, token or theme files, content guidance, and screens that solve the same interaction. Prefer relevant precedents over a broad repository inventory.
2. Extract the local pattern for:
   - visual hierarchy, spacing, typography, color roles, and responsive layout;
   - component variants and composition;
   - action order, validation, feedback, focus, and recovery;
   - domain terms, tone, and button labels.
3. Implement with existing primitives and semantic tokens. Extend an existing component when the new case belongs to the same concept; create a new primitive only when the responsibility is genuinely distinct.
4. Compare the result with every directly analogous screen or component. Resolve accidental differences and keep intentional differences only when the user need or domain rule explains them.
5. Verify the changed states and responsive layouts using the project's existing checks. The work is complete when each new visual value, component, term, and interaction either follows a relevant precedent or has a stated product reason to differ.

## Decision rules

- Let product evidence outrank generic UI conventions. When precedents conflict, favor the maintained shared primitive or the pattern used by the closest current workflow.
- Reuse semantic roles such as `danger` and `success` rather than copying their current raw values.
- Keep one concept's wording stable across states: for example, use the same domain noun and action verb in the trigger, dialog, progress message, and result.
- Consolidate repeated behavior at its existing ownership boundary. Keep a local special case local when sharing it would add configuration for unrelated consumers.
- Preserve accessibility while matching appearance: semantics, contrast, keyboard behavior, focus management, and status announcements remain part of the pattern.
- Keep the requested scope. Record broader inconsistencies as findings unless fixing them is necessary for the requested change.

Ask for product direction when repository evidence cannot decide a material choice such as the primary action, information hierarchy, brand tone, or terminology. Present the conflicting evidence and the smallest decision needed.

In the handoff, name the precedents reused, any new shared pattern introduced, and each intentional deviation.
