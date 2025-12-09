1import pandas as pd
2
3def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
4    merged = students.merge(
5        departments[['id']],
6        how='left',
7        left_on = 'department_id',
8        right_on = 'id',
9        suffixes=('', '_dept')
10    )
11
12    invalid = merged[merged['id_dept'].isna()]
13
14    return invalid[['id', 'name']]