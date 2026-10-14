import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def record_count_match(source, target):
    return len(source) == len(target)

def amount_match(source, target):
    return source["amount"].sum() == target["amount"].sum()