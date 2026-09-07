# Python 基本应用实验教程

《Python 基本应用》课程的在线实验教程网站。

## 网站技术栈

```text
GitHub Repository
        ↓
Markdown 课程内容
        ↓
MkDocs Material
        ↓
自动生成 HTML
        ↓
GitHub Actions
        ↓
GitHub Pages
```

学生通过浏览器访问课程网站，阅读知识点、示例代码、实验要求与作业题目。

## 本站提供什么

1. 课程知识点
2. 教师讲授内容
3. 示例代码
4. 实验要求与题目
5. 课后作业题目
6. 实验数据说明与数据下载入口

## 本站不提供什么

1. 学生答案填写
2. 在线作业提交
3. 文件上传
4. 在线评分
5. 作业批改

**所有作业和实验结果统一提交到「雨课堂」。**

## 本地预览

```bash
pip install -r requirements.txt
mkdocs serve
```

浏览器打开提示的本地地址即可预览。正式提交前建议执行：

```bash
mkdocs build
```

## 目录结构

```text
PythonCourse/
├── README.md
├── mkdocs.yml
├── requirements.txt
├── .gitignore
├── data/                  # 课程原始数据（勿重复复制到 docs/assets）
├── docs/                  # Markdown 课程内容
│   ├── index.md
│   ├── sop0-data.md
│   ├── guide/
│   ├── labs/
│   ├── project/
│   └── assets/
└── .github/workflows/     # GitHub Pages 自动部署
```

## 部署说明

1. 将本仓库推送到 GitHub
2. 修改 `mkdocs.yml` 中的 `repo_url` 与 `site_url` 为实际地址
3. 仓库 Settings → Pages → Build and deployment → Source → **GitHub Actions**
4. 推送到 `main` / `master` 后，Actions 会自动构建并发布

## 数据说明

课程使用 `data/` 目录中的真实住院记录数据（`diabetic_data.csv` 与 `IDS_mapping.csv`）作为贯穿全学期的项目主线。

本数据仅用于 Python 编程、数据处理和软件开发教学，不用于临床诊断或真实医疗活动。

## 安全提醒

- 禁止将真实 API Key、Token、Secret 写入公开代码
- 使用环境变量或 `.env`（已在 `.gitignore` 中忽略）
- 公开示例请使用 `YOUR_API_KEY` 或 `os.getenv("API_KEY")`
