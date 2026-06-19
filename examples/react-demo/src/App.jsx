import { useState } from "react";
import {
  ArrowRight,
  CheckCircle2,
  Component,
  LayoutGrid,
  Menu,
  Moon,
  Search,
  ShieldCheck,
  Smartphone,
  Sun,
} from "lucide-react";
import "./styles.css";

const features = [
  {
    icon: LayoutGrid,
    title: "布局语法清晰",
    body: "从首页、落地页到归档视图，先选布局模式，再映射组件与状态。",
  },
  {
    icon: Component,
    title: "组件状态完整",
    body: "按钮、卡片、表单和浮层都保留 hover、focus、loading 与错误语义。",
  },
  {
    icon: Smartphone,
    title: "移动端先可用",
    body: "单列堆叠、44px 触控目标、稳定媒体比例和自然换行是默认要求。",
  },
  {
    icon: ShieldCheck,
    title: "可访问性前置",
    body: "焦点、键盘、对比度、状态文字和 reduced motion 都进入交付清单。",
  },
];

const cards = [
  "读取 design tokens 并建立 CSS variables",
  "选择主布局和备选布局",
  "生成组件配方与响应式行为",
  "运行发布清洁和可访问性检查",
];

function App() {
  const [dark, setDark] = useState(false);

  return (
    <main className={dark ? "app dark" : "app"}>
      {/* Navigation */}
      <nav className="topbar" aria-label="主导航">
        <a className="brand" href="#top" aria-label="Home UI Design 首页">
          <span className="brand-mark" aria-hidden="true">
            H
          </span>
          <span>Home UI Design</span>
        </a>
        <div className="nav-links" aria-label="页面链接">
          <a href="#features">能力</a>
          <a href="#workflow">流程</a>
          <a href="#quality">校验</a>
        </div>
        <div className="tools">
          <button className="icon-button" aria-label="搜索">
            <Search size={18} aria-hidden="true" />
          </button>
          <button
            className="icon-button"
            aria-label={dark ? "切换到浅色模式" : "切换到暗色模式"}
            onClick={() => setDark((value) => !value)}
          >
            {dark ? <Sun size={18} aria-hidden="true" /> : <Moon size={18} aria-hidden="true" />}
          </button>
          <button className="icon-button menu-button" aria-label="打开菜单">
            <Menu size={18} aria-hidden="true" />
          </button>
        </div>
      </nav>

      {/* Hero */}
      <section className="hero" id="top">
        <div className="hero-copy">
          <span className="eyebrow">开源 UI design skill</span>
          <h1>把柔和模块化界面变成可复用规范</h1>
          <p>
            这套 demo 展示 token、布局、组件状态、响应式和可访问性如何在一个 React 页面中落地。
          </p>
          <div className="hero-actions">
            <a className="button primary" href="#features">
              查看能力
              <ArrowRight size={18} aria-hidden="true" />
            </a>
            <a className="button ghost" href="#quality">
              校验清单
            </a>
          </div>
        </div>
        <div className="preview-card" aria-label="界面预览">
          <img src="/ui-preview.png" alt="一个使用圆角卡片和冷色强调的中性产品界面预览" />
        </div>
      </section>

      {/* Feature cards */}
      <section className="section" id="features" aria-labelledby="features-title">
        <div className="section-heading">
          <span className="eyebrow">Feature cards</span>
          <h2 id="features-title">从审美规则到可执行界面</h2>
          <p>每张卡片都使用同一套 token、圆角、状态和响应式约束。</p>
        </div>
        <div className="feature-grid">
          {features.map((feature) => {
            const Icon = feature.icon;
            return (
              <article className="feature-card" key={feature.title}>
                <span className="icon-tile" aria-hidden="true">
                  <Icon size={20} />
                </span>
                <h3>{feature.title}</h3>
                <p>{feature.body}</p>
              </article>
            );
          })}
        </div>
      </section>

      {/* Workflow content cards */}
      <section className="section workflow" id="workflow" aria-labelledby="workflow-title">
        <div className="section-heading compact">
          <span className="eyebrow">Workflow</span>
          <h2 id="workflow-title">生成前先建立稳定结构</h2>
          <p>先确定 token 和布局，再把组件、状态、文案和断点逐层补齐。</p>
        </div>
        <div className="workflow-list">
          {cards.map((item, index) => (
            <article className="task-card" key={item}>
              <span className="step">{String(index + 1).padStart(2, "0")}</span>
              <p>{item}</p>
              <CheckCircle2 size={18} aria-hidden="true" />
            </article>
          ))}
        </div>
      </section>

      {/* Stats */}
      <section className="stats" id="quality" aria-label="质量摘要">
        <article>
          <strong>12+</strong>
          <span>规则文件</span>
        </article>
        <article>
          <strong>44px</strong>
          <span>触控目标</span>
        </article>
        <article>
          <strong>2</strong>
          <span>语言镜像</span>
        </article>
      </section>

      {/* CTA */}
      <section className="cta-panel" aria-labelledby="cta-title">
        <div>
          <span className="eyebrow">CTA</span>
          <h2 id="cta-title">用同一套规则继续扩展页面</h2>
          <p>复制这个 demo 的 token 映射，替换中性内容，就能继续生成新的首页、section 或组件库。</p>
        </div>
        <a className="button primary" href="#top">
          回到顶部
          <ArrowRight size={18} aria-hidden="true" />
        </a>
      </section>

      {/* Footer */}
      <footer className="footer">
        <span>Home UI Design Demo</span>
        <a href="#features">能力</a>
        <a href="#workflow">流程</a>
        <a href="#quality">校验</a>
      </footer>
    </main>
  );
}

export default App;
