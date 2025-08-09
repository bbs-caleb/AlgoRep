import pandas as pd

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    from functools import reduce
    import operator

    common_perms = reduce(operator.and_, user_permissions['permissions'])
    any_perms    = reduce(operator.or_ , user_permissions['permissions'])
    return pd.DataFrame({'common_perms':[common_perms], 'any_perms':[any_perms]})

    