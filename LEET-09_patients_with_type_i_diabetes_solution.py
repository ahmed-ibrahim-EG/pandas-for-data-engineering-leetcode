
import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    """Filters the Patients DataFrame to find patients with Type I Diabetes.

    Criteria:
    - A condition code must start with 'DIAB1'.
    - Condition codes are separated by spaces.
    - The matching code may appear anywhere in the conditions column.

    Returns:
    - DataFrame containing 'patient_id', 'patient_name', and 'conditions'
      for patients with Type I Diabetes.
    """
    # 1. Define a function to check whether any condition starts with 'DIAB1'
    def has_type_i_diabetes(conditions):
        codes = conditions.split()
        return any(code.startswith('DIAB1') for code in codes)

    # 2. Apply the function to create a boolean mask
    mask = patients['conditions'].apply(has_type_i_diabetes)

    # 3. Select matching rows and the required columns using .loc
    return patients.loc[mask, ['patient_id', 'patient_name', 'conditions']]


if __name__ == '__main__':
    # Sample test case
    data = {
        'patient_id': [1, 2, 3, 4, 5],
        'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
        'conditions': [
            'YFEV COUGH',
            '',
            'DIAB100 MYOP',
            'ACNE DIAB100',
            'DIAB201',
        ],
    }

    patients_df = pd.DataFrame(data)
    result_df = find_patients(patients_df)
    print(result_df)
