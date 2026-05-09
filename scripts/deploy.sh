#!/usr/bin/env bash
# 本地一键部署：在 blog 仓库根目录执行构建，可选提交并 push 以触发 GitHub Pages。
# 用法见下方 print_usage。

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

REMOTE="${DEPLOY_REMOTE:-origin}"
BRANCH="${DEPLOY_BRANCH:-main}"
DRY_RUN=0
NO_PUSH=0
BUILD_ONLY=0
COMMIT_MSG=""

print_usage() {
	cat <<'EOF'
用法:
  ./scripts/deploy.sh --build-only          仅 npm run build，不执行 git
  ./scripts/deploy.sh "提交说明"            构建后 git commit + push（默认 origin main）
  ./scripts/deploy.sh -m "提交说明"         同上
  ./scripts/deploy.sh --dry-run -m "说明"  只打印将要执行的步骤后退出（不修改仓库）
  ./scripts/deploy.sh -m "说明" --no-push  提交但不 push

环境变量（可选）:
  DEPLOY_REMOTE   默认 origin
  DEPLOY_BRANCH   默认 main

说明:
  - 会执行 npm run build；失败则中止，不会提交。
  - 暂存范围: git add -u（已跟踪文件的修改/删除）+ git add src/（含未跟踪的 src 下新文件）。
  - 不会自动 git add 仓库根下其它未跟踪目录（如 .agents/、.claude/）。
EOF
}

while [[ $# -gt 0 ]]; do
	case "$1" in
		-h | --help)
			print_usage
			exit 0
			;;
		--dry-run)
			DRY_RUN=1
			shift
			;;
		--no-push)
			NO_PUSH=1
			shift
			;;
		--build-only)
			BUILD_ONLY=1
			shift
			;;
		-m | --message)
			if [[ $# -lt 2 ]]; then
				echo "错误: $1 需要紧跟提交说明。" >&2
				exit 1
			fi
			COMMIT_MSG="$2"
			shift 2
			;;
		--)
			shift
			if [[ $# -gt 0 ]]; then
				COMMIT_MSG="$*"
				break
			fi
			;;
		-*)
			echo "未知参数: $1" >&2
			print_usage >&2
			exit 1
			;;
		*)
			if [[ -n "$COMMIT_MSG" ]]; then
				echo "错误: 多余的参数: $*" >&2
				exit 1
			fi
			COMMIT_MSG="$1"
			shift
			;;
	esac
done

require_git_repo() {
	if ! git rev-parse --git-dir >/dev/null 2>&1; then
		echo "错误: 当前目录不是 git 仓库: $ROOT" >&2
		exit 1
	fi
}

if [[ "$DRY_RUN" -eq 1 ]]; then
	if [[ "$BUILD_ONLY" -eq 1 ]]; then
		echo "[dry-run] npm run build"
		exit 0
	fi
	require_git_repo
	if [[ -z "$COMMIT_MSG" ]]; then
		echo "错误: --dry-run 部署预览也需要 -m 提交说明（或改用 --build-only）。" >&2
		exit 1
	fi
	echo "[dry-run] npm run build"
	echo "[dry-run] git add -u && git add -- src/"
	echo "[dry-run] git commit -m $(printf '%q' "$COMMIT_MSG")  # 仅当有暂存变更时"
	if [[ "$NO_PUSH" -eq 1 ]]; then
		echo "[dry-run] (跳过 git push: 已指定 --no-push)"
	else
		echo "[dry-run] git push $(printf '%q' "$REMOTE") $(printf '%q' "$BRANCH")"
	fi
	exit 0
fi

if [[ "$BUILD_ONLY" -eq 1 ]]; then
	npm run build
	echo "完成: 仅构建（--build-only）。"
	exit 0
fi

require_git_repo

if [[ -z "$COMMIT_MSG" ]]; then
	echo "错误: 部署到远端需要提供提交说明。" >&2
	echo "示例: ./scripts/deploy.sh -m \"chore: deploy\"" >&2
	echo "或仅构建: ./scripts/deploy.sh --build-only" >&2
	exit 1
fi

npm run build

git add -u
if [[ -d "$ROOT/src" ]]; then
	git add -- src/
fi

if ! git diff --cached --quiet; then
	git commit -m "$COMMIT_MSG"
else
	echo "提示: 没有需要提交的变更（工作区与上次提交一致），跳过 commit。"
fi

if [[ "$NO_PUSH" -eq 1 ]]; then
	echo "完成: 已按 --no-push 跳过 push。"
	exit 0
fi

git push "$REMOTE" "$BRANCH"
echo "完成: 已 push 到 $REMOTE/$BRANCH。GitHub Actions 部署完成后见: https://shiml20.github.io/myblog/"
