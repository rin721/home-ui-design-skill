# Adaptation Rules

## Replace The Primary Color

1. Change `color.brand.hue`.
2. Recalculate `color.brand.primary` and `color.brand.primary.dark`.
3. Adjust `color.surface.page` with low chroma.
4. Keep text and card surfaces neutral.
5. Verify contrast for links, focus rings, and selected controls.

## Replace Typography

- Choose a clean sans-serif family.
- Keep body size, heading scale, and line height stable at first.
- Recheck card title wrapping after font changes.
- Avoid decorative display type unless it is limited to large hero headings.

## Adjust Radius

- Use 12px for a sharper product feel.
- Use 16px for the default soft modular feel.
- Use 20px for a friendlier, more personal feel.
- Keep control radius smaller than card radius.
- Do not mix many radius values in one surface group.

## Adjust Card Style

- Default cards are flat with background separation.
- Add subtle borders when page and card surfaces become too close.
- Use floating shadows only for overlays and menus.
- Use accent rails to mark selected or important cards.

## Adjust Page Density

- Increase density by reducing card padding and metadata gaps by 12 to 20 percent.
- Decrease density by increasing section spacing and card padding by 15 to 25 percent.
- Keep touch targets unchanged.
- Hide low-priority metadata before reducing readable text.

## Adjust Motion Strength

- Minimal: opacity only, 120ms to 180ms.
- Default: opacity plus small scale or translate, 150ms to 300ms.
- Expressive: stronger transform allowed only on non-critical decorative moments.
- Always provide reduced-motion behavior.

## Shift Style Character

### More Technical

- Lower radius toward 12px.
- Increase divider visibility slightly.
- Use tighter metadata and denser card lists.
- Keep the cool accent precise and restrained.

### More Premium

- Reduce visible controls.
- Increase whitespace.
- Use softer text contrast in secondary areas.
- Use fewer tags and cleaner card bodies.

### More Minimal

- Remove decorative media.
- Use plain sections and fewer panels.
- Keep one accent use per component.
- Reduce badge count.

### More Corporate

- Use more conservative copy.
- Increase structure through grids and section headings.
- Use more explicit CTA hierarchy.
- Keep social or profile details secondary.

### More Product-Led

- Use feature grids, media blocks, plan cards, and proof sections.
- Put CTA after value statements.
- Use icon tiles and concise benefit copy.

## Replaceable Tokens

- `color.brand.hue`
- `color.brand.primary`
- `color.surface.page`
- `typography.family.sans`
- `radius.card.default`
- `radius.control`
- `spacing.section.md`
- `shadow.panel.float`
- `motion.duration.base`

## Stable Structure Rules

- Keep semantic token names stable.
- Keep card, button, navigation, tag, and panel state models stable.
- Keep desktop, tablet, and mobile breakpoint roles stable.
- Keep accessibility behavior stable.

## Verify Consistency After Changes

- Accent appears in the same component roles.
- Cards share one radius family.
- Focus remains visible.
- Text contrast passes.
- Mobile layout remains one column where needed.
- Floating panels remain above content and close predictably.
- Placeholder copy remains neutral.

## Avoid Component Imbalance

- Do not pair very round cards with sharp controls.
- Do not pair high-chroma accents with many colored badges.
- Do not increase motion while keeping dense content.
- Do not use heavy shadows on every card.
- Do not reduce spacing until metadata wraps awkwardly.
