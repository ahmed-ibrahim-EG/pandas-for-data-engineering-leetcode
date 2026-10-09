
import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """Filters the Users DataFrame to find users with valid email addresses.

    Criteria:
    - Prefix must start with an English letter (A-Z or a-z).
    - Prefix may contain letters, digits, underscores, periods, and dashes.
    - Domain must be exactly '@leetcode.com' in lowercase.

    Returns:
    - DataFrame containing all columns for users with valid emails.
    """
    # 1. Define boolean mask using regex to validate email addresses
    mask = users['mail'].str.match(
        r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    )

    # 2. Select rows satisfying the mask using .loc
    return users.loc[mask]


if __name__ == '__main__':
    # Sample test case
    data = {
        'user_id': [1, 2, 3, 4, 5, 6, 7],
        'name': [
            'Winston',
            'Jonathan',
            'Annabelle',
            'Sally',
            'Marwan',
            'David',
            'Shapiro',
        ],
        'mail': [
            'winston@leetcode.com',
            'jonathanisgreat',
            'bella-@leetcode.com',
            'sally.come@leetcode.com',
            'quarz#2020@leetcode.com',
            'david69@gmail.com',
            '.shapo@leetcode.com',
        ],
    }

    users_df = pd.DataFrame(data)
    result_df = valid_emails(users_df)
    print(result_df)
