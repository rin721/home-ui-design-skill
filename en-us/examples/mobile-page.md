# Mobile Page Example

## Input

- Page type: `mobile-page`
- Goal: create a mobile-first content page with search, list items, and secondary tools
- Output: UI design spec + HTML/CSS notes
- Device priority: mobile-first

## Reusable Output Structure

1. Compact top bar: placeholder brand, search, display settings, theme, and menu icons.
2. Search panel: full-width rounded field opened below the top bar.
3. Card feed: stacked cards with title, metadata, summary, tags, and action icon.
4. Pagination: `Load more` or pagination controls.
5. Secondary widgets: categories, filters, or summary widgets after the main list on mobile.
6. Footer: low-emphasis links.

## Token Choices

- `container.mobile.gutter` for page padding.
- `radius.card.default` for card groups.
- `radius.control` for icon buttons, tags, and pagination.
- `color.surface.control` for metadata icons and chips.
- `motion.duration.base` for search panel visibility.

## Responsive Behavior

- Mobile: single column by default; critical controls are at least 44px.
- Tablet: secondary widgets may form two columns when space allows.
- Desktop: secondary widgets can move into a sidebar; main list remains 48rem to 60rem wide.

## Accessibility Checks

- Menu, search, and settings panels close with Escape.
- Search field has a visible label or reliable `aria-label`.
- Long titles wrap naturally without clipping body text.
- No hover-only information.
- Reduced motion removes search panel translation.

## Neutral Placeholder Copy

- Item title: `Content item title`
- Metadata: `Category · 3 min · Updated`
- Empty state: `No items yet. Add the first item to start the list.`
