import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    merged = students.merge(
        departments,
        left_on='department_id',
        right_on='id',
        how='left',
        indicator=True
    )

    output = merged.loc[merged['_merge']=='left_only'].rename(columns={'id_x':'id', 'name_x': 'name'})[['id', 'name']]
    return output

    