# Product Section Example

## 输入

- 页面类型：`product-section`
- 目标：为产品能力区生成可嵌入 section
- 输出：component spec + React notes
- 设备优先级：balanced

## 可复用输出结构

1. Section header：短 eyebrow、`h2`、一段摘要。
2. Feature grid：3 到 4 张能力卡片，使用 icon tile 和短文案。
3. Media block：本地或用户提供的产品预览，设置明确比例。
4. Detail list：紧凑项目列表，使用元信息图标和弱分隔线。
5. Inline CTA：一个主操作和一个次级链接。

## Token 选择

- `spacing.section.md` 控制 section 节奏。
- `grid.feature.cards` 控制功能卡响应式列。
- `radius.media` 控制媒体圆角。
- `color.brand.primary` 用于 icon tile、accent rail 和 CTA。
- `color.text.secondary` 用于辅助说明。

## 响应式行为

- Desktop：feature grid 和 media/detail 可双列。
- Tablet：只在两列可读时保留双列。
- Mobile：标题、功能卡、媒体、细节和 CTA 顺序堆叠。

## 可访问性验收

- Section heading 层级承接页面结构。
- 媒体有 `alt` 或空 `alt`，取决于是否传达信息。
- 推荐能力不能只靠颜色表达。
- CTA 文案描述动作，不使用 `点击这里`。

## 中性占位文案

- Section title：`把核心流程放进同一个界面`
- CTA：`查看能力`
- Feature：`清晰整理`、`快速协作`、`状态同步`
