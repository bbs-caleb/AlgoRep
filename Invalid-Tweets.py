1import pandas as pd
2
3def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
4    mask = tweets["content"].str.len() > 15
5    return tweets.loc[mask, ["tweet_id"]]
6