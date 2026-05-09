# 熵减心流 · 博客

基于 [Astro](https://astro.build/) 的静态个人站点：中文长文、RSS、sitemap、MDX、Mermaid 与数学公式（KaTeX）。线上部署在 **GitHub Pages**：<https://shiml20.github.io/myblog/>（生产环境 `base` 为 `/myblog`，见 `astro.config.mjs`）。

## 本地开发

需要 **Node.js ≥ 22.12**（见 `package.json` 的 `engines`）。

```sh
npm install
npm run dev
```

开发地址默认为 `http://localhost:4321`。

| 命令 | 说明 |
|------|------|
| `npm run dev` | 本地开发 |
| `npm run build` | 构建到 `dist/` |
| `npm run preview` | 本地预览生产构建 |

## 部署

仓库推送到 `main` 后由 GitHub Actions 发布。也可在仓库根目录使用脚本（会先 `build`、再提交并 push）：

```sh
./scripts/deploy.sh -m "chore: 更新首页"
```

常用选项：`--build-only` 只构建不提交；`--dry-run` 打印将执行的命令；`--no-push` 只提交不推送。详见脚本内注释。

## 目录结构（摘要）

```text
public/          # 静态资源（favicon 等）
src/
  components/    # Header、Footer、BaseHead 等
  content/blog/    # 文章 Markdown / MDX
  layouts/         # 文章页布局
  pages/           # 路由（含首页 index.astro）
  styles/          # 全局样式与设计 token
scripts/deploy.sh
DESIGN.md / PRODUCT.md   # 设计与产品说明（维护站点时可参考）
```

## 设计说明

视觉与排版约定写在 **`DESIGN.md`**；站点定位与内容方向写在 **`PRODUCT.md`**。

## 许可与致谢

初版由 Astro Blog 模板演进而来；主题气质与 Bear Blog 一脉相承。具体许可以仓库内 LICENSE 为准（若未添加可自行补充）。
