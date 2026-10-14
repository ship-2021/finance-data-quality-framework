import pandas as pd

df = pd.read_csv("data/source_transactions.csv")

def test_financial_threshold():
    assert (df["amount"] <= 10000).all()

def test_total_amount():
    assert df["amount"].sum() == 7000