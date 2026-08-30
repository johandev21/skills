# Structure — Placement, Layering, Naming

Reference for SKILL.md steps 1–3 and 5. Load when placing files, auditing layout, or fixing imports.

## Canonical layout

```text
src/
├── app/            # providers, router, config, app.tsx
│   ├── providers/
│   ├── router/
│   └── config/
├── pages/          # route composition only (dashboard/login/settings)
├── features/       # business domains — owns its behavior
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/       # domain behavior (use-login, use-current-user)
│   │   ├── api/         # endpoint functions (login.ts, get-current-user.ts)
│   │   ├── types/       # auth.types.ts
│   │   ├── schemas/     # auth.schema.ts
│   │   ├── utils/       # normalize-user.ts
│   │   └── index.ts     # public API
│   ├── projects/
│   └── billing/
├── shared/         # genuinely cross-domain reuse only
│   ├── components/ # button, modal, dialog
│   ├── hooks/      # use-debounce, use-media-query
│   ├── utils/      # format-date, cn
│   ├── api/        # api-client.ts, api-error.ts
│   ├── types/      # common.types.ts
│   └── constants/
├── assets/
├── styles/
└── main.tsx
```

## Placement: feature-local vs shared

Default to feature-local. Promote only after concrete reuse.

| Keep in `features/<domain>/` | Promote to `shared/` only when |
|---|---|
| `features/orders/components/order-status.tsx` — used by several order pages but still order-owned | `shared/components/button/` — no domain ownership |
| `features/projects/hooks/use-projects.ts` | `shared/hooks/use-debounce.ts` — generic React behavior |
| `features/projects/utils/sort-projects.ts` | `shared/utils/format-date.ts` — cross-domain pure utility |
| `features/projects/api/get-projects.ts` | `shared/api/api-client.ts` — transport only |

Check: would renaming the item require a domain term (project, order, billing)? If yes, it stays feature-local.

## API split

- `shared/api/api-client.ts` — HTTP client, interceptors, `ApiError` (no endpoint knowledge).
- `features/<domain>/api/*.ts` — endpoint functions wrapping the client:

```ts
// features/projects/api/get-projects.ts
export async function getProjects(params: GetProjectsParams) {
  return apiClient.get<Project[]>("/projects", { params });
}
```

Hooks in `features/<domain>/hooks/` orchestrate server state:

```ts
export function useProjects(params: GetProjectsParams) {
  return useQuery({ queryKey: projectKeys.list(params), queryFn: () => getProjects(params) });
}
```

## Dependency direction

```text
app → pages → features → shared
```

| Import | Verdict |
|---|---|
| `features → shared` | ✅ |
| `pages → features`, `pages → shared` | ✅ |
| `app → everything` | ✅ |
| `shared → features` | ❌ |
| `shared → pages` | ❌ |
| `features → pages` | ❌ |

Treat each feature's `index.ts` as public boundary:

```ts
// ✅ Good — consume public API
import { ProjectCard, useProjects } from "@/features/projects";

// ❌ Avoid — reach into internals
import { useProjects } from "@/features/projects/hooks/queries/internal/use-projects";
```

## Naming and barrels

Use predictable, searchable filenames:

| Kind | Pattern | Examples |
|---|---|---|
| Hooks | `use-<domain>-<action>.ts` | `use-projects.ts`, `use-create-project.ts` |
| API | `<verb>-<resource>.ts` | `get-projects.ts`, `delete-project.ts` |
| Components | `<domain>-<thing>.tsx` | `project-card.tsx`, `project-table.tsx` |
| Types/schemas | `<domain>.types.ts` / `<domain>.schema.ts` | `project.types.ts`, `login.schema.ts` |

Avoid vague names `helpers.ts`, `common.ts`, `utils.ts`, `manager.ts`, `service.ts` when a specific name is possible.

Barrels: moderate use at feature boundary only. `features/projects/index.ts` re-exports the public surface. Do not add `index.ts` in every subdirectory for its own sake.

## Anti-pattern to fix

```text
src/components/  src/hooks/  src/services/  src/utils/  src/types/  src/stores/
```

At ~20 files it looks tidy; at 800 files one feature scatters across 7 folders (`components/project-table.tsx`, `hooks/use-projects.ts`, `services/project-service.ts`, …). Consolidate into `features/projects/` with its own `components/`, `hooks/`, `api/`, `types/`, `utils/`.
