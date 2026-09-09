---
name: no-ui-slop
description: Eliminate ui-slop from generated interfaces into intentional product UI. Use when building or reviewing layouts, components, visual styles, motion, or density where generic, decorative, or over-containerized output is a risk.
---

# No UI Slop

Make each interface feel intentionally designed for its task. Treat hierarchy, spacing, and product-specific decisions as the design; treat containers, decoration, and motion as costs that earn their place.

## Workflow

1. Establish hierarchy with type, spacing, and alignment before adding containers. Set reading flow and emphasis first; add a container only when open layout cannot express the grouping.
2. Justify every card, border, separator, badge, icon, shadow, and animation against one test: it communicates hierarchy, state, grouping, or interaction. Remove what fails the test.
3. Apply one restrained system for surfaces, radius, color, type, and elevation. Reuse the product's tokens and primitives; introduce a new value only for a distinct semantic role — see [reference.md](reference.md).
4. Fit density, actions, and responsiveness to the task. Keep related information close, keep one clear control per action with primary/secondary/tertiary order, and re-place hierarchy and actions for small screens rather than stacking the desktop grid — see [reference.md](reference.md).
5. Run the final justification pass over every container and decoration. The work is complete when each remaining element passes the step-2 test, each new value belongs to the system from step 3, and every state in [reference.md](reference.md) renders with its precedence intact.

## Restraint rules

- Prefer `Page → Section → Content` with whitespace and alignment. Separate stacked rows and sections with gap, padding, and layout rhythm, not divider lines. Reserve cards for independent units: selectable entities, reusable objects, collection items, content needing containment.
- Keep one visual system: small consistent radius with pills only for naturally pill-shaped controls, one accent plus semantic states, flat surfaces over gradients and glass, elevation only for floating layers.
- Let typography carry hierarchy through size, weight, and spacing in Title Case. Keep body text quieter than headings and actions.
- Give each action one clear control. Use links or text actions for low emphasis, icons only when they improve recognition, and standard navigation over invented controls.
- Reserve badges for compact status, category, or state. Render ordinary metadata as text and keep navigation quieter than content. Keep filter tabs as plain labels with counts living in the footer, set numerals bare, and lay out multi-part labels as spaced elements.
- Keep stronger states stable over hover and focus: selected, active, checked, and disabled never yield visually to hover. Keep motion subtle, functional, and respectful of `prefers-reduced-motion`.
- Design for the task's density: scanning and completion over decorative composition. Keep product workflows over generic dashboards, and never invent metrics, testimonials, or filler data.
- When repository precedents exist, delegate to `product-coherence` for matching them. This skill governs restraint; that skill governs fit.

## Reference

Load only what the current branch needs:

- **[reference.md](reference.md)** — intentional targets and hard guardrails per concern: layout, surfaces, color, typography, cards, actions, icons, badges, forms, navigation, states, motion, shadows, libraries, density, responsiveness, product specificity, and the final checklist.

Do not load it preemptively. The workflow states which step each section serves.

## Completion

The work is complete when:

- Every container, border, divider, badge, icon, count, shadow, and animation communicates hierarchy, state, grouping, or interaction, and what does not is removed.
- Every visual value belongs to one restrained system with no transplantable generic pattern surviving.
- Every action has one clear control with stable state precedence, and density serves the task on desktop and small screens.

In the handoff, name elements removed, values consolidated into the system, and each intentional deviation with its product reason.
