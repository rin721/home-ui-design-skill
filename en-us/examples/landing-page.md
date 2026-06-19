# Landing Page Example

## Input

- Page type: `landing`
- Goal: create a product landing page for a small-team productivity tool
- Output: UI design spec + Tailwind implementation notes
- Device priority: balanced

## Reusable Output Structure

1. Navigation: rounded top bar, placeholder brand, primary links, search icon, theme icon, menu button.
2. Hero: one value proposition, short subtitle, primary CTA, secondary link, local product preview media.
3. Feature cards: 3 to 6 cards with icon tiles, titles, and short descriptions.
4. Workflow section: explanatory copy plus step cards or a media block.
5. Stats row: neutral numbers with context, no invented customer outcomes.
6. CTA panel: one primary action and one quieter secondary link.
7. Footer: low-emphasis utility links.

## Token Choices

- `color.surface.page` for the canvas.
- `color.surface.card` for navigation, features, stats, and CTA panels.
- `color.brand.primary` for active links, icon tiles, focus rings, and primary CTA.
- `radius.card.default` for cards and `radius.action` for CTAs.
- `grid.feature.cards` for feature cards.

## Responsive Behavior

- Desktop: centered 75rem shell, optional two-column hero, auto-fit feature grid.
- Tablet: stack or keep hero columns only when both columns are at least 280px.
- Mobile: single column, icon-led navigation, full-width stacked CTAs, stable media `aspect-ratio`.

## Accessibility Checks

- Use exactly one `h1`.
- CTA and navigation buttons have visible focus.
- Decorative icons are hidden from assistive tech; semantic icons get text or `aria-label`.
- Motion respects `prefers-reduced-motion`.
- Metrics include units and context.

## Neutral Placeholder Copy

- H1: `Organize team work with a calmer flow`
- CTA: `Start planning`
- Features: `Task groups`, `Clear status`, `Fast review`
