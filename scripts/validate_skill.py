#!/usr/bin/env python3
"""Repository checks for home-ui-design-skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".py",
    ".yml",
    ".yaml",
}

REQUIRED_ROOT_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "design-tokens.json",
    "style-profile.md",
    "layout-patterns.md",
    "component-recipes.md",
    "interaction-rules.md",
    "responsive-rules.md",
    "content-rules.md",
    "adaptation-rules.md",
    "output-modes.md",
    "validation-checklist.md",
    "agents/openai.yaml",
]

REQUIRED_EXAMPLES = [
    "examples/landing-page.md",
    "examples/mobile-page.md",
    "examples/product-section.md",
    "examples/corporate-homepage.md",
]

REQUIRED_DEMO_FILES = [
    "examples/react-demo/package.json",
    "examples/react-demo/package-lock.json",
    "examples/react-demo/vite.config.js",
    "examples/react-demo/index.html",
    "examples/react-demo/src/main.jsx",
    "examples/react-demo/src/App.jsx",
    "examples/react-demo/src/styles.css",
    "examples/react-demo/public/ui-preview.png",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path} is not valid UTF-8: {exc}")


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = read_text(skill_md)
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail(f"{skill_md} is missing YAML frontmatter")
    frontmatter: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def check_required_files(root: Path) -> None:
    for relative in REQUIRED_ROOT_FILES + REQUIRED_EXAMPLES + REQUIRED_DEMO_FILES:
        path = root / relative
        if not path.exists():
            fail(f"Missing required file: {relative}")
    if (root / "zh-cn").exists():
        fail("Remove zh-cn/: the Chinese skill is the repository root")


def check_utf8(root: Path) -> None:
    for path in root.rglob("*"):
        if ".git" in path.parts or "node_modules" in path.parts or "dist" in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
            read_text(path)


def check_skill_frontmatter(root: Path) -> None:
    root_meta = parse_frontmatter(root / "SKILL.md")
    en_meta = parse_frontmatter(root / "en-us" / "SKILL.md")
    for label, meta in (("root", root_meta), ("en-us", en_meta)):
        if meta.get("name") != "home-ui-design-skill":
            fail(f"{label} SKILL.md must use name: home-ui-design-skill")
        description = meta.get("description", "")
        if len(description) < 80:
            fail(f"{label} SKILL.md description is too short for reliable triggering")
    if "高密度企业数据表" not in root_meta["description"]:
        fail("Root description must include non-goals to reduce over-triggering")
    if "dense enterprise data grids" not in en_meta["description"]:
        fail("English description must include non-goals to reduce over-triggering")


def check_tokens(root: Path) -> None:
    for relative in ("design-tokens.json", "en-us/design-tokens.json"):
        data = json.loads(read_text(root / relative))
        if data.get("meta", {}).get("skill") != "home-ui-design-skill":
            fail(f"{relative} meta.skill mismatch")
        names: list[str] = []
        for value in data.values():
            if isinstance(value, list):
                names.extend(item.get("name", "") for item in value if isinstance(item, dict))
        duplicates = sorted({name for name in names if names.count(name) > 1})
        if duplicates:
            fail(f"{relative} has duplicate token names: {', '.join(duplicates)}")
        required_tokens = {
            "color.brand.hue",
            "color.brand.primary",
            "color.surface.control.dark",
            "color.surface.control.hover.dark",
            "color.focus.ring",
            "color.focus.ring.dark",
            "radius.card.default",
        }
        if not required_tokens.issubset(set(names)):
            missing = sorted(required_tokens.difference(names))
            fail(f"{relative} missing tokens: {', '.join(missing)}")


def check_agents_yaml(root: Path) -> None:
    text = read_text(root / "agents" / "openai.yaml")
    required = [
        'display_name: "Home UI Design"',
        'short_description: "生成柔和模块化 UI 设计规范、组件规则与响应式实现"',
        'default_prompt: "使用 $home-ui-design-skill 为内容型产品首页生成响应式 UI 设计规范和 React 实现。"',
    ]
    for item in required:
        if item not in text:
            fail(f"agents/openai.yaml missing: {item}")


def check_demo(root: Path) -> None:
    package = json.loads(read_text(root / "examples/react-demo/package.json"))
    for script in ("dev", "build", "preview"):
        if script not in package.get("scripts", {}):
            fail(f"React demo missing npm script: {script}")
    dependencies = package.get("dependencies", {})
    for dependency in ("@vitejs/plugin-react", "vite", "react", "react-dom", "lucide-react"):
        if dependency not in dependencies and dependency not in package.get("devDependencies", {}):
            fail(f"React demo missing dependency: {dependency}")
    app = read_text(root / "examples/react-demo/src/App.jsx")
    css = read_text(root / "examples/react-demo/src/styles.css")
    for marker in ("Navigation", "Hero", "Feature cards", "Stats", "CTA", "Footer"):
        if marker not in app:
            fail(f"React demo App.jsx missing marker: {marker}")
    for marker in (
        "prefers-reduced-motion",
        "@media",
        "@supports (color: oklch",
        "@supports (background: color-mix",
        "--color-brand-primary",
        "--color-focus-ring",
        ":focus-visible",
        "color-scheme: dark",
    ):
        if marker not in css:
            fail(f"React demo CSS missing marker: {marker}")
    check_demo_theme_css(css)


def css_block(css: str, selector: str) -> str:
    match = re.search(rf"{re.escape(selector)}\s*\{{(?P<body>.*?)\n\}}", css, re.DOTALL)
    if not match:
        fail(f"React demo CSS missing block: {selector}")
    return match.group("body")


def has_property(block: str, property_name: str, value_fragment: str | None = None) -> bool:
    pattern = rf"^\s*{re.escape(property_name)}\s*:\s*(?P<value>.*?);"
    for match in re.finditer(pattern, block, re.MULTILINE | re.DOTALL):
        if value_fragment is None or value_fragment in match.group("value"):
            return True
    return False


def check_demo_theme_css(css: str) -> None:
    root_block = css_block(css, ":root")
    if has_property(root_block, "color"):
        fail("React demo must not set text color on :root; use the active theme scope")
    if re.search(r"^\s*transition\s*:[^;]*\b(?:color|background)\b", css, re.MULTILINE | re.DOTALL):
        fail("React demo must not transition theme-bound color or background during theme changes")

    app_block = css_block(css, ".app")
    if re.search(r"^\s*transition\s*:.*(?:color|background)", app_block, re.MULTILINE | re.DOTALL):
        fail("React demo .app must not transition text color or page background during theme changes")
    for property_name, fragment in (
        ("color-scheme", "light"),
        ("color", "var(--color-text-primary)"),
        ("background", "var(--color-surface-page)"),
    ):
        if not has_property(app_block, property_name, fragment):
            fail(f"React demo .app must set {property_name}: {fragment}")

    dark_block = css_block(css, ".app.dark")
    for property_name, fragment in (
        ("color-scheme", "dark"),
        ("color", "var(--color-text-primary)"),
        ("background", "var(--color-surface-page)"),
    ):
        if not has_property(dark_block, property_name, fragment):
            fail(f"React demo .app.dark must set {property_name}: {fragment}")

    topbar_block = css_block(css, ".topbar")
    if not has_property(topbar_block, "background", "var(--color-surface-card)"):
        fail("React demo .topbar must provide a non-color-mix background fallback")


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.exists():
        fail(f"Path does not exist: {root}")
    check_required_files(root)
    check_utf8(root)
    check_skill_frontmatter(root)
    check_tokens(root)
    check_agents_yaml(root)
    check_demo(root)
    print("[OK] home-ui-design-skill validation passed")


if __name__ == "__main__":
    main()
