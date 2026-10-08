import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """Finds authors who viewed at least one of their own articles.

    Criteria:
    - author_id == viewer_id

    Returns:
    - DataFrame containing unique 'id' values sorted in ascending order.
    """
    # 1. Define boolean mask where the author viewed their own article
    mask = views['author_id'] == views['viewer_id']

    # 2. Select matching rows and pick the required column using .loc
    result = views.loc[mask, ['author_id']]

    # 3. Remove duplicate authors
    result = result.drop_duplicates()

    # 4. Rename column to match required output format
    result = result.rename(columns={'author_id': 'id'})

    # 5. Sort IDs in ascending order
    return result.sort_values('id').reset_index(drop=True)
