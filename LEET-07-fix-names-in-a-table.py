```python
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """Fixes user names by processing the first word.

    Process:
    - Split the name into words
    - Take the first word
    - Convert it to lowercase
    - Capitalize the first character

    Returns:
    - DataFrame containing 'user_id' and corrected 'name',
      ordered by user_id.
    """

    def fix_word(word: str) -> str:
        return word.lower().capitalize()

    # 1. Split each name into words
    users['name'] = users['name'].str.split(' ')

    # 2. Take the first word and apply the function
    users['name'] = users['name'].apply(
        lambda words: fix_word(words[0])
    )

    # 3. Select required columns and sort by user_id
    return users[['user_id', 'name']].sort_values(
        'user_id'
    ).reset_index(drop=True)
```
