"""生成第 10 讲 Matplotlib 演示页用的三张示例图。

用法：
    python scripts/generate_matplotlib_lesson10_figures.py

输出目录：
    docs/Presentations/assets/matplotlib/
"""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

OUT_DIR = Path(__file__).resolve().parents[1] / "docs" / "Presentations" / "assets" / "matplotlib"

DPI = 160


def save(fig, name):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_DIR / name, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def line_demo():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    minutes = [20, 30, 15, 40, 35, 60, 45]

    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(days, minutes, marker="o", color="blue")
    ax.set_title("Weekly Exercise Time")
    ax.set_xlabel("Day")
    ax.set_ylabel("Minutes")
    ax.grid(True, alpha=0.3)
    save(fig, "line_demo.png")


def bar_demo():
    clubs = ["Sports", "Music", "Art", "Coding"]
    students = [32, 25, 18, 28]

    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.bar(clubs, students, color="skyblue")
    ax.set_title("Students by Club")
    ax.set_xlabel("Club")
    ax.set_ylabel("Students")
    save(fig, "bar_demo.png")


def scatter_demo():
    hours = [1, 2, 3, 4, 5, 6]
    scores = [56, 60, 65, 74, 79, 86]

    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.scatter(hours, scores, s=60, color="teal", alpha=0.8)
    ax.set_title("Study Hours vs Score (simulated)")
    ax.set_xlabel("Study hours")
    ax.set_ylabel("Score")
    ax.grid(True, alpha=0.3)
    save(fig, "scatter_demo.png")


if __name__ == "__main__":
    line_demo()
    bar_demo()
    scatter_demo()
    print("已生成：", OUT_DIR)
