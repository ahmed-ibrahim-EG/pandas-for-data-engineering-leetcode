import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """Calculates the bonus for each employee.

    Criteria:
    - employee_id is odd
    - name does not start with 'M'

    Bonus:
    - 100% of salary if both conditions are met
    - 0 otherwise

    Returns:
    - DataFrame containing 'employee_id' and 'bonus',
      ordered by employee_id.
    """
    # 1. Define boolean mask for employees who qualify for a bonus
    mask = (employees['employee_id'] % 2 == 1) & (
        ~employees['name'].str.startswith('M')
    )

    # 2. Assign salary as bonus when mask is True, otherwise 0
    employees['bonus'] = employees['salary'].where(mask, 0)

    # 3. Select required columns and sort by employee_id
    return employees[['employee_id', 'bonus']].sort_values(
        'employee_id'
    ).reset_index(drop=True)
