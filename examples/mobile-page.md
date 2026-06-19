# Mobile Page Example

## 输入需求

创建移动端优先内容页，包含紧凑导航、可搜索条目和卡片摘要。

## 使用到的 Skill 规则

- Mobile navigation rules。
- Card feed layout。
- Search form recipe。
- Floating panel interaction。
- Tag and metadata rules。

## 生成策略

- 使用紧凑顶部栏，包含品牌、搜索、显示控制、主题控制和菜单。
- 搜索放在顶部栏下方的全宽圆角面板中。
- 使用堆叠卡片，包含标题、元信息、摘要和操作图标。
- 次级组件移动到主列表之后。
- 页脚链接保持低强调。

## 结构草案

1. Compact top bar。
2. Optional search panel。
3. Stacked content cards。
4. Pagination or load-more action。
5. Secondary widgets。
6. Footer。

## Token 使用说明

- `container.mobile.gutter` 用于页面 padding。
- `radius.card.default` 用于卡片组。
- `radius.control` 用于图标按钮和标签。
- `color.surface.control` 用于元信息图标。
- `motion.duration.base` 用于浮层。

## 响应式说明

- 该布局从移动端开始。
- 平板端可引入双列功能区。
- 桌面端可把次级组件移动到侧栏。

## 可访问性说明

- 菜单支持键盘并可用 Escape 关闭。
- 搜索字段有 label。
- 触控目标满足 44px 最小值。
- 长标题不裁切。
- Reduced motion 移除面板平移。

## 质量检查要点

- 移动端内容可读。
- 控件可触达且有 label。
- 卡片 hover 不移动布局。
- 次级内容位于主列表之后。
