---
name: 思维生产线
description: 中文长文写作与方法论沉淀博客
colors:
  accent: "#b04a25"
  accent-dark: "#813317"
  paper: "#f8f6f2"
  text-primary: "#2f3236"
  text-strong: "#1a1b1d"
  border-soft: "#e9e7e4"
typography:
  display:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.2rem)"
    fontWeight: 650
    lineHeight: 1.1
  body:
    fontFamily: "Source Han Serif SC, Noto Serif SC, Songti SC, STSong, PMingLiU, serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.95
  label:
    fontFamily: "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 500
    lineHeight: 1.4
rounded:
  sm: "8px"
  md: "12px"
  lg: "16px"
spacing:
  xs: "0.4rem"
  sm: "0.8rem"
  md: "1.2rem"
  lg: "2rem"
components:
  nav-link:
    textColor: "{colors.text-strong}"
    typography: "{typography.label}"
    padding: "1em 0.5em"
  post-card:
    backgroundColor: "#ffffff"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.md}"
    padding: "1.2rem 1.3rem"
---

# Design System: 思维生产线

## 1. Overview

**Creative North Star: "中文长文的安静工作台"**

这个站点的视觉目标不是“炫”，而是“稳”。读者打开页面后，第一感受应是可信赖、可进入、可持续阅读，而不是被营销化布局或视觉特效打断。信息密度保持中等偏低，把注意力集中在标题、摘要、时间、标签这些决策关键信号上。

整体风格遵循“纸面感 + 结构化”策略：暖色纸面底色承载长文阅读，清晰的版面分区支持快速扫描。页面组件应保持节制，避免将博客页面演化成产品仪表盘。

**Key Characteristics:**
- 中文阅读优先，正文节奏稳定
- 暖中性色底 + 单主强调色
- 卡片与边框只服务信息分组，不做装饰性堆叠

## 2. Colors

颜色策略采用 restrained 路线，强调“一个品牌色 + 多层中性色”。

### Primary
- **Clay Accent** (`#b04a25`): 仅用于链接、标签边框、导航激活和关键视觉锚点。

### Neutral
- **Warm Paper** (`#f8f6f2`): 全站主背景，提供纸面阅读感。
- **Strong Ink** (`#1a1b1d`): 标题与高优先级文字。
- **Body Ink** (`#2f3236`): 正文与说明文本。
- **Soft Border** (`#e9e7e4`): 分割线、容器边界、低权重结构线。

**The One Accent Rule.** 主强调色在单屏占比应保持克制，只在“可点击”与“层级提示”处出现。

## 3. Typography

**Display Font:** `PingFang SC` 系列 sans  
**Body Font:** `Source Han Serif SC` 系列 serif  
**Label/Mono Font:** 导航与标签延续 sans，代码使用 `JetBrains Mono` 回退栈

**Character:** 以中文衬线正文承载论述深度，用无衬线标题与导航提供结构清晰度。

### Hierarchy
- **Display** (650, `clamp(2rem, 5vw, 3.2rem)`, 1.1): 首页主标题与关键区块标题。
- **Headline** (650, `2.1em`, 1.28): 页面级 h2。
- **Title** (650, `1.6em`, 1.28): 卡片标题与 h3。
- **Body** (400, `20px`, 1.95): 长文正文，建议行宽保持 65 到 75ch。
- **Label** (500, `0.85rem`, 1.4): 标签、导航、元信息文字。

**The Reading Rhythm Rule.** 正文行高优先保障阅读连续性，不因追求紧凑而压缩段落呼吸。

## 4. Elevation

默认使用轻阴影表达层级，强调“有分组感但不过度悬浮”。阴影仅用于内容容器和 hover 反馈，不作为常驻装饰。

### Shadow Vocabulary
- **Surface Lift** (`0 10px 30px rgba(40, 30, 10, 0.08)`): 首页模块、文章卡片等一级容器。

**The Flat-At-Rest Rule.** 正文区域保持平稳，交互时才出现轻微抬升反馈。

## 5. Components

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

### Navigation
- **Style:** 顶部粘性导航，透明度轻微降低，突出阅读连续性。
- **State:** 当前页面通过底边线和字重提示，避免过重背景块。

## 6. Do's and Don'ts

### Do:
- **Do** 把首页和列表页设计为“帮助选择文章”的界面，而不是展示特效的舞台。
- **Do** 让标题、日期、摘要、标签形成固定扫描顺序。
- **Do** 在移动端保持足够触控面积和稳定行高。
- **Do** 用一套一致的间距与圆角尺度维护长期可扩展性。

### Don't:
- **Don't** 使用“科技蓝紫渐变 + 玻璃拟态 + 发光描边”的 AI 模板视觉。
- **Don't** 把博客页面做成 SaaS 仪表盘式布局和指标叙事。
- **Don't** 使用夸张动效抢夺正文注意力。
- **Don't** 通过重复嵌套卡片制造伪层级。
