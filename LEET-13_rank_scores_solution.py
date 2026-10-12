import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """Ranks game scores from highest to lowest.

    Criteria:
    - Rank scores in descending order.
    - Assign the same rank to equal scores.
    - Use consecutive ranks without gaps after ties.

    Returns:
    - DataFrame containing 'score' and 'rank', ordered by score descending.
    """
    # 1. Create a rank column using dense ranking
    scores.loc[:, 'rank'] = scores['score'].rank(
        method='dense',
        ascending=False
    )

    # 2. Sort scores from highest to lowest
    result = scores.sort_values(by='score', ascending=False)

    # 3. Select the required columns
    return result[['score', 'rank']]


if __name__ == '__main__':
    # Sample test case
    scores_data = {
        'id': [1, 2, 3, 4, 5, 6],
        'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65],
    }

    scores_df = pd.DataFrame(scores_data)

    result_df = order_scores(scores_df)
    print(result_df)
