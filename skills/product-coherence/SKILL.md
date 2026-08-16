---
name: product-coherence
description: Enforce design-system consistency, product-specific hierarchy, and cross-screen coherence when building or modifying UIs. Use this skill whenever the user mentions design system, component library, visual consistency, product polish, UI patterns, design tokens, brand guidelines, cross-screen consistency, interaction patterns, confirmation dialogs, button ordering, spacing systems, typography scale, or when they express concern about generic-looking interfaces, inconsistent components, drifting styles, incoherent UX, fragmented design, or multiple similar elements that don't match. Also use when reviewing generated UI code to prevent the "polished but generic" failure mode where each screen looks good in isolation but the product lacks cohesion. This skill is critical for maintaining professional product quality beyond individual component generation.
compatibility: Requires read access to existing UI files, design token files, component libraries, and style guides. Works with React, Vue, Svelte, Angular, Next.js, Nuxt, and other frontend frameworks.
---

# Product Coherence Skill

This skill prevents **Generic and Incoherent Product Design** — a documented AI failure mode where agents produce familiar polished patterns without product-specific hierarchy, then drift across screens in spacing, components, wording, and interaction.

## Why this matters

Research on 2026 AI-generated frontends found that while individual screens can look polished in isolation, products lose cohesion rapidly without explicit design intent. A blinded study with 92 participants rated AI prototypes positively on pragmatic usability but neutral/negative on originality and innovation. The root cause: conventional patterns are statistically safe for LLMs; repository-scale design intent is under-specified.

**Consequences of incoherence:**
- Weak differentiation from competitors
- Increased cognitive load for users
- Inconsistent behavior expectations
- Expensive redesign later
- Review overload as duplication accumulates

## Core principles

1. **Design tokens before inline styles** - Centralize spacing, colors, typography, radii, shadows
2. **Component inventory before new components** - Check what exists before creating variants
3. **Cross-screen review before shipping** - Verify consistency across related workflows
4. **Product-specific language** - Avoid generic labels; use domain terminology consistently
5. **Interaction pattern documentation** - Document how common actions (confirmations, forms, navigation) behave

## Workflow

### Phase 1: Audit existing design language

Before making changes, understand what already exists:

1. **Find design tokens**: Search for `theme`, `tokens`, `design-system`, `variables`, `colors.ts`, `spacing.ts`, or framework-specific theming files
2. **Inventory components**: List reusable UI components in `components/`, `ui/`, or similar directories
3. **Check content guidelines**: Look for copy patterns, label conventions, button text standards
4. **Review recent screens**: Examine 2-3 recently built pages for patterns and inconsistencies

If no design system exists, propose creating one rather than adding more ad-hoc styles.

### Phase 2: Apply coherence constraints

When generating or modifying UI:

#### Spacing and layout
- Use the project's spacing scale (e.g., `spacing-1` through `spacing-8`) instead of arbitrary values
- Maintain consistent padding/margin relationships within component types
- Use established grid or flex patterns from existing pages

#### Typography
- Use defined type scale (heading sizes, body text, captions)
- Maintain consistent heading hierarchy (h1 > h2 > h3)
- Don't introduce new font weights or sizes unless justified

#### Colors
- Use semantic color tokens (`primary`, `danger`, `success`) not raw hex codes
- Respect established color roles (primary actions, destructive actions, informational)
- Maintain sufficient contrast ratios (documented minimums)

#### Components
- Reuse existing component variants before creating new ones
- If a variant is needed, extend the existing component rather than duplicating it
- Document new variants in the component's storybook/docs if they exist

#### Interaction patterns
- **Confirmation dialogs**: Consistent button order (typically Cancel left, Confirm right), consistent terminology ("Delete" vs "Remove"), consistent styling
- **Form validation**: Consistent error placement, messaging tone, recovery options
- **Loading states**: Consistent spinner/loading pattern, skeleton screens, or progress indicators
- **Empty states**: Consistent illustration style, messaging, call-to-action placement
- **Error states**: Consistent error messaging, retry mechanisms, escalation paths

#### Language and microcopy
- Use domain-specific terms consistently (not mixing "user", "customer", "member")
- Maintain consistent tone (formal/casual) across screens
- Use consistent verb forms in buttons ("Save" vs "Saving..." vs "Saved")

### Phase 3: Cross-screen validation

After implementing changes:

1. **Compare with similar screens**: If you built a confirmation dialog, check other confirmation dialogs in the codebase
2. **Verify token usage**: Ensure no hardcoded values slipped in
3. **Check responsive behavior**: Test at multiple breakpoints using existing patterns
4. **Review accessibility**: Ensure semantic HTML, keyboard navigation, focus management match project standards
5. **Document deviations**: If intentional differences exist (e.g., special case), document why

### Phase 4: Prevent scope creep

AI agents tend to add rather than consolidate. Counter this by:

- **Reuse checks**: Before creating `NewButton.tsx`, search for existing button components
- **Architecture budgets**: Limit new dependencies, state management patterns, form libraries
- **Small diffs**: Prefer extending existing infrastructure over introducing competing patterns
- **Characterization tests**: Ensure changes don't break distant behavior

## Red flags

Watch for these signs of incoherence:

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Multiple confirmation dialog styles | No shared component | Extract to `<ConfirmDialog>` |
| Hardcoded spacing values | Missing design tokens | Add to theme/tokens file |
| Mixed terminology ("delete"/"remove") | No content guidelines | Create copy reference doc |
| Different loading patterns per page | No loading strategy | Standardize with `<LoadingState>` |
| New CSS utility classes every PR | Ad-hoc styling | Use existing design system classes |
| Three different form libraries | Scope creep | Standardize on one |

## Example: Fixing confirmation dialog inconsistency

**Problem**: Three screens have visually different confirmation dialogs with different button orders and terminology.

**Bad approach**: Generate a fourth dialog matching none of the others.

**Good approach**:
1. Audit all three existing dialogs
2. Identify the most accessible, consistent pattern
3. Extract shared logic into `<ConfirmDialog>` component
4. Update all three screens to use it
5. Document the pattern for future use

```tsx
// Before: Inline dialog in DeleteUser.tsx
<div className="fixed inset-0 bg-black/50">
  <div className="bg-white p-6 rounded">
    <p>Delete this user?</p>
    <button>No</button>
    <button>Yes</button>
  </div>
</div>

// After: Reusable component
import { ConfirmDialog } from '@/components/ui/confirm-dialog'

<ConfirmDialog
  open={showDeleteConfirm}
  title="Delete user"
  description={`Are you sure you want to delete ${user.name}? This action cannot be undone.`}
  cancelLabel="Cancel"
  confirmLabel="Delete user"
  variant="destructive"
  onCancel={() => setShowDeleteConfirm(false)}
  onConfirm={handleDelete}
/>
```

## When to escalate

Some coherence issues require human judgment:

- **Brand positioning**: Should the product feel playful or serious?
- **Visual hierarchy**: What's the primary action on this screen?
- **Information architecture**: How should content be grouped?
- **Accessibility tradeoffs**: When design conflicts with WCAG requirements

Flag these for designer/product owner review rather than guessing.

## Integration with other skills

- Use with `frontend-design` skill when building new interfaces from scratch
- Combine with accessibility audits to ensure coherence doesn't compromise accessibility
- Pair with component testing to verify reused components work in all contexts

## References

Based on 2026 research:
- "Usable but Conventional" study: AI prototypes rated neutral/negative on originality despite positive usability scores
- Practitioner reports: Rapid cohesion loss without design system enforcement
- Agentic behavior studies: Lower-experience contributors changed 1.47× more files with AI assistance, leading to duplication

The goal is not to eliminate creativity but to channel it within a coherent product vision.
