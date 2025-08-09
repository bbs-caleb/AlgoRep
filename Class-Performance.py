import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    scores['total'] = scores.iloc[:, 2:5].sum(axis=1)
    diff = int(scores['total'].max() - scores['total'].min())
    return pd.DataFrame({'difference_in_score': [diff]})