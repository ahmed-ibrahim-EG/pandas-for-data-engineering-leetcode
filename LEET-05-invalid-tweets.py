import pandas as pd


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    """Finds tweets whose content length is strictly greater than 15.

    Criteria:
    - len(content) > 15

    Returns:
    - DataFrame containing 'tweet_id' for invalid tweets.
    """
    # 1. Define boolean mask for tweets with more than 15 characters
    mask = tweets['content'].str.len() > 15

    # 2. Select matching rows and pick only the required column using .loc
    return tweets.loc[mask, ['tweet_id']]
