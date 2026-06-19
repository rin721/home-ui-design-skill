---
name: home-ui-design-skill
description: Generate calm, rounded, content-first modular UI with cool accent tokens, compact navigation, responsive layouts, component states, and accessibility constraints. Use for content homepages, landing pages, product sections, profile pages, knowledge indexes, archive views, mobile content pages, component library specs, HTML/CSS, React, Vue, Tailwind, Figma prompts, and reusable interface rules. Do not use for dense enterprise data grids, trading screens, game HUDs, cyberpunk themes, luxury editorial art direction, heavy brand reproduction, unlicensed assets, or one-to-one page copies.
---

# home-ui-design-skill

## Goal

Use this skill to generate calm, rounded, content-first modular UI. The default visual language is low-chroma cool accents, paired light/dark tokens, rounded cards, compact metadata, icon-led tool controls, clear heading hierarchy, and verifiable responsive behavior.

## Accepted Inputs

- `page_type`: `homepage`, `landing`, `product-section`, `profile`, `archive`, `article`, `mobile-page`, `component-library`, or `custom`.
- `audience`: target users, reading context, and device context.
- `content_inventory`: headings, body copy, metadata, tags, metrics, forms, media, and CTAs.
- `brand_controls`: optional hue, accent intensity, typography, density, radius, and motion strength.
- `technology_target`: `design-spec`, `html-css`, `react`, `vue`, `tailwind`, `figma-prompt`, `wireframe`, or `component-library`.
- `accessibility_level`: `baseline`, `strict`, or `enhanced`.
- `device_priority`: `desktop-first`, `mobile-first`, or `balanced`.

When input is incomplete, make the smallest reasonable assumption: content-oriented page, default cool accent, balanced device priority, baseline accessibility, and neutral replaceable placeholder content.

## Runtime Procedure

1. Identify page type, audience, content inventory, device priority, technology target, and accessibility level.
2. Read `design-tokens.json` and choose the light/dark tokens and replaceable tokens.
3. Read `style-profile.md` to lock the visual boundaries and adaptation range.
4. Read `layout-patterns.md`; for full pages, choose one primary layout and one fallback layout; for sections, choose only relevant patterns.
5. Read `component-recipes.md` and load only the component recipes needed for the request.
6. Read `interaction-rules.md`, `responsive-rules.md`, and `content-rules.md` to add state, keyboard, breakpoint, and copy rules.
7. Read `adaptation-rules.md` only when the user asks to change hue, type, radius, density, motion, or style direction.
8. Read `output-modes.md` and format the deliverable as a spec, code, prompt, wireframe, or component library.
9. Before delivery, run `validation-checklist.md` and fix missing tokens, states, responsive behavior, accessibility, or release hygiene.

## File Reading Order

1. `design-tokens.json`
2. `style-profile.md`
3. `layout-patterns.md`
4. `component-recipes.md`
5. `interaction-rules.md`
6. `responsive-rules.md`
7. `content-rules.md`
8. `adaptation-rules.md`, only for style substitutions
9. `output-modes.md`
10. `validation-checklist.md`
11. `prompt-templates.md`, only when reusable prompts are requested
12. `examples/`, only when an example format or demo reference is useful

## Output Rules

- Default to a structured UI design spec; when a technology target is provided, add matching implementation details after the design decisions.
- Map colors, radii, shadows, spacing, type, motion, breakpoints, and z-index to semantic tokens.
- Code output must define CSS variables or framework theme mappings before component structure.
- Dark mode must set token overrides, `color`, `background`, and `color-scheme` on the same theme scope. Do not set text color only on `:root` and then override tokens in a nested `.dark` scope.
- React and Vue output must include props/state models, accessible attributes, keyboard behavior, and reduced-motion handling.
- Tailwind output must explain the token-to-theme strategy; use arbitrary values only when a token is missing.
- Figma prompts must include frames, tokens, layout, component list, interaction annotations, responsive variants, and accessibility notes.
- Placeholder content must be neutral and replaceable. Do not invent real brands, people, domains, prices, or unsupported metrics.

## Core Design Principles

- Use a calm cool-hue system with low-chroma backgrounds and a clear primary accent.
- Keep surfaces rounded, readable, and modular. Use cards for repeated items, modals, tool panels, or content that genuinely needs framing.
- Do not turn every page section into a floating card. Page sections should be full-width bands or unframed layouts.
- Prefer compact icons for tool buttons and clear text for primary navigation and CTA actions.
- Use strong headings, muted metadata, and short descriptions. Keep pages spacious but not sparse.
- Hover must not shift layout; active, focus, disabled, loading, empty, error, and success states must be complete for applicable controls.
- Mobile uses a single column, compact top bar, 44px touch targets, natural wrapping, and stable media ratios.
- Accessibility wins over decoration: visible focus, keyboard support, non-color-only states, and reduced-motion behavior are required.
- Check actual computed colors in both light and dark modes for headings, brand text, navigation, card titles, body copy, muted copy, buttons, icons, and focus rings.

## Forbidden Output

- Do not use private marks, private illustrations, owned photos, copied icon sets, unlicensed copy, or recognizable business data.
- Do not create a one-to-one page copy or require a fixed page order or fixed item count.
- Do not ship interactive components without keyboard behavior, focus, error text, or reduced-motion behavior.
- Do not use pure gradients, purely decorative backgrounds, or one-note color palettes as substitutes for real interface structure.
- Do not name real entities in examples unless the user supplied them.
- Do not include hidden preparation notes, creation-history notes, or private naming.

## Example Calls

```text
Use home-ui-design-skill to create a mobile-first product landing page for a team productivity app. Output a UI design spec and Tailwind implementation notes.
```

```text
Use home-ui-design-skill to generate a component library spec for navigation, cards, tags, forms, modals, and archive lists.
```

```text
Use home-ui-design-skill to produce a React homepage with a cool accent palette, rounded cards, compact metadata, and strict accessibility checks.
```
