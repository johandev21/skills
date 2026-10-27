# Mobile-Native Web Design Reference

## Viewport and Document Head

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
```

- `viewport-fit=cover` is mandatory; without it, `env(safe-area-inset-*)` evaluates to 0.
- Never add `user-scalable=no` or `maximum-scale=1`. Fix auto-zoom via input typography instead.
- Target a base design width of 390px, validating at 360px and 430px. Ensure no layout breakage down to 320px.

## Base CSS Reset

```css
html {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  -webkit-tap-highlight-color: transparent;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: system-ui, -apple-system, "SF Pro Text", "Segoe UI", Roboto, sans-serif;
  font-size: 17px;
  line-height: 1.4;
  overscroll-behavior-y: none;
  -webkit-font-smoothing: antialiased;
}

/* Eliminate tap delay */
button, a, [role="button"], input, select, textarea, label {
  touch-action: manipulation;
}

/* Prevent accidental text selection on controls */
button, [role="button"], .tab, .chip {
  -webkit-user-select: none;
  user-select: none;
  -webkit-touch-callout: none;
}

img {
  -webkit-user-drag: none;
}

/* Restrict hover effects to fine pointer devices */
@media (hover: hover) and (pointer: fine) {
  .row:hover { background: var(--hover); }
}

/* Instant press feedback */
button:active, [role="button"]:active {
  transform: scale(0.97);
  opacity: 0.85;
  transition: transform 60ms ease, opacity 60ms ease;
}

/* Reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Safe Area Insets and Full-Height Shell

```css
:root {
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left: env(safe-area-inset-left, 0px);
  --safe-right: env(safe-area-inset-right, 0px);
}

.top-bar {
  padding-top: var(--safe-top);
}

.bottom-bar {
  padding-bottom: var(--safe-bottom);
}

.sheet {
  padding-bottom: calc(16px + var(--safe-bottom));
}

.page {
  padding-inline: max(16px, var(--safe-left)) max(16px, var(--safe-right));
}

/* Shell that adapts to browser chrome */
.app-shell {
  min-height: 100vh; /* Fallback */
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
}
```

## Form Inputs and Virtual Keyboard

```css
/* Prevent iOS zoom on focus */
input, select, textarea {
  font-size: max(16px, 1em);
}
```

- **Input Attributes**: Always supply `type` (`email`, `tel`, `search`, etc.), `inputmode` (`numeric`, `decimal`), `autocomplete`, and `enterkeyhint` (`send`, `next`, `done`, `search`).
- **Keyboard Overlap Defense**:
  - Avoid `position: fixed; bottom: 0` for composer bars or submit buttons on iOS Safari; prefer flex column shells with `height: 100dvh`.
  - Add `interactive-widget=resizes-content` to viewport meta where Android Chrome is targeted.
  - Set `scroll-margin-bottom: 2rem` or `scroll-padding-bottom: 4rem` on inputs to maintain scroll clearance when focused.

## Component Specifications

| Component | Dimensions & Placement | Interaction Rules |
|---|---|---|
| **Bottom Tab Bar** | 49–56px height + `var(--safe-bottom)`. 3–5 destinations max. | Highlight active tab with filled icon and distinct color. Short 1-word labels. |
| **Top Navigation Bar** | 44–56px height + `var(--safe-top)`. | Back button at top-left. Left-aligned or centered title. Max 2 trailing action buttons. |
| **Bottom Sheet** | 16–24px top border radius. Dimmed backdrop. | Include drag handle. Drag down to dismiss or tap backdrop. Prevent background scroll with `overscroll-behavior: contain`. |
| **Grouped List** | 52–60px row height. Inset 1px dividers. | Chevron right for navigational items. Whole row tappable (≥44px height). |
| **Switch** | ~51×31px container. | Direct thumb toggle for on/off states; replace binary checkboxes. |
| **Segmented Control** | 32–40px height, full-width or natural width. | 2–4 options max for immediate view filtering. |

## State Handling Matrix

| State | Pattern | Implementation Rule |
|---|---|---|
| **Initial Load** | Skeletons with soft shimmer | Skeletons match layout geometry; avoid full-screen blocking spinners. |
| **Incremental Load** | Local indicators | Keep existing list/feed content rendered; load more inline. |
| **Optimistic Action** | Immediate visual change | Update state in UI instantly; roll back quietly with notification only on failure. |
| **Empty** | Icon + explanation + action | Clarify what belongs here and offer a single primary CTA. |
| **Error** | Plain message + retry CTA | Keep any previously fetched data visible; isolate error banner to failing section. |
| **Offline** | Persistent status banner | Indicate what remains functional and queue pending offline actions. |

## PWA and Standalone Configuration

```html
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="App Title">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
```

- When using `black-translucent`, content draws behind the iOS status bar; pad top navigation bars with `env(safe-area-inset-top)`.
- Set `background_color` in the web manifest to match the primary splash background to prevent launch flashes.

## Mobile Audit Checklist

- [ ] Viewport meta specifies `viewport-fit=cover` and allows user zoom.
- [ ] Application shell utilizes `100dvh` (with `100vh` fallback); no raw `100vh` on full-screen containers.
- [ ] Safe-area padding applied to top bar, bottom bar, modal sheets, and horizontal screen edges.
- [ ] Every tap target measures ≥44×44px with ≥8px separation.
- [ ] Primary actions and primary navigation live in the thumb zone (lower screen half).
- [ ] All inputs, selects, and textareas set `font-size: max(16px, 1em)`.
- [ ] Appropriate `inputmode`, `autocomplete`, and `enterkeyhint` configured for each field.
- [ ] No sticky elements obscured when the virtual keyboard is triggered.
- [ ] `:active` states respond immediately (<100ms) on touch.
- [ ] Hover styles restricted to `@media (hover: hover) and (pointer: fine)`.
- [ ] Animations use exclusively `transform` and `opacity`, honoring `prefers-reduced-motion`.
- [ ] Skeletons, empty, error, and offline representations tested and styled.
