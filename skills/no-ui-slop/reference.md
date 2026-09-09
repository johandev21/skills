# Reference — Intentional Targets per Concern

Reference for SKILL.md steps 3–5. Load the section the current branch touches; skip the rest.

The bar throughout: each element communicates hierarchy, state, grouping, or interaction. What fails the bar goes.

## Layout and hierarchy

Build with open layout, whitespace, alignment, and typography. Keep nesting shallow at `Page → Section → Content`. Center and symmetrize only when the reading flow calls for it; align to content hierarchy by default. Give the page a deliberate spacing rhythm and size heroes and padding to the content they hold.

Guardrails: one card level per region, never cards inside cards; no outer card around a major page section unless the section is a genuinely independent object.

## Borders and surfaces

Separate stacked rows and sections with gap, padding, and layout rhythm. Let whitespace carry the separation and keep row height to content plus breathing room. Reach for a border, divider, or tinted surface only to signal grouping, state, or interaction. Keep glass and backdrop blur for products whose direction explicitly calls for them.

Guardrail: no `border-b` row or section dividers.

## Border radius

Hold one small, consistent radius scale across buttons, inputs, cards, badges, and panels. Reserve fully rounded pills for controls and semantics that are naturally pill-shaped.

## Color

Work from one clear accent plus semantic state colors drawn from the product tokens. Keep gradients, gradient text, and neon-on-dark for brands whose direction explicitly requires them.

## Typography

Carry hierarchy with type size, weight, and spacing before reaching for containers. Write labels in Title Case. Vary weight with intent: headings and actions lead, body text stays quiet and readable. Set counts and amounts as bare numerals with tabular alignment. Follow the product's type system over component-library defaults.

Guardrail: no parenthesized counts such as (3).

## Cards

Give cards to independent, meaningful units: selectable entities, reusable objects, collection items, content needing containment. Lay out headings with short text, related fields, and breathing room as plain sections.

## Buttons and actions

Give each action one clear control with primary, secondary, and tertiary order. Reach for links or text actions at low emphasis. Add an icon to a button only when it improves recognition or navigation.

Guardrail: never duplicate the same action in a section header and its body.

## Icons

Place an icon where it communicates information or aids navigation, following established conventions. Leave headings and cards unadorned when text alone is clearer. Keep icons unboxed unless the box itself carries meaning.

Guardrail: no emoji as interface icons.

## Badges and pills

Give badges to compact status, category, or state. Render ordinary metadata as normal text. Keep one badge style per meaning; add a style only for a meaningful distinction.

Guardrail: no pill sitting above a heading as decoration.

## Forms

Structure forms with labels, helper text, and spacing. Write helper text that adds what the label does not state. Keep selected, hover, focus, disabled, and error states visually distinct, with the stronger state holding steady under hover.

## Navigation

Reach for chevrons, tabs, breadcrumbs, and simple links before inventing controls. Keep icon-only controls for immediately obvious meanings. Keep filter tabs as plain labels and let the result count live where results are counted: the table footer, pagination, or result summary. Lay out multi-part context as spaced elements or hierarchical breadcrumbs rather than one inline string. Keep navigation visually quieter than primary content.

Guardrails: no per-tab counts; no `·`-joined inline labels such as Accounts Payable · Freight.

## Interaction states

Design each state explicitly: default, hover, focus, active, selected, disabled, loading, error, success. Hold this precedence: selected, active, checked, and disabled stay visually stable under hover and focus. Keep hover to a subtle functional shift, never a generic `scale()` with shadow-and-lift.

## Animation

Animate to explain a state change, spatial relationship, or feedback event. Leave static what is already clear. Keep motion subtle and functional, free of bounce, glow, parallax, and floating effects, and honor `prefers-reduced-motion`.

Guardrail: no entrance cascade applied section by section down a page.

## Shadows

Spend elevation where it communicates layering, floating behavior, or hierarchy. Keep resting surfaces flat. Reserve large soft shadows for genuinely floating layers, never as generic polish.

## Component libraries

Treat library components as primitives, not final designs. Strip default borders, radii, padding, and separators that fight the product layout. Compose `Card`, `Badge`, `Separator`, and `Button` deliberately: each instance passes the top-of-file bar or goes.

Guardrail: no symmetric three-column card grid as the default for unrelated content.

## Content density

Set density to the task: product interfaces optimize for scanning and completion. Keep related information spatially close. Spend whitespace to separate meanings, not to imitate landing-page airiness.

## Responsiveness

Reconsider hierarchy and action placement per breakpoint rather than stacking the desktop grid into one long column. Reset desktop-scale padding for small screens. Keep overlays, popovers, and dropdowns inside the usable viewport with collision-aware positioning.

## Product specificity

Shape every element to the actual task, content, and interaction model. Prefer product-specific workflows over generic dashboards and SaaS section filler. Ship only real content and data.

Guardrail: no invented metrics, testimonials, statistics, or decorative datasets.

## Final design test

Review every card, border, divider, separator, badge, icon, count, tab label, gradient, shadow, animation, and container. For each one, ask: does this communicate hierarchy, state, grouping, or interaction? What fails the bar goes. The interface reads as intentional hierarchy, spacing, and product-specific decisions.
