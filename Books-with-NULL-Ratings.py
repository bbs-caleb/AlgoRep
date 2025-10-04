import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    out = (books
           .loc[lambda d: d['rating'].isna(), ['book_id', 'title', 'author', 'published_year']]
           .sort_values('book_id', ascending=True, kind='stable')
           .reset_index(drop=True))
    return out
