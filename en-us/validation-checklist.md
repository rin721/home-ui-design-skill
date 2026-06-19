# Validation Checklist

## How To Run

- After generating UI, check each applicable item in this file.
- When maintaining the repository, run `python scripts/validate_skill.py .`.
- Before release, confirm root `SKILL.md` is the Chinese default entry, `en-us/` is a synchronized mirror, and `agents/openai.yaml` matches the skill description.

## Aesthetic Fit

- The UI feels calm, modular, rounded, and content-first.
- Accent color is cool, controlled, and used consistently.
- Large surfaces stay neutral and readable.
- Visual density matches the page type.

## Token Usage

- Colors use semantic tokens.
- Typography uses semantic size and weight rules.
- Spacing, radius, shadow, border, and motion use tokens.
- Dark mode has matching token behavior.
- The dark theme scope sets token overrides, `color`, `background`, and `color-scheme` together.
- Theme changes do not transition text color, icon color, control backgrounds, or page background through low-contrast intermediate states.

## Layout Grammar

- Page shell follows the selected layout pattern.
- Desktop, tablet, and mobile layouts are defined.
- Section rhythm is consistent.
- Cards and panels do not create unnecessary nesting.
- No fixed page order is required unless the task demands it.

## Component Recipes

- Required components are selected.
- Each component has structure, token dependencies, and usage rules.
- Buttons, cards, navigation, tags, forms, modals, CTA, footer, media, stats, and plan blocks follow their recipes when present.

## Component States

- Hover state exists where useful.
- Active state exists for controls.
- Focus state is visible.
- Disabled state is clear.
- Loading state preserves layout.
- Error and success states include text or icon meaning.
- Empty state explains the next step.

## Responsive Behavior

- Mobile layout is one column where needed.
- Touch targets are at least 44px for primary controls.
- Navigation adapts to available width.
- Card actions reflow cleanly.
- Long text wraps without clipping.
- Images use stable aspect ratios.

## Accessibility

- Text contrast is readable.
- In dark mode, headings, brand text, navigation, card titles, body copy, muted copy, buttons, icons, and focus rings are readable.
- Focus is visible.
- Keyboard operation is supported.
- Reduced motion is honored.
- Forms have labels.
- Error messages are linked to fields.
- Images have appropriate alt text.
- Heading hierarchy is logical.
- Color is not the only information carrier.

## Content Rules

- Headings are concise.
- Metadata is compact and muted.
- CTA copy is short and action-oriented.
- Placeholder copy is neutral and replaceable.
- No invented private data appears.

## Asset Safety

- No private marks are included.
- No unlicensed images are included.
- No copied icons are required.
- No recognizable private copy appears.
- No unsupported metrics or claims are introduced.

## Agent Independence

- The output can be used without hidden context.
- The required files or sections are named clearly.
- Design rules are executable.
- Validation steps are included.

## Release Hygiene

- No creation-history or hidden preparation language appears.
- No private names, domains, or identifiable assets appear unless supplied by the user for the new task.
- No JSON syntax errors exist.
- Markdown headings are clear and ordered.
- Examples use neutral placeholders.
- Accessibility and responsive rules are present.
