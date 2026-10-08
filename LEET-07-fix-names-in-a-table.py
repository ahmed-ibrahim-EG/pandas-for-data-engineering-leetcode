import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """Fixes user names so the first character is uppercase
    and the remaining characters are lowercase.

    Criteria:
    - First character is uppercase
    - Remaining characters are lowercase

    Returns:
    - DataFrame containing 'user_id' and corrected 'name',
      ordered by user_id.
    """
    # 1. Convert names to title case
    users['name'] = users['name'].str.lower().str.title()

    # 2. Sort by user_id and select the required columns
    return users.loc[:, ['user_id', 'name']].sort_values(
        'user_id'
    ).reset_index(drop=True)
