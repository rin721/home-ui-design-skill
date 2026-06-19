# Responsive Rules

## Desktop

- Use a max-width shell of 75rem.
- Use full text navigation and inline utility controls.
- Use optional sidebar plus main content grid when secondary content supports scanning.
- Keep content cards broad and readable, with action affordance at the right edge when useful.
- Use 16px base body text and strong headings.

## Tablet

- Reduce gutters to 24px.
- Keep two columns only when both columns remain at least 280px wide.
- Collapse utility-heavy navigation before primary navigation.
- Keep card radius and token values consistent with desktop.
- Reduce hero height and section spacing by 15 to 25 percent.

## Mobile

- Use a single column.
- Use compact top navigation with icon controls.
- Place menus, search, and settings in floating panels near their triggers.
- Move sidebar widgets below the main content.
- Use 14px body text and maintain strong heading hierarchy.
- Turn desktop card action columns into inline title actions or bottom action rows.

## Container Width

- Mobile gutter: 16px.
- Tablet gutter: 24px.
- Desktop gutter: 32px.
- Main shell max width: 75rem.
- Article max width without sidebar: 48rem to 60rem.
- Floating panel width on mobile: viewport width minus 32px unless it is a small menu.

## Grid Changes

- Feature grids use one column on mobile.
- Feature grids use two columns on tablet when space allows.
- Feature grids use three or more columns on desktop only when cards stay readable.
- Sidebar grids collapse below main content at desktop breakpoint and below.
- Timeline layouts stack date, marker, title, and tags on mobile.

## Navigation Changes

- Desktop: brand, primary links, search, display settings, theme, and utility links can appear inline.
- Tablet: hide lower-priority utility labels first.
- Mobile: show brand, search icon, display icon, theme icon, and menu icon.
- Mobile menu opens as a floating panel and uses 44px item height.
- Search opens as a rounded full-width field below the top bar.

## Card Reflow

- Desktop feed cards can use a right action rail or edge action zone.
- Mobile feed cards should place the action icon beside the title.
- Desktop card lists use 16px to 24px vertical gaps.
- Mobile card lists can use subtle dividers inside one rounded group when density is high.
- Feature cards stack and preserve icon/title/body order.

## Type Scaling

- Do not scale text with viewport units.
- Desktop body: 16px.
- Mobile body: 14px.
- Desktop h1: 32px to 40px.
- Mobile h1: 26px to 32px.
- Keep line height between 1.45 and 1.75 depending on copy length.

## Section Spacing Scaling

- Desktop section spacing: 48px to 80px.
- Tablet section spacing: 40px to 64px.
- Mobile section spacing: 32px to 48px.
- Compact widgets use 12px to 16px internal gaps.

## Image Ratio

- Hero media: 16:9, 21:9, or responsive height crop.
- Profile and thumbnail media: square or 4:3.
- Product media: 16:10 or 4:3.
- Always set `aspect-ratio` or fixed responsive dimensions to avoid layout shift.

## Mobile Touch Target Size

- Minimum target: 44px by 44px.
- Compact tags can be 32px high only when not primary controls.
- Keep 8px minimum gap between adjacent action controls.
- Avoid tiny close, next, or settings buttons.

## Orientation Notes

- Landscape mobile should keep navigation compact and reduce hero height.
- Avoid fixed-height panels that exceed viewport height.
- Allow floating panels to scroll internally only when content is long.

## Long Text Wrapping

- Use `overflow-wrap: anywhere` for badges, URLs, and long tokens.
- Use max-width on body copy.
- Avoid fixed-width buttons with long labels.
- Allow CTA groups to stack before text clips.
- Keep metadata rows wrapping cleanly with consistent gaps.
