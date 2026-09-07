南京中医药大学人工智能与信息技术学院

# Python 高级应用

[![COURSE WEBSITE](https://img.shields.io/static/v1?style=flat-square&label=COURSE%20WEBSITE&message=LIVE&color=00c853&labelColor=333333&logo=github&logoColor=white)](https://shaoxunyuan.github.io/PythonCourse/)
[![TUTORIAL](https://img.shields.io/static/v1?style=flat-square&label=TUTORIAL&message=LABS&color=008b8b&labelColor=333333)](https://shaoxunyuan.github.io/PythonCourse/labs/)
[![DATASET](https://img.shields.io/static/v1?style=flat-square&label=DATASET&message=SOP0&color=ff9800&labelColor=333333)](https://shaoxunyuan.github.io/PythonCourse/sop0-data/)

> **教程入口：** 点击 [TUTORIAL](https://shaoxunyuan.github.io/PythonCourse/labs/) 先进入实验目录，再点击对应实验开始练习。

## 教程页面

| 入口 | 链接 |
|------|------|
| **实验教程目录（推荐）** | [https://shaoxunyuan.github.io/PythonCourse/labs/](https://shaoxunyuan.github.io/PythonCourse/labs/) |
| 课程网站首页 | [https://shaoxunyuan.github.io/PythonCourse/](https://shaoxunyuan.github.io/PythonCourse/) |
| 认识课程数据 | [SOP0](https://shaoxunyuan.github.io/PythonCourse/sop0-data/) |
| 课程说明 | [课程介绍](https://shaoxunyuan.github.io/PythonCourse/guide/course/) |
| 综合项目 | [项目说明](https://shaoxunyuan.github.io/PythonCourse/project/overview/) |
| 原始数据下载 | [`data/`](data/) |

## 课程简介

本课程围绕一份真实住院记录数据，学习 Python 高级应用相关能力：数据处理、文件读写、pandas、可视化、大模型 API、Web 应用与在线部署。

整个学期将逐步建设一个「Python 数据分析与智能报告平台」。

**作业统一通过雨课堂提交。** 本仓库与课程网站只提供题目、要求、数据和教学内容，不接收在线提交。

## 课程数据概况

课程数据存放在 [`data/`](data/) 目录：

| 文件 | 说明 |
|------|------|
| [`diabetic_data.csv`](data/diabetic_data.csv) | 主数据：住院记录 |
| [`IDS_mapping.csv`](data/IDS_mapping.csv) | 辅助编码说明 |

**`diabetic_data.csv`**

- 规模：**101,766 行 × 50 列**
- 不同患者编号（`patient_nbr`）：**71,518**
- 一行表示一次住院记录（`encounter`），不是一名唯一患者
- 同一患者可能有多次住院（`encounter_id`）

**`readmitted` 字段分布（教学用分类字段）**

| 取值 | 条数 |
|------|------|
| `NO` | 54,864 |
| `>30` | 35,545 |
| `<30` | 11,357 |

更完整说明请进入教程页：

➡️ [SOP0：认识我们的课程数据](https://shaoxunyuan.github.io/PythonCourse/sop0-data/)

## 学习路径

```text
一条病例
  → 多条病例 / 列表与字典
  → 条件判断 / 循环 / 函数
  → CSV / JSON / 文件处理
  → 完整真实数据与清洗
  → pandas 与可视化
  → 大模型 API 生成摘要
  → Web 平台与在线部署
```

## 重要声明

本数据仅用于 Python 编程、数据处理和软件开发教学。

课程中的病例筛选规则、统计结果以及大模型生成内容，均不用于临床诊断、治疗决策或真实医疗活动。
