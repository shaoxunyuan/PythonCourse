# 环境准备

## 你需要安装什么

建议准备：

1. Python 3.10 或以上版本
2. 代码编辑器（推荐 VS Code / Cursor）
3. 能在终端运行 `python`、`pip`

## 克隆课程仓库

将本课程仓库克隆到本地后，可以：

- 阅读 `docs/` 中的实验说明（也可用网站在线阅读）
- 使用 `data/` 中的课程数据完成实验

## 本地预览课程网站（可选）

如果你想在本地预览本站：

```bash
pip install -r requirements.txt
mkdocs serve
```

浏览器打开终端提示的地址即可。

> 注意：`requirements.txt` 主要用于网站构建（MkDocs）。学生实验项目所需的第三方包，会在后续各次实验中单独说明，请勿与网站依赖混为一谈。

## 数据路径约定

本地运行示例代码时，建议从仓库根目录读取数据，例如：

```python
data_path = "data/diabetic_data.csv"
```

## API Key 提醒（后续实验）

后续涉及大模型 API 时：

- 不要把真实密钥写进公开代码
- 使用环境变量或 `.env`
- 示例中请使用 `YOUR_API_KEY` 或 `os.getenv("API_KEY")`
