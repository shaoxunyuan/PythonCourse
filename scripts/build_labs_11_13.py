#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Practice labs 11–13 and update index / redirects."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "docs/Practice"

COMMON_HEAD = '''  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css" crossorigin="anonymous" referrerpolicy="no-referrer">'''

COMMON_SCRIPTS = r'''
  <script>
    (function () {
      document.querySelectorAll('pre > code').forEach((code) => {
        const pre = code.parentElement;
        if (!pre || pre.querySelector('.copy-btn')) return;
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.type = 'button';
        btn.textContent = '复制';
        btn.addEventListener('click', async () => {
          try {
            await navigator.clipboard.writeText(code.innerText);
            btn.dataset.state = 'ok';
            btn.textContent = '已复制';
            setTimeout(() => { delete btn.dataset.state; btn.textContent = '复制'; }, 1200);
          } catch (e) {
            const range = document.createRange();
            range.selectNodeContents(code);
            const sel = window.getSelection();
            sel.removeAllRanges();
            sel.addRange(range);
            btn.textContent = '请 Ctrl+C';
            setTimeout(() => { btn.textContent = '复制'; }, 1200);
          }
        });
        pre.appendChild(btn);
      });
    })();
  </script>
  <script>
    (function () {
      const links = Array.from(document.querySelectorAll('.toc a[href^="#"]'));
      const idToLink = new Map();
      links.forEach((a) => {
        const id = decodeURIComponent(a.getAttribute('href').slice(1));
        if (id) idToLink.set(id, a);
      });
      const headings = Array.from(document.querySelectorAll('h2[id], h3[id], section[id]'))
        .filter((h) => idToLink.has(h.id));
      if (headings.length === 0) return;
      const clear = () => links.forEach((a) => a.classList.remove('is-active'));
      const setActive = (id) => { clear(); const a = idToLink.get(id); if (a) a.classList.add('is-active'); };
      const initial = (location.hash && location.hash.slice(1)) || headings[0].id;
      setActive(decodeURIComponent(initial));
      const obs = new IntersectionObserver((entries) => {
        const visible = entries.filter((e) => e.isIntersecting).sort((a, b) => (a.boundingClientRect.top - b.boundingClientRect.top));
        if (visible.length > 0) setActive(visible[0].target.id);
      }, { rootMargin: '-15% 0px -75% 0px', threshold: [0, 1] });
      headings.forEach((h) => obs.observe(h));
    })();
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <script>hljs.highlightAll();</script>
  <script src="./split.js"></script>
'''

LABS = [
    ("sop00-dataset.html", "SOP0：认识课程数据"),
    ("sop01-syntax.html", "实验1：Python语法元素、基本数据类型与表达式"),
    ("sop02-structures.html", "实验2：组合数据类型"),
    ("sop03-control.html", "实验3：程序控制结构"),
    ("sop04-design.html", "实验4：程序设计基本方法"),
    ("sop05-functions.html", "实验5：函数、参数与模块化"),
    ("sop06-file-formatting.html", "实验6：Python 文件与数据格式化"),
    ("sop07-files.html", "实验7：Python异常处理与数据校验"),
    ("sop08-numpy.html", "实验8：NumPy数组与数值计算"),
    ("sop09-pandas.html", "实验9：pandas数据处理与分析"),
    ("sop10-matplotlib.html", "实验10：Matplotlib数据可视化"),
    ("sop11-web.html", "实验11：Python网络请求与网页解析"),
    ("sop12-api.html", "实验12：Python API与大模型调用"),
    ("sop13-platform.html", "实验13：Python综合项目与Streamlit Web应用"),
]


def pager(file):
    idx = next(i for i, x in enumerate(LABS) if x[0] == file)
    prev = LABS[idx - 1] if idx > 0 else None
    nxt = LABS[idx + 1] if idx + 1 < len(LABS) else None
    parts = []
    if prev:
        parts.append(f'上一节：<a href="{prev[0]}">{escape(prev[1])}</a>')
    if nxt:
        parts.append(f'下一节：<a href="{nxt[0]}">{escape(nxt[1])}</a>')
    return '<p class="practice-footer-note">' + "　|　".join(parts) + "</p>"


def code(py):
    return f'<pre><code class="language-python">{escape(py)}</code></pre>'


def p(t):
    return f'<p style="margin: 0 0 10px; color: var(--ink-light);">{t}</p>'


def p_gap(t):
    return f'<p style="margin: 16px 0 10px; color: var(--ink-light);">{t}</p>'


def step(t):
    return f'<div class="step-label">{t}</div>'


def check(t):
    return f'<div class="check-point"><strong>检查点：</strong>{t}</div>'


def callout(t):
    return f'<div class="book-callout">{t}</div>'


def tasks(items):
    return "<ul class=\"tasks\">\n" + "\n".join(f"            <li>{i}</li>" for i in items) + "\n          </ul>"


def page(title, crumb, lead, goal, stage, method, toc_items, body, filename):
    toc_html = []
    for href, label, children in toc_items:
        kids = "\n".join(
            f'              <a href="{h}"><span class="n">{n}</span>{t}</a>' for h, n, t in children
        )
        toc_html.append(
            f"""          <li>
            <a class="lv1" href="{href}">{label}</a>
            <div class="lv2">
{kids}
            </div>
          </li>"""
        )
    toc = "\n".join(toc_html)
    foot = pager(filename)
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
  <link rel="stylesheet" href="./practice.css">
{COMMON_HEAD}
</head>
<body>
  <div class="book-shell practice-page">
    <aside class="book-sidebar" aria-label="本页目录">
      <div class="toc-scroll">
        <div class="toc__title">目录</div>
        <ul class="book-nav toc">
{toc}
        </ul>
      </div>
    </aside>

    <main class="book-main">
      <article class="article">
        <div class="practice-breadcrumb">
          <a href="./">Practice</a><span class="sep">/</span>{crumb}
        </div>
        <h1>{title}</h1>
        <p class="practice-lead">{lead}</p>

        <div class="meta-row">
          <div>
            <strong>本课目标</strong>
            <span>{goal}</span>
          </div>
          <div>
            <strong>项目阶段</strong>
            <span>{stage}</span>
          </div>
          <div>
            <strong>练习方式</strong>
            <span>{method}</span>
          </div>
        </div>

{body}
        {foot}
      </article>
    </main>
  </div>
{COMMON_SCRIPTS}
</body>
</html>
"""


def std_toc(items, a="任务 A", b="任务 B"):
    return [
        ("#p1", "1. 练习", items),
        ("#p2", "2. 任务", [("#p2-1", "2.1", a), ("#p2-2", "2.2", b)]),
        (
            "#p3",
            "3. 实验结果与作业",
            [
                ("#p3-1", "3.1", "本次实验结果要求"),
                ("#p3-2", "3.2", "作业"),
                ("#p3-3", "3.3", "实验提交"),
            ],
        ),
    ]


def redirect(target, label):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
  <title>已迁移</title>
</head>
<body>
  <p><a href="{target}">进入{label}</a></p>
</body>
</html>
"""


# ===================== LAB 11: scraping =====================
body11 = f"""
        <section class="exercise" id="p1">
          <h2>1. 练习</h2>
          {callout('本节只使用第三方库 <code>requests</code> 与 <code>beautifulsoup4</code>。统一练习网站：<a href="https://books.toscrape.com/" target="_blank" rel="noopener">https://books.toscrape.com/</a>（专为教学爬取设计的沙箱站点）。请遵守课堂节奏，不要高频连续请求。')}

          <h3 id="p1-1">1.1 安装与第一次网页获取</h3>
          {p('先安装依赖，再用 GET 获取首页 HTML 文本。注意设置 <code>timeout</code>，并检查状态码。')}
          {code('''# pip install requests beautifulsoup4
import requests

URL = "https://books.toscrape.com/"
resp = requests.get(URL, timeout=15)
print("状态码:", resp.status_code)
resp.raise_for_status()
html = resp.text
print("文本长度:", len(html))
print(html[:200])''')}
          {check('状态码为 200；能打印一段以 <code>&lt;!DOCTYPE html&gt;</code> 开头的文本。')}

          <h3 id="p1-2">1.2 用 Beautiful Soup 解析 HTML</h3>
          {p('HTML 是带标签的文档。Beautiful Soup 把它解析成可查询的树，而不是当成普通字符串硬切。')}
          {code('''from bs4 import BeautifulSoup
import requests

html = requests.get("https://books.toscrape.com/", timeout=15).text
soup = BeautifulSoup(html, "html.parser")
print("页面标题:", soup.title.get_text(strip=True) if soup.title else None)
print("一级标题数量 h1:", len(soup.select("h1")))
print("图书卡片数量:", len(soup.select("article.product_pod")))''')}
          {check('首页应能找到 20 个 <code>article.product_pod</code>（每页 20 本）。')}

          <h3 id="p1-3">1.3 提取单本图书：书名、价格、评分</h3>
          {step('Step 1 / 观察一张卡片的结构')}
          {p('每本书在 <code>article.product_pod</code> 中：完整书名在 <code>h3 &gt; a</code> 的 <code>title</code> 属性；价格在 <code>p.price_color</code>；星级在 <code>p.star-rating</code> 的 class（如 <code>Three</code>）。')}
          {code('''from bs4 import BeautifulSoup
import requests

html = requests.get("https://books.toscrape.com/", timeout=15).text
soup = BeautifulSoup(html, "html.parser")
pod = soup.select_one("article.product_pod")

title = pod.h3.a["title"]
price_text = pod.select_one("p.price_color").get_text(strip=True)  # 如 £51.77
rating_class = pod.select_one("p.star-rating")["class"]  # ['star-rating', 'Three']
rating_word = [c for c in rating_class if c != "star-rating"][0]

WORD_TO_NUM = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
price = float(price_text.replace("£", ""))
rating = WORD_TO_NUM[rating_word]
print(title, price, rating)''')}
          {check('能打印书名、浮点价格与 1–5 的整数评分。')}

          <h3 id="p1-4">1.4 提取本页全部图书并做条件筛选</h3>
          {code('''from bs4 import BeautifulSoup
import requests

WORD_TO_NUM = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def parse_list_page(url):
    html = requests.get(url, timeout=15).text
    soup = BeautifulSoup(html, "html.parser")
    books = []
    for pod in soup.select("article.product_pod"):
        title = pod.h3.a["title"]
        href = pod.h3.a["href"]
        price = float(pod.select_one("p.price_color").get_text(strip=True).replace("£", ""))
        rating_word = [c for c in pod.select_one("p.star-rating")["class"] if c != "star-rating"][0]
        rating = WORD_TO_NUM[rating_word]
        books.append({"title": title, "price": price, "rating": rating, "href": href})
    return books

books = parse_list_page("https://books.toscrape.com/")
cheap_high = [b for b in books if b["price"] < 30 and b["rating"] >= 4]
print("本页图书数:", len(books))
print("价格&lt;30 且评分≥4:", len(cheap_high))
for b in cheap_high[:5]:
    print(f'{b["rating"]}星 £{b["price"]:.2f} {b["title"]}')''')}
          {check('本页 20 本；筛选结果随页面内容变化，但代码逻辑正确。')}

          <h3 id="p1-5">1.5 分页访问：跟随 “next”</h3>
          {p('列表页底栏有 <code>li.next &gt; a</code>。相对链接需用 <code>urllib.parse.urljoin</code> 拼成绝对 URL。')}
          {code('''from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import time

BASE = "https://books.toscrape.com/"
WORD_TO_NUM = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def parse_list_page(url):
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    books = []
    for pod in soup.select("article.product_pod"):
        title = pod.h3.a["title"]
        href = urljoin(url, pod.h3.a["href"])
        price = float(pod.select_one("p.price_color").get_text(strip=True).replace("£", ""))
        rating_word = [c for c in pod.select_one("p.star-rating")["class"] if c != "star-rating"][0]
        books.append({"title": title, "price": price, "rating": WORD_TO_NUM[rating_word], "url": href})
    next_a = soup.select_one("li.next > a")
    next_url = urljoin(url, next_a["href"]) if next_a else None
    return books, next_url

all_books = []
url = BASE
for page_i in range(1, 4):  # 课堂先抓前 3 页
    books, url = parse_list_page(url)
    all_books.extend(books)
    print(f"第{page_i}页: {len(books)} 本，累计 {len(all_books)}")
    if not url:
        break
    time.sleep(0.5)  # 礼貌间隔

print("合计:", len(all_books))''')}
          {check('前 3 页合计约 60 本；每页请求之间有短暂停顿。')}

          <h3 id="p1-6">1.6 详情页解析：库存与品类</h3>
          {p('列表页信息有限。进入详情页可读取品类面包屑、产品信息表（UPC、库存等）。')}
          {code('''from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

list_html = requests.get("https://books.toscrape.com/", timeout=15).text
list_soup = BeautifulSoup(list_html, "html.parser")
first_href = list_soup.select_one("article.product_pod h3 a")["href"]
detail_url = urljoin("https://books.toscrape.com/", first_href)

detail = BeautifulSoup(requests.get(detail_url, timeout=15).text, "html.parser")
title = detail.select_one("div.product_main h1").get_text(strip=True)
# 面包屑：Home > Books > Category > Title
crumbs = [a.get_text(strip=True) for a in detail.select("ul.breadcrumb li a")]
category = crumbs[2] if len(crumbs) >= 3 else ""

info = {}
for row in detail.select("table.table.table-striped tr"):
    key = row.th.get_text(strip=True)
    val = row.td.get_text(strip=True)
    info[key] = val

print("书名:", title)
print("品类:", category)
print("UPC:", info.get("UPC"))
print("库存原文:", info.get("Availability"))''')}
          {check('能打印书名、品类、UPC 与库存原文。')}

          <h3 id="p1-7">1.7 保存为 CSV</h3>
          {code('''import csv
from pathlib import Path

rows = [
    {"title": "Demo Book", "price": 12.5, "rating": 4, "category": "Poetry", "url": "https://books.toscrape.com/"}
]
out = Path("books_sample.csv")
with out.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating", "category", "url"])
    writer.writeheader()
    writer.writerows(rows)
print("已写入", out.resolve())''')}
          {check('生成带表头的 CSV，可用表格软件打开且中文不乱码（utf-8-sig）。')}

          <h3 id="p1-8">1.8 常见错误</h3>
          {p('<strong>错误 1：</strong>用字符串 <code>split</code> 硬拆 HTML，页面稍变就全错。')}
          {p_gap('<strong>错误 2：</strong>忘记 <code>urljoin</code>，相对链接打不开详情页。')}
          {p_gap('<strong>错误 3：</strong>把价格字符串 <code>£51.77</code> 直接当数字运算。')}
          {p_gap('<strong>错误 4：</strong>循环抓取不加 <code>timeout</code> / 间隔，请求失败难排查。')}
          {p_gap('<strong>错误 5：</strong>只取 <code>a</code> 标签可见文本（可能被截断），忽略 <code>title</code> 属性中的全名。')}
        </section>

        <section class="exercise" id="p2">
          <h2>2. 任务</h2>
          {p('依赖：<code>pip install requests beautifulsoup4</code>。若教室网络不稳定，可先保存 1～2 页 HTML 到本地文件，用 <code>BeautifulSoup(Path(...).read_text(), "html.parser")</code> 完成解析练习。')}

          <h3 id="p2-1">2.1 任务 A：多页采集并筛选导出（必做）</h3>
          {tasks([
            '抓取至少 3 个列表页（或本地保存的等价 HTML）',
            '提取每本书的 title、price、rating、详情 url',
            '筛选：rating ≥ 4 且 price &lt; 40（阈值可在注释中写明）',
            '将筛选结果保存为 <code>books_filtered.csv</code>（utf-8-sig）',
            '打印：抓取总数、筛选后数量、价格均值',
          ])}

          <h3 id="p2-2">2.2 任务 B：详情页增强（拓展）</h3>
          {tasks([
            '对筛选结果中的前 5 本书访问详情页',
            '补充 category 与 Availability（库存原文）字段',
            '另存 <code>books_enriched.csv</code>',
            '用 2～3 句话说明列表页与详情页各自适合提取什么信息',
          ])}
        </section>

        <section class="exercise" id="p3">
          <h2>3. 实验结果与作业</h2>
          <h3 id="p3-1">3.1 本次实验结果要求</h3>
          {tasks([
            '使用 requests 获取网页并处理状态码 / timeout',
            '使用 Beautiful Soup 选择卡片与字段',
            '完成价格与星级的类型转换',
            '实现分页或本地多页解析',
            '将结果保存为 CSV',
          ])}
          <h3 id="p3-2">3.2 作业</h3>
          {p_gap('<strong>题目1：</strong>为什么完整书名应读 <code>title</code> 属性而不是链接可见文本？')}
          {p_gap('<strong>题目2：</strong>写出任务 A 的抓取总数、筛选数量与均价。')}
          {p_gap('<strong>题目3：</strong>提交核心解析函数与 CSV 表头截图。')}
          <h3 id="p3-3">3.3 实验提交</h3>
          {p('提交 <code>.py</code>、CSV、两处关键步骤截图。按雨课堂要求填写实验记录。仅使用 books.toscrape.com 教学站点。')}
        </section>
"""

html11 = page(
    "实验11：Python网络请求与网页解析",
    "实验11",
    "从打开 books.toscrape.com 开始。完成本节后，能用 requests 获取页面，用 Beautiful Soup 提取图书信息，完成筛选、分页并保存 CSV。",
    "掌握 requests 获取 HTML、Beautiful Soup 解析、字段提取、条件筛选、分页与详情页、CSV 导出",
    "网页解析专训。只打 requests + BS4，不引入 API Key / 大模型（留给实验12）",
    "本地运行代码并完成任务，再通过雨课堂填写实验记录",
    std_toc(
        [
            ("#p1-1", "1.1", "网页获取"),
            ("#p1-2", "1.2", "HTML 解析"),
            ("#p1-3", "1.3", "图书信息提取"),
            ("#p1-4", "1.4", "条件筛选"),
            ("#p1-5", "1.5", "分页访问"),
            ("#p1-6", "1.6", "详情页解析"),
            ("#p1-7", "1.7", "CSV 保存"),
            ("#p1-8", "1.8", "常见错误"),
        ],
        "任务 A：多页筛选导出",
        "任务 B：详情页增强",
    ),
    body11,
    "sop11-web.html",
)
(P / "sop11-web.html").write_text(html11, encoding="utf-8")
print("wrote sop11-web", len(html11))

# ===================== LAB 12: API =====================
body12 = f"""
        <section class="exercise" id="p1">
          <h2>1. 练习</h2>
          {callout('实验11处理的是<strong>网页 HTML</strong>；本实验处理的是<strong>结构化 API（多为 JSON）</strong>。不要在这里讲 Beautiful Soup 解析页面。无付费密钥也可完成本节基础练习。')}

          <h3 id="p1-1">1.1 HTTP API 是什么</h3>
          {p('API 返回的是给程序读的数据（常见 JSON 对象/数组），不是给人浏览的完整网页布局。')}
          {code('''# JSON 示例（字典 / 列表）
sample = {
    "id": 1,
    "title": "demo task",
    "completed": False
}
print(sample["title"], type(sample["completed"]))''')}
          {check('能区分 HTML 字符串与 JSON 数据结构。')}

          <h3 id="p1-2">1.2 GET：公开 JSON 接口</h3>
          {p('下列公共接口无需登录。若网络不可用，改用本地 <code>todo_1.json</code>。')}
          {code('''import json
from pathlib import Path
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
except Exception as exc:
    print("在线失败，改用本地:", exc)
    data = json.loads(Path("todo_1.json").read_text(encoding="utf-8"))

print("编号:", data["id"])
print("任务:", data["title"])
print("完成:", data["completed"])''')}
          {step('本地备份文件 todo_1.json')}
          {code('''{"userId": 1, "id": 1, "title": "demo task", "completed": false}''')}
          {check('无论在线或离线，都能读出三个字段。')}

          <h3 id="p1-3">1.3 请求参数：GET params 与 POST json</h3>
          {code('''import requests

# GET 查询参数
r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
    timeout=10,
)
r.raise_for_status()
posts = r.json()
print("条数:", len(posts))

# POST JSON 正文
r2 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "course-demo", "body": "hello api", "userId": 1},
    timeout=10,
)
print("POST 状态码:", r2.status_code)
print(r2.json())''')}
          {check('理解 params（拼到 URL）与 json=（放进请求体）的差别。')}

          <h3 id="p1-4">1.4 嵌套 JSON 与缺字段</h3>
          {code('''payload = {
    "data": {
        "items": [
            {"id": 1, "name": "alpha"},
            {"id": 2}
        ]
    }
}
for item in payload["data"]["items"]:
    name = item.get("name")
    print(item["id"], name if name is not None else "(缺少 name)")''')}
          {check('缺字段时不崩溃，能给出提示。')}

          <h3 id="p1-5">1.5 错误处理：超时、状态码、有限重试</h3>
          {code('''import time
import requests

def fetch_json(url, retries=2, timeout=10):
    last_error = None
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, timeout=timeout)
            if r.status_code in (401, 403, 429) or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}", response=r)
            r.raise_for_status()
            return r.json()
        except (requests.Timeout, requests.HTTPError, requests.RequestException) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(0.5)
                continue
            raise RuntimeError(f"请求失败: {last_error}") from last_error

print(fetch_json("https://jsonplaceholder.typicode.com/todos/1"))''')}
          {check('必须设置 timeout；重试次数有上限；错误信息可读。')}

          <h3 id="p1-6">1.6 API Key：环境变量，不进仓库</h3>
          {code('''import os

api_key = os.environ.get("COURSE_API_KEY", "")
if not api_key:
    print("未设置 COURSE_API_KEY → 使用模拟数据路径")
else:
    print("已检测到密钥，长度 =", len(api_key), "（不要打印完整密钥）")
    # headers = {"Authorization": f"Bearer {api_key}"}''')}
          {callout('严禁把真实密钥写进代码仓库、网页或截图。')}
          {check('无密钥时基础练习仍可完成。')}

          <h3 id="p1-7">1.7 大模型接口：请求结构与模拟响应</h3>
          {p('真实供应商路径与计费不同。课堂用模拟响应理解 messages / choices 结构；有合法密钥的同学可选做真实调用。')}
          {code('''def build_chat_request(user_text, model="demo-model"):
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是课程助教，用中文简明回答。"},
            {"role": "user", "content": user_text},
        ],
    }

def parse_chat_response(resp):
    try:
        return resp["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ValueError("响应结构不符合预期") from exc

def mock_chat(user_text):
    req = build_chat_request(user_text)
    fake = {
        "choices": [
            {"message": {"role": "assistant", "content": f"【模拟】已收到：{user_text[:20]}"}}
        ]
    }
    return req, parse_chat_response(fake)

req, answer = mock_chat("用一句话总结：本日采集了 60 本图书")
print("模型:", req["model"], "消息数:", len(req["messages"]))
print("回复:", answer)''')}
          {check('能构造请求并解析回复；理解费用与不确定性边界。')}

          <h3 id="p1-8">1.8 综合：统一请求函数 + 模拟报告</h3>
          {code('''import json
from pathlib import Path

def load_records():
    # 基础练习：不依赖付费 API
    path = Path("records_demo.json")
    if not path.exists():
        demo = [
            {"id": 1, "title": "Book A", "price": 12.0},
            {"id": 2, "title": "Book B", "price": 25.5},
        ]
        path.write_text(json.dumps(demo, ensure_ascii=False, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))

records = load_records()
avg_price = sum(r["price"] for r in records) / len(records)
summary = f"共 {len(records)} 条，均价 {avg_price:.2f}"
_, answer = mock_chat(summary)
print(summary)
print(answer)''')}
          {check('无网络、无密钥也能跑通“读数据 → 汇总 → 模拟生成说明”。')}

          <h3 id="p1-9">1.9 常见错误</h3>
          {p('<strong>错误 1：</strong>把 API JSON 当成 HTML 去用 Beautiful Soup 解析。')}
          {p_gap('<strong>错误 2：</strong>不设置 timeout。')}
          {p_gap('<strong>错误 3：</strong>在代码里硬编码并打印密钥。')}
          {p_gap('<strong>错误 4：</strong>无限重试，触发 429 后仍狂打接口。')}
          {p_gap('<strong>错误 5：</strong>没有本地/模拟降级，断网就无法交作业。')}
        </section>

        <section class="exercise" id="p2">
          <h2>2. 任务</h2>
          {p('依赖：<code>pip install requests</code>。基础路径不要求付费 API Key。')}
          <h3 id="p2-1">2.1 任务 A：请求函数与字段输出（必做）</h3>
          {tasks([
            '编写带 timeout、状态码检查的 GET 函数',
            '在线拉取公开 JSON，或离线读取本地 JSON',
            '打印至少 3 个字段；异常时给出清晰信息',
            '不打印、不提交任何密钥',
          ])}
          <h3 id="p2-2">2.2 任务 B：大模型模板（拓展）</h3>
          {tasks([
            '实现 build_chat_request / parse_chat_response / mock_chat',
            '把任务 A 的汇总文本送入模拟对话并打印回复',
            '可选：自有合法密钥下做一次真实调用，并说明费用与风险',
          ])}
        </section>

        <section class="exercise" id="p3">
          <h2>3. 实验结果与作业</h2>
          <h3 id="p3-1">3.1 本次实验结果要求</h3>
          {tasks(['区分网页 HTML 与 API JSON','掌握 GET/POST 与 JSON 解析','完成错误处理与环境变量密钥读取','用模拟方式理解大模型请求/响应'])}
          <h3 id="p3-2">3.2 作业</h3>
          {p_gap('<strong>题目1：</strong>实验11与实验12的对象分别是什么？')}
          {p_gap('<strong>题目2：</strong>写出任务 A 的三个字段取值。')}
          {p_gap('<strong>题目3：</strong>说明你的离线 JSON 路径或在线 URL。')}
          <h3 id="p3-3">3.3 实验提交</h3>
          {p('提交代码与运行截图；禁止提交密钥。按雨课堂要求作答。')}
        </section>
"""

html12 = page(
    "实验12：Python API与大模型调用",
    "实验12",
    "从一次公开 JSON 接口开始。完成本节后，能安全调用 HTTP API、解析 JSON，并用模拟方式理解大模型接口结构——即使没有付费密钥也能完成基础练习。",
    "掌握 GET/POST、请求参数、JSON 响应、API Key 环境变量、错误处理与大模型消息结构",
    "结构化接口调用。与实验11的 HTML 解析明确分工",
    "本地运行代码并完成任务，再通过雨课堂填写实验记录",
    std_toc(
        [
            ("#p1-1", "1.1", "什么是 API"),
            ("#p1-2", "1.2", "GET JSON"),
            ("#p1-3", "1.3", "GET/POST 参数"),
            ("#p1-4", "1.4", "嵌套与缺字段"),
            ("#p1-5", "1.5", "错误处理"),
            ("#p1-6", "1.6", "API Key"),
            ("#p1-7", "1.7", "大模型结构"),
            ("#p1-8", "1.8", "综合模拟报告"),
            ("#p1-9", "1.9", "常见错误"),
        ],
        "任务 A：请求函数",
        "任务 B：大模型模板",
    ),
    body12,
    "sop12-api.html",
)
(P / "sop12-api.html").write_text(html12, encoding="utf-8")
print("wrote sop12-api", len(html12))

# ===================== LAB 13: Streamlit =====================
body13 = f"""
        <section class="exercise" id="p1">
          <h2>1. 练习</h2>
          {callout('本实验整合文件读写、异常处理思路、pandas 与 Matplotlib，交付可本地运行的 Streamlit 应用。教学演示 ≠ 生产上云，勿上传真实患者身份信息。')}

          <h3 id="p1-1">1.1 最小可运行页面</h3>
          {code('''import streamlit as st

st.title("病例数据分析平台")
st.write("实验13：综合项目与 Streamlit Web 应用")''')}
          {p_gap('启动命令：<code>streamlit run app.py</code>（不要只用 <code>python app.py</code>）。')}
          {check('浏览器能打开本地页面并看到标题。')}

          <h3 id="p1-2">1.2 数据上传与默认演示数据</h3>
          {code('''import streamlit as st
import pandas as pd

st.title("病例数据分析平台")

def default_df():
    return pd.DataFrame({
        "case_id": ["C001", "C002", "C003", "C004", "C005"],
        "group": ["A", "B", "A", "B", "A"],
        "stay_days": [4, 7, 5, 8, 6],
        "age": [45, 52, 38, 61, 47],
    })

uploaded = st.file_uploader("上传 CSV（可选）", type=["csv"])
if uploaded is None:
    df = default_df()
    st.info("未上传文件，使用内置教学模拟数据。")
else:
    try:
        df = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"读取失败：{exc}")
        df = default_df()

required = {"group", "stay_days"}
missing = required - set(df.columns)
if missing:
    st.warning(f"缺少列：{missing}。已回退到演示数据。")
    df = default_df()

st.session_state["df"] = df
st.dataframe(df)''')}
          {check('无上传、坏文件、缺列时都有可读提示，并仍能继续演示。')}

          <h3 id="p1-3">1.3 数据预览与质量概览</h3>
          {code('''import streamlit as st
import pandas as pd

df = st.session_state.get("df", pd.DataFrame({"group": ["A"], "stay_days": [4]}))
c1, c2, c3 = st.columns(3)
c1.metric("记录数", len(df))
c2.metric("字段数", df.shape[1])
c3.metric("分组数", df["group"].nunique(dropna=True) if "group" in df.columns else 0)
st.write("缺失率（%）")
st.write((df.isna().mean() * 100).round(1))
st.dataframe(df.head(20))''')}
          {check('页面同时显示指标、缺失概况与表预览。')}

          <h3 id="p1-4">1.4 侧栏筛选</h3>
          {p('每次控件变化都会重新执行脚本。把筛选条件放在 sidebar。')}
          {code('''import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "group": ["A", "B", "A", "B", "A"],
    "stay_days": [4, 7, 5, 8, 6],
    "age": [45, 52, 38, 61, 47],
})
groups = sorted(df["group"].dropna().unique().tolist())
sel = st.sidebar.multiselect("组别", groups, default=groups)
min_stay, max_stay = st.sidebar.slider(
    "住院天数范围",
    int(df["stay_days"].min()),
    int(df["stay_days"].max()),
    (int(df["stay_days"].min()), int(df["stay_days"].max())),
)
subset = df[df["group"].isin(sel) & df["stay_days"].between(min_stay, max_stay)]
if subset.empty:
    st.info("当前筛选无数据，请调整侧栏条件。")
else:
    st.success(f"筛选后 {len(subset)} 条")
    st.dataframe(subset)''')}
          {check('改变组别或天数范围后，表格同步更新。')}

          <h3 id="p1-5">1.5 统计分析</h3>
          {code('''import streamlit as st
import pandas as pd

subset = pd.DataFrame({"group": ["A", "A", "B"], "stay_days": [4, 6, 8]})
st.subheader("统计分析")
st.metric("平均住院天数", round(subset["stay_days"].mean(), 2))
st.metric("最大住院天数", int(subset["stay_days"].max()))
summary = (
    subset.groupby("group", as_index=False)["stay_days"]
    .agg(count="count", mean_stay="mean")
)
st.dataframe(summary)''')}
          {check('至少两个总体指标 + 一张分组汇总表。')}

          <h3 id="p1-6">1.6 图表展示（Matplotlib）</h3>
          {code('''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

subset = pd.DataFrame({
    "group": ["A", "B", "A", "B", "A"],
    "stay_days": [4, 7, 5, 8, 6],
    "age": [45, 52, 38, 61, 47],
})
summary = subset.groupby("group", as_index=False)["stay_days"].mean()

fig1, ax1 = plt.subplots(figsize=(5, 3))
ax1.bar(summary["group"], summary["stay_days"], color="black")
ax1.set(xlabel="Group", ylabel="Mean stay", title="Mean stay by group")
fig1.tight_layout()
st.pyplot(fig1)

fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.scatter(subset["age"], subset["stay_days"], color="black")
ax2.set(xlabel="Age", ylabel="Stay days", title="Age vs stay")
fig2.tight_layout()
st.pyplot(fig2)''')}
          {check('至少两张图，且基于<strong>当前筛选后</strong>的数据。')}

          <h3 id="p1-7">1.7 结果下载</h3>
          {code('''import streamlit as st
import pandas as pd

subset = pd.DataFrame({"group": ["A"], "stay_days": [4]})
csv_bytes = subset.to_csv(index=False).encode("utf-8-sig")
st.download_button(
    "下载当前筛选结果 CSV",
    data=csv_bytes,
    file_name="filtered_cases.csv",
    mime="text/csv",
)''')}
          {check('下载内容与页面当前筛选一致。')}

          <h3 id="p1-8">1.8 项目结构建议</h3>
          {code('''# 推荐提交结构
# app.py
# requirements.txt
# README.md
# sample_data/demo_cases.csv

# requirements.txt 示例
# streamlit
# pandas
# matplotlib''')}
          {p_gap('README 至少写清：安装命令、启动命令、功能截图说明、演示数据说明。')}
          {check('换一台电脑按 README 能安装并启动。')}

          <h3 id="p1-9">1.9 常见错误</h3>
          {p('<strong>错误 1：</strong>用 <code>python app.py</code> 启动。')}
          {p_gap('<strong>错误 2：</strong>图表/下载仍基于全表，未使用筛选后子集。')}
          {p_gap('<strong>错误 3：</strong>缺列时直接 KeyError 崩溃。')}
          {p_gap('<strong>错误 4：</strong>缺少 requirements.txt / README。')}
          {p_gap('<strong>错误 5：</strong>上传含真实身份信息的数据。')}
        </section>

        <section class="exercise" id="p2">
          <h2>2. 任务</h2>
          <h3 id="p2-1">2.1 任务 A：完整 Streamlit 应用（必做）</h3>
          {tasks([
            '数据上传（可选）+ 内置演示数据回退',
            '数据预览与至少两个质量/规模指标',
            '侧栏筛选（至少两个条件）',
            '统计分析（总体指标 + groupby 表）',
            '至少两张 Matplotlib 图',
            '下载当前筛选结果',
            '提供 requirements.txt 与 README',
          ])}
          <h3 id="p2-2">2.2 任务 B：增强与说明（拓展）</h3>
          {tasks([
            '增加数据质量提示（缺失率阈值告警）或数值范围自定义',
            '可选：读取实验11导出的 CSV 作为默认数据',
            '用 3～5 句话说明本应用串联了哪些已学技能',
          ])}
        </section>

        <section class="exercise" id="p3">
          <h2>3. 实验结果与作业</h2>
          <h3 id="p3-1">3.1 本次实验结果要求</h3>
          {tasks(['独立运行 Streamlit 应用','完成上传→预览→筛选→统计→图表→下载闭环','异常与空数据有提示','提交可复现材料'])}
          <h3 id="p3-2">3.2 作业</h3>
          {p_gap('<strong>题目1：</strong>正确启动命令是？')}
          {p_gap('<strong>题目2：</strong>列出两个指标与两张图的含义。')}
          {p_gap('<strong>题目3：</strong>描述一次缺列或空筛选时的页面提示。')}
          <h3 id="p3-3">3.3 实验提交</h3>
          {p('提交应用代码、requirements.txt、README、至少两张运行截图。勿提交真实隐私数据或 API 密钥。')}
        </section>
"""

html13 = page(
    "实验13：Python综合项目与Streamlit Web应用",
    "实验13",
    "把本学期的数据读取、清洗思路、统计与绘图接到一个可交互页面上。完成本节后，能交付具备上传、预览、筛选、统计、图表与下载的 Streamlit 应用。",
    "整合 pandas / Matplotlib 与 Streamlit，完成端到端教学演示应用",
    "综合交付。输入 → 预览 → 筛选 → 统计 → 可视化 → 下载",
    "本地运行应用并完成任务，再通过雨课堂填写实验记录",
    std_toc(
        [
            ("#p1-1", "1.1", "最小页面"),
            ("#p1-2", "1.2", "上传与默认数据"),
            ("#p1-3", "1.3", "预览与质量"),
            ("#p1-4", "1.4", "侧栏筛选"),
            ("#p1-5", "1.5", "统计分析"),
            ("#p1-6", "1.6", "图表展示"),
            ("#p1-7", "1.7", "结果下载"),
            ("#p1-8", "1.8", "项目结构"),
            ("#p1-9", "1.9", "常见错误"),
        ],
        "任务 A：完整应用",
        "任务 B：增强说明",
    ),
    body13,
    "sop13-platform.html",
)
(P / "sop13-platform.html").write_text(html13, encoding="utf-8")
print("wrote sop13-platform", len(html13))

# Redirects for compatibility
(P / "sop11-api.html").write_text(
    redirect("sop12-api.html", "实验12：Python API与大模型调用"), encoding="utf-8"
)
(P / "sop12-platform.html").write_text(
    redirect("sop13-platform.html", "实验13：Python综合项目与Streamlit Web应用"),
    encoding="utf-8",
)
(P / "sop10-api.html").write_text(
    redirect("sop12-api.html", "实验12：Python API与大模型调用"), encoding="utf-8"
)
(P / "sop11-platform.html").write_text(
    redirect("sop13-platform.html", "实验13：Python综合项目与Streamlit Web应用"),
    encoding="utf-8",
)
print("redirects updated")

# Practice index
nav_items = LABS
descs = {
    "sop00-dataset.html": "数据规模、一行含义、主要字段，以及这份数据如何贯穿全学期。",
    "sop01-syntax.html": "表示和处理一条病例 · 单病例",
    "sop02-structures.html": "表示一名患者和一组病例 · 病例集合",
    "sop03-control.html": "自动筛选、统计病例 · 规则处理",
    "sop04-design.html": "医学病例数据的处理与分析 · 病例信息处理器",
    "sop05-functions.html": "把重复逻辑做成工具 · 工具箱",
    "sop06-file-formatting.html": "写入、读取、TXT / CSV / JSON 与 f-string · 成绩存取",
    "sop07-files.html": "try / except / else / finally / raise 与数据有效性检查",
    "sop08-numpy.html": "ndarray、索引切片、数组运算与统计计算",
    "sop09-pandas.html": "读取、清洗、缺失值、条件筛选与 groupby",
    "sop10-matplotlib.html": "折线、柱状、散点与直方图",
    "sop11-web.html": "requests + Beautiful Soup · books.toscrape.com",
    "sop12-api.html": "HTTP API、JSON、API Key 与大模型接口（可无密钥完成）",
    "sop13-platform.html": "Streamlit 上传、预览、筛选、统计、图表与下载",
}

nav_html = "\n".join(f'        <li><a href="{f}">{escape(t)}</a></li>' for f, t in nav_items)
list_html = "\n".join(
    f'''        <li>
          <a href="{f}">
            <div class="pl-tit">{escape(t)}</div>
            <div class="pl-desc">{escape(descs[f])}</div>
          </a>
        </li>'''
    for f, t in nav_items
)

index = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Practice · Python 高级应用</title>
  <link rel="stylesheet" href="../style.css">
  <link rel="stylesheet" href="./practice.css">
</head>
<body class="practice-index">
  <div class="book-shell">
    <aside class="book-sidebar" aria-label="导航">
      <div class="book-brand"><a href="https://github.com/shaoxunyuan/PythonCourse">Python 高级应用</a></div>
      <ul class="book-nav">
{nav_html}
      </ul>
    </aside>
    <main class="book-main">
      <h1>Practice</h1>
      <ul class="practice-list">
{list_html}
      </ul>
    </main>
  </div>
  <script src="./split.js"></script>
</body>
</html>
"""
(P / "index.html").write_text(index, encoding="utf-8")
print("wrote index")
print("done")
