// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = '熵减心流';
/** 顶栏首页链接展示名（用于无障碍与 title 提示） */
export const SITE_HEADER_MARK = 'Minglei Shi';
export const SITE_DESCRIPTION =
	'记录 AI 时代个人工作流、心流状态与生产关系的长期写作与实践。';
export const SITE_MAIN_URL = 'https://shiml20.github.io/';

/** 更换 `public/favicon.svg` 时递增，避免浏览器长期缓存旧图标 */
export const FAVICON_VERSION = '2';

const baseUrl = import.meta.env.BASE_URL ?? '/';

export function toInternalPath(path = '/'): string {
	const cleanBase = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
	const cleanPath = path.replace(/^\/+/, '');
	return cleanPath ? `${cleanBase}${cleanPath}` : cleanBase;
}