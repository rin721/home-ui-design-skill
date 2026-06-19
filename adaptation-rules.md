# Adaptation Rules

## 替换主色

1. 修改 `color.brand.hue`。
2. 重新计算 `color.brand.primary` 和 `color.brand.primary.dark`。
3. 使用低 chroma 调整 `color.surface.page`。
4. 文本和卡片表面保持中性。
5. 检查链接、focus ring 和选中控件的对比度。

## 替换字体

- 选择干净的 sans-serif 字体族。
- 初始阶段保持正文大小、标题比例和行高稳定。
- 字体变化后重新检查卡片标题换行。
- 装饰性 display type 只可用于大 hero 标题。

## 调整圆角

- 12px 适合更锐利的产品感。
- 16px 是默认柔和模块化风格。
- 20px 适合更友好的个人感。
- 控件圆角应小于卡片圆角。
- 同一表面组不要混用过多圆角值。

## 调整卡片风格

- 默认卡片为 flat，通过背景区分。
- 页面表面和卡片表面对比过弱时，加入轻边框。
- 阴影只用于浮层和菜单。
- 重要或选中卡片使用 accent rail。

## 调整页面密度

- 提高密度：将卡片 padding 和元信息 gap 减少 12 到 20 percent。
- 降低密度：将 section spacing 和卡片 padding 增加 15 到 25 percent。
- 触控目标不缩小。
- 先隐藏低优先级元信息，再减少可读文本空间。

## 调整动效强度

- Minimal: 仅 opacity，120ms 到 180ms。
- Default: opacity 加小幅 scale 或 translate，150ms 到 300ms。
- Expressive: 只在非关键装饰时刻使用更强 transform。
- 始终提供 reduced-motion 行为。

## 风格方向转换

### 更技术感

- 圆角降低到 12px。
- 分隔线略微增强。
- 元信息更紧凑，卡片列表更密。
- 冷色强调保持精确克制。

### 更高级感

- 减少可见控件。
- 增加留白。
- 次级区域使用更柔和文字对比。
- 减少标签数量并清理卡片正文。

### 更极简

- 移除装饰媒体。
- 使用 plain sections 和更少面板。
- 每个组件只保留一个强调点。
- 减少 badge 数量。

### 更企业感

- 使用更保守文案。
- 通过 grid 和 section 标题增强结构。
- CTA 层级更明确。
- 社交或资料细节降为次级。

### 更产品感

- 使用功能网格、媒体块、方案卡片和证明 section。
- CTA 放在价值表达之后。
- 使用 icon tile 和短收益文案。

## 可替换 Tokens

- `color.brand.hue`
- `color.brand.primary`
- `color.surface.page`
- `typography.family.sans`
- `radius.card.default`
- `radius.control`
- `spacing.section.md`
- `shadow.panel.float`
- `motion.duration.base`

## 稳定结构规则

- 保持语义化 token 名称稳定。
- 保持 card、button、navigation、tag 和 panel 的状态模型稳定。
- 保持 desktop、tablet、mobile 断点角色稳定。
- 保持可访问性行为稳定。

## 替换后验证

- 强调色仍出现在相同组件角色中。
- 卡片共享同一圆角家族。
- Focus 仍然可见。
- 文本对比度通过。
- 需要时移动端仍保持单列。
- 浮层位于内容上方并可预测关闭。
- 占位文案保持中性。

## 避免组件失衡

- 不要将超圆卡片与尖锐控件搭配。
- 不要将高 chroma 强调色与大量彩色 badge 搭配。
- 不要在高密度内容中增强动效。
- 不要给每张卡片都加重阴影。
- 元信息换行不佳时，不要继续压缩间距。
