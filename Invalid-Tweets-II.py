1import pandas as pd
2
3def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
4    s = tweets["content"]
5
6    too_long = s.str.len() > 140
7    too_many_mentions = s.str.count(r"@") > 3
8    too_many_hashtags = s.str.count(r"#") > 3
9
10    invalid = too_long | too_many_mentions | too_many_hashtags
11
12    return (tweets.loc[invalid, ["tweet_id"]].sort_values("tweet_id").reset_index(drop=True))
13