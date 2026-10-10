
import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame,
    department: pd.DataFrame
) -> pd.DataFrame:
    """Finds employees who earn the highest salary in each department.

    Criteria:
    - Compare each employee's salary with the maximum salary in their department.
    - Include all employees tied for the highest salary.

    Returns:
    - DataFrame containing 'Department', 'Employee', and 'Salary'.
    """
    # 1. Get the maximum salary for each department
    max_salary = employee.groupby('departmentId')['salary'].transform('max')

    # 2. Create a boolean mask for employees with the highest salary
    mask = employee['salary'] == max_salary

    # 3. Filter employees and merge with Department to get department names
    result = employee.loc[mask].merge(
        department,
        left_on='departmentId',
        right_on='id'
    )

    # 4. Select and rename the required columns
    return result[['name_y', 'name_x', 'salary']].rename(
        columns={
            'name_y': 'Department',
            'name_x': 'Employee',
            'salary': 'Salary'
        }
    )


if __name__ == '__main__':
    # Sample test case
    employee_data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
        'salary': [70000, 90000, 80000, 60000, 90000],
        'departmentId': [1, 1, 2, 2, 1],
    }

    department_data = {
        'id': [1, 2],
        'name': ['IT', 'Sales'],
    }

    employee_df = pd.DataFrame(employee_data)
    department_df = pd.DataFrame(department_data)

    result_df = department_highest_salary(employee_df, department_df)
    print(result_df)
