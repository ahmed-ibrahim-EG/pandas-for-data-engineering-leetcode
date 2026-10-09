# 🐼 LeetCode Pandas Solutions

### *Building Practical Data Manipulation Skills for Data Engineering*

A structured collection of my solutions to LeetCode Pandas problems, focused on developing practical data manipulation skills using Python and Pandas.

The goal is to strengthen my understanding of data filtering, transformation, string operations, sorting, and DataFrame manipulation through hands-on problem-solving.

---

## 📊 Progress

**10 / 30 Problems Completed — 33.3%**

```text
Progress: [██████░░░░░░░░░░░░░░] 33.3%
```

---

## 📚 Problems & Solutions

| # | Problem | Difficulty | Key Concepts | Solution |
|---|---|---|---|---|
| 01 | [Big Countries](https://leetcode.com/problems/big-countries/) | Easy | Boolean Masking, `.loc[]`, Column Projection | `LEET-01-big-countries.py` |
| 02 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy | Multiple Conditions (`&`), Boolean Indexing | `LEET-02-recyclable-and-low-fat-products.py` |
| 03 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | Easy | `.isin()`, `~`, `.loc[]`, `.rename()` | `LEET-03-customers-who-never-order.py` |
| 04 | [Article Views I](https://leetcode.com/problems/article-views-i/) | Easy | Boolean Masking, `.loc[]`, `.drop_duplicates()`, `.rename()`, `.sort_values()` | `LEET-04-article-views.py` |
| 05 | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets/) | Easy | String Operations, `.str.len()`, Boolean Masking, `.loc[]` | `LEET-05-invalid-tweets.py` |
| 06 | [Calculate Special Bonus](https://leetcode.com/problems/calculate-special-bonus/) | Easy | Boolean Masking, `.str.startswith()`, Modulo, `.where()`, `.sort_values()` | `LEET-06-calculate-special-bonus.py` |
| 07 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | Easy | String Operations, `.str.split()`, `.str.join()`, `.apply()`, String Slicing, `.sort_values()` | `LEET-07-fix-names-in-a-table.py` |
| 08 | [Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails/) | Easy | Regular Expressions, `.str.match()`, Boolean Masking, `.loc[]` | `LEET-08_valid_emails_solution.py` |
| 09 | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/) | Easy | `.str.split()`, `.apply()`, Custom Functions, `any()`, `.startswith()`, Boolean Masking | `LEET-09_patients_with_type_i_diabetes_solution.py` |
| 10 | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | Medium | `.drop_duplicates()`, `.sort_values()`, `.iloc[]`, Conditional Logic, DataFrame Construction | `LEET-10_nth_highest_salary_solution.py` |

---

## 🧠 Concepts Practiced

### 1. Data Filtering & Selection
- Boolean Masking and Boolean Indexing
- `.loc[]` and column projection
- `.isin()` and negation with `~`
- Combining conditions with `&` and `|`
- Conditional filtering

### 2. String Operations
- `.str.len()`
- `.str.startswith()`
- `.str.split()`
- `.str.join()`
- `.str.match()`
- String slicing
- Regular expressions (Regex)
- String transformation and normalization

### 3. Data Transformation
- `.where()`
- `.apply()`
- Custom functions
- `any()`
- Creating calculated columns
- Conditional value selection

### 4. Sorting, Deduplication & Indexing
- `.drop_duplicates()`
- `.rename()`
- `.sort_values()`
- `.reset_index()`
- `.iloc[]`
- Handling distinct values
- Sorting and retrieving ranked values

### 5. DataFrame Construction & Output
- `pd.DataFrame()`
- Dynamic column names
- Returning the expected output schema
- Handling missing results with `None`

---

## 📁 Repository Structure

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
├── LEET-08_valid_emails_solution.py
├── LEET-09_patients_with_type_i_diabetes_solution.py
├── LEET-10_nth_highest_salary_solution.py
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3
- Pandas

### Installation

Clone the repository:

```bash
git clone https://github.com/ahmed-ibrahim-EG/pandas-leetcode-solutions.git
```

Navigate to the project directory:

```bash
cd pandas-leetcode-solutions
```

Install the required library:

```bash
pip install pandas
```

Run a solution:

```bash
python LEET-10_nth_highest_salary_solution.py
```

---

## 🎯 Learning Goals

This repository is part of my ongoing journey toward becoming a **Data Engineer**.

By working through these problems, I aim to improve my ability to:

- Manipulate and transform structured datasets using Pandas.
- Write clear, readable, and maintainable Python code.
- Apply data-cleaning and data-filtering techniques.
- Understand the relationship between SQL operations and Pandas methods.
- Build a strong foundation for practical ETL and data pipeline development.

The repository will continue to grow toward **30 LeetCode Pandas problems**, with a focus on understanding the logic behind each solution rather than simply memorizing code.

---

## 👤 Author

**Ahmed Ibrahim**

Computer Science & Data Science Student  
Aspiring Data Engineer

- **GitHub:** [ahmed-ibrahim-EG](https://github.com/ahmed-ibrahim-EG)
- **LinkedIn:** [Ahmed Ibrahim](https://linkedin.com/in/ahmed-ibrahim-36600b2a5)
