import pandas as pd

df = pd.read_csv("data/source_transactions.csv")

def test_transaction_limit():
    assert (df["amount"] <= 10000).all()