# Interaction Rules

## Hover

- Hover 应使用主强调色家族对表面或文字进行轻微 tint。
- Hover 不得改变内容尺寸或移动相邻元素。
- 卡片可显示轻微操作入口，但表面应保持稳定。
- 标签和紧凑控件应将柔和填充加深一级。

## Active

- 文本按钮可缩放到 0.95。
- 图标按钮可缩放到 0.90。
- Active 状态应在 `motion.duration.fast` 内完成。
- 除非整张大卡片是明确操作目标，否则不要对其应用 active transform。

## Focus

- 每个交互元素都必须有可见 focus。
- Focus 在浅色和深色模式下都必须清晰。
- Focus 不能只依赖颜色；使用 outline、ring、underline 或 surface 变化。
- Focus 顺序应符合视觉顺序。

## Disabled

- Disabled 控件降低 opacity 并移除指针交互。
- Disabled 控件保持尺寸和标签可见。
- Disabled 文本仍应满足非活动 UI 的可读要求。
- 禁用主操作可能造成困惑时，提供原因说明。

## Loading

- Loading 控件保持宽高。
- 只有能帮助用户理解等待状态时才使用 spinner、进度文字或 skeleton。
- Loading 区域使用 `aria-busy`。
- 不要在替代内容准备好之前隐藏已有内容。

## Error

- 使用 `color.state.error`，并搭配图标或文字标签。
- 错误消息与相关字段关联。
- 消息简洁且可执行。
- 不只用红色表达错误。

## Success

- 使用 `color.state.success`，并搭配文字或图标反馈。
- 成功反馈保持简短，除非确认重大状态变化。
- 瞬时反馈结束后，控件可回到常态。

## Empty

- 空状态包含小标题、一句话说明、可选图标和一个明确操作。
- 空状态放在圆角卡片表面内。
- 避免没有下一步说明的纯装饰空状态。

## Scroll

- 有助于定位时保持顶部导航稳定。
- 只有用户触发锚点移动时才使用 smooth scroll。
- 遵守 reduced-motion 设置。
- 长页面保持清晰 section 间距，并可提供快速导航。

## Transition

- Hover 和 active 使用 `motion.duration.fast`。
- 面板开合使用 `motion.duration.base`。
- 内容入场使用 `motion.duration.enter`。
- 组件统一使用 `motion.easing.standard`。
- 主题切换不得让文字色、图标色、控件背景和页面背景跨越低对比中间态；暗色/浅色切换应即时更新这些主题绑定值，或只为非文本装饰做短透明度变化。

## Micro-Interaction

- 紧凑控件使用小幅缩放。
- 面板入场使用 opacity 加轻微位移。
- 选中状态使用强调色标记。
- 交互应安静、可预测。

## Motion Duration

- Hover: 120ms 到 180ms。
- Active press: 80ms 到 150ms。
- Panel open: 160ms 到 220ms。
- Content entry: 240ms 到 320ms。
- Modal open: 180ms 到 260ms。

## Easing

- 标准 UI transition 使用 `cubic-bezier(0.4, 0, 0.2, 1)`。
- 只有进度指示器使用 linear。
- 除非用户要求更活泼风格，否则避免弹性 easing。

## Reduced Motion

- 移除 translate 和 scale。
- 保留 150ms 以内的 opacity transition。
- 禁用自动滚动和自动切换。
- 保留即时状态反馈。

## Keyboard Interaction

- Tab 顺序符合视觉顺序。
- Escape 关闭菜单、popover、modal 和搜索面板。
- Enter 或 Space 激活 focused button。
- 菜单、tabs 和 segmented controls 可使用方向键移动。
- Modal 在关闭前应限制 focus。

## Touch Interaction

- 触控目标至少 44px by 44px。
- 相邻紧凑控件至少 8px 间距。
- 不使用 hover-only 信息。
- 移动端常用控件放在拇指可触区域附近。
- 基本任务不依赖高精度拖拽。
