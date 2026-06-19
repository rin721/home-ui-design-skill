---
name: home-ui-design-skill
description: Generate calm, rounded, content-rich UI systems with cool accent tokens, modular cards, compact navigation, responsive editorial or product layouts, interaction states, and accessibility checks. Use when Codex needs to create UI design specs, HTML/CSS, React, Vue, Tailwind, Figma prompts, component libraries, landing pages, homepages, product sections, archive views, mobile pages, or reusable interface rules with a soft modular visual language.
---

# home-ui-design-skill

## Skill Name

home-ui-design-skill

## Description

This skill creates clean, soft, modular interfaces for content-heavy pages, product storytelling, knowledge hubs, profile surfaces, landing pages, and mobile-first page flows. It uses cool-hue accents, rounded cards, calm page backgrounds, concise metadata, icon-led controls, readable type, and responsive layout rules.

## Use This Skill For

- Homepages, landing pages, product introduction pages, documentation indexes, profile pages, archive timelines, dashboards with light content density, and mobile page shells.
- UI design specs that need tokens, layout grammar, component recipes, interaction states, responsive behavior, and validation checks.
- Frontend implementation plans for HTML/CSS, React, Vue, or Tailwind.
- Figma prompts, wireframe outlines, and component library specifications.

## Do Not Use This Skill For

- Dense enterprise data grids, trading screens, dark cyberpunk themes, luxury editorial art direction, game HUDs, or highly experimental motion.
- Interfaces that require heavy skeuomorphism, aggressive gradients, oversized marketing spectacle, or brand asset reproduction.
- Any output that depends on private assets, recognizable marks, owned illustrations, or unlicensed copy.

## Trigger Phrases

- "Use home-ui-design-skill"
- "Create a calm modular UI"
- "Generate a rounded card homepage"
- "Build a soft editorial layout"
- "Make a cool-accent landing page"
- "Design a mobile content page"
- "Create component recipes for a gentle product UI"

## Input Parameters

- `page_type`: homepage, landing, product-section, profile, archive, article, mobile-page, component-library, or custom.
- `audience`: target user group and reading context.
- `content_inventory`: headings, body copy, metadata, tags, metrics, forms, media, and CTA needs.
- `brand_controls`: optional primary hue, accent intensity, typography choice, density, and motion strength.
- `technology_target`: design-spec, html-css, react, vue, tailwind, figma-prompt, wireframe, or component-library.
- `accessibility_level`: baseline, strict, or enhanced.
- `device_priority`: desktop-first, mobile-first, or balanced.

## Output Forms

- Structured UI design spec.
- HTML/CSS implementation.
- React component plan or implementation.
- Vue component plan or implementation.
- Tailwind class strategy.
- Figma prompt.
- Wireframe outline.
- Component library specification.
- Landing page structure.
- Responsive layout plan.

Default output is a structured UI design spec. When a technology target is provided, include the matching implementation details after the design decisions.

## Runtime Procedure

1. Identify `page_type`, `audience`, `content_inventory`, `device_priority`, and `technology_target`.
2. Read `design-tokens.json` first and choose the token set.
3. Read `style-profile.md` to lock the visual direction.
4. Read `layout-patterns.md` to select a layout grammar.
5. Read `component-recipes.md` for the needed components.
6. Read `interaction-rules.md` for states, motion, and keyboard behavior.
7. Read `responsive-rules.md` for breakpoint behavior.
8. Read `content-rules.md` for headings, copy density, metadata, labels, and CTA rhythm.
9. Read `adaptation-rules.md` if the user changes color, type, radius, density, or motion.
10. Read `output-modes.md` to format the deliverable.
11. Generate the output.
12. Run `validation-checklist.md` before delivery.
13. Apply the release hygiene checks in this file.

## Runtime Decision Tree

1. If the user asks for a full page, choose a page grammar from `layout-patterns.md`.
2. If the user asks for a section, select only the needed section and component recipes.
3. If the user asks for code, map tokens to CSS variables before writing component code.
4. If no copy is provided, create neutral placeholder copy and mark it replaceable.
5. If no brand controls are provided, use the default cool accent palette.
6. If mobile priority is high, begin with the single-column mobile rules and expand upward.
7. If the page has many items, use card lists, compact metadata, tags, and pagination.
8. If the output includes motion, honor reduced-motion requirements.
9. If any requirement conflicts with accessibility, prefer accessibility.
10. If the deliverable is complete, run the validation checklist and release hygiene checks.

## File Reading Order

1. `design-tokens.json`
2. `style-profile.md`
3. `layout-patterns.md`
4. `component-recipes.md`
5. `interaction-rules.md`
6. `responsive-rules.md`
7. `content-rules.md`
8. `adaptation-rules.md`
9. `output-modes.md`
10. `validation-checklist.md`
11. `prompt-templates.md` when reusable prompts are requested
12. `examples/` when an example pattern is useful

## Core Design Principles

- Use a calm cool-hue system with low-chroma surfaces and a clear primary accent.
- Keep surfaces rounded, readable, and modular.
- Prefer light borders, soft fills, and minimal shadow. Reserve shadows for floating panels.
- Make cards feel structured through spacing, metadata, badges, and action affordances.
- Use compact icon buttons for tools and clear text labels for primary navigation and CTA actions.
- Keep layouts spacious but not sparse. Content should scan quickly.
- Use strong headings, muted metadata, and short descriptive text.
- Ensure every component has hover, active, focus, disabled, loading, empty, error, and success rules when applicable.

## Design Token Rules

- Use semantic token names only.
- Map all colors, radii, shadows, spacing, typography, motion, and breakpoints to tokens.
- Keep the default primary hue replaceable through `color.brand.hue`.
- Use OKLCH values where supported and provide hex or rgb fallbacks when needed.
- Maintain light and dark token pairs.
- Never hard-code component colors when a token exists.

## Component Generation Rules

- Build each component from a small set of primitives: surface, accent rail, icon control, metadata row, badge, list item, panel, and CTA.
- Cards use 16px radius by default, white or dark surface fills, and restrained separators.
- Buttons use 8px radius for compact controls and 12px radius for primary actions.
- Floating panels use stronger shadow, 12px to 16px radius, and a clear active trigger state.
- Lists use metadata icons, muted text, and dotted or soft separators when items are dense.
- Article or long-form blocks use a single broad content card and stable typographic rhythm.

## Responsive Rules

- Desktop uses a centered page width up to 75rem with optional sidebar and main content columns.
- Tablet uses reduced gutters and two-column layouts only when content remains readable.
- Mobile uses a single column, compact top bar, icon controls, stacked cards, and deferred side content.
- Hero media can sit behind or above content, but must not reduce text contrast.
- Touch targets must be at least 44px square for primary controls.

## Interaction Rules

- Hover states should brighten or tint surfaces without layout shift.
- Active states may scale controls to 0.95 or 0.90 for tactile feedback.
- Focus states must be visible and must not rely only on color.
- Floating panels open near the trigger and close on Escape, outside click, or route change.
- Motion should be short, calm, and optional.
- Reduced motion must remove translate and scale effects while preserving opacity changes.

## Content Rules

- Headings should be direct, short, and high contrast.
- Metadata should be compact and icon-assisted.
- Tags should be short chips with semantic grouping.
- Body copy should use short paragraphs and stable line height.
- CTA text should be action-oriented and under 5 words when possible.
- Placeholder content must remain neutral and replaceable.

## Technology Mapping

- CSS variables: define tokens under `:root` and override dark mode with a `.dark` class or media query.
- Tailwind: map tokens through theme variables or arbitrary values only when a token is missing.
- React: create token-aware primitives and pass component state through props.
- Vue: use token-aware components and class bindings for state.
- HTML/CSS: use semantic landmarks, token variables, and progressive enhancement.

## Adaptation Rules

- Replace the primary hue first, then adjust accent intensity, then surface tint.
- Keep radius, spacing, and typography hierarchy stable unless the user asks for a stronger style shift.
- When density changes, adjust spacing and metadata visibility together.
- When motion changes, keep duration ranges consistent across components.
- Run validation after every style substitution.

## Forbidden Output

- Do not use private marks, private illustrations, owned photos, copied icon sets, unlicensed copy, or recognizable business data.
- Do not create a one-to-one page copy.
- Do not include hidden preparation notes, hidden assumptions, creation-history notes, or private naming.
- Do not name any non-user-provided entity in generated examples.
- Do not rely on color alone to convey state.
- Do not ship components without keyboard and reduced-motion behavior.

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

## Quality Checklist

- Uses semantic tokens.
- Follows the selected layout grammar.
- Includes required component states.
- Includes responsive behavior for desktop, tablet, and mobile.
- Maintains readable contrast.
- Provides visible focus states.
- Provides reduced-motion behavior.
- Uses neutral, replaceable placeholder content.
- Avoids private or recognizable assets.
- Can be executed by an AI agent without additional context.

## Release Hygiene Check

Before final output, verify:

- No creation-history or hidden preparation language appears.
- No private names, domains, marks, or owned copy appear unless supplied by the user for the new task.
- No copied page order or fixed structure is required.
- No token, filename, example, or variable uses identifiable naming.
- JSON is valid.
- Markdown headings are clear.
- Component examples use neutral placeholders.
- Accessibility rules are present.
