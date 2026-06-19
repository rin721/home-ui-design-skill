# Runtime Decision Tree

## 1. Determine Page Type

- If the request asks for a whole page, classify it as homepage, landing, product-section, profile, archive, article, mobile-page, or custom.
- If the request asks for a component, classify the component group and skip full-page layout selection.
- If the page type is unclear, choose the closest reusable pattern and state the assumption in the response, not in generated repository files.

## 2. Check Provided Inputs

- Brand color or hue.
- Copy or placeholder needs.
- Technology target.
- Component requirements.
- Device priority.
- Accessibility level.
- Content inventory.

## 3. Read Tokens

- Load `design-tokens.json`.
- Choose default tokens unless the user supplies replacements.
- Map tokens to CSS variables or framework theme values when code is requested.

## 4. Read Layout Rules

- Load `layout-patterns.md`.
- Select one primary layout and one backup layout when the user asks for options.
- Avoid fixed page order unless the user explicitly asks for it.

## 5. Read Component Rules

- Load `component-recipes.md`.
- Select only components needed for the request.
- Ensure every selected component includes visual structure, states, responsive behavior, and accessibility.

## 6. Read Interaction Rules

- Load `interaction-rules.md`.
- Add hover, active, focus, disabled, loading, error, success, empty, scroll, transition, and reduced-motion behavior where applicable.

## 7. Read Responsive Rules

- Load `responsive-rules.md`.
- Define desktop, tablet, and mobile behavior.
- If mobile priority is high, create the mobile layout first.

## 8. Read Content Rules

- Load `content-rules.md`.
- Structure headings, subtitles, metadata, paragraphs, CTAs, empty states, helper copy, and placeholder copy.

## 9. Select Output Mode

- Load `output-modes.md`.
- If no technology target is supplied, use UI design spec.
- If a technology target is supplied, include implementation details for that target.

## 10. Generate

- Produce the requested output.
- Use semantic tokens.
- Keep placeholder content neutral.
- Use accessible structure and states.

## 11. Validate

- Load `validation-checklist.md`.
- Check each applicable item.
- Fix missing states, missing responsive rules, or weak accessibility before delivery.

## 12. Release Hygiene

- Remove creation-history notes, hidden preparation notes, or private naming.
- Remove unowned assets and invented private data.
- Ensure JSON is valid and Markdown structure is clean.
- Ensure the output can stand alone.
