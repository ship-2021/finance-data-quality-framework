def null_check(df):
    return df.isnull().sum().sum() == 0

def duplicate_check(df):
    return df["transaction_id"].duplicated().sum() == 0

def negative_amount_check(df):
    return (df["amount"] >= 0).all()