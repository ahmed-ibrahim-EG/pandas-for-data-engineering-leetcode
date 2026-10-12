import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """Deletes duplicate emails while keeping the row with the smallest id.

    Criteria:
    - Identify duplicate emails using the 'email' column.
    - Keep only the row with the smallest id for each email.
    - Modify the original DataFrame in place.

    Returns:
    - None. The original DataFrame is modified in place.
    """
    # 1. Sort rows by id in ascending order
    person.sort_values(by='id', inplace=True)

    # 2. Remove duplicate emails, keeping the first occurrence
    person.drop_duplicates(
        subset=['email'],
        keep='first',
        inplace=True
    )


if __name__ == '__main__':
    # Sample test case
    person_data = {
        'id': [1, 2, 3],
        'email': [
            'john@example.com',
            'bob@example.com',
            'john@example.com'
        ],
    }

    person_df = pd.DataFrame(person_data)

    delete_duplicate_emails(person_df)
    print(person_df)
