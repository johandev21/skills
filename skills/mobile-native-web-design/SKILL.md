---
name: mobile-native-web-design
description: Build or audit mobile-native web interfaces for phones. Use when designing mobile layouts, touch targets, safe areas, mobile forms, navigation bars, bottom sheets, or mobile gestures.
---

# Mobile-Native Web Design

Make web interfaces feel natively built for mobile phones. Prioritize single-thumb ergonomics, immediate touch feedback, edge-to-edge layouts with safe-area padding, and complete state handling.

## Workflow

1. **Set viewport and app shell.** Configure `viewport-fit=cover`, responsive color schemes, dynamic viewport units (`100dvh`), and safe-area insets for notches and system bars — see [reference.md](reference.md).
2. **Lay out for the thumb zone.** Place primary navigation and primary actions in the lower reach zone. Enforce an 8px layout grid with 16px side margins. Maintain touch targets at ≥44×44px with ≥8px spacing — see [reference.md](reference.md).
3. **Fit inputs and virtual keyboard behavior.** Set inputs to `font-size: max(16px, 1em)` to eliminate iOS auto-zoom. Apply explicit input modes, autocomplete, and keyboard action hints (`enterkeyhint`). Ensure sticky or primary actions remain visible when the software keyboard opens — see [reference.md](reference.md).
4. **Apply native components and instant feedback.** Replace desktop patterns (dropdowns, dialogs, hover) with mobile primitives (bottom sheets, segmented controls, grouped lists, switches). Apply immediate active feedback (<100ms) and constrain animations to `transform` and `opacity` with reduced-motion support — see [reference.md](reference.md).
5. **Implement state coverage and verify.** Provide dedicated presentations for loading (skeletons), empty, error, and offline states. Audit the interface against the checklist in [reference.md](reference.md).

## Core rules

- Place primary actions and tab navigation in the bottom third of the viewport; reserve top corners for secondary or non-destructive actions.
- Target minimum touch areas of 44×44px (prefer 48×48px), expanding small icons with internal padding rather than inflating graphic assets.
- Eliminate website tells: disable tap highlights (`-webkit-tap-highlight-color: transparent`), disable double-tap delay (`touch-action: manipulation`), disable user selection on chrome elements, and isolate hover effects behind `@media (hover: hover) and (pointer: fine)`.
- Use `100dvh` for full-height application shells and `100svh` for non-collapsing hero viewports; avoid raw `100vh`.
- Keep text readable without zoom: body text at ≥16px (minimum 12px for microcopy), using system font stacks and tabular numbers for figures.
- Prevent scroll chaining on overlays and sheets using `overscroll-behavior: contain`.

## Reference

Load only what the current branch needs:

- **[reference.md](reference.md)** — Viewport and base CSS resets, safe-area calculations, keyboard-resilient layout patterns, component specifications, state matrix, PWA standalone tags, and the verification checklist.

Do not load it preemptively. The workflow states which step each section serves.

## Completion

The work is complete when:

- Viewport is configured with `viewport-fit=cover`, without disabling user scalability.
- All tappable controls measure ≥44×44px with ≥8px separation and instant pressed feedback.
- All form inputs use `font-size: max(16px, 1em)` and stay in view when focused under keyboard opening.
- Safe areas (`env(safe-area-inset-*)`) are padded on all boundaries touching screen edges.
- Loading, empty, error, and offline states render with distinct layouts.
- Interface passes all verification items in [reference.md](reference.md).

In the handoff, name the thumb-zone adaptations made, keyboard/viewport fixes applied, safe-area considerations configured, and states verified.
