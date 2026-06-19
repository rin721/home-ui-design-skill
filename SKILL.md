---
name: home-ui-design-skill
description: 生成冷色强调、圆角模块、紧凑导航、内容优先布局、响应式页面、组件状态和可访问性约束的柔和模块化 UI。适用于内容型首页、落地页、产品介绍区、个人资料页、知识索引、归档视图、移动端内容页、组件库规范、HTML/CSS、React、Vue、Tailwind、Figma 提示词和可复用界面规则。不适用于高密度企业数据表、交易界面、游戏 HUD、暗黑赛博主题、奢华杂志风、强品牌复刻、不可授权素材或一比一页面复制。
---

# home-ui-design-skill 中文版

## 目标

使用这套 skill 生成平静、圆润、内容优先的模块化 UI。默认视觉语言是低饱和冷色强调、浅色或暗色 token 成对、圆角卡片、紧凑元信息、图标化工具按钮、清晰标题层级和可验证响应式行为。

## 适用输入

- `page_type`: `homepage`、`landing`、`product-section`、`profile`、`archive`、`article`、`mobile-page`、`component-library` 或 `custom`。
- `audience`: 目标用户、阅读场景和使用设备。
- `content_inventory`: 标题、正文、元信息、标签、指标、表单、媒体和 CTA。
- `brand_controls`: 可选 hue、强调强度、字体、密度、圆角和动效强度。
- `technology_target`: `design-spec`、`html-css`、`react`、`vue`、`tailwind`、`figma-prompt`、`wireframe` 或 `component-library`。
- `accessibility_level`: `baseline`、`strict` 或 `enhanced`。
- `device_priority`: `desktop-first`、`mobile-first` 或 `balanced`。

缺少输入时，先做最小合理假设：使用内容型页面、默认冷色强调、平衡设备优先级、baseline 可访问性和中性可替换占位内容。

## 运行流程

1. 判断页面类型、受众、内容清单、设备优先级、技术目标和可访问性等级。
2. 读取 `design-tokens.json`，选择 light/dark token 和可替换 token。
3. 读取 `style-profile.md`，锁定本 skill 的视觉边界和可调整范围。
4. 读取 `layout-patterns.md`，为完整页面选一个主布局和一个备选布局；局部 section 只选相关模式。
5. 读取 `component-recipes.md`，只加载所需组件配方。
6. 读取 `interaction-rules.md`、`responsive-rules.md` 和 `content-rules.md`，补齐状态、键盘、断点和文案规则。
7. 用户要求改 hue、字体、圆角、密度、动效或风格方向时，再读取 `adaptation-rules.md`。
8. 读取 `output-modes.md`，按目标交付设计规范、代码、提示词、线框或组件库说明。
9. 交付前运行 `validation-checklist.md`，修复缺少 token、状态、响应式、可访问性或发布清洁的问题。

## 文件读取顺序

1. `design-tokens.json`
2. `style-profile.md`
3. `layout-patterns.md`
4. `component-recipes.md`
5. `interaction-rules.md`
6. `responsive-rules.md`
7. `content-rules.md`
8. `adaptation-rules.md`，仅在风格替换时读取
9. `output-modes.md`
10. `validation-checklist.md`
11. `prompt-templates.md`，仅在需要可复用提示词时读取
12. `examples/`，仅在需要范例格式或演示参考时读取

## 输出规则

- 默认输出结构化 UI 设计规范；用户指定技术目标时，在设计决策后补对应实现。
- 所有颜色、圆角、阴影、间距、字体、动效、断点和 z-index 必须映射到语义 token。
- 代码输出先写 CSS variables 或框架 theme 映射，再写组件结构。
- 暗色模式必须在同一主题作用域内同时设置 token 覆盖、`color`、`background` 和 `color-scheme`；不要只在 `:root` 设置文字颜色，再在子级 `.dark` 中改 token。
- React 和 Vue 输出应包含 props/state 模型、可访问属性、键盘行为和 reduced-motion 处理。
- Tailwind 输出应说明 token-to-theme 策略；只有缺少 token 时才使用任意值。
- Figma prompt 应包含 frame、tokens、布局、组件、交互标注、响应式 variants 和可访问性说明。
- 占位内容必须中性、可替换，不虚构真实品牌、人物、域名、价格或不可验证指标。

## 核心设计原则

- 使用平静冷色系统、低饱和背景和清晰主强调色。
- 让表面圆润、可读、模块化；卡片用于重复项、modal、工具面板或真正需要框定的内容。
- 不把每个页面 section 都做成浮动卡片；页面大区应使用全宽区带或无框布局。
- 工具按钮优先使用紧凑图标；主导航和 CTA 使用清晰文字。
- 标题强、元信息弱、描述短，页面宽松但不空散。
- Hover 不造成布局跳动；active、focus、disabled、loading、empty、error 和 success 状态在适用控件上必须完整。
- 移动端使用单列、紧凑顶部栏、44px 触控目标、自然换行和稳定媒体比例。
- 可访问性优先于装饰效果；focus 可见、键盘可用、状态不只依赖颜色、动效遵守 reduced motion。
- Light/dark 都要检查标题、品牌文字、导航、卡片标题、正文、次级文案、按钮、图标和 focus ring 的实际 computed color。

## 禁止输出

- 不使用私人标志、私人插图、专有照片、复制图标集、不可授权文案或可识别业务数据。
- 不创建一比一页面复刻，也不要求固定页面顺序或固定条目数量。
- 不交付缺少键盘行为、focus、错误文本或 reduced-motion 行为的交互组件。
- 不用纯渐变、纯装饰背景或单一色系替代真实界面结构。
- 不在范例中命名非用户提供的真实实体。
- 不包含隐藏准备记录、创建历史说明或私人命名。

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
