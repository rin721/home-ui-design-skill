# Mobile Page Example

## 输入

- 页面类型：`mobile-page`
- 目标：创建移动端优先内容页，包含搜索、列表和次级工具
- 输出：UI design spec + HTML/CSS notes
- 设备优先级：mobile-first

## 可复用输出结构

1. Compact top bar：品牌占位、搜索、显示设置、主题和菜单图标。
2. Search panel：触发后在顶部栏下方打开的全宽圆角字段。
3. Card feed：堆叠内容卡片，包含标题、元信息、摘要、标签和操作图标。
4. Pagination：`加载更多` 或分页控件。
5. Secondary widgets：分类、筛选或摘要组件，移动端放在主列表之后。
6. Footer：低强调链接。

## Token 选择

- `container.mobile.gutter` 用于页面 padding。
- `radius.card.default` 用于卡片组。
- `radius.control` 用于图标按钮、标签和分页控件。
- `color.surface.control` 用于元信息图标和 chip。
- `motion.duration.base` 用于搜索面板显隐。

## 响应式行为

- Mobile：默认单列，所有关键操作至少 44px。
- Tablet：如果宽度充足，可将次级 widgets 放成双列。
- Desktop：可把 secondary widgets 移到侧栏，主列表保持 48rem 到 60rem 可读宽度。

## 可访问性验收

- 菜单、搜索和设置浮层支持 Escape 关闭。
- 搜索字段有可见 label 或可靠的 `aria-label`。
- 长标题自然换行，不裁切正文。
- 不依赖 hover-only 信息。
- Reduced motion 移除搜索面板位移动效。

## 中性占位文案

- 列表标题：`内容条目标题`
- 元信息：`分类 · 3 min · 已更新`
- 空状态：`暂无条目。添加第一个条目以开始列表。`
