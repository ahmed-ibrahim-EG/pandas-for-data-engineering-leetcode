<div align="center">

# 🐼 LeetCode Pandas Solutions

### *Clean, Vectorized, and Documented Data Manipulation Solutions*

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-study-plan-progress">Study Plan Progress</a> •
  <a href="#-key-pandas-concepts-covered">Key Pandas Concepts</a> •
  <a href="#-repository-structure">Repository Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-learning-goal">Learning Goal</a>
</p>

</div>

---

## 📌 Overview

This repository contains my solutions to **LeetCode Pandas problems**, focused on building practical skills in **data manipulation and transformation using Pandas**.

The goal is to solve problems using clean, readable, and efficient Pandas operations while documenting the main concepts used in each solution.

---

## 📊 Study Plan Progress

**7 / 50 Problems Completed — 14%**

| #  | Problem                                                                                           | Difficulty | Main Pandas Concepts                                                                           | Solution                                                                                  |
| -- | ------------------------------------------------------------------------------------------------- | ---------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 01 | [Big Countries](https://leetcode.com/problems/big-countries/)                                     | Easy       | Boolean Masking, `.loc[]`, Column Projection                                                   | [LEET-01 — Big Countries](./LEET-01-big-countries.py)                                     |
| 02 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy       | Multiple Conditions (`&`), Boolean Indexing                                                    | [LEET-02 — Recyclable and Low Fat Products](./LEET-02-recyclable-and-low-fat-products.py) |
| 03 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)             | Easy       | Membership Testing (`.isin()`), Bitwise NOT (`~`), `.loc[]`, `.rename()`                       | [LEET-03 — Customers Who Never Order](./LEET-03-customers-who-never-order.py)             |
| 04 | [Article Views I](https://leetcode.com/problems/article-views-i/)                                 | Easy       | Boolean Masking, `.loc[]`, `.drop_duplicates()`, `.rename()`, `.sort_values()`                 | [LEET-04 — Article Views](./LEET-04-article-views.py)                                     |
| 05 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/)                                   | Easy       | String Operations, `.str.len()`, Boolean Masking, `.loc[]`                                     | [LEET-05 — Invalid Tweets](./LEET-05-invalid-tweets.py)                                   |
| 06 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/)                 | Easy       | Boolean Masking, `.str.startswith()`, Modulo, `.where()`, `.sort_values()`                     | [LEET-06 — Calculate Special Bonus](./LEET-06-calculate-special-bonus.py)                 |
| 07 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/)                       | Easy       | String Operations, `.str.split()`, `.str.join()`, `.apply()`, String Slicing, `.sort_values()` | [LEET-07 — Fix Names in a Table](./LEET-07-fix-names-in-a-table.py)                       |

---

## 🧠 Key Pandas Concepts Covered

### 🔹 Data Filtering & Selection

* Boolean Masking
* Boolean Indexing
* `.loc[]`
* Column Projection
* `.isin()`
* Bitwise Operators (`&`, `~`)

### 🔹 String Operations

* `.str.len()`
* `.str.startswith()`
* `.str.split()`
* `.str.join()`
* String Slicing
* `.upper()`
* `.lower()`

### 🔹 Data Transformation

* `.where()`
* `.apply()`
* Creating calculated columns
* String transformation

### 🔹 Basic Data Manipulation Patterns

* `.drop_duplicates()`
* `.rename()`
* `.sort_values()`
* `.reset_index()`

---

## 📂 Repository Structure

```text
pandas-leetcode-solutions/
│
├── LEET-01-big-countries.py
├── LEET-02-recyclable-and-low-fat-products.py
├── LEET-03-customers-who-never-order.py
├── LEET-04-article-views.py
├── LEET-05-invalid-tweets.py
├── LEET-06-calculate-special-bonus.py
├── LEET-07-fix-names-in-a-table.py
│
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ahmed-ibrahim-EG/pandas-leetcode-solutions.git
cd pandas-leetcode-solutions
```

### 2. Install Pandas

```bash
pip install pandas
```

### 3. Run a Solution

```bash
python "LEET-07-fix-names-in-a-table.py"
```

---

## 🎯 Learning Goal

The main goal of this repository is to strengthen my ability to:

* Manipulate tabular data using **Pandas**
* Translate business requirements into data transformations
* Use **vectorized operations** instead of unnecessary loops
* Work confidently with filtering, transformation, and aggregation
* Develop clean and readable data-processing code
* Build patterns that are directly useful in **Data Engineering workflows**

The repository will continue to grow toward **50 LeetCode Pandas problems**, with each problem reinforcing practical data manipulation patterns.

---

## 👤 Author

**Ahmed Ibrahim**

Computer Science & Data Science Student
Aspiring Data Engineer

GitHub: [ahmed-ibrahim-EG](https://github.com/ahmed-ibrahim-EG)

</div>
