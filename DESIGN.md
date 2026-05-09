---
name: 熵减心流
description: 中文长文写作与方法论沉淀博客
colors:
  accent: "#A14A2A"
  accent-dark: "#7E351F"
  accent-warm: "#C86A3D"
  accent-wash: "#F3E8E2"
  paper: "#F8F3EE"
  text-primary: "#2f3236"
  text-strong: "#1a1b1d"
  border-soft: "#E8D8CE"
typography:
  home-display:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "clamp(3.5rem, 9vw, 5.75rem)"
    fontWeight: 800
    lineHeight: 0.98
  page-h1:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "clamp(2.25rem, 4.2vw, 3.25rem)"
    fontWeight: 760
    lineHeight: 1.08
  section-h2:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "clamp(1.5rem, 2.4vw, 2rem)"
    fontWeight: 720
    lineHeight: 1.3
  item-h3:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "Source Han Serif SC, Noto Serif SC, Songti SC, STSong, PMingLiU, serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.95
  excerpt:
    fontFamily: "Source Han Serif SC, Noto Serif SC, Songti SC, STSong, PMingLiU, serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  meta:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.45
  prose-h2:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 650
    lineHeight: 1.3
  prose-h3:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 650
    lineHeight: 1.35
rounded:
  sm: "8px"
  md: "12px"
  lg: "16px"
spacing:
  xs: "0.4rem"
  sm: "0.8rem"
  md: "1.2rem"
  lg: "2rem"
  list-gap: "1.4rem"
  section-gap: "2.4rem"
  page-padding-y: "3rem"
  page-width: "760px"
  home-width: "1180px"
components:
  nav-link:
    textColor: "{colors.text-strong}"
    typography: "{typography.meta}"
    padding: "1em 0.5em"
  list-item:
    textColor: "{colors.text-primary}"
    typography: "{typography.item-h3}"
  meta-line:
    textColor: "{colors.text-primary}"
    typography: "{typography.meta}"
  chip:
    textColor: "{colors.accent-dark}"
    typography: "{typography.meta}"
    rounded: "999px"
    padding: "0.2rem 0.6rem"
---

# Design System: 熵减心流

## 1. Overview

**Creative North Star: "熵减心流：个人知识工作的操作系统"**

这个站点的视觉目标不是普通博客模板，而是一个长期思想工程的入口。读者打开页面后，第一感受应是：这里在持续研究 AI 时代的个人工作流、认知结构与生产关系，并且有一套稳定的输入、思考、输出、反馈系统。

整体风格遵循"研究日志 + 系统设计图"策略：暖色纸面底色承载中文长文，右侧辅助栏展示 Now、主题地图与工作流循环，让首页既能阅读，也能感知站点的长期研究方向。

**Key Characteristics:**
- 中文阅读优先，正文节奏稳定
- Warm Rust 单一强调色系统，带纸面、人文与研究感
- 首页有明确视觉重心：大标题、右侧工作流图与出版化文章入口

## 2. Colors

颜色策略采用 Warm Rust 路线，强调"一个品牌色 + 多层暖中性色"。

### Primary
- **Warm Rust** (`#A14A2A`): 用于链接、标签边框、导航激活和关键视觉锚点。
- **Rust Glow** (`#C86A3D`): 用于 Hero 结构图、渐变与 hover 高光。
- **Rust Wash** (`#F3E8E2`): 用于轻背景、侧栏模块和低权重强调区域。

### Neutral
- **Warm Paper** (`#F8F3EE`): 全站主背景，提供纸面阅读感。
- **Strong Ink** (`#1a1b1d`): 标题与高优先级文字。
- **Body Ink** (`#2f3236`): 正文与说明文本。
- **Soft Border** (`#e9e7e4`): 分割线、容器边界、低权重结构线。

**The One Accent Rule.** 主强调色在单屏占比应保持克制，只在"可点击"与"层级提示"处出现。

## 3. Typography

**Display Font:** `PingFang SC` 系列 sans
**Body Font:** `Source Han Serif SC` 系列 serif
**Label/Mono Font:** 导航与标签延续 sans，代码使用 `JetBrains Mono` 回退栈

**Character:** 以中文衬线正文承载论述深度，用无衬线标题与导航提供结构清晰度。

### One Site-wide Heading Scale

整站只用一套页面级标题阶梯。**所有页面（首页、文章列表、主题、关于、Now、文章详情）的 H1/H2/H3 视觉尺寸必须一致**。

| 角色 | Token | 尺寸 | 字重 | 字体 | 用例 |
|------|-------|------|------|------|------|
| 首页品牌标题 | `--text-display` | `clamp(3.5rem, 9vw, 5.75rem)` | 800 | sans | 首页 Hero 的「熵减心流」 |
| 页面 H1 | `--text-h1` | `clamp(2.25rem, 4.2vw, 3.25rem)` | 760 | sans | 每个页面唯一的页面主标题 |
| 区块 H2 | `--text-h2` | `clamp(1.5rem, 2.4vw, 2rem)` | 720 | sans | 「最新文章」「写作主线」「关于」「Now」「主题索引」分组 |
| 条目 H3 | `--text-h3` | `1.125rem` | 600 | sans | 文章列表项标题、卡片标题 |
| 正文 Body | `--text-body` | `1rem` | 400 | serif | UI 区域的正文段 |
| 摘要 Excerpt | `--text-excerpt` | `0.9375rem` | 400 | serif | 列表项摘要、说明性长句 |
| 说明 Caption | `--text-caption` | `0.875rem` | 400 | sans | 区块下面的短说明 |
| 元信息 Meta | `--text-meta` | `0.8125rem` | 500 | sans | 日期、系列、统计、tag 文案 |

**The Display Exception Rule.** 站点共享一套 H1/H2/H3 阶梯，但首页 Hero 允许使用 `--text-display` 建立品牌视觉重心。文章正文（`.prose`）内是第二个例外：它有自己更大的 `prose-h2` (`1.625rem`) 与 `prose-h3` (`1.25rem`)，仅用于长文章节导航，不会用在 UI 区块。

### Long-form Body
- 中文衬线正文，行高 1.95
- 文章正文宽度 720px，与其他页面 `--page-width` 一致

**The Reading Rhythm Rule.** 正文行高优先保障阅读连续性，不因追求紧凑而压缩段落呼吸。

## 4. Layout

整站有两个容器系统：文章阅读页保持稳定窄栏，首页使用更宽的 12-column 网格建立视觉重心：

- `--page-width: 760px`：文章详情、列表页、关于、Now 使用的阅读栏宽。
- `--home-width: 1180px`：首页使用的宽屏布局容器。
- `--page-padding-y: 3rem`：页面顶部到 H1 的呼吸空间。
- `--section-gap: 2.4rem`：相邻 H2 区块之间的垂直距离。
- `--list-gap: 1.4rem`：列表项之间的垂直距离。

**The Home Grid Rule.** 首页必须使用主内容 + 辅助信息的二维结构。推荐 12-column grid：左侧 7 列用于 Hero 与最新文章，右侧 5 列用于工作流图、Now、主题地图、Quote 或 Reading。文章详情页不使用侧栏，以保证长文阅读连续性。

## 5. Elevation

默认使用轻阴影表达层级，强调"有分组感但不过度悬浮"。阴影仅用于内容容器和 hover 反馈，不作为常驻装饰。

### Shadow Vocabulary
- **Surface Lift** (`0 10px 30px rgba(40, 30, 10, 0.08)`): 文章 hero 图、列表卡片 hover 抬升。

**The Flat-At-Rest Rule.** 正文区域保持平稳，交互时才出现轻微抬升反馈。

## 6. Components

### Buttons / Text Links
- **Primary action:** 使用强调色文字或下划线，不依赖大块实心按钮。
- **Hover / Focus:** 颜色加深，保留可见 focus 线索。

### Tags / Chips
- **Style:** 细边框胶囊标签，强调分类而非视觉主角。
- **Role:** 只用于主题聚合与扫描辅助。

### Cards / Containers
- **Corner Style:** 柔和圆角（12 到 16px）。
- **Background:** 白底或低饱和浅色底，确保正文对比度。
- **Border:** 细边界线用于分组，避免嵌套卡片。
- **Internal Padding:** 以 1.2rem 以上步长保持内容呼吸。

**The No-Wrapper-Card Rule.** 整页内容**不允许**整体被一个白底/边框/box-shadow 卡片包住。卡片只用于真的需要"独立单元"的列表项；像 about/now 这种短篇页面应直接呼吸。

### Navigation
- **Style:** 顶部粘性导航，透明度轻微降低，突出阅读连续性。
- **State:** 当前页面通过底边线和字重提示，避免过重背景块。

### Page Skeleton（所有页面通用骨架）

```
<Header />
<main>
  <h1>页面主标题</h1>          ← --text-h1
  <p class="page-lead">…</p>   ← 一句承诺/导读，--text-body 或 --text-excerpt
  <section>
    <h2>区块标题</h2>          ← --text-h2
    <p class="caption">…</p>   ← 可选 --text-caption
    <ul class="list">
      <li>
        <div class="meta">…</div>   ← --text-meta
        <h3>条目标题</h3>            ← --text-h3
        <p class="excerpt">…</p>   ← 可选 --text-excerpt
      </li>
    </ul>
  </section>
  <section>
    <h2>另一个区块</h2>
    …
  </section>
</main>
<Footer />
```

每个页面都遵循这个骨架；任何样式覆盖必须保留 H1/H2/H3 的尺寸与字重一致。

## 7. Do's and Don'ts

### Do:
- **Do** 把所有页面 H1 视觉对齐到 `--text-h1`，所有 H2 对齐到 `--text-h2`，所有 H3 对齐到 `--text-h3`。
- **Do** 所有 `<main>` 用 `--page-width`，避免每页飘忽不同宽度。
- **Do** 让标题、日期、摘要、标签形成固定扫描顺序。
- **Do** 在移动端保持足够触控面积和稳定行高。

### Don't:
- **Don't** 在某个页面把 H1 放大到 `clamp(2rem, 5vw, 3.2rem)` 这种"hero-only"尺寸，导致跨页面 H1 不一致。
- **Don't** 用 H2 / H3 自定义到一组新尺寸（例如 1.25rem、1.5rem 同时存在）。
- **Don't** 把整页内容包在一个白底 + 边框 + box-shadow 的"卡片壳"里。
- **Don't** 用"科技蓝紫渐变 + 玻璃拟态 + 发光描边"的 AI 模板视觉。
- **Don't** 使用夸张动效抢夺正文注意力。
- **Don't** 在列表里使用虚线分隔，违反 The No-Segmented-Rule。
