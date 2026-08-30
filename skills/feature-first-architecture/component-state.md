# Component & State — Composition, Extraction, State Ownership

Reference for SKILL.md steps 4–5. Load when editing `.tsx`/`hooks` or deciding where state lives.

## .tsx is composition; .ts owns behavior

Make `.tsx` tell what the UI does; hide implementation details in `.ts` modules.

**Before — component owns everything:**

```tsx
export function ProjectList() {
  const [query, setQuery] = useState("");
  const { data, isLoading } = useQuery({ queryKey: ["projects", query], queryFn: () => fetch(`/api/projects?q=${query}`).then(r => r.json()) });
  const filteredProjects = data?.filter(p => p.active).sort((a,b) => a.name.localeCompare(b.name));
  const handleDelete = async (id: string) => { await fetch(`/api/projects/${id}`, { method: "DELETE" }); };
  return <div>{/* lots of JSX */}</div>;
}
```

**After — extract to feature modules:**

```text
features/projects/
├── components/project-list.tsx   # composition only
├── hooks/use-project-list.ts    # query + UI state + actions
├── api/get-projects.ts          # fetch
├── api/delete-project.ts
└── utils/sort-projects.ts       # transforms
```

```tsx
export function ProjectList() {
  const { projects, query, setQuery, isLoading, deleteProject } = useProjectList();
  if (isLoading) return <ProjectListSkeleton />;
  return (
    <section>
      <ProjectSearch value={query} onChange={setQuery} />
      <ProjectGrid>{projects.map(p => <ProjectCard key={p.id} project={p} onDelete={deleteProject} />)}</ProjectGrid>
    </section>
  );
}
```

## What to extract vs keep inline

| Keep inline in `.tsx` | Extract to `.ts` / hook / utils |
|---|---|
| Trivial UI state `const [isOpen, setIsOpen] = useState(false)` | Chain transforms `filter → map → reduce → sort` → `utils/sort-projects.ts` |
| Direct setter `<Button onClick={() => setOpen(true)}>` | Event sequences with side effects → `handleDelete` in hook |
| Obvious one-line expression in JSX | Fetches, query keys, invalidation → `api/*.ts` + `hooks/use-*.ts` |
| | Meaningful derivation worth naming → `visibleProjects`, `getStatusClassName` |

Rule: extract when naming the piece removes nested reasoning from the `.tsx` outline. Leave it inline when extraction would make the reader jump without clarifying the parent. For intra-component composition (focused subcomponents, branch states), use `readable-react`.

## State ownership

Prefer the narrowest owner. Promote only after concrete cross-feature need.

| Category | Owner | Examples |
|---|---|---|
| Server state | `TanStack Query` (or equivalent) in `features/*/hooks` + `api` | `useProjects`, `useCreateProject`, `projectKeys` |
| URL state | Router / search params | filters, pagination, tab — `useSearchParams` |
| Form state | Form library / local state | `react-hook-form`, `useState` in form component |
| Local UI state | `useState` / `useReducer` in component | `isOpen`, `selectedId` |
| Cross-feature app state | Global store / context (last resort) | auth session, theme |

Avoid a huge global `store/` for server, URL, or form state. Not everything belongs in Redux/Zustand/Context.

## Colocation — option, not requirement

When a component is complex, colocating its tightly coupled files keeps context together. Use only when the logic belongs to that single component.

```text
# Global-feature layout (default — scales well)
features/projects/
├── components/project-table.tsx
├── hooks/use-projects.ts
├── api/get-projects.ts
└── utils/sort-projects.ts

# Colocated layout (option for complex components)
features/projects/components/project-table/
├── project-table.tsx
├── project-table.hooks.ts      # component-specific behavior only
├── project-table.columns.tsx
├── project-table.types.ts
└── index.ts
```

Guidance:

- Use colocation when a hook/type/column definition is used by exactly one component. Name it `project-table.hooks.ts` to signal scope.
- Keep shared domain behavior in `features/<domain>/hooks/` (e.g., `use-projects`), not inside a single component folder.
- Keep project-wide conventions (file naming, barrel rules) from `structure.md` even inside colocated folders.
- Do not create every layer upfront (`entities/repositories/use-cases/adapters`). Start with `app/pages/features/shared` and add abstractions after a concrete need appears.
