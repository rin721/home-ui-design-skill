# Layout Patterns

## How To Use

- Full pages must include one primary layout and one alternative layout.
- Sections should use only relevant patterns instead of forcing a full page order.
- Page sections are not framed by default; use cards only for repeated items, modals, tool panels, and content that genuinely needs grouping.
- Every layout must describe desktop, tablet, and mobile reflow.
- When the user asks for code, include stable container widths, grid tracks, media ratios, and mobile stacking rules.

## Page Shell

- Use a centered max-width shell of `container.page.max`.
- Place the top navigation in a rounded card surface.
- Use a cool-tinted background behind the content shell.
- Use a main content area with optional secondary column on desktop.
- Keep the shell readable without requiring a fixed page order.

## Section Rhythm

- Start major sections with strong heading hierarchy and clear spacing.
- Use 48px to 80px vertical spacing for large sections.
- Use 16px to 24px spacing between cards in lists.
- Use dotted or subtle dividers only where repeated content needs scan support.
- Avoid decorative section wrappers around every block.

## Hero Modes

### Media Banner Hero

- Use a wide image or gradient-free media plane behind the first content band.
- Overlay the navigation above the media plane when contrast remains clear.
- Let the first card or content panel overlap the lower edge of the media plane.
- Keep title and action surfaces in a rounded card if text contrast is unstable.

### Split Content Hero

- Use a two-column layout with content and media on desktop.
- Collapse to content first, media second on mobile unless media is critical.
- Use one primary CTA and one secondary action.

### Compact Intro Hero

- Use a card with heading, short paragraph, metadata row, and optional avatar or small media block.
- Use this mode for profile, archive, and article pages.

## Content Area Modes

### Card Feed

- Use stacked cards in the main column.
- Each card should contain title, metadata, excerpt, optional tags, and an action affordance.
- Place action affordance at the card edge or next to the title on mobile.

### Article Panel

- Use one large card for long-form content.
- Put metadata above the title.
- Use a divider between metadata/title and body content.
- Add previous and next navigation as separate cards.

### Timeline Archive

- Use year groups with date, marker, title, and tags.
- Use a vertical line or dotted marker column to guide scanning.
- Keep tags muted and right-aligned on desktop when space allows.
- Stack date, title, and tags on mobile.

### Widget Sidebar

- Use secondary cards for profile, filters, categories, tags, summaries, or helper controls.
- Keep sidebar width near `container.sidebar.width`.
- Move sidebar content below the main feed on mobile.

## Card Area Modes

- Use a one-column card feed for articles and content indexes.
- Use `grid.feature.cards` for benefits, features, plan blocks, and testimonials.
- Keep card heights content-driven, but align key controls.
- Use soft square icon tiles at the start of feature cards.

## CTA Area Modes

- Compact CTA card: heading, short body, primary button, optional secondary link.
- Inline CTA strip: short phrase plus action button inside a rounded surface.
- Bottom CTA panel: centered text and controls after content sections.
- Mobile CTA: full-width stacked actions with at least 44px height.

## Footer Pattern

- Use centered low-emphasis text.
- Use inline utility links separated with subtle dividers.
- Keep footer detached from primary content with generous top spacing.
- On mobile, stack links if wrapping becomes crowded.

## Grid Rules

- Desktop two-column shell: `minmax(0, 17.5rem) minmax(0, 1fr)`.
- Desktop full-width shell: one column when secondary content is absent.
- Feature grid: `repeat(auto-fit, minmax(16rem, 1fr))`.
- Mobile: one column for all page types.
- Use consistent gutters of 16px on mobile, 24px on tablet, and 32px on desktop.

## Container Width

- Top navigation: max 75rem.
- Main shell: max 75rem.
- Article panel: 48rem to 60rem when no sidebar is present.
- Form panel: 32rem to 44rem.
- Modal: max 36rem.

## Responsive Reflow

- Desktop: navigation shows text labels and inline controls.
- Tablet: navigation may keep text labels if width allows; hide low-priority utilities first.
- Mobile: top bar shows brand, search, display controls, theme, and menu icons.
- Sidebar widgets move below the main content on mobile.
- Card action columns convert to inline title actions on mobile.

## Common Page Templates

### Homepage

- Top navigation.
- Optional media banner or compact hero.
- Main content feed or feature grid.
- Optional sidebar widgets on desktop.
- Pagination or final CTA.
- Footer.

### Landing Page

- Top navigation.
- Hero with primary CTA.
- Feature cards.
- Proof or stats.
- Product section.
- CTA panel.
- Footer.

### Product Section Page

- Header card.
- Feature grid.
- Media block.
- Plan or option cards.
- FAQ or details.
- CTA.

### Profile Page

- Top navigation.
- Profile card.
- Content card with sections.
- Contact or social controls.
- Footer.

### Archive Page

- Top navigation.
- Optional sidebar filters.
- Timeline card.
- Pagination or year jump controls.
- Footer.

## Alternative Layout Combinations

- Media banner plus card feed.
- Compact intro plus feature grid.
- Sidebar filters plus timeline.
- Full-width article panel plus previous/next cards.
- Product hero plus stacked mobile sections.

## Over-Specification Avoidance

- Do not require a fixed order for hero, cards, CTA, and footer.
- Do not require specific labels or item counts.
- Do not require specific media content.
- Do not require the same sidebar content across page types.
- Provide at least two layout options for every full-page output.
