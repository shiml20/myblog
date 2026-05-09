// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = '思维生产线';
export const SITE_DESCRIPTION = '记录 AI 时代个人工作流、生产力与生产关系的长期思考。';
export const SITE_MAIN_URL = 'https://shiml20.github.io/';

const baseUrl = import.meta.env.BASE_URL ?? '/';

export function toInternalPath(path = '/'): string {
	const cleanBase = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
	const cleanPath = path.replace(/^\/+/, '');
	return cleanPath ? `${cleanBase}${cleanPath}` : cleanBase;
}
