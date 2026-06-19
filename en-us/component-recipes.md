# Component Recipes

Every component should use semantic tokens, neutral placeholder content, visible focus states, and responsive rules.

## Reading Guide

- Read only the components required by the task.
- Every selected component must keep the same component contract: usage, visual structure, token dependencies, states, responsive behavior, accessibility, implementation notes, forbidden patterns, and neutral examples.
- For code output, map tokens to CSS variables or framework theme values before writing classes, props, or variants.
- For component library specs, keep component names stable: Button, Navigation, Hero, Section, Card, Tag, Form, Modal, Footer, CTA, Stats, Media Block, and Pricing / Plan Block.

## Shared Component Contract

- Interactive controls must include applicable hover, active, focus, disabled, and loading states.
- Forms, modals, menus, tabs, segmented controls, and popovers must include keyboard behavior.
- Error, success, recommended, selected, and trend states must not rely on color alone.
- Every text component must inherit from the active theme scope or explicitly use text tokens in light and dark modes. It must not inherit stale light text from `:root`.
- Mobile touch targets must be at least 44px; non-primary tags may be 32px tall only when they do not carry critical actions.
- Long text, URLs, badges, and button labels must wrap or stack naturally without escaping their containers.

## Button

- Usage: primary actions, secondary links, icon tools, pagination, and panel triggers.
- Visual structure: rounded control, centered content, optional icon, clear active state.
- Token dependencies: `color.brand.primary`, `color.surface.control`, `radius.control`, `radius.action`, `motion.duration.fast`.
- States: hover uses a tinted fill; active scales to `motion.scale.active`; disabled reduces opacity and removes pointer action; loading reserves width and shows spinner or progress text.
- Responsive: maintain at least 44px height on touch devices.
- Accessibility: use descriptive labels, visible focus ring, and `aria-busy` for loading.
- Implementation hint: expose `variant`, `size`, `icon`, `loading`, and `disabled` props.
- Forbidden: tiny tap areas, color-only state, layout shift on hover.
- Example: `Primary action`, `View details`, `Open menu`.

## Navigation

- Usage: global page movement and utility actions.
- Visual structure: rounded card bar, brand area, primary links, search, display controls, theme, and menu trigger.
- Token dependencies: `color.surface.card`, `color.text.primary`, `color.brand.primary`, `radius.card.default`, `zIndex.nav`.
- States: active link uses accent color; hover tints text or surface; menu trigger remains highlighted while panel is open.
- Responsive: show inline labels on desktop; use icon controls and floating menu on mobile.
- Accessibility: use `nav`, list semantics where practical, `aria-label`, and keyboard-close behavior.
- Implementation hint: keep utility controls separate from primary links.
- Forbidden: hiding navigation without an accessible menu trigger.
- Example: `Brand label | Overview | Features | Pricing | Search | Menu`.

## Hero

- Usage: first major page statement or compact introduction.
- Visual structure: heading, short copy, metadata or proof, primary CTA, optional media.
- Token dependencies: `spacing.section.lg`, `typography.size.h1`, `color.brand.primary`, `radius.card.default`.
- States: CTA follows button rules; media should not obstruct text.
- Responsive: split hero collapses to one column; media banner may crop but must keep important content centered.
- Accessibility: one `h1`, readable contrast, alt text for meaningful media.
- Implementation hint: support `media-banner`, `split`, and `compact-card` variants.
- Forbidden: decorative text embedded in images, low contrast, crowded CTA groups.
- Example: `Build clearer workflows with a calm modular interface.`

## Section

- Usage: group related content blocks.
- Visual structure: optional eyebrow, heading, summary, content grid or stack.
- Token dependencies: `spacing.section.md`, `spacing.4`, `typography.size.h2`, `color.text.secondary`.
- States: none unless section has controls.
- Responsive: reduce vertical spacing by 25 percent on mobile.
- Accessibility: preserve heading order and landmark labels for long pages.
- Implementation hint: create section variants for `plain`, `carded`, `split`, and `grid`.
- Forbidden: nested card inside card unless the inner card is a modal or repeated item.
- Example: `Key capabilities`, `Workflow overview`, `Latest updates`.

## Card

- Usage: content preview, feature, profile, plan, stat, or CTA.
- Visual structure: rounded surface, optional accent rail, title, metadata, body, and action.
- Token dependencies: `color.surface.card`, `radius.card.default`, `shadow.none`, `spacing.4`, `color.border.subtle`.
- States: hover can tint action area; active link areas scale only if the full card is interactive; selected cards use accent rail.
- Responsive: full width on mobile; grid cards use equal column widths on desktop.
- Accessibility: if a card is clickable, use a single clear link target or button target.
- Implementation hint: split `Card`, `CardHeader`, `CardMeta`, `CardBody`, and `CardAction`.
- Forbidden: multiple competing primary actions in one card.
- Example: `Feature title`, `Short description`, `View details`.

## Feature List

- Usage: benefits, product capabilities, service summaries, and content categories.
- Visual structure: icon tile, title, one or two lines of copy, optional tag.
- Token dependencies: `grid.feature.cards`, `color.surface.control`, `radius.control`, `spacing.4`.
- States: card hover may tint icon tile; active item follows button rules.
- Responsive: grid on desktop, stacked cards on mobile.
- Accessibility: icons are decorative unless they convey unique meaning.
- Implementation hint: keep feature copy under 120 characters.
- Forbidden: long paragraphs inside feature lists.
- Example: `Organized content`, `Fast scanning`, `Accessible states`.

## Tag / Badge

- Usage: metadata, filters, categories, states, and compact labels.
- Visual structure: rounded pill or soft square label with short text.
- Token dependencies: `color.surface.control`, `color.brand.primary`, `radius.control`, `typography.size.body.mobile`.
- States: hover deepens tint; selected uses accent text and stronger fill; disabled lowers opacity.
- Responsive: wrap tags and keep gaps consistent.
- Accessibility: selected filter tags use `aria-pressed` or selected state text.
- Implementation hint: keep text short and allow wrapping only at chip boundaries.
- Forbidden: using badges for long sentences.
- Example: `New`, `Category`, `3 min`, `Active`.

## Form

- Usage: search, contact, settings, newsletter, account, and filtering.
- Visual structure: label, rounded input, helper text, validation message, and action row.
- Token dependencies: `color.surface.card`, `color.border.subtle`, `radius.action`, `color.state.error`, `color.state.success`.
- States: focus ring; invalid border plus message; disabled muted surface; loading action button.
- Responsive: fields stack on mobile; action buttons become full width when narrow.
- Accessibility: every input has a label; errors are linked with `aria-describedby`.
- Implementation hint: search fields can expand on focus if width is reserved.
- Forbidden: placeholder-only labels.
- Example: `Email address`, `Search content`, `Message`.

## Modal

- Usage: focused confirmation, settings, preview, form, or compact help.
- Visual structure: overlay, centered rounded panel, title, content, action row, close control.
- Token dependencies: `zIndex.modal`, `shadow.panel.float`, `radius.card.default`, `opacity.overlay`.
- States: open, closing, loading, error, success.
- Responsive: full-width bottom sheet is allowed on mobile.
- Accessibility: trap focus, restore focus, support Escape, and label the dialog.
- Implementation hint: use inert background or equivalent focus blocking.
- Forbidden: modal without keyboard close.
- Example: `Confirm action`, `Edit details`, `Display settings`.

## Footer

- Usage: utility links, small ownership text, secondary navigation.
- Visual structure: centered low-emphasis text with inline links.
- Token dependencies: `color.text.secondary`, `spacing.section.md`, `color.border.subtle`.
- States: links follow text link rules.
- Responsive: wrap links into multiple lines on mobile.
- Accessibility: use semantic footer and descriptive link text.
- Implementation hint: keep footer visually quiet.
- Forbidden: large promotional footer when the page content is compact.
- Example: `All rights reserved | RSS | Sitemap`.

## CTA

- Usage: guide the next action after content or product sections.
- Visual structure: rounded panel, bold heading, short support copy, primary action, optional secondary action.
- Token dependencies: `color.surface.card`, `color.brand.primary`, `radius.card.default`, `spacing.6`.
- States: buttons follow button rules.
- Responsive: stack text and buttons on mobile.
- Accessibility: one primary action with clear text.
- Implementation hint: place CTA after meaningful content, not before context.
- Forbidden: more than two competing actions.
- Example: `Start building`, `View plans`.

## Testimonial

- Usage: social proof, quotes, user stories, and feedback cards.
- Visual structure: quote text, optional avatar placeholder, role label, and short attribution.
- Token dependencies: `color.surface.card`, `radius.card.default`, `color.text.secondary`, `spacing.4`.
- States: none unless carousel controls are used.
- Responsive: one card per row on mobile, grid on desktop.
- Accessibility: avoid auto-rotating testimonials unless pause controls exist.
- Implementation hint: keep quotes concise.
- Forbidden: invented real names or recognizable private claims.
- Example: `This workflow helped the team move faster.`

## Stats

- Usage: metrics, summaries, counts, progress indicators.
- Visual structure: value, label, optional icon, optional trend.
- Token dependencies: `typography.size.h1`, `color.brand.primary`, `color.surface.card`, `radius.card.default`.
- States: trend color must include text or icon meaning.
- Responsive: two columns on mobile only when labels remain readable.
- Accessibility: include units and context.
- Implementation hint: use neutral sample numbers unless user supplies data.
- Forbidden: unsupported claims or unexplained metrics.
- Example: `24 tasks`, `8 teams`, `99.9 percent`.

## Media Block

- Usage: product preview, profile image, gallery preview, or atmospheric banner.
- Visual structure: rounded media, optional caption, optional overlay controls.
- Token dependencies: `radius.media`, `shadow.none`, `color.border.subtle`.
- States: hover can reveal controls; active opens preview.
- Responsive: maintain aspect ratio and avoid important crop loss.
- Accessibility: meaningful media needs alt text; decorative media uses empty alt.
- Implementation hint: set explicit dimensions or aspect ratio.
- Forbidden: unlicensed or recognizable media when not supplied for the new task.
- Example: `Dashboard preview image with descriptive alt`.

## Pricing / Plan Block

- Usage: plans, tiers, packages, option comparison.
- Visual structure: plan name, short description, price or placeholder, feature list, CTA.
- Token dependencies: `grid.feature.cards`, `color.surface.card`, `color.brand.primary`, `radius.card.default`.
- States: highlighted plan uses accent rail or soft accent fill.
- Responsive: cards stack on mobile and align CTAs on desktop.
- Accessibility: do not rely on color alone for recommended plans.
- Implementation hint: use a semantic list for features.
- Forbidden: fake real pricing or unsupported promises.
- Example: `Starter`, `Growth`, `Scale`.
