---
name: tablet-native-web-design
description: Build or audit adaptive tablet and medium-width web interfaces (600–1200px). Use when designing for tablets, foldables, split-screen views, list-detail layouts, navigation rails, or mixed touch/keyboard/pointer input.
---

# Tablet-Native Web Design

Make web interfaces feel natively built for tablet form factors and adaptive window sizes. Exploit available width for multi-pane hierarchy, accommodate side-grip ergonomics and multi-modal input (touch, keyboard, trackpad, pen), and ensure non-destructive reflow.

## Workflow

1. **Classify by window width, not device identity.** Target standard window size classes: Compact (<600px), Medium (600–839px), Expanded (840–1199px), Large (≥1200px). Design from expanded down, folding gracefully into compact — see [reference.md](reference.md).
2. **Structure the multi-pane adaptive shell.** Use CSS Grid and container queries to map content to available width (list-detail, supporting panes, or responsive card grids). Cap reading line lengths at `max-width: 65ch` and forms at 480–640px — see [reference.md](reference.md).
3. **Map navigation to width and destinations.** Switch between bottom tabs (compact), navigation rail (medium / few destinations), and persistent sidebar (expanded / many destinations) — see [reference.md](reference.md).
4. **Adapt touch, reach, and multi-modal input.** Position common controls toward side edges for two-hand grip. Preserve ≥44px touch targets. Scope hover strictly behind `(any-hover: hover) and (any-pointer: fine)`, provide visible `:focus-visible` rings, and support keyboard shortcuts, pointer drag-and-drop, and pen events — see [reference.md](reference.md).
5. **Adapt components, verify resilience, and audit.** Replace full-width mobile sheets with anchored popovers, side sheets, or centered form sheets. Verify that resizing windows or rotating orientation preserves scroll, selection, and state without destructive loss. Run the audit checklist in [reference.md](reference.md).

## Core rules

- Base layout strictly on the active viewport/container width; never infer layout capabilities from user-agent sniffing or screen size.
- Ensure non-destructive resizing: cycling from wide to narrow and back must retain active selection, scroll offset, and draft state.
- Keep reading containers bounded: cap prose to 50–75 characters per line (`max-width: 65ch`), form sheets to 480–640px, and dialogs to 480–640px.
- Anchor high-frequency actions toward screen sides where holding thumbs rest, rather than centering full-width actions across wide viewports.
- Maintain a single shared route and navigation history across window classes; never fork URLs or screen states by breakpoint.
- Support multi-modal inputs: support keyboard tab navigation, shortcut keys (Escape to close, Cmd/Ctrl+K, arrow navigation), and pointer hover without making hover a requirement for actions.

## Reference

Load only what the current branch needs:

- **[reference.md](reference.md)** — Window size classes, adaptive layout patterns, CSS grid and container query shell boilerplate, component translation matrix (phone vs. tablet), multi-input styles, and the verification checklist.

Do not load it preemptively. The workflow states which step each section serves.

## Completion

The work is complete when:

- Layout reflows smoothly across Compact (<600px), Medium (600–839px), and Expanded (840–1199px) without horizontal clipping.
- Content widths remain constrained (`max-width: 65ch` for prose, 480–640px for forms/dialogs) rather than stretched.
- Navigation transitions appropriately between tabs, rail, and sidebar depending on width.
- Touch targets remain ≥44×44px, and interactive controls sit within comfortable grip zones.
- Popovers, side sheets, or centered panels replace full-bleed mobile sheets.
- Window resizing and orientation rotation do not reset user state, scroll position, or selections.
- Interface passes all verification items in [reference.md](reference.md).

In the handoff, name the multi-pane patterns implemented, navigation transition breakpoints established, input adaptations handled, and resize/rotation behaviors verified.
