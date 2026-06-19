# Product Section Example

## 输入需求

为协作功能创建产品介绍区，并包含组件级设计规范。

## 使用到的 Skill 规则

- Section recipe。
- Feature list recipe。
- Media block recipe。
- Tag and badge recipe。
- CTA recipe。

## 生成策略

- 以 section 标题和简洁收益陈述开始。
- 桌面端使用媒体与功能细节双列。
- 添加三个带 icon tile 的功能卡片。
- 以一个主操作和一个次级链接收尾。

## 结构草案

1. Section header。
2. Media block。
3. Feature cards。
4. Compact metadata badges。
5. CTA row。

## Token 使用说明

- `radius.media` 用于产品预览。
- `color.surface.control` 用于 icon tiles 和 badges。
- `spacing.6` 用于 section 内部节奏。
- `motion.scale.active` 用于 CTA 按压反馈。

## 响应式说明

- 桌面端使用双列。
- 平板端宽度紧张时媒体在上、功能在下。
- 移动端使用单列和全宽 CTA 控件。

## 可访问性说明

- 有意义媒体提供描述性 alt。
- 功能图标默认装饰。
- CTA 顺序符合视觉顺序。
- 每个操作都有可见 focus。

## 质量检查要点

- 无不支持产品声明。
- 功能文案保持简短。
- 媒体具备稳定 aspect ratio。
- 包含状态规则。
