# Product Section Example

## Input

- Page type: `product-section`
- Goal: create an embeddable product capability section
- Output: component spec + React notes
- Device priority: balanced

## Reusable Output Structure

1. Section header: short eyebrow, `h2`, one summary paragraph.
2. Feature grid: 3 to 4 capability cards with icon tiles and short copy.
3. Media block: local or user-provided product preview with explicit ratio.
4. Detail list: compact list with metadata icons and soft dividers.
5. Inline CTA: one primary action and one secondary link.

## Token Choices

- `spacing.section.md` for section rhythm.
- `grid.feature.cards` for responsive feature columns.
- `radius.media` for media corners.
- `color.brand.primary` for icon tiles, accent rails, and CTA.
- `color.text.secondary` for helper copy.

## Responsive Behavior

- Desktop: feature grid plus media/detail can use two columns.
- Tablet: keep two columns only when both remain readable.
- Mobile: stack header, feature cards, media, details, and CTA.

## Accessibility Checks

- Section heading level follows the page hierarchy.
- Media has meaningful `alt` or empty `alt`, depending on whether it conveys information.
- Recommended capabilities are not expressed by color alone.
- CTA copy describes the action and avoids `click here`.

## Neutral Placeholder Copy

- Section title: `Bring the core workflow into one surface`
- CTA: `View capabilities`
- Features: `Clear sorting`, `Fast collaboration`, `Status sync`
