# Corporate Homepage Example

## 输入

- 页面类型：`homepage`
- 目标：为专业服务团队创建克制可信的首页
- 输出：UI design spec
- 风格方向：更企业感

## 可复用输出结构

1. Navigation：清晰品牌占位、主链接、联系 CTA。
2. Hero：split hero，左侧价值主张，右侧本地界面或服务流程预览。
3. Service cards：3 到 6 张服务卡，描述短且保守。
4. Process section：步骤或方法论列表，不使用夸大承诺。
5. Proof cards：中性证明模块，可用流程指标或能力摘要，不虚构真实客户。
6. CTA strip：低压主操作和次级链接。
7. Footer：工具链接和低强调说明。

## Token 选择

- `color.brand.primary` 用于 CTA、active indicators 和 focus ring。
- `color.text.secondary` 用于辅助文案和元信息。
- `grid.feature.cards` 用于服务卡。
- `shadow.none` 用于静态卡片。
- `shadow.panel.float` 只用于 dropdown、popover 或 modal。

## 响应式行为

- Desktop：hero 可双列，服务卡使用 responsive grid。
- Tablet：先减少工具标签，再折叠导航。
- Mobile：hero 文本优先，CTA 全宽，服务卡堆叠，证明模块放在主内容之后。

## 可访问性验收

- 导航使用语义 links。
- CTA 按钮有清晰 label。
- 证明模块不自动轮播；如使用 carousel，必须提供暂停控件。
- 对比度和 focus 在浅色、暗色模式下都可读。

## 中性占位文案

- H1：`为复杂服务建立清晰入口`
- CTA：`预约沟通`
- 服务卡：`需求梳理`、`流程设计`、`交付支持`
