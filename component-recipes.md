# Component Recipes

每个组件都应使用语义化 tokens、中性占位文案、可见 focus 状态和响应式规则。

## 读取导航

- 只读取任务需要的组件，不为未出现的组件生成规则。
- 每个选中组件都必须保留同一份组件契约：使用场景、视觉结构、token 依赖、状态、响应式、可访问性、实现提示、禁止事项和中性示例。
- 输出代码时，先把 token 映射到 CSS variables 或框架 theme，再写组件 class、props 或 variants。
- 输出组件库规范时，保留组件命名稳定：Button、Navigation、Hero、Section、Card、Tag、Form、Modal、Footer、CTA、Stats、Media Block 和 Pricing / Plan Block。

## 通用组件契约

- 交互控件必须包含 hover、active、focus、disabled 和 loading 的适用状态。
- 表单、modal、menu、tabs、segmented controls 和 popover 必须说明键盘行为。
- 错误、成功、推荐、选中和趋势状态不能只依赖颜色。
- 每个文本组件在 light/dark 下都必须从当前主题作用域继承或显式使用文本 token，不得继承过期的 `:root` 浅色文字。
- 移动端触控目标至少 44px，非主控标签可为 32px 高但不得承载关键操作。
- 长文本、URL、badge 和按钮标签必须能自然换行或堆叠，不能挤出容器。

## Button

- 使用场景：主操作、次级链接、图标工具、分页和面板触发器。
- 视觉结构：圆角控件、居中内容、可选图标、明确 active 状态。
- Token 依赖：`color.brand.primary`、`color.surface.control`、`radius.control`、`radius.action`、`motion.duration.fast`。
- 状态规则：hover 使用 tinted fill；active 缩放到 `motion.scale.active`；disabled 降低 opacity 并移除指针动作；loading 保留宽度并显示 spinner 或进度文字。
- 响应式规则：触控设备保持至少 44px 高度。
- 可访问性规则：使用描述性 label，提供可见 focus ring，loading 使用 `aria-busy`。
- 技术实现提示：暴露 `variant`、`size`、`icon`、`loading` 和 `disabled` props。
- 禁止事项：过小点击区域、只用颜色表达状态、hover 时产生布局跳动。
- 生成示例：`主要操作`、`查看详情`、`打开菜单`。

## Navigation

- 使用场景：全局页面移动和工具操作。
- 视觉结构：圆角卡片栏、品牌区、主链接、搜索、显示控制、主题和菜单触发器。
- Token 依赖：`color.surface.card`、`color.text.primary`、`color.brand.primary`、`radius.card.default`、`zIndex.nav`。
- 状态规则：active link 使用强调色；hover tint 文字或表面；菜单触发器在打开时保持高亮。
- 响应式规则：桌面端显示内联 label；移动端使用图标控件和浮动菜单。
- 可访问性规则：使用 `nav`，适合时使用列表语义、`aria-label` 和键盘关闭行为。
- 技术实现提示：工具控件与主链接分组。
- 禁止事项：没有可访问菜单触发器就隐藏导航。
- 生成示例：`品牌标签 | 概览 | 功能 | 价格 | 搜索 | 菜单`。

## Hero

- 使用场景：页面第一核心表达或紧凑介绍。
- 视觉结构：标题、短文案、元信息或证明、主 CTA、可选媒体。
- Token 依赖：`spacing.section.lg`、`typography.size.h1`、`color.brand.primary`、`radius.card.default`。
- 状态规则：CTA 遵循 button 规则；媒体不得遮挡文字。
- 响应式规则：split hero 折叠为单列；media banner 可裁剪但重要内容应居中。
- 可访问性规则：一个 `h1`；文字对比足够；有意义媒体提供 alt。
- 技术实现提示：支持 `media-banner`、`split` 和 `compact-card` variants。
- 禁止事项：把装饰文字嵌进图片、低对比、CTA 过多。
- 生成示例：`用平静的模块化界面建立清晰工作流。`

## Section

- 使用场景：组织相关内容块。
- 视觉结构：可选 eyebrow、标题、摘要、内容 grid 或 stack。
- Token 依赖：`spacing.section.md`、`spacing.4`、`typography.size.h2`、`color.text.secondary`。
- 状态规则：无控件时不需要状态。
- 响应式规则：移动端垂直间距减少 25 percent。
- 可访问性规则：保持 heading 顺序；长页面使用 landmark label。
- 技术实现提示：创建 `plain`、`carded`、`split`、`grid` variants。
- 禁止事项：除 modal 或重复项目外，不要 card 内套 card。
- 生成示例：`核心能力`、`流程概览`、`最近更新`。

## Card

- 使用场景：内容预览、功能、资料、方案、统计或 CTA。
- 视觉结构：圆角表面、可选 accent rail、标题、元信息、正文和操作。
- Token 依赖：`color.surface.card`、`radius.card.default`、`shadow.none`、`spacing.4`、`color.border.subtle`。
- 状态规则：hover 可 tint 操作区；只有整卡可交互时才应用 active scale；选中卡片使用 accent rail。
- 响应式规则：移动端全宽；桌面 grid 卡片使用等宽列。
- 可访问性规则：可点击卡片应有单一清晰 link 或 button 目标。
- 技术实现提示：拆分 `Card`、`CardHeader`、`CardMeta`、`CardBody`、`CardAction`。
- 禁止事项：一张卡片内多个竞争性主操作。
- 生成示例：`功能标题`、`简短描述`、`查看详情`。

## Feature List

- 使用场景：收益、产品能力、服务摘要和内容分类。
- 视觉结构：icon tile、标题、一到两行文案、可选标签。
- Token 依赖：`grid.feature.cards`、`color.surface.control`、`radius.control`、`spacing.4`。
- 状态规则：卡片 hover 可 tint icon tile；active item 遵循 button 规则。
- 响应式规则：桌面 grid，移动端堆叠卡片。
- 可访问性规则：图标默认装饰，除非传达独立含义。
- 技术实现提示：功能文案控制在 120 字符以内。
- 禁止事项：功能列表内放长段落。
- 生成示例：`内容有序`、`快速扫描`、`可访问状态`。

## Tag / Badge

- 使用场景：元信息、筛选、分类、状态和短标签。
- 视觉结构：圆角 pill 或柔和方形 label，包含短文字。
- Token 依赖：`color.surface.control`、`color.brand.primary`、`radius.control`、`typography.size.body.mobile`。
- 状态规则：hover 加深 tint；selected 使用强调文字和更强 fill；disabled 降低 opacity。
- 响应式规则：标签可换行，gap 保持一致。
- 可访问性规则：可选筛选标签使用 `aria-pressed` 或选中文本。
- 技术实现提示：文字要短，只在 chip 边界换行。
- 禁止事项：用 badge 承载长句。
- 生成示例：`新`、`分类`、`3 min`、`Active`。

## Form

- 使用场景：搜索、联系、设置、订阅、账户和筛选。
- 视觉结构：label、圆角 input、辅助文字、校验消息和操作行。
- Token 依赖：`color.surface.card`、`color.border.subtle`、`radius.action`、`color.state.error`、`color.state.success`。
- 状态规则：focus ring；invalid border 加消息；disabled 使用弱化表面；操作按钮支持 loading。
- 响应式规则：移动端字段堆叠；窄屏动作按钮全宽。
- 可访问性规则：每个 input 都有 label；错误通过 `aria-describedby` 关联。
- 技术实现提示：搜索字段可在 focus 时扩展，但必须预留宽度。
- 禁止事项：只用 placeholder 当 label。
- 生成示例：`邮箱地址`、`搜索内容`、`消息`。

## Modal

- 使用场景：确认、设置、预览、表单或紧凑帮助。
- 视觉结构：overlay、居中圆角 panel、标题、内容、操作行、关闭控件。
- Token 依赖：`zIndex.modal`、`shadow.panel.float`、`radius.card.default`、`opacity.overlay`。
- 状态规则：open、closing、loading、error、success。
- 响应式规则：移动端可使用全宽 bottom sheet。
- 可访问性规则：限制 focus、恢复 focus、支持 Escape，并标注 dialog。
- 技术实现提示：使用 inert background 或等效 focus blocking。
- 禁止事项：没有键盘关闭的 modal。
- 生成示例：`确认操作`、`编辑详情`、`显示设置`。

## Footer

- 使用场景：工具链接、小版权文本、次级导航。
- 视觉结构：居中低强调文字和内联链接。
- Token 依赖：`color.text.secondary`、`spacing.section.md`、`color.border.subtle`。
- 状态规则：链接遵循 text link 规则。
- 响应式规则：移动端链接可换行。
- 可访问性规则：使用语义 footer 和描述性链接文本。
- 技术实现提示：页脚视觉保持安静。
- 禁止事项：紧凑页面中使用大型促销页脚。
- 生成示例：`保留所有权利 | RSS | Sitemap`。

## CTA

- 使用场景：在内容或产品 section 后引导下一步。
- 视觉结构：圆角 panel、加粗标题、短辅助文案、主操作、可选次级操作。
- Token 依赖：`color.surface.card`、`color.brand.primary`、`radius.card.default`、`spacing.6`。
- 状态规则：按钮遵循 button 规则。
- 响应式规则：移动端文字和按钮堆叠。
- 可访问性规则：一个主操作，文字清晰。
- 技术实现提示：CTA 放在有足够上下文之后。
- 禁止事项：超过两个竞争操作。
- 生成示例：`开始构建`、`查看方案`。

## Testimonial

- 使用场景：社会证明、引用、用户故事和反馈卡片。
- 视觉结构：引言文字、可选头像占位、角色标签和短 attribution。
- Token 依赖：`color.surface.card`、`radius.card.default`、`color.text.secondary`、`spacing.4`。
- 状态规则：除非有 carousel controls，否则无需状态。
- 响应式规则：移动端一行一张，桌面端 grid。
- 可访问性规则：自动轮播必须提供暂停控件。
- 技术实现提示：引言保持简短。
- 禁止事项：虚构真实姓名或可识别私人断言。
- 生成示例：`这个流程让团队更快完成工作。`

## Stats

- 使用场景：指标、摘要、计数、进度。
- 视觉结构：数值、标签、可选图标、可选趋势。
- Token 依赖：`typography.size.h1`、`color.brand.primary`、`color.surface.card`、`radius.card.default`。
- 状态规则：趋势色必须搭配文字或图标含义。
- 响应式规则：移动端只有 label 可读时才使用两列。
- 可访问性规则：提供单位和上下文。
- 技术实现提示：除非用户提供数据，否则使用中性示例数值。
- 禁止事项：不支持的声明或无解释指标。
- 生成示例：`24 tasks`、`8 teams`、`99.9 percent`。

## Media Block

- 使用场景：产品预览、资料图、gallery preview 或氛围 banner。
- 视觉结构：圆角媒体、可选 caption、可选 overlay controls。
- Token 依赖：`radius.media`、`shadow.none`、`color.border.subtle`。
- 状态规则：hover 可显示控件；active 打开预览。
- 响应式规则：保持 aspect ratio，避免关键裁剪丢失。
- 可访问性规则：有意义媒体需要 alt；装饰媒体使用空 alt。
- 技术实现提示：设置明确尺寸或 aspect ratio。
- 禁止事项：使用非用户提供的不可授权或可识别媒体。
- 生成示例：`带描述性 alt 的界面预览图`。

## Pricing / Plan Block

- 使用场景：方案、套餐、包、选项比较。
- 视觉结构：方案名、短描述、价格或占位、功能列表、CTA。
- Token 依赖：`grid.feature.cards`、`color.surface.card`、`color.brand.primary`、`radius.card.default`。
- 状态规则：高亮方案使用 accent rail 或柔和强调 fill。
- 响应式规则：移动端卡片堆叠，桌面端 CTA 对齐。
- 可访问性规则：推荐方案不能只依赖颜色。
- 技术实现提示：功能使用语义 list。
- 禁止事项：虚构真实价格或不支持承诺。
- 生成示例：`Starter`、`Growth`、`Scale`。
