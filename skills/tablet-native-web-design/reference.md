# Tablet-Native Web Design Reference

## Window Size Classes and Breakpoints

Layout responds to available window width rather than hardware model:

| Class | Viewport Width | Typical Window Context | Navigation Pattern |
|---|---|---|---|
| **Compact** | < 600px | Phones, narrow split-view (1/3), slide-over | Bottom tab bar or drawer |
| **Medium** | 600–839px | Portrait tablet, small tablet, half split-view (1/2) | Navigation rail (72–80px) or tabs |
| **Expanded** | 840–1199px | Landscape tablet, full-screen tablet portrait | Collapsible or persistent sidebar (240–280px) |
| **Large** | ≥ 1200px | Large tablet landscape, desktop window | Persistent sidebar + multi-pane content |

*Note: For landscape windows with height < 480px, collapse vertical panes and avoid fixed two-column layouts.*

## Adaptive Layout Patterns

- **List-Detail (Two-pane)**: List occupies 320–400px; detail pane takes remaining space. On Compact (<600px), display one pane at a time, pushing the detail view onto the navigation stack with a return back button. Always display a placeholder in the detail pane when no row is selected.
- **Supporting Pane**: Main content area alongside a 280–360px contextual panel (filters, inspector, metadata). Collapses into a sheet or overlay on Medium/Compact.
- **Adaptive Grid**: Fluid card layouts using CSS Grid auto-fill:
  ```css
  .grid {
    display: grid;
    gap: 16px;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  }
  ```
- **Content Width Constraints**:
  ```css
  .prose { max-width: 65ch; }
  .form-container { max-width: 40rem; width: 100%; }
  .dialog-panel { max-width: 36rem; width: 100%; }
  ```

## Adaptive Shell Boilerplate

```css
:root {
  --pad: 16px;
  --nav-w: 0px;
  --list-w: 0px;
}

/* Compact layout (<600px) */
.app-shell {
  height: 100dvh;
  display: grid;
  grid-template-columns: var(--nav-w) minmax(0, 1fr);
  grid-template-rows: 1fr auto;
  grid-template-areas: "content content" "tabs tabs";
}

.nav-rail, .nav-sidebar { display: none; }
.tabbar {
  grid-area: tabs;
  padding-bottom: env(safe-area-inset-bottom);
}
.content {
  grid-area: content;
  min-height: 0;
  overflow: auto;
  overscroll-behavior: contain;
  padding-inline: var(--pad);
}

/* Medium layout (600–839px): Navigation rail */
@media (min-width: 600px) {
  :root { --pad: 24px; --nav-w: 80px; }
  .app-shell {
    grid-template-areas: "nav content";
    grid-template-rows: 1fr;
  }
  .nav-rail { display: flex; flex-direction: column; grid-area: nav; }
  .tabbar { display: none; }
}

/* Expanded layout (≥840px): Sidebar and multi-pane */
@media (min-width: 840px) {
  :root { --pad: 32px; --nav-w: 280px; --list-w: 360px; }
  .nav-rail { display: none; }
  .nav-sidebar { display: flex; flex-direction: column; grid-area: nav; }
  .content {
    display: grid;
    grid-template-columns: var(--list-w) minmax(0, 1fr);
    padding-inline: 0;
    overflow: hidden;
  }
  .pane-list, .pane-detail {
    overflow: auto;
    overscroll-behavior: contain;
    padding-inline: var(--pad);
  }
  .pane-list {
    border-inline-end: 1px solid var(--border-subtle);
  }
}

/* Container query for self-adapting pane components */
.pane {
  container-type: inline-size;
}

@container (min-width: 520px) {
  .card-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

## Component Adaptations: Phone vs. Tablet

| Component | Phone (Compact) | Tablet (Medium / Expanded) |
|---|---|---|
| **Action Sheet / Menu** | Full-bleed bottom sheet | Popover anchored to the triggering control |
| **Modal Forms** | Full-screen pushed view | Centered form sheet (480–640px wide) with dimmed backdrop |
| **Primary Actions** | Full-width button at screen bottom | Normal-width button aligned inside the active pane |
| **Filter Chips** | Single-line horizontal scroll | Wrapping chip group across multiple lines |
| **Navigation** | Bottom tab bar (3–5 items) | Navigation rail (medium) or persistent sidebar (expanded) |
| **Tab Controls** | Full-width segmented buttons | Natural-width segmented control or tabs |
| **Data Views** | Card stack / grouped rows | Multi-column table with sorting or list-detail pane |

## Multi-Modal Input Handling

```css
/* Base touch target */
.btn, .list-row, .menu-item {
  min-height: 44px;
}

/* Isolate hover to secondary pointer/trackpad environments */
@media (any-hover: hover) and (any-pointer: fine) {
  .row:hover {
    background-color: var(--surface-hover);
  }
}

/* Unambiguous focus indicators for physical keyboards */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

- **Keyboard Traversal**: Maintain logical DOM order matching visual layout. Support Escape to dismiss modals/popovers and arrow keys for list/grid navigation.
- **Pointer & Pen Support**: Rely on Pointer Events (`pointerdown`, `pointerup`, `pointermove`). Check `e.pointerType === 'pen'` for stylus interactions and keep standard `<input>` elements intact to preserve OS handwriting-to-text integration.

## Tablet Audit Checklist

- [ ] Breakpoints defined via window width classes (<600px, 600–839px, ≥840px), not user-agent strings.
- [ ] No stretched phone views: prose capped at `max-width: 65ch`; forms/dialogs capped at 480–640px.
- [ ] List-detail panes render correctly in expanded view, collapsing smoothly to single-pane navigation in compact view.
- [ ] Detail pane displays an intentional empty state when no list item is selected.
- [ ] Navigation adapts appropriately: bottom tabs on compact, rail on medium, persistent sidebar on expanded.
- [ ] Common interactive controls positioned near side edges for comfortable landscape grip.
- [ ] Touch targets remain ≥44×44px across all screen widths.
- [ ] Hover styles restricted to `(any-hover: hover) and (any-pointer: fine)`.
- [ ] Clear `:focus-visible` styling and logical keyboard tab progression verified.
- [ ] Resizing or rotating the screen preserves active selection, draft inputs, and scroll offsets.
