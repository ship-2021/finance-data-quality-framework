import pandas as pd
from validation.data_quality import *

df = pd.read_csv("data/source_transactions.csv")

def test_null_check():
    assert null_check(df)

def test_duplicate_check():
    assert duplicate_check(df)

def test_negative_amount():
    assert negative_amount_check(df)