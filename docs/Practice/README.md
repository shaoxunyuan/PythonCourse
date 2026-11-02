# Practice 调整说明（12 次实验 → 13 次实验）

更新时间：2026-11-02  
仓库：https://github.com/shaoxunyuan/PythonCourse  
站点：https://shaoxunyuan.github.io/PythonCourse/Practice/

## 1. 目标摘要

在保持原有 Practice 版式（侧栏目录、练习 / 任务 / 实验结果与作业）的前提下，将实验序列扩展为 **13 次**，并重新划分实验 11–13 的职责：

- 实验 11：网页 HTML 解析（`requests` + Beautiful Soup，统一站点 books.toscrape.com）
- 实验 12：结构化 HTTP API 与大模型调用（与实验 11 明确区分，无付费 Key 可完成基础练习）
- 实验 13：Streamlit 综合项目（由原实验 12 迁移并扩充）

实验 1–6 **内容未改**（仅补齐上一节 / 下一节页脚导航）。

## 2. 实验目录对应关系

| 编号 | 标题 | 主 URL（保留优先） | 说明 |
|------|------|-------------------|------|
| SOP0 | 认识课程数据 | `sop00-dataset.html` | 不变 |
| 1 | Python语法元素、基本数据类型与表达式 | `sop01-syntax.html` | 内容不变 |
| 2 | 组合数据类型 | `sop02-structures.html` | 内容不变 |
| 3 | 程序控制结构 | `sop03-control.html` | 内容不变 |
| 4 | 程序设计基本方法 | `sop04-design.html` | 内容不变 |
| 5 | 函数、参数与模块化 | `sop05-functions.html` | 内容不变 |
| 6 | Python 文件与数据格式化 | `sop06-file-formatting.html` | 内容不变 |
| 7 | Python异常处理与数据校验 | `sop07-files.html` | **保留 URL**；标题与定位对齐异常/校验 |
| 8 | NumPy数组与数值计算 | `sop08-numpy.html` | 保留 |
| 9 | pandas数据处理与分析 | `sop09-pandas.html` | **保留 URL**；标题改为“处理与分析”（仍为一次实验） |
| 10 | Matplotlib数据可视化 | `sop10-matplotlib.html` | 保留 |
| 11 | Python网络请求与网页解析 | `sop11-web.html` | **新建** |
| 12 | Python API与大模型调用 | `sop12-api.html` | **新建**（承接原“API/大模型”主题） |
| 13 | Python综合项目与Streamlit Web应用 | `sop13-platform.html` | **新建**（承接原实验 12） |

### 旧链接兼容（重定向）

| 旧路径 | 现指向 |
|--------|--------|
| `sop11-api.html` | `sop12-api.html` |
| `sop12-platform.html` | `sop13-platform.html` |
| `sop10-api.html` | `sop12-api.html` |
| `sop11-platform.html` | `sop13-platform.html` |
| `sop08-pandas-clean.html` | `sop09-pandas.html`（原有） |
| `sop09-analysis.html` | `sop10-matplotlib.html`（原有） |
| `sop06-dynamic.html` | （原有动态页，未改用途） |

## 3. 主要变动文件

### Practice

- 更新：`index.html`（目录扩至 13 次）
- 更新：`sop07-files.html` … `sop10-matplotlib.html`（标题/导语/页脚导航）
- 新增：`sop11-web.html`、`sop12-api.html`、`sop13-platform.html`
- 更新重定向：`sop11-api.html`、`sop12-platform.html`、`sop10-api.html`、`sop11-platform.html`
- 页脚导航：`sop00`–`sop13` 均补充「上一节 / 下一节」
- 本说明：`docs/Practice/README.md`

### Presentations（目录对齐）

- 更新：`docs/Presentations/index.html`（13 项）
- 新增：`11-web.html`（占位，指向 Practice 实验 11）
- 复制对齐：`12-api.html`（自原 `11-api.html`）、`13-platform.html`（自原 `12-platform.html`）
- 原 `11-api.html` / `12-platform.html` 文件仍保留，避免旧书签失效

### 其他

- 生成脚本：`scripts/build_labs_11_13.py`（可复现 11–13 页骨架）
- 根目录 `README.md`：补充 Practice 13 次实验入口说明

## 4. 各实验内容要点（7–13）

1. **实验7**：`try/except/else/finally`、`raise`、校验函数、CSV 有效/错误分流  
2. **实验8**：`ndarray`、索引切片、向量化、布尔索引、按轴统计  
3. **实验9**：读表、清洗、缺失/重复、筛选、`groupby`（不拆两次）  
4. **实验10**：折线 / 柱状 / 散点 / 直方 + 标注保存  
5. **实验11**：获取 → BS4 解析 → 字段提取 → 筛选 → 分页 → 详情页 → CSV；站点固定为 books.toscrape.com  
6. **实验12**：GET/POST、JSON、超时与状态码、环境变量 API Key、大模型消息结构与**模拟调用**  
7. **实验13**：Streamlit 上传/默认数据、预览、筛选、统计、两图、下载、`requirements.txt` + README

## 5. 构建与验证结果

本站为静态 GitHub Pages（`docs/` 直出），无单独前端构建步骤。验证于本地完成：

| 检查项 | 结果 |
|--------|------|
| 实验 1–13 主文件存在 | 通过 |
| Practice 内部相对链接（`a[href]`） | 抽查通过，**无失效相对路径** |
| `index.html` 含 sop11-web / sop12-api / sop13-platform | 通过 |
| 页脚导航链 6→7→…→13 | 通过 |
| books.toscrape.com 示例抓取（20 个 `product_pod`） | 通过（需代理/外网时） |
| 示例代码依赖 | 11：`requests`+`beautifulsoup4`；12：`requests`；8–10/13：`numpy`/`pandas`/`matplotlib`/`streamlit`（按页说明安装） |

部署：推送 `main` 后由 `.github/workflows/deploy.yml` 发布 GitHub Pages。

## 6. 遗留问题

1. **Presentations 实验11**（`11-web.html`）目前为占位页，完整演示文稿待后续补齐；Practice 实验页已完整。  
2. **Presentations 12/13** 由旧 11/12 文稿复制对齐编号，讲稿标题可能仍带旧“实验序号”字样，需人工润色。  
3. 部分教室网络无法直连 books.toscrape.com / jsonplaceholder 时，需按页面说明改用**本地保存的 HTML/JSON** 降级完成练习。  
4. `requests` 抓取英镑符号时建议设置 `resp.encoding = "utf-8"`（实验11首页示例已注明）。  
5. 根目录课程建设 SOP md 已不在仓库内；本 README 作为本次结构调整的追溯文档。

## 7. 建议验收清单

- [ ] 打开 Practice 首页，侧栏可见实验 1–13  
- [ ] 依次打开实验 7–13，确认三大部分与可运行代码块齐全  
- [ ] 访问旧 URL `Practice/sop11-api.html` 应跳到实验12  
- [ ] 访问旧 URL `Practice/sop12-platform.html` 应跳到实验13  
- [ ] 实验1–6正文与改版前一致（仅页脚导航可能新增）
