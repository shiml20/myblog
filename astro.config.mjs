// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import rehypeKatex from 'rehype-katex';
import remarkMath from 'remark-math';
import { defineConfig } from 'astro/config';

// https://astro.build/config
const isProduction = process.env.NODE_ENV === 'production';

export default defineConfig({
	site: 'https://shiml20.github.io',
	base: isProduction ? '/myblog' : '/',
	integrations: [mdx(), sitemap()],
	markdown: {
		remarkPlugins: [remarkMath],
		rehypePlugins: [rehypeKatex],
	},
});
