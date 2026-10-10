
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Finds the second highest distinct salary from the Employee DataFrame.

    Criteria:
    - Salaries must be distinct.
    - Salaries are sorted in descending order.
    - If no second highest salary exists, return None.

    Returns:
    - DataFrame containing 'SecondHighestSalary'.
    """
    # 1. Remove duplicate salaries and sort them in descending order
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    # 2. Return the second highest salary if it exists, otherwise None
    second_salary = salaries.iloc[1] if len(salaries) > 1 else None

    # 3. Return the result using the required column name
    return pd.DataFrame({'SecondHighestSalary': [second_salary]})


if __name__ == '__main__':
    # Sample test case
    data = {
        'id': [1, 2, 3],
        'salary': [100, 200, 300],
    }

    employee_df = pd.DataFrame(data)
    result_df = second_highest_salary(employee_df)
    print(result_df)
