# TagAI 文档

内容由 [GitBook：TagAI](https://coincidence-labs.gitbook.io/tagai) 导出为 Markdown，使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 构建，经 GitHub Actions 发布到 **GitHub Pages**。

## 本地预览

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

浏览器打开 <http://127.0.0.1:8000/>。

## 从 GitBook 同步更新正文

若 GitBook 上仍有改动，可拉取最新 `.md`（会覆盖 `docs/` 中对应文件）：

```bash
python3 scripts/fetch_gitbook.py
```

**注意：** 重新拉取后，若 GitBook 仍使用旧的 `/tagai/...` 绝对链接，你可能需要再次把站内链接改成相对路径。文档已改为**中文目录与文件名**；站点根路径仍为 `docs/index.md`，通过片段引用包含 `TagAI是什么.md`，改首页请编辑后者。

## GitHub Pages 与 Actions

1. 将本仓库推送到 GitHub（默认分支为 `main`）。
2. 打开仓库 **Settings → Pages**，**Build and deployment** 的 **Source** 选 **Deploy from a branch**，**Branch** 选 **`gh-pages`** / **`/(root)`**。  
   （首次推送前没有该分支：推送 `main` 后，工作流会创建 `gh-pages`。）
3. 推送 `main` 会触发 [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml)：安装依赖、`mkdocs build` 后将 `site/` 发布到 `gh-pages`。

线上地址（与 `mkdocs.yml` 中 `site_url` 一致）：<https://tagai-dao.github.io/TagAI-doc/>

若仓库名或组织变更，请同步修改 `mkdocs.yml` 里的 `site_url`、`repo_url`、`edit_uri`。

## 目录说明

| 路径 | 说明 |
|------|------|
| `docs/` | 文档源 Markdown（含从 GitBook 导出的图片外链） |
| `mkdocs.yml` | 站点配置与侧栏 `nav` |
| `scripts/fetch_gitbook.py` | 从 GitBook 拉取 `.md` 的脚本 |
