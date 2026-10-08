<div align="center">

# 🐼 LeetCode Pandas Solutions

**Clean, Vectorized, and Documented Data Manipulation Solutions**

[![GitHub](https://img.shields.io/badge/GitHub-ahmed--ibrahim--EG-181717?style=for-the-badge\&logo=github)](https://github.com/ahmed-ibrahim-EG)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-Data%20Engineering-150458?style=for-the-badge\&logo=pandas)](https://pandas.pydata.org/)

</div>

---

## 📖 Overview

This repository documents my structured solutions to **LeetCode Pandas** and data manipulation challenges.

The primary focus is writing clean, idiomatic Pandas code with an emphasis on:

* **Vectorized Operations:** Avoiding unnecessary loops and leveraging Pandas-native operations.
* **Boolean Masking:** Filtering DataFrames using clear and composable conditions.
* **Explicit Indexing:** Clean row and column selection using `.loc[]`.
* **Data Transformation:** Renaming, deduplicating, sorting, and creating derived columns.
* **Data Engineering Relevance:** Practicing practical data manipulation patterns used in ETL and data transformation workflows.

---

## 📊 Study Plan Progress

|  #  | Problem                                                                                           | Difficulty | Core Topics & Methods                                                          | Solution                                                                                     |
| :-: | :------------------------------------------------------------------------------------------------ | :--------: | :----------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
|  01 | [Big Countries](https://leetcode.com/problems/big-countries/)                                     |    Easy    | Boolean Masking, `.loc[]`, Column Projection                                   | [LEET-01 — Big Countries.py](./LEET-01-big-countries.py)                                     |
|  02 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) |    Easy    | Multiple Conditions (`&`), Boolean Indexing                                    | [LEET-02 — Recyclable and Low Fat Products.py](./LEET-02-recyclable-and-low-fat-products.py) |
|  03 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/)             |    Easy    | Membership Testing (`.isin()`), Bitwise NOT (`~`), `.loc[]`, `.rename()`       | [LEET-03 — Customers Who Never Order.py](./LEET-03-customers-who-never-order.py)             |
|  04 | [Article Views I](https://leetcode.com/problems/article-views-i/)                                 |    Easy    | Boolean Masking, `.loc[]`, `.drop_duplicates()`, `.rename()`, `.sort_values()` | [LEET-04 — Article Views I.py](./LEET-04-article-views.py)                                   |
|  05 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/)                                   |    Easy    | String Operations, `.str.len()`, Boolean Masking, `.loc[]`                     | [LEET-05 — Invalid Tweets.py](./LEET-05-invalid-tweets.py)                                   |
|  06 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/)                 |    Easy    | Boolean Masking, `.str.startswith()`, Modulo, `.where()`, `.sort_values()`     | [LEET-06 — Calculate Special Bonus.py](./LEET-06-calculate-special-bonus.py)                 |

**Progress: 6 / 50 — 12%**

*More challenges are added continuously as I work through the LeetCode Pandas curriculum.*

---

## 🧠 Key Pandas Concepts Covered

### 1. Data Filtering & Selection

* Conditional row filtering with Boolean masks.
* Combining multiple conditions using `&`, `|`, and `~`.
* Explicit row and column selection with `.loc[]`.
* Column projection using lists of column names.
* Membership testing with `.isin()`.

### 2. String Operations

* Measuring string length with `.str.len()`.
* Prefix matching with `.str.startswith()`.
* Applying vectorized string operations directly to Series.

### 3. Data Transformation

* Creating derived columns.
* Conditional value assignment using `.where()`.
* Renaming columns with `.rename()`.
* Removing duplicate rows with `.drop_duplicates()`.
* Sorting results with `.sort_values()`.

### 4. Basic Data Manipulation Patterns

* Boolean Mask → Filter → Transform → Select.
* Vectorized conditional transformations.
* Selecting only the columns required by the problem.
* Building readable and maintainable DataFrame workflows.

---

## 📂 Repository Structure

```text
.
├── README.md
├── LEET-01-big-countries.py
├── LEET-02-recyclable-and-low-fat-products.py
├── LEET-03-customers-who-never-order.py
├── LEET-04-article-views.py
├── LEET-05-invalid-tweets.py
├── LEET-06-calculate-special-bonus.py
└── ...
```

Each solution script follows a consistent structure:

1. **Type-Annotated Function:** Matches the LeetCode Pandas runtime signature.
2. **Docstring:** Describes the problem criteria and expected output.
3. **Boolean / Vectorized Logic:** Uses Pandas-native operations instead of unnecessary loops.
4. **Clean Output:** Returns only the required columns in the required format.

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
python "LEET-06-calculate-special-bonus.py"
```

---

## 🎯 Learning Goal

The goal of this repository is not simply to solve LeetCode problems.

It is to build practical familiarity with **Pandas data manipulation patterns** that are useful in:

* Data Cleaning
* Data Transformation
* ETL Pipelines
* Data Validation
* Data Engineering Workflows

The focus is on understanding **why and when** to use each Pandas operation rather than simply memorizing syntax.

---

## 👤 Author

* **GitHub:** [@ahmed-ibrahim-EG](https://github.com/ahmed-ibrahim-EG)
