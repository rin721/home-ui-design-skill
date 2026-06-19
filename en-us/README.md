# home-ui-design-skill

An installable, verifiable, demo-backed Codex UI design skill for calm, rounded, content-first modular interfaces. The Chinese root directory is the default install entry. `en-us/` is kept as an English mirror.

## Use It For

- Turning loose UI requests into structured design specs.
- Generating homepages, landing pages, product sections, profiles, knowledge indexes, archive pages, mobile content pages, and component library specs.
- Producing HTML/CSS, React, Vue, Tailwind, Figma prompts, wireframes, or implementation plans.
- Keeping colors, radii, spacing, type, motion, breakpoints, and states tokenized.
- Requiring accessibility: visible focus, keyboard behavior, 44px touch targets, error copy, and reduced motion.

## Avoid It For

- Dense enterprise back offices, trading screens, game HUDs, cyberpunk themes, or luxury editorial art direction.
- One-to-one brand site copies, proprietary visual assets, or unlicensed media.
- Pages that depend mainly on marketing spectacle, aggressive gradients, or highly experimental motion.

## Installation

Place the repository root in a Codex skills directory or reference the root folder through the Codex skill installation flow. The default entry is the root `SKILL.md`; do not install `en-us/` separately by default.

```text
home-ui-design-skill/
  SKILL.md
  design-tokens.json
  agents/openai.yaml
```

English readers can use `en-us/` as a mirror.

## Agent Workflow

1. Read `SKILL.md` and confirm the task fits the soft modular UI scope.
2. Load `design-tokens.json` and establish token mappings first.
3. Read `style-profile.md`, `layout-patterns.md`, `component-recipes.md`, `interaction-rules.md`, `responsive-rules.md`, and `content-rules.md` as needed.
4. Read `adaptation-rules.md` for style substitutions.
5. Format the deliverable with `output-modes.md`.
6. Validate with `validation-checklist.md` and `scripts/validate_skill.py` before delivery.

## Examples And Demo

- `examples/*.md` contains reusable output examples.
- `examples/react-demo/` is a Vite React demo showing tokens, components, responsive behavior, dark mode, focus, and reduced motion.

Run the demo:

```bash
cd examples/react-demo
npm ci
npm run dev
```

Build the demo:

```bash
cd examples/react-demo
npm run build
```

## Maintenance And Validation

Run repository validation:

```bash
python scripts/validate_skill.py .
```

Run Codex skill validation:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\xiaol\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\coder\rin721\home-ui-design-skill
python C:\Users\xiaol\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\coder\rin721\home-ui-design-skill\en-us
```

Keep the Chinese and English mirrors synchronized. Do not add private names, real brands, unlicensed assets, or unsupported data.

## License

MIT
