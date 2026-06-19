# Landing Page Example

## 输入需求

为面向小团队的效率工具创建落地页。使用平静模块化视觉语言，并输出设计规范。

## 使用到的 Skill 规则

- 冷色强调 palette。
- 圆角卡片表面。
- Split 或 compact hero。
- 功能卡片 grid。
- CTA panel。
- Desktop、tablet 和 mobile 行为。
- 可见 focus 和 reduced-motion rules。

## 生成策略

- 使用紧凑顶部导航，包含主链接和工具控件。
- Hero 包含一个主主张、一句辅助文案和两个操作。
- 功能卡使用 icon tile 和短文案。
- 使用证明或 stats row，并使用中性占位指标。
- 以圆角 CTA panel 结束。

## 结构草案

1. Navigation。
2. Hero。
3. Feature grid。
4. Workflow section。
5. Stats row。
6. CTA panel。
7. Footer。

## Token 使用说明

- `color.surface.page` 用于页面画布。
- `color.surface.card` 用于面板。
- `color.brand.primary` 用于 active links、icons 和 primary CTA。
- `radius.card.default` 用于卡片。
- `spacing.section.lg` 用于 hero 间距。
- `motion.duration.base` 用于面板和控件。

## 响应式说明

- 桌面端使用居中壳和功能卡 grid。
- 平板端宽度允许时使用双列功能卡。
- 移动端使用单列、全宽 CTA 和紧凑导航控件。

## 可访问性说明

- 一个 `h1`。
- CTA 按钮具备可见 focus。
- 图标默认为装饰，除非有独立含义。
- 动效遵守 reduced-motion 设置。
- 浅色和暗色模式均检查文本对比。

## 质量检查要点

- 颜色和间距 token 化。
- 可复用 card recipes。
- CTA 层级清晰。
- 移动端触控目标合格。
- 中性占位内容。
