# SOP0：认识我们的课程数据

本页不是正式 Python 实验，而是整个学期项目的数据背景介绍。

开始第一次正式实验之前，你需要清楚：

1. 我们整个学期在处理什么数据
2. 数据有多大
3. 一行代表什么
4. 数据大概包含什么
5. 后续为什么可以一直用这一份数据学习 Python

---

## 0.1 数据文件

课程使用的数据存放在仓库的 `data/` 目录：

| 文件 | 说明 |
|------|------|
| [diabetic_data.csv](https://github.com/YOUR_USERNAME/PythonCourse/blob/main/data/diabetic_data.csv) | 主数据：住院记录 |
| [IDS_mapping.csv](https://github.com/YOUR_USERNAME/PythonCourse/blob/main/data/IDS_mapping.csv) | 辅助编码说明 |

> 推送到 GitHub 后，请将上方链接中的 `YOUR_USERNAME` 替换为实际仓库用户名；或直接在仓库 `data/` 目录下载。

---

## 0.2 diabetic_data.csv 数据维度

实际数据维度：

**101,766 行 × 50 列**

也就是：

- 101,766 条住院记录
- 50 个字段

其中：

- 不同 `patient_nbr` 数量为 **71,518**

因此必须明确：

> **101,766 行并不代表 101,766 名患者。**

这个数据中的一行表示：

**一次住院记录（encounter）**

而不是：

**一名唯一患者**

同一名患者可能发生多次住院：

| 字段 | 含义 |
|------|------|
| `patient_nbr` | 患者编号 |
| `encounter_id` | 一次具体住院记录编号 |

数据关系可以简单表示为：

```text
患者 patient_nbr
        ↓
可能存在多次住院
        ↓
encounter_id 1
encounter_id 2
encounter_id 3
……
```

---

## 0.3 数据主要包含什么

50 个字段大致可以分为以下类型：

### A. 患者基本信息

例如：`race`、`gender`、`age`

### B. 入院相关信息

例如：`admission_type_id`、`discharge_disposition_id`、`admission_source_id`、`time_in_hospital`

### C. 医疗过程相关数据

例如：`num_lab_procedures`、`num_procedures`、`num_medications`、`number_outpatient`、`number_emergency`、`number_inpatient`

### D. 诊断信息

例如：`diag_1`、`diag_2`、`diag_3`

### E. 检验相关信息

例如：`max_glu_serum`、`A1Cresult`

### F. 糖尿病相关药物信息

例如：`metformin`、`glipizide`、`glyburide`、`pioglitazone`、`insulin` 等

### G. 治疗变化信息

例如：`change`、`diabetesMed`

### H. 再入院信息

字段：`readmitted`

主要取值：

| 取值 | 含义（教学理解） | 实际条数 |
|------|------------------|----------|
| `NO` | 未再入院 | 54,864 |
| `>30` | 超过 30 天后再入院 | 35,545 |
| `<30` | 30 天内再入院 | 11,357 |

本课程**不以机器学习预测为主要教学目标**。

`readmitted` 主要作为一个真实的分类字段，用于练习：

- 条件判断
- 数据筛选
- 循环
- 函数
- 统计
- 分组
- 数据可视化
- 文件输出
- 综合数据分析

---

## 0.4 IDS_mapping.csv

`IDS_mapping.csv` 是辅助编码说明文件。

实际维度：**67 行数据 × 2 列**（另含表头）

它主要用于解释 `diabetic_data.csv` 中部分数字编码字段，例如：

- `admission_type_id`
- `discharge_disposition_id`
- `admission_source_id`

这些字段在原始数据中使用数字编码。例如：

```text
admission_type_id = 1
```

通过 `IDS_mapping.csv` 可以知道：

```text
1 = Emergency
```

因此这个文件可以用于后续课程练习：

- 字典
- 映射
- 文件读取
- 数据关联
- 数据转换
- merge
- 数据解释

---

## 0.5 这份数据在课程中有什么用

这份数据不是为了让你学习医学诊断，也不是为了训练一个复杂机器学习模型。

它主要作为整个 Python 课程的一条统一数据主线。

课程将从少量病例开始，逐渐过渡到完整的 101,766 条真实记录：

```text
一条病例
    ↓
多条病例
    ↓
列表和字典
    ↓
条件判断
    ↓
循环处理
    ↓
函数封装
    ↓
动态规则
    ↓
CSV / JSON / TXT
    ↓
完整真实数据
    ↓
数据清洗
    ↓
pandas
    ↓
数据统计与可视化
    ↓
大模型 API
    ↓
自动生成分析摘要
    ↓
Web 平台
    ↓
在线部署
```

因此，这份数据主要用于覆盖：

Python 语法元素、数据类型、列表与字典、程序控制结构、函数、动态函数、文件处理、CSV、JSON、数据格式化、异常处理、综合数据处理、pandas、可视化、HTTP、API、JSON 网络通信、大模型 API、Web 应用、平台部署。

!!! warning "教学用途声明"
    本数据仅用于 Python 编程、数据处理和软件开发教学。

    课程中的病例筛选规则、统计结果以及大模型生成内容，均不用于临床诊断、治疗决策或真实医疗活动。

---

下一步：阅读 [数据使用说明](guide/dataset.md)，然后进入 [实验教程](labs/sop01.md)。
