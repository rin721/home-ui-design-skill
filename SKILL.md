---
name: home-ui-design-skill
description: 生成冷色强调、圆角模块、紧凑导航、内容优先布局、响应式页面、组件状态和可访问性约束的柔和模块化 UI。适用于 UI 设计规范、HTML/CSS、React、Vue、Tailwind、Figma 提示词、组件库、落地页、首页、产品区、归档视图、移动端页面和可复用界面规则。
---

# home-ui-design-skill 中文版

## Skill 名称

home-ui-design-skill

## 描述

该 skill 用于创建干净、柔和、模块化的界面，适合内容型页面、产品叙事、知识中心、个人资料、落地页和移动端页面。设计语言使用冷色强调、圆角卡片、平静背景、紧凑元信息、图标化工具按钮、清晰字体和响应式布局规则。

## 适用场景

- 首页、落地页、产品介绍页、文档索引、个人资料页、归档时间线、看板式轻量内容页和移动页面壳。
- 需要 tokens、布局语法、组件配方、交互状态、响应式行为和校验清单的 UI 设计规范。
- HTML/CSS、React、Vue 或 Tailwind 的前端实现计划。
- Figma 提示词、线框草案和组件库规范。

## 不适用场景

- 高密度企业数据表、交易界面、暗黑赛博主题、奢华杂志风、游戏 HUD 或高实验性动效。
- 依赖重拟物、强渐变、夸张营销视觉或复刻品牌资产的界面。
- 依赖私人素材、可识别标志、专有插图或不可授权文案的输出。

## 触发短语

- "使用 home-ui-design-skill"
- "创建柔和模块化 UI"
- "生成圆角卡片首页"
- "设计柔和内容布局"
- "做一个冷色强调的落地页"
- "设计移动端内容页"
- "生成产品 UI 组件配方"

## 输入参数

- `page_type`: homepage、landing、product-section、profile、archive、article、mobile-page、component-library 或 custom。
- `audience`: 目标用户和阅读场景。
- `content_inventory`: 标题、正文、元信息、标签、指标、表单、媒体和 CTA 需求。
- `brand_controls`: 可选主色 hue、强调强度、字体选择、密度和动效强度。
- `technology_target`: design-spec、html-css、react、vue、tailwind、figma-prompt、wireframe 或 component-library。
- `accessibility_level`: baseline、strict 或 enhanced。
- `device_priority`: desktop-first、mobile-first 或 balanced。

## 输出形式

- 结构化 UI 设计规范。
- HTML/CSS 实现。
- React 组件计划或实现。
- Vue 组件计划或实现。
- Tailwind class 策略。
- Figma 提示词。
- 线框草案。
- 组件库规范。
- 落地页结构。
- 响应式布局计划。

默认输出为结构化 UI 设计规范。用户提供技术目标时，在设计决策后补充对应实现细节。

## 运行流程

1. 判断 `page_type`、`audience`、`content_inventory`、`device_priority` 和 `technology_target`。
2. 先读取 `design-tokens.json` 并选择 token 集。
3. 读取 `style-profile.md` 锁定视觉方向。
4. 读取 `layout-patterns.md` 选择布局语法。
5. 读取 `component-recipes.md` 获取所需组件规则。
6. 读取 `interaction-rules.md` 获取状态、动效和键盘行为。
7. 读取 `responsive-rules.md` 获取断点行为。
8. 读取 `content-rules.md` 获取标题、文案密度、元信息、标签和 CTA 节奏。
9. 用户改变颜色、字体、圆角、密度或动效时读取 `adaptation-rules.md`。
10. 读取 `output-modes.md` 格式化交付物。
11. 生成结果。
12. 交付前运行 `validation-checklist.md`。
13. 执行本文件的发布清洁检查。

## 运行决策树

1. 如果用户要求完整页面，从 `layout-patterns.md` 选择页面语法。
2. 如果用户要求局部 section，只选择需要的 section 和组件配方。
3. 如果用户要求代码，先把 tokens 映射为 CSS variables。
4. 如果未提供文案，创建中性可替换占位文案。
5. 如果未提供品牌控制，使用默认冷色强调 palette。
6. 如果移动端优先，先生成单列移动规则，再向大屏扩展。
7. 如果页面条目很多，使用卡片列表、紧凑元信息、标签和分页。
8. 如果输出包含动效，必须遵守 reduced-motion。
9. 如果需求与可访问性冲突，优先可访问性。
10. 完成后运行质量检查和发布清洁检查。

## 文件读取顺序

1. `design-tokens.json`
2. `style-profile.md`
3. `layout-patterns.md`
4. `component-recipes.md`
5. `interaction-rules.md`
6. `responsive-rules.md`
7. `content-rules.md`
8. `adaptation-rules.md`
9. `output-modes.md`
10. `validation-checklist.md`
11. 需要可复用提示词时读取 `prompt-templates.md`
12. 需要范例时读取 `examples/`

## 核心设计原则

- 使用平静的冷色系统、低饱和背景和清晰主强调色。
- 让表面圆润、可读、模块化。
- 优先使用轻边界、柔和填充和少量阴影；阴影只用于浮层。
- 通过间距、元信息、徽标和操作入口建立卡片结构。
- 工具按钮优先使用紧凑图标；主导航和 CTA 使用清晰文字。
- 页面要宽松但不空散，内容应便于快速扫描。
- 标题强、元信息弱、描述短。
- 适用组件必须具备 hover、active、focus、disabled、loading、empty、error 和 success 规则。

## Design Token 规则

- 只使用语义化 token 名称。
- 颜色、圆角、阴影、间距、字体、动效和断点都要映射到 token。
- 默认主色 hue 通过 `color.brand.hue` 替换。
- 支持时使用 OKLCH，并提供 hex 或 rgb fallback。
- 保持 light 和 dark 成对 token。
- 组件已有 token 时不得硬编码颜色。

## 组件生成规则

- 组件由少量基础结构构成：surface、accent rail、icon control、metadata row、badge、list item、panel 和 CTA。
- 默认卡片使用 16px 圆角、浅色或深色表面和克制分隔线。
- 紧凑控件使用 8px 圆角，主操作使用 12px 圆角。
- 浮层使用更强阴影、12px 到 16px 圆角和明确的触发态。
- 列表使用元信息图标、弱化文本和点状或柔和分隔线。
- 长文模块使用单个宽内容卡片和稳定排版节奏。

## 响应式规则

- 桌面端使用最大 75rem 的居中容器，可使用侧栏和主内容列。
- 平板端缩小 gutter；只有内容仍可读时才保留双列。
- 移动端使用单列、紧凑顶部栏、图标控制、堆叠卡片和后置侧栏内容。
- Hero 媒体可位于内容后方或上方，但不得降低文字对比度。
- 触控目标至少 44px。

## 交互规则

- Hover 应通过提亮或着色表面反馈，不得造成布局跳动。
- Active 可将控件缩放到 0.95 或 0.90。
- Focus 必须可见，不能只依赖颜色。
- 浮层靠近触发器打开，并可通过 Escape、外部点击或路由变化关闭。
- 动效短促、安静、可关闭。
- Reduced motion 移除平移和缩放，同时保留必要透明度变化。

## 内容规则

- 标题直接、简短、高对比。
- 元信息紧凑并可搭配图标。
- 标签使用短 chip，并保持语义分组。
- 正文使用短段落和稳定行高。
- CTA 文案尽量为 5 个词以内的动作表达。
- 占位内容必须中性且可替换。

## 技术映射

- CSS variables: 在 `:root` 定义 tokens，并用 `.dark` class 或媒体查询覆盖暗色模式。
- Tailwind: 通过 theme variables 映射 tokens；只有缺失 token 时使用任意值。
- React: 创建 token-aware primitives，并通过 props 传递组件状态。
- Vue: 使用 token-aware components 和 class bindings 表达状态。
- HTML/CSS: 使用语义 landmarks、token variables 和渐进增强。

## 适配与替换规则

- 先替换 primary hue，再调整强调强度，最后调整 surface tint。
- 除非用户要求更强风格变化，否则保持圆角、间距和字体层级稳定。
- 改变密度时，应同时调整间距和元信息可见性。
- 改变动效时，应保持组件之间的 duration 范围一致。
- 每次风格替换后运行校验。

## 禁止输出

- 不使用私人标志、私人插图、专有照片、复制图标集、不可授权文案或可识别业务数据。
- 不创建一比一页面复刻。
- 不包含隐藏准备记录、隐藏假设、创建历史说明或私人命名。
- 不在范例中命名任何非用户提供的实体。
- 不只用颜色表达状态。
- 不交付缺少键盘行为和 reduced-motion 行为的组件。

## 调用示例

```text
使用 home-ui-design-skill 为团队协作应用创建移动端优先的产品落地页。输出 UI 设计规范和 Tailwind 实现说明。
```

```text
使用 home-ui-design-skill 生成导航、卡片、标签、表单、模态框和归档列表的组件库规范。
```

```text
使用 home-ui-design-skill 生成 React 首页，要求冷色强调、圆角卡片、紧凑元信息和严格可访问性检查。
```

## 质量检查

- 使用语义化 tokens。
- 遵循选定布局语法。
- 包含必需组件状态。
- 包含桌面、平板和移动端响应式行为。
- 保持可读对比度。
- 提供可见 focus 状态。
- 提供 reduced-motion 行为。
- 使用中性可替换占位内容。
- 避免私人或可识别资产。
- 无需额外上下文即可由 AI agent 执行。

## 发布清洁检查

交付前确认：

- 不出现创建历史或隐藏准备表述。
- 不出现私人名称、域名、标志或专有文案，除非用户为新任务提供。
- 不要求复制式页面顺序或固定结构。
- token、文件名、范例和变量不使用可识别命名。
- JSON 有效。
- Markdown 标题清晰。
- 组件范例使用中性占位文案。
- 可访问性规则完整。
