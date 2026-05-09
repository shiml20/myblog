# Blog Homepage Optimization Report (2026-05-09)

## 中文版

### 目标

在 Astro 博客基础上执行完整的 impeccable 风格优化流程，先完成结构与质量基线，再针对首页做两次连续视觉迭代（第 2 轮与第 3 轮）。

### 初始状态

- 框架：Astro 静态博客
- 部署：GitHub Pages 子路径（`/myblog`）
- 初始问题：
  - 首页层级与节奏不够清晰，视觉观感偏模板化
  - 存在可检测的反模式与可访问性细节问题
  - 内链存在子路径部署风险

### 第 1 轮优化（结构与质量基线）

**思路**
1. 先补齐设计上下文，避免后续迭代风格漂移。  
2. 优先修复影响正确性与稳定性的问题（路由、RSS、运行时加载）。  
3. 用可检测规则清理反模式，再进入视觉层优化。  

**关键改动**
- 新增上下文：
  - `PRODUCT.md`
  - `DESIGN.md`
- 路由与部署安全：
  - `src/consts.ts` 增加 `toInternalPath()`，统一处理子路径链接
- 功能与性能：
  - `src/layouts/BlogPost.astro` 中 Mermaid 改为按需动态加载
  - `src/pages/rss.xml.js` 过滤草稿
- 可访问性与基础视觉：
  - 全局 `focus-visible`
  - `prefers-reduced-motion` 支持
  - 导航语义增强（`aria-label`）
  - blockquote 去除侧边重色条反模式

**验证**
- `npx impeccable detect src/` 通过
- `npm run build` 通过

### 第 2 轮优化（首页重构 v1）

**触发**
- 用户反馈：首页仍然“太丑”，需要明显提升首屏观感。

**思路**
1. 重排首屏信息结构，突出“快速理解 + 快速进入”。  
2. 降低视觉噪声，缓解链接下划线造成的割裂感。  
3. 保持中文长文阅读场景的稳态风格，不走炫技路线。  

**关键改动**
- `src/pages/index.astro`
  - 首屏层级重构
  - 新增 quick-jump（读最新文章 / 按主题浏览 / 查看最近进展）
  - 最新文章改为卡片化信息块（时间、标题、摘要）
- `src/components/Header.astro`
  - 导航容器居中，提升版式秩序
- `src/styles/global.css`
  - 链接与正文链接样式微调，减少视觉疲劳

**验证**
- `npx impeccable detect src/` 通过
- `npm run build` 通过

### 第 3 轮优化（首页重构 v2）

**触发**
- 在第 2 轮基础上继续提升首页质感，强化“编辑感”而不是“组件堆叠感”。

**思路**
1. 把“最新文章”改为主次分层（Featured + Briefs），强化阅读入口优先级。  
2. 精简边框密度与视觉竞争，形成更稳定的扫描路径。  
3. 将“写作主线”从短句列表改为“主题 + 解释”结构，提升信息密度。  

**关键改动**
- `src/pages/index.astro`
  - 最新文章区改为：
    - 1 个 Featured（日期/系列/标题/摘要）
    - 2 个 Brief（日期/系列/标题）
  - 写作主线改为“标题 + 解释”三条主线
  - 面板间距、字号与 hover 节奏再次微调

**验证**
- `npx impeccable detect src/` 通过
- `npm run build` 通过

### 第 4 轮优化（设计文档驱动 + 首页自然化，当前轮）

**触发**
- 反馈：第 3 轮首页不够自然；最新文章区出现多条虚线分段，像“五段下划线”；各模块字号不统一；希望规则先写在主设计 MD 里再实现。

**思路**
1. 在 `DESIGN.md` 增加 **Homepage modules** 专节：信息结构、字号阶梯表、禁止虚线分段、首条与后续标题同字号等规则。  
2. 在 `global.css` 的 `:root` 增加 `--home-*` 变量，与文档表格一一对应，避免页面内随意写 `rem`。  
3. 首页最新文章改回**单一列表**：仅用垂直 `gap` 分隔，去掉 `border-bottom: dashed`；所有条目标题同一字号，仅首条展示摘要。  
4. 去掉包住整个首页的巨大 `home-shell` 卡片，把首页改成 Hero、轻量主站注记、双栏内容三个自然分区。  
5. 侧卡与写作主线字号对齐同一阶梯。

**关键改动**
- `DESIGN.md`：`### Homepage modules`、**The No-Segmented-Rule**、**The One-Card-Accent**、Don't 增补  
- `src/styles/global.css`：`--home-*` 系列变量，含首页宽度、间距、hairline、surface token  
- `src/pages/index.astro`：列表结构重写，样式全部引用 `--home-*`；整页大卡片改为分区式编辑首页

**验证**
- `npx impeccable detect src/` 通过  
- `npm run build` 通过  

### 第 5 轮优化（站点统一标题阶梯 + 全站简化，当前轮）

**触发**
- 反馈：主页仍显得“丑”；不同页面的同级标题大小不一致（首页 H1 用 `clamp(2rem, 5vw, 3.2rem)`，其他页面 H1 用全局 `2.8em`；首页 panel H2 = `1.25rem`，themes/about 页面 H2 = `2.1em`；blog 列表条目标题 = `1.5rem`，首页对应条目 = `1.125rem`），观感跳跃，违反“简洁、美观”要求。

**思路**
1. **建立单一站点级标题阶梯**：H1/H2/H3 在所有页面共享同一组尺寸，禁止任一页面再单独定义页面级标题字号。
2. 把首页从“双栏 + 多套自定义字号”改为与其他页面**完全一致的单栏垂直流**：H1 + lead + chips → 区块 H2 + caption + 列表（H3）。
3. 去掉 `about` / `now` / `themes` 上的 `*-shell` 大白底卡片壳，让短页面正文直接呼吸。
4. 把 `BlogPost.astro` 文章详情页的 H1 也对齐到全局 H1 阶梯（不再居中放大），并保留 `.prose` 内章节阶梯（`prose-h2` 1.625rem / `prose-h3` 1.25rem）作为唯一例外，仅服务长文章节导航。
5. 统一所有 `<main>` 宽度到 `--page-width: 720px`，避免每页飘忽不同宽度造成版心错位。

**关键改动**
- `src/styles/global.css`
  - 新增统一 token：`--text-h1` / `--text-h2` / `--text-h3` / `--text-h4` / `--text-body` / `--text-excerpt` / `--text-caption` / `--text-meta`、`--page-width`、`--page-padding-y`、`--list-gap`、`--section-gap`、`--hairline` 系列。
  - 全局 `h1/h2/h3/h4/h5/h6` 默认值统一指向 token，跨页面同尺寸；`.prose h2/h3/h4` 保留略大的章节阶梯。
- `DESIGN.md`：
  - 第 3 节重写为 **One Site-wide Heading Scale**，列出 H1/H2/H3 + body/excerpt/caption/meta 单一阶梯。
  - 增加 **The One Heading Scale Rule**、**The Single-Column Rule**、**The No-Wrapper-Card Rule**、**Page Skeleton** 通用骨架。
  - Don't 列表新增禁止把页面 H1 放大成 hero-only 尺寸、禁止整页卡片壳。
- `src/pages/index.astro` 完全重写：
  - 单栏垂直流：Hero（H1 + lead + chips）→ 「最新文章」H2 区块（H3 列表）→ 「写作主线」H2 区块（H3 列表）→ 主站注记。
  - 删除 hero `clamp(2rem, 5vw, 3.2rem)`、`.panel h2 { font-size: ... }` 等所有页面级覆盖。
  - 删除 `--home-*` 自定义阶梯，统一改用全站 token。
- `src/pages/blog/index.astro`：宽度对齐 `--page-width`；`.title` 改用全局 H3；卡片化 `.post-item` 改为留白+边框分隔的扁平列表项，跨页面与首页“最新文章”视觉同构。
- `src/pages/themes.astro`：移除 `.group` 卡片壳；改为细分隔线分组；`.group h2` 走全局 H2；条目用 H3 字号。
- `src/pages/about.astro` / `src/pages/now.astro`：去掉 `.about-shell` / `.now-shell` 白底盒子，正文直接展开；增加 H2 二级分组，全部走全局阶梯。
- `src/layouts/BlogPost.astro`：宽度对齐 `--page-width`；H1 不再居中放大；hero 图与日期改为左对齐 header；`.prose` 显式 serif，章节阶梯走 `global.css` 中的 `prose-h2/h3`。

**验证**
- `npx impeccable detect src/` 通过（0 项）
- `npm run build` 通过（11 页）
- 标题一致性人工核对：
  - 首页 H1、文章列表 H1、主题 H1、关于 H1、Now H1、文章详情 H1 → 全部 `clamp(1.875rem, 3.2vw, 2.25rem)`
  - 首页「最新文章」H2、首页「写作主线」H2、主题 `#tag` H2、关于「写作约束」H2、Now「正在做」H2 → 全部 `1.375rem`
  - 首页文章条目 H3、文章列表条目 H3、主题列表项 H3、写作主线条目 H3 → 全部 `1.125rem`

### 结果总结

- 检测问题：由初始 3 项下降到 0 项
- 构建状态：持续 green
- 站点观感升级：
  - **跨页面 H1/H2/H3 视觉完全一致**，扫描页面之间不再产生“跳一下”的不适感
  - 移除首页大字号 hero、移除 about/now 卡片壳，整个站点回到“安静的纸面工作台”形态
  - DESIGN.md 不再描述“首页专属阶梯”，而是描述“站点单一阶梯 + 文章正文的唯一例外”，更易长期维护

### 后续建议（可选）

1. 在 `BaseHead.astro` 增加自定义 og:image，让外链分享视觉与站点同构。
2. 将 `Header.astro` 当前页高亮做为 token，统一与 `--text-meta` 阶梯。
3. 预埋 dark mode token 体系（默认关闭）。

---

## English Version

### Goal

Run a full impeccable-style optimization workflow on the Astro blog, establish a structural quality baseline first, then execute two additional homepage-focused visual iterations (Round 2 and Round 3).

### Baseline

- Framework: Astro static blog
- Deployment: GitHub Pages subpath (`/myblog`)
- Initial pain points:
  - Homepage hierarchy and rhythm felt template-like
  - Detectable anti-pattern and accessibility gaps existed
  - Internal links had subpath deployment risk

### Round 1 (Structural and quality baseline)

**Thinking**
1. Establish stable design context to prevent style drift.
2. Fix correctness and reliability first (routing, RSS, runtime loading).
3. Remove measurable anti-patterns before deeper visual refinement.

**Key changes**
- Added context files:
  - `PRODUCT.md`
  - `DESIGN.md`
- Deployment-safe linking:
  - `src/consts.ts` with `toInternalPath()`
- Runtime and content correctness:
  - Mermaid switched to lazy dynamic loading in `src/layouts/BlogPost.astro`
  - Draft filtering in `src/pages/rss.xml.js`
- Accessibility and baseline UX:
  - global `focus-visible`
  - `prefers-reduced-motion`
  - semantic nav enhancement (`aria-label`)
  - removed side-stripe blockquote anti-pattern

**Validation**
- `npx impeccable detect src/` passed
- `npm run build` passed

### Round 2 (Homepage redesign v1)

**Trigger**
- User feedback indicated the homepage still looked unattractive.

**Thinking**
1. Rebuild first-screen information order for scanability.
2. Reduce visual noise from excessive underline perception.
3. Preserve calm long-form reading tone without over-styling.

**Key changes**
- `src/pages/index.astro`
  - hero hierarchy and spacing refined
  - quick-jump actions added
  - latest posts redesigned into concise editorial cards
- `src/components/Header.astro`
  - centered nav container for stronger structure
- `src/styles/global.css`
  - global and prose link styling tuned

**Validation**
- `npx impeccable detect src/` passed
- `npm run build` passed

### Round 3 (Homepage redesign v2)

**Trigger**
- Continue improving homepage quality beyond Round 2 and remove remaining stacked-component feel.

**Thinking**
1. Introduce stronger content priority with Featured + Brief latest-post layout.
2. Reduce border and visual competition for cleaner scan flow.
3. Upgrade writing-track section from plain bullets to “theme + explanation”.

**Key changes**
- `src/pages/index.astro`
  - latest posts split into:
    - one Featured block (date/series/title/summary)
    - two Brief items (date/series/title)
  - writing tracks upgraded to labeled lines with explanatory text
  - spacing, typography, and hover rhythm refined again

**Validation**
- `npx impeccable detect src/` passed
- `npm run build` passed

### Round 4 (Design-doc-driven homepage, current)

**Trigger**
- Feedback: Round 3 felt unnatural; latest-post area showed multiple dashed segment lines; module font sizes were inconsistent; rules should live in the primary design markdown first.

**Thinking**
1. Add a **Homepage modules** section to `DESIGN.md` with a fixed type scale, structure, and explicit bans (no dashed dividers between list items; same title size for all posts).
2. Mirror that scale in `global.css` as `--home-*` custom properties.
3. Replace Featured + Brief markup with one list, spacing-only separation, first item only shows excerpt.
4. Remove the giant `home-shell` wrapper card and turn the homepage into three natural editorial sections: Hero, lightweight homepage note, and content grid.
5. Align aside note and writing-track typography to the same scale.

**Key changes**
- `DESIGN.md`: Homepage modules, No-Segmented-Rule, One-Card-Accent, extended Don't list
- `src/styles/global.css`: `--home-*` tokens including page width, section gap, hairline, and soft surface values
- `src/pages/index.astro`: rebuilt to consume tokens; removed dashed borders and replaced the whole-page card with a sectional editorial layout

**Validation**
- `npx impeccable detect src/` passed
- `npm run build` passed

### Outcome summary

- Detector findings: reduced from 3 to 0
- Build status: consistently green
- Homepage quality improvements:
  - clearer first-screen hierarchy with less large-card template feel
  - better reading-entry prioritization
  - less template-like visual language
  - stronger alignment with Chinese long-form blog intent

### Optional next steps

1. Run two hero variants (analytic vs narrative) and pick one by review.
2. Further tune mobile first-fold density.
3. Add dark-mode token architecture (disabled by default).
