<div align="center">

# 🐼 LeetCode Pandas Solutions

**Clean, Vectorized, and Documented Data Manipulation Solutions**

[![GitHub](https://img.shields.io/badge/GitHub-ahmed--ibrahim--EG-181717?style=for-the-badge&logo=github)](https://github.com/ahmed-ibrahim-EG)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-Data%20Engineering-150458?style=for-the-badge&logo=pandas)](https://pandas.pydata.org/)

</div>

---

## 📖 Overview

This repository documents my structured solutions to **LeetCode Pandas** and data manipulation challenges. The primary focus is writing idiomatic, high-performance Pandas code emphasizing:
- **Vectorized Operations:** Avoiding slow loops and leveraging C-backed Pandas routines.
- **Explicit Indexing:** Clean row and column projections via `.loc[]` and `.iloc[]`.
- **Memory & Readability:** Production-ready transformations suited for data pipelines and data engineering tasks.

---

## 📊 Study Plan Progress

| # | Problem | Difficulty | Core Topics & Methods | Solution |
| :---: | :--- | :---: | :--- | :---: |
| 0595 | [Big Countries](https://leetcode.com/problems/big-countries/) | Easy | Boolean Masking, `.loc[]`, Column Projection | [0595_big_countries.py](./0595_big_countries.py) |

*More challenges are added continuously as I work through the LeetCode curriculum.*

---

## 🧠 Key Pandas Concepts Covered

### 1. Data Filtering & Selection
- Conditional row filtering with logical operators (`&`, `|`, `~`).
- Explicit row/column slicing with `df.loc[mask, ['col1', 'col2']]`.
- Value membership checks via `.isin()` and pattern matching with `.str.contains()`.

### 2. Aggregation & Grouping
- Split-Apply-Combine patterns using `groupby()` and `.agg()`.
- Cumulative calculations (`cumsum()`, `cummax()`).
- Rank calculations with `rank(method='dense')`.

### 3. Data Transformation & Cleaning
- Handling missing data with `fillna()` and `dropna()`.
- Deduplication using `drop_duplicates()`.
- Modifying and casting column schemas (`astype()`, `rename()`).

### 4. Merging & Reshaping
- Joins using `pd.merge()` (inner, left, right, outer).
- Reshaping structures via `pivot()`, `pivot_table()`, and `melt()`.

---

## 📂 Repository Structure

```text
.
├── README.md
├── 0595_big_countries.py
└── ...
```

Each solution script is structured as:
1. **Type-Annotated Function:** Matches the LeetCode runtime signature.
2. **Docstring:** Summarizes the problem constraints and logic.
3. **Local Test Harness:** Standalone executable block (`if __name__ == '__main__':`) with sample inputs for quick local verification.

---

## 🛠️ Getting Started

### Prerequisites

Clone the repository and install `pandas`:

```bash
git clone https://github.com/ahmed-ibrahim-EG/pandas-leetcode-solutions.git
cd pandas-leetcode-solutions
pip install pandas
```

### Running a Solution Locally

Execute any solution directly using Python:

```bash
python 0595_big_countries.py
```

---

## 👤 Author

- **GitHub:** [@ahmed-ibrahim-EG](https://github.com/ahmed-ibrahim-EG)
