# Responsive Rules

## Desktop

- 使用最大宽度 75rem 的页面壳。
- 使用完整文字导航和内联工具控件。
- 当次级内容有助于扫描时，使用侧栏加主内容 grid。
- 内容卡片保持宽且可读，必要时在右侧提供操作入口。
- 使用 16px 基础正文和强标题。

## Tablet

- gutter 缩小到 24px。
- 只有两列都至少 280px 宽时才保留双列。
- 先折叠低优先级工具导航，再折叠主导航。
- 卡片圆角和 token 值与桌面端保持一致。
- Hero 高度和 section 间距减少 15 到 25 percent。

## Mobile

- 使用单列。
- 使用带图标控件的紧凑顶部导航。
- 菜单、搜索和设置在触发器附近用浮层呈现。
- 侧栏组件移动到主内容之后。
- 使用 14px 正文，同时保持强标题层级。
- 桌面端卡片操作列转为标题内联操作或底部操作行。

## 容器宽度

- Mobile gutter: 16px。
- Tablet gutter: 24px。
- Desktop gutter: 32px。
- Main shell max width: 75rem。
- 无侧栏文章最大宽度: 48rem 到 60rem。
- 移动端浮层宽度：viewport width 减 32px，小菜单除外。

## Grid 变化

- 功能 grid 在移动端使用单列。
- 平板端空间允许时使用两列功能卡。
- 桌面端只有卡片仍可读时才使用三列或更多列。
- 侧栏 grid 在桌面断点及以下移动到主内容下方。
- Timeline 在移动端堆叠日期、标记、标题和标签。

## 导航变化

- 桌面端：品牌、主链接、搜索、显示设置、主题和工具链接可内联。
- 平板端：先隐藏低优先级工具标签。
- 移动端：显示品牌、搜索图标、显示图标、主题图标和菜单图标。
- 移动端菜单作为浮层打开，条目高度 44px。
- 搜索作为顶部栏下方全宽圆角字段打开。

## 卡片重排

- 桌面内容流卡片可使用右侧操作栏或边缘操作区。
- 移动端内容流卡片应把操作图标放在标题旁。
- 桌面卡片列表使用 16px 到 24px 垂直 gap。
- 高密度移动端列表可在一个圆角组内使用柔和分隔线。
- 功能卡片堆叠时保持 icon、title、body 顺序。

## 字号缩放

- 不使用 viewport units 缩放文字。
- Desktop body: 16px。
- Mobile body: 14px。
- Desktop h1: 32px 到 40px。
- Mobile h1: 26px 到 32px。
- 根据文案长度，行高保持在 1.45 到 1.75。

## Section Spacing 缩放

- Desktop section spacing: 48px 到 80px。
- Tablet section spacing: 40px 到 64px。
- Mobile section spacing: 32px 到 48px。
- 紧凑组件使用 12px 到 16px 内部 gap。

## 图片比例

- Hero media: 16:9、21:9 或响应式高度裁剪。
- 资料和缩略图 media: square 或 4:3。
- 产品 media: 16:10 或 4:3。
- 始终设置 `aspect-ratio` 或固定响应式尺寸，避免 layout shift。

## 移动端触控目标

- 最小目标：44px by 44px。
- 紧凑标签只有在不是主控件时可为 32px 高。
- 相邻操作控件至少 8px gap。
- 避免过小 close、next 或 settings 按钮。

## 横竖屏注意事项

- 横屏移动端应保持导航紧凑并降低 hero 高度。
- 避免超过 viewport 高度的固定高度面板。
- 只有内容很长时，浮层才允许内部滚动。

## 长文本折行

- badges、URLs 和长 tokens 使用 `overflow-wrap: anywhere`。
- 正文设置 max-width。
- 避免固定宽度按钮搭配长标签。
- 在文字截断前让 CTA 组堆叠。
- 元信息行应使用一致 gap 并自然换行。
