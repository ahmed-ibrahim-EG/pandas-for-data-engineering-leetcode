
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int):
    """Returns the nth highest distinct salary.

    Criteria:
    - Salaries must be sorted in descending order.
    - Duplicate salaries must be removed.
    - Return None if fewer than n distinct salaries exist.

    Returns:
    - The nth highest distinct salary, or None if unavailable.
    """
    # 1. Sort salaries in descending order and remove duplicates
    salaries = employee['salary'].drop_duplicates().sort_values(
        ascending=False
    )

    # 2. Return the nth highest salary if enough distinct salaries exist
    if len(salaries) < n:
        return None

    return salaries.iloc[n - 1]


if __name__ == '__main__':
    # Sample test case
    data = {
        'id': [1, 2, 3, 4],
        'salary': [100, 200, 200, 300],
    }

    employee_df = pd.DataFrame(data)
    n = 2

    result = nth_highest_salary(employee_df, n)
    print(result)
