
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    """Returns the nth highest distinct salary.

    Criteria:
    - Salaries are sorted in descending order.
    - Duplicate salaries are removed.
    - Return None if n is not positive or fewer than n distinct salaries exist.

    Returns:
    - DataFrame containing the nth highest distinct salary,
      or None if unavailable.
    """
    # 1. Sort salaries in descending order and remove duplicates
    salaries = employee['salary'].drop_duplicates().sort_values(
        ascending=False
    )

    # 2. Validate n and retrieve the requested salary
    salary = (
        salaries.iloc[n - 1]
        if 1 <= n <= len(salaries)
        else None
    )

    # 3. Return the result as a DataFrame
    return pd.DataFrame({f'getNthHighestSalary({n})': [salary]})


if __name__ == '__main__':
    # Sample test case
    data = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300],
    }

    employee_df = pd.DataFrame(data)
    n = -1

    result_df = nth_highest_salary(employee_df, n)
    print(result_df)
