# Personal Skills

A collection of my personal skills for AI coding agents.

## Install

Install every skill in this repo with:

```bash
npx skills add johandev21/skills
```

To install a single skill, point at its directory. Or just copy the `skills/<name>/SKILL.md` into your agent's skill folder.

## Skills

| Skill | What it does |
| ----- | ------------ |
| [feature-first-architecture](skills/feature-first-architecture/SKILL.md) | Enforce feature-first architecture for React/TypeScript frontends - organize code by domain (`app/pages/features/shared`), direct dependency flow, and keep `.tsx` composition-focused. |
| [readable-react](skills/readable-react/SKILL.md) | Write and refactor React components with composition and readability as the primary goals: main component on top reading like a high-level description of the UI, implementation details in small named components and helpers below. |
| [missing-non-happy-states](skills/missing-non-happy-states/SKILL.md) | Audit and improve frontend features for complete loading, empty, error, offline, partial, permission, malformed-data, and recovery state coverage. |
| [product-coherence](skills/product-coherence/SKILL.md) | Enforce design-system consistency and product-specific hierarchy across screens: design tokens over hardcoded values, component reuse over duplication, consistent terminology and interaction patterns, and cross-screen validation so every screen feels like the same product. |
| [flashcards](skills/flashcards/SKILL.md) | Turn source material into high-quality Anki flashcards - one atomic fact per card, active recall, standalone prompts - and push them into Anki automatically in source order, skipping duplicates. |
| [no-ui-slop](skills/no-ui-slop/SKILL.md) | Eliminate generic AI-generated UI patterns into intentional product interfaces: hierarchy through type and spacing before containers, one restrained visual system, justified decoration, and task-fit density. |

