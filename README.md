[repository_readme.md](https://github.com/user-attachments/files/32694210/repository_readme.md)
# 🐼 LeetCode Pandas Solutions

An organized and documented repository containing optimized Python (Pandas) solutions for LeetCode database and data manipulation problems. 

This repository serves as a practical portfolio demonstrating core data engineering concepts, DataFrame wrangling, vectorized filtering, and aggregation patterns.

---

## 📌 Problem Solving Progress

| # | Problem Title | Difficulty | Key Concepts / Methods | Solution |
|---|---------------|------------|------------------------|----------|
| 0595 | [Big Countries](https://leetcode.com/problems/big-countries/) | Easy | Boolean Masking, `.loc[]`, Column Projection | [Python](./0595_big_countries.py) |

---

## 🛠️ Key Pandas Topics Covered

- **Data Filtering & Selection:**
  - Boolean indexing using logical operators (`|`, `&`, `~`)
  - Label-based indexing and column slicing with `.loc[]`
  - Positional indexing with `.iloc[]`
- **Data Transformation & Cleaning:**
  - Handling missing data (`dropna`, `fillna`)
  - Renaming and casting data types (`rename`, `astype`)
  - Value mapping and conditional mutation (`apply`, `np.where`)
- **Aggregation & Grouping:**
  - Summary metrics using `groupby()` and `.agg()`
  - Pivot tables and reshaping (`melt`, `pivot`)
- **Merging & Joining:**
  - Relational operations (`merge`, `concat`, `join`)

---

## 📂 Repository Structure

```text
.
├── README.md
├── 0595_big_countries.py
└── ...
```

Each solution file includes:
1. The standard LeetCode function signature with type hints.
2. Docstrings detailing the criteria and logic.
3. A reproducible standalone test runner using a local DataFrame.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed along with `pandas`:

```bash
pip install pandas
```

### Running a Solution Locally

You can test any solution file directly via the terminal:

```bash
python 0595_big_countries.py
```

---

## 👤 Author

- **GitHub:** [@your-username](https://github.com/your-username)
- **LeetCode:** [@your-handle](https://leetcode.com/your-handle/)
