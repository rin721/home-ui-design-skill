# Mobile Page Example

## Input Request

Create a mobile-first content page with compact navigation, searchable items, and card summaries.

## Skill Rules Used

- Mobile navigation rules.
- Card feed layout.
- Search form recipe.
- Floating panel interaction.
- Tag and metadata rules.

## Generation Strategy

- Use a compact top bar with brand, search, display control, theme control, and menu.
- Put search in a full-width rounded panel below the top bar.
- Use stacked cards with title, metadata, excerpt, and action icon.
- Move secondary widgets below the main list.
- Use footer links with low emphasis.

## Structure Draft

1. Compact top bar.
2. Optional search panel.
3. Stacked content cards.
4. Pagination or load-more action.
5. Secondary widgets.
6. Footer.

## Token Use

- `container.mobile.gutter` for page padding.
- `radius.card.default` for card groups.
- `radius.control` for icon buttons and tags.
- `color.surface.control` for metadata icons.
- `motion.duration.base` for floating panels.

## Responsive Notes

- This layout begins mobile-first.
- Tablet can introduce two-column feature areas.
- Desktop can move secondary widgets into a sidebar.

## Accessibility Notes

- Menu opens with keyboard support and closes on Escape.
- Search field has a label.
- Touch targets meet 44px minimum.
- Long titles wrap without clipping.
- Reduced motion removes panel translation.

## Quality Check

- Mobile content is readable.
- Controls are reachable and labeled.
- Cards do not shift on hover.
- Secondary content appears after the main list.
