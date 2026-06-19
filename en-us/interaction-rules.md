# Interaction Rules

## Hover

- Hover should tint surfaces or text with the primary accent family.
- Hover must not resize content or move neighboring elements.
- Cards may reveal a subtle action affordance, but the card surface should remain stable.
- Tags and compact controls should deepen their soft fill by one step.

## Active

- Text buttons may scale to 0.95.
- Icon buttons may scale to 0.90.
- Active states should complete within `motion.duration.fast`.
- Avoid active transformations on large content cards unless the whole card is a clear action target.

## Focus

- Every interactive element must have a visible focus indicator.
- Focus must remain visible in light and dark mode.
- Focus cannot rely only on color; use outline, ring, underline, or surface change.
- Focus order should follow visual order.

## Disabled

- Disabled controls use reduced opacity and remove pointer action.
- Disabled controls must keep their size and label visible.
- Disabled text should still meet readability expectations for inactive UI.
- Provide reason text when disabling a primary action could confuse users.

## Loading

- Loading controls keep their width and height.
- Use spinner, progress text, or skeleton only when it helps the user understand wait state.
- Use `aria-busy` on loading regions.
- Do not hide existing content unless replacement content is ready.

## Error

- Use `color.state.error` plus an icon or text label.
- Link error messages to the relevant field.
- Keep messages concise and actionable.
- Do not use red as the only signal.

## Success

- Use `color.state.success` plus text or icon feedback.
- Keep success feedback brief unless it confirms a major state change.
- Return controls to normal state after transient feedback where appropriate.

## Empty

- Empty states use a small heading, one sentence, optional icon, and one clear action.
- Empty states should sit inside a rounded card surface.
- Avoid decorative emptiness that does not explain the next step.

## Scroll

- Keep top navigation stable when it helps orientation.
- Use smooth scroll only for user-triggered anchor movement.
- Respect reduced-motion settings.
- Long pages should maintain clear section spacing and optional quick navigation.

## Transition

- Use `motion.duration.fast` for hover and active states.
- Use `motion.duration.base` for panel open and close.
- Use `motion.duration.enter` for content entrance.
- Use `motion.easing.standard` across components.
- Theme changes must not animate text color, icon color, control backgrounds, or page background through low-contrast intermediate states. Light/dark switches should update those theme-bound values immediately, or animate only non-text decoration with short opacity changes.

## Micro-Interaction

- Use small scale changes for compact controls.
- Use opacity plus slight translate for panel entry.
- Use accent color to mark selected states.
- Keep interactions quiet and predictable.

## Motion Duration

- Hover: 120ms to 180ms.
- Active press: 80ms to 150ms.
- Panel open: 160ms to 220ms.
- Content entry: 240ms to 320ms.
- Modal open: 180ms to 260ms.

## Easing

- Use `cubic-bezier(0.4, 0, 0.2, 1)` for standard UI transitions.
- Use linear easing only for progress indicators.
- Avoid bouncy easing unless the user requests a playful style shift.

## Reduced Motion

- Remove translate and scale effects.
- Keep opacity transitions under 150ms.
- Disable auto-scroll and auto-advance.
- Preserve instant state feedback.

## Keyboard Interaction

- Tab order follows visual order.
- Escape closes menus, popovers, modals, and search panels.
- Enter or Space activates focused buttons.
- Arrow keys may move within menus, tabs, and segmented controls.
- Modal focus is trapped until closed.

## Touch Interaction

- Touch targets are at least 44px by 44px.
- Keep at least 8px between adjacent compact controls.
- Avoid hover-only information.
- Place frequent controls near thumb-reachable zones on mobile.
- Do not require precision dragging for essential tasks.
