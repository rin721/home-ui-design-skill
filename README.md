# home-ui-design-skill

该仓库定义一套可复用 UI design skill，用于生成平静、圆润、内容优先的模块化界面。它帮助 AI agent 生成设计规范、响应式布局、tokens、组件、提示词和实现规则，并保持统一视觉语言。

## 能解决的问题

- 将松散 UI 需求转化为结构化设计系统。
- 生成可复用页面和组件规则，而不是一次性界面。
- 让颜色、圆角、字体、间距、动效和响应式行为保持 token 化。
- 支持可访问性：可见 focus、键盘行为、触控目标和 reduced motion。
- 支持设计规范、HTML/CSS、React、Vue、Tailwind、Figma 提示词、线框和组件库规范等输出。

## 适合页面类型

- 首页
- 落地页
- 产品介绍页
- 个人资料或创作者页面
- 内容索引
- 归档时间线
- 文章页
- 移动端内容页
- 组件库规范

## AI Agent 使用方式

1. 读取 `SKILL.md`。
2. 加载 `design-tokens.json`。
3. 从 `style-profile.md` 选择视觉方向。
4. 从 `layout-patterns.md` 选择布局。
5. 应用 `component-recipes.md` 中的组件。
6. 加入 `interaction-rules.md` 中的状态。
7. 应用 `responsive-rules.md` 中的断点规则。
8. 使用 `content-rules.md` 组织文案。
9. 使用 `output-modes.md` 确定交付形式。
10. 运行 `validation-checklist.md`。

## 输入准备

建议准备：

- 页面类型和目标受众。
- 主要内容模块。
- 必需组件。
- 目标技术栈。
- 可选主色 hue、字体选择、密度和动效级别。
- 可访问性等级。
- 桌面、平板或移动端优先级。

## 输出形态

- UI 设计规范
- HTML/CSS
- React
- Vue
- Tailwind
- Figma 提示词
- 线框草案
- 组件库规范
- 落地页结构
- 响应式布局计划

## 扩展或替换风格

使用 `adaptation-rules.md` 调整 hue、字体、圆角、卡片处理、密度和动效。保持 token 名称稳定，以便组件继续兼容。

## 更新 Design Tokens

编辑 `design-tokens.json` 中 token 的 `value`、`role`、`usage`、`modifiable` 或 `fallback`。不要加入创建历史字段。名称应保持语义化和稳定。

## 更新 Component Recipes

编辑 `component-recipes.md` 添加或调整组件。每个组件都应包含使用场景、视觉结构、token 依赖、状态、响应式行为、可访问性、实现提示、禁止模式和中性范例。

## 运行质量检查

每次生成 UI 后使用 `validation-checklist.md`。同时扫描仓库，确保没有私人名称、非自有文本、创建历史语言、无效 JSON、缺失可访问性状态或过度固定布局。
