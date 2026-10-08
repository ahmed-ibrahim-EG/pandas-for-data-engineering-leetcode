```python
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """Fixes user names so the first character is uppercase
    and all remaining characters are lowercase.

    Criteria:
    - First character is uppercase
    - Remaining characters are lowercase

    Returns:
    - DataFrame containing 'user_id' and corrected 'name',
      ordered by user_id.
    """

    def fix_name(name: str) -> str:
        return name[0].upper() + name[1:].lower()

    # 1. Split each name into words
    users['name'] = users['name'].str.split(' ')

    # 2. Join the words back together
    users['name'] = users['name'].str.join(' ')

    # 3. Apply the function to the complete name
    users['name'] = users['name'].apply(fix_name)

    # 4. Select required columns and sort by user_id
    return users.loc[:, ['user_id', 'name']].sort_values(
        'user_id'
    ).reset_index(drop=True)
```
