import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    dep_ids = pd.Index(departments['id']).unique()
    invalid = ~students['department_id'].isin(dep_ids)
    return students.loc[invalid, ['id', 'name']]