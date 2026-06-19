# Style Profile

## Keywords

- Calm
- Modular
- Friendly
- Cool-accented
- Rounded
- Content-first
- Lightweight
- Personal but structured
- Soft technical
- Readable

## Brand Character

The interface should feel approachable, quietly confident, and organized. It should support personal, editorial, product, and knowledge-centered content without becoming decorative or loud. The character is gentle rather than corporate-heavy, but still precise enough for technical or product information.

## Visual Density

- Use medium density for desktop content lists.
- Use lower density for hero, profile, CTA, and empty states.
- Use higher density only for archive timelines, tag clusters, metadata rows, and compact navigation.
- Preserve a clear separation between primary content and secondary widgets.

## Space

- Use a cool-tinted page canvas around white or dark content cards.
- Keep cards separated by background contrast rather than heavy borders.
- Use 16px to 24px internal padding for standard cards.
- Use 48px to 80px spacing around major sections.
- Let mobile cards fill the width with small gutters and rounded top edges when they follow media.

## Color Direction

- Default to a cool blue hue with low-chroma page surfaces.
- Use accent color for active states, icon strokes, small rails, links, and selected controls.
- Keep large surfaces neutral.
- Use soft blue control fills for tags, metadata icons, and icon buttons.
- Dark mode should invert surfaces to cool near-black while keeping accent clarity.

## Type Character

- Use a clean sans-serif stack.
- Use bold, high-contrast headings.
- Use muted metadata text.
- Use short line lengths for long-form reading.
- Keep body text practical and unornamented.

## Image And Icon Style

- Use images as broad atmosphere, profile media, thumbnails, or product previews.
- Round image corners to match card geometry.
- Do not use images as the only structure.
- Use simple line icons or filled social/action icons inside soft square controls.
- Use icon plus text for metadata when space allows.

## Suitable Scenarios

- Personal profile pages.
- Product homepages with calm technical tone.
- Content indexes.
- Documentation or knowledge hubs.
- Archive timelines.
- Article pages.
- Mobile content feeds.
- Component library previews.

## Unsuitable Scenarios

- Highly ornate editorial layouts.
- Dense tabular operations.
- Flashy launch campaigns with heavy animation.
- Premium luxury identity systems.
- Game interfaces.
- Interfaces that require strong industrial, brutalist, or monochrome aesthetics.

## Replaceable Style Parameters

- `color.brand.hue`
- Accent chroma and lightness.
- Sans-serif family.
- Card radius from 12px to 20px.
- Card density through padding and gap tokens.
- Motion duration from 120ms to 300ms.
- Page background tint.
- Shadow strength for floating panels.

## Visual Consistency Standard

- Accent hue appears in navigation, metadata icons, tags, focus, and selected controls.
- Cards share the same radius family.
- Secondary text remains visibly lower emphasis than headings.
- Floating panels use stronger elevation than static cards.
- Mobile and desktop share the same component shapes even when layout changes.
- No component introduces an unrelated color family unless it represents state.
