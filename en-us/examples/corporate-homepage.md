# Corporate Homepage Example

## Input

- Page type: `homepage`
- Goal: create a restrained, credible homepage for a professional services team
- Output: UI design spec
- Style direction: more corporate

## Reusable Output Structure

1. Navigation: clear placeholder brand, primary links, contact CTA.
2. Hero: split hero with value proposition on the left and local interface or service-flow preview on the right.
3. Service cards: 3 to 6 cards with conservative short descriptions.
4. Process section: steps or methodology list without exaggerated claims.
5. Proof cards: neutral proof modules using process metrics or capability summaries, not invented clients.
6. CTA strip: low-pressure primary action and secondary link.
7. Footer: utility links and quiet notes.

## Token Choices

- `color.brand.primary` for CTAs, active indicators, and focus rings.
- `color.text.secondary` for helper copy and metadata.
- `grid.feature.cards` for service cards.
- `shadow.none` for static cards.
- `shadow.panel.float` only for dropdowns, popovers, or modals.

## Responsive Behavior

- Desktop: hero can use two columns; service cards use responsive grid.
- Tablet: reduce tool labels before collapsing navigation.
- Mobile: hero text first, full-width CTAs, stacked service cards, proof modules after main content.

## Accessibility Checks

- Navigation uses semantic links.
- CTA buttons use clear labels.
- Proof modules do not auto-rotate; if carousel controls exist, include pause controls.
- Contrast and focus remain readable in both light and dark modes.

## Neutral Placeholder Copy

- H1: `Create a clear entry for complex services`
- CTA: `Book a call`
- Service cards: `Discovery`, `Process design`, `Delivery support`
