# Runtime Decision Tree

## 1. 判断页面类型

- 如果需求是完整页面，分类为 homepage、landing、product-section、profile、archive、article、mobile-page 或 custom。
- 如果需求是组件，分类组件组并跳过完整页面布局选择。
- 如果页面类型不清晰，选择最接近的可复用模式，并在回复中说明假设，不写入生成的仓库文件。

## 2. 检查用户输入

- 品牌色或 hue。
- 文案或占位需求。
- 技术目标。
- 组件需求。
- 设备优先级。
- 可访问性等级。
- 内容清单。

## 3. 读取 Tokens

- 加载 `design-tokens.json`。
- 除非用户提供替换，否则使用默认 tokens。
- 需要代码时，将 tokens 映射到 CSS variables 或框架 theme values。

## 4. 读取布局规则

- 加载 `layout-patterns.md`。
- 用户要求选项时，选择一个主布局和一个备选布局。
- 除非用户明确要求，不使用固定页面顺序。

## 5. 读取组件规则

- 加载 `component-recipes.md`。
- 只选择需求所需组件。
- 确保每个选中组件包含视觉结构、状态、响应式行为和可访问性。

## 6. 读取交互规则

- 加载 `interaction-rules.md`。
- 在适用位置加入 hover、active、focus、disabled、loading、error、success、empty、scroll、transition 和 reduced-motion 行为。

## 7. 读取响应式规则

- 加载 `responsive-rules.md`。
- 定义 desktop、tablet 和 mobile 行为。
- 移动端优先时，先创建移动布局。

## 8. 读取内容规则

- 加载 `content-rules.md`。
- 组织标题、副标题、元信息、段落、CTA、空状态、辅助文案和占位文案。

## 9. 选择输出模式

- 加载 `output-modes.md`。
- 未提供技术目标时，使用 UI design spec。
- 提供技术目标时，加入对应实现细节。

## 10. 生成

- 生成所需输出。
- 使用语义化 tokens。
- 保持占位内容中性。
- 使用可访问结构和状态。

## 11. 验证

- 加载 `validation-checklist.md`。
- 检查每个适用项目。
- 交付前修复缺失状态、缺失响应式规则或可访问性问题。

## 12. 发布清洁

- 移除创建历史说明、隐藏准备说明和私人命名。
- 移除非自有资产和虚构私人数据。
- 确保 JSON 有效且 Markdown 结构清晰。
- 确保输出可独立使用。
