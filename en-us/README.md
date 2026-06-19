# home-ui-design-skill

This repository defines a reusable UI design skill for calm, rounded, content-rich interfaces. It helps AI agents generate design specs, responsive layouts, tokens, components, prompts, and implementation guidance with a consistent visual language.

## What It Solves

- Turns loose UI requests into structured design systems.
- Produces reusable page and component rules instead of one-off screens.
- Keeps color, radius, typography, spacing, motion, and responsive behavior tokenized.
- Supports accessible interfaces with visible focus, keyboard behavior, touch targets, and reduced motion.
- Provides output modes for design specs, HTML/CSS, React, Vue, Tailwind, Figma prompts, wireframes, and component library specs.

## Suitable Page Types

- Homepages
- Landing pages
- Product introduction pages
- Profile or creator pages
- Editorial indexes
- Archive timelines
- Article pages
- Mobile content pages
- Component library specs

## How Agents Use The Skill

1. Read `SKILL.md`.
2. Load `design-tokens.json`.
3. Choose visual direction from `style-profile.md`.
4. Select layouts from `layout-patterns.md`.
5. Apply components from `component-recipes.md`.
6. Add states from `interaction-rules.md`.
7. Apply breakpoints from `responsive-rules.md`.
8. Shape copy with `content-rules.md`.
9. Use `output-modes.md` for the requested deliverable.
10. Run `validation-checklist.md`.

## Input Preparation

Useful inputs include:

- Page type and target audience.
- Main content blocks.
- Required components.
- Preferred technology target.
- Optional primary hue, type choice, density, and motion level.
- Accessibility level.
- Desktop, tablet, or mobile priority.

## Output Shapes

- UI design spec
- HTML/CSS
- React
- Vue
- Tailwind
- Figma prompt
- Wireframe outline
- Component library spec
- Landing page structure
- Responsive layout plan

## Extend Or Replace Style

Use `adaptation-rules.md` to adjust hue, typography, radius, card treatment, density, and motion. Keep token names stable so components remain compatible.

## Update Design Tokens

Edit `design-tokens.json` by changing token `value`, `role`, `usage`, `modifiable`, or `fallback`. Do not add creation-history fields. Keep names semantic and stable.

## Update Component Recipes

Edit `component-recipes.md` by adding or adjusting component sections. Every component should include usage, visual structure, token dependencies, states, responsive behavior, accessibility, implementation hints, forbidden patterns, and a neutral example.

## Run Quality Checks

Use `validation-checklist.md` after every generated UI. Also scan the repository for private names, unowned text, creation-history language, invalid JSON, missing accessibility states, and over-specific layouts.
