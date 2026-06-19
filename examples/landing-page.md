# Landing Page Example

## 输入

- 页面类型：`landing`
- 目标：为小团队效率工具创建产品落地页
- 输出：UI design spec + Tailwind 实现说明
- 设备优先级：balanced

## 可复用输出结构

1. Navigation：圆角顶部栏、品牌占位、主链接、搜索图标、主题图标、菜单按钮。
2. Hero：一句主张、短副标题、主 CTA、次级链接、本地产品预览媒体。
3. Feature cards：3 到 6 张功能卡，使用 icon tile、标题和短描述。
4. Workflow section：左侧说明，右侧步骤卡片或媒体块。
5. Stats row：中性数值和上下文，不虚构真实客户结果。
6. CTA panel：一个主操作和一个弱次级链接。
7. Footer：低强调工具链接。

## Token 选择

- `color.surface.page` 用于页面画布。
- `color.surface.card` 用于导航、feature、stats 和 CTA panel。
- `color.brand.primary` 用于 active link、icon tile、focus ring 和 primary CTA。
- `radius.card.default` 用于卡片，`radius.action` 用于 CTA。
- `grid.feature.cards` 用于功能卡片。

## 响应式行为

- Desktop：居中 75rem 页面壳，hero 可双列，feature cards 使用 auto-fit grid。
- Tablet：hero 堆叠或保留双列，前提是两列都至少 280px。
- Mobile：单列，导航折叠为图标控件，CTA 全宽堆叠，媒体设置稳定 `aspect-ratio`。

## 可访问性验收

- 页面只有一个 `h1`。
- CTA 和导航按钮都有可见 focus。
- 图标默认装饰，独立语义图标提供文本或 `aria-label`。
- 动效遵守 `prefers-reduced-motion`。
- 所有指标使用单位和上下文。

## 中性占位文案

- H1：`用清晰工作流整理团队任务`
- CTA：`开始规划`
- 功能卡：`任务分组`、`状态清晰`、`快速回顾`
