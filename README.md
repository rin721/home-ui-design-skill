# home-ui-design-skill

一套可安装、可验证、可演示的 Codex UI design skill，用于生成平静、圆润、内容优先的模块化界面。根目录中文版本是默认安装入口，`en-us/` 保留英文镜像。

## 适合做什么

- 将松散 UI 需求转化为结构化设计规范。
- 生成首页、落地页、产品介绍区、个人资料页、知识索引、归档页、移动端内容页和组件库规范。
- 输出 HTML/CSS、React、Vue、Tailwind、Figma prompt、线框草案或实现计划。
- 保持颜色、圆角、间距、字体、动效、断点和状态 token 化。
- 强制纳入可访问性：可见 focus、键盘行为、44px 触控目标、错误说明和 reduced motion。

## 不适合做什么

- 高密度企业后台、交易界面、游戏 HUD、暗黑赛博或奢华杂志风。
- 一比一复刻品牌官网、复制专有视觉资产或使用不可授权素材。
- 只追求营销视觉冲击、强渐变装饰或高度实验性动效的页面。

## 安装

将仓库根目录放入 Codex skills 目录或通过 Codex skill 安装流程引用该目录即可。默认入口是根目录的 `SKILL.md`，无需安装 `en-us/`。

```text
home-ui-design-skill/
  SKILL.md
  design-tokens.json
  agents/openai.yaml
```

英文使用者可以参考 `en-us/`，但它不是单独的默认入口。

## AI Agent 使用方式

1. 读取 `SKILL.md`，判断任务是否落在柔和模块化 UI 范围内。
2. 加载 `design-tokens.json`，先建立 token 映射。
3. 按需读取 `style-profile.md`、`layout-patterns.md`、`component-recipes.md`、`interaction-rules.md`、`responsive-rules.md` 和 `content-rules.md`。
4. 风格替换时读取 `adaptation-rules.md`。
5. 按 `output-modes.md` 组织交付物。
6. 交付前使用 `validation-checklist.md` 和 `scripts/validate_skill.py` 校验。

## 示例与 Demo

- `examples/*.md` 提供可复用输出样例。
- `examples/react-demo/` 是 Vite React demo，展示 token、组件、响应式、暗色模式、focus 和 reduced motion 的落地方式。

运行 demo：

```bash
cd examples/react-demo
npm ci
npm run dev
```

构建 demo：

```bash
cd examples/react-demo
npm run build
```

## 维护与校验

运行仓库校验：

```bash
python scripts/validate_skill.py .
```

运行 Codex skill 基础校验：

```powershell
$env:PYTHONUTF8='1'
python C:\Users\xiaol\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\coder\rin721\home-ui-design-skill
python C:\Users\xiaol\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\coder\rin721\home-ui-design-skill\en-us
```

更新规则时保持中英文镜像同步，避免新增私人名称、真实品牌、不可授权素材或无来源数据。

## License

MIT
