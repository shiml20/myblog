# Blog Homepage Optimization Report (2026-05-09)

## Goal

Deliver a full-pass optimization for the Astro blog with impeccable-style quality gates, then iterate a second round focused on homepage aesthetics after visual feedback.

## Baseline

- Framework: Astro static blog
- Deployment: GitHub Pages subpath (`/myblog`)
- Initial pain points:
  - Homepage visual hierarchy felt heavy and generic
  - Some anti-patterns and accessibility details missing
  - Internal links carried deployment path risk

## Round 1

### Thinking

Round 1 prioritized structural quality before visual flourish:

1. Stabilize the system context so design decisions remain consistent over time.
2. Fix deployment and content correctness issues that can break UX.
3. Resolve measurable anti-patterns from detector feedback.
4. Improve typography and interaction states to prepare for deeper visual refinement.

### Changes

- Added design context files:
  - `PRODUCT.md`
  - `DESIGN.md`
- Fixed subpath-safe internal routing:
  - `src/consts.ts` (`toInternalPath()`)
  - applied to nav and content links
- Improved runtime behavior:
  - Mermaid switched to lazy dynamic import in `src/layouts/BlogPost.astro`
  - RSS now excludes draft posts in `src/pages/rss.xml.js`
- Accessibility and interaction updates:
  - global focus-visible treatment
  - reduced-motion support
  - improved nav semantics (`aria-label`)
- Visual cleanup:
  - removed side-stripe blockquote anti-pattern
  - adjusted typography hierarchy and card readability on list pages
  - refined about/now pages into structured content panels

### Validation

- `npx impeccable detect src/` passed after fixes
- `npm run build` passed

## Round 2 (Homepage redesign)

### Trigger

User feedback: homepage still looked unattractive and not aligned with expected quality.

### Thinking

Round 2 focused on homepage experience quality:

1. Rebuild first-screen information order for scanability.
2. Reduce visual noise (especially link underline fatigue).
3. Improve editorial rhythm while keeping the brand restrained.
4. Keep compatibility with the Round 1 design system and deployment constraints.

### Changes

- Homepage rebuilt in `src/pages/index.astro`:
  - tightened hero spacing and hierarchy
  - added quick-jump chips (`读最新文章 / 按主题浏览 / 查看最近进展`)
  - redesigned latest posts as concise editorial cards
  - refined side profile card tone and typography
- Header container polish in `src/components/Header.astro`:
  - centered nav container with max width
  - improved hover/active polish and mobile spacing
- Global typography/link tuning in `src/styles/global.css`:
  - wider reading container
  - reduced visual harshness of underlines
  - better prose link behavior and consistency

### Validation

- `npx impeccable detect src/` passed
- `npm run build` passed

## Results summary

- Detector issues: from 3 findings to 0
- Build status: green
- Homepage quality:
  - stronger visual hierarchy
  - cleaner scan path
  - less generic AI-looking styling
  - better consistency with Chinese long-form reading intent

## Remaining optional improvements

1. Add hero variant A/B exploration with browser snapshots.
2. Tune mobile first-screen density (title and card fold behavior).
3. Add dark-mode token architecture (disabled by default, design-ready).
