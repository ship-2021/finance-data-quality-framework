from validation.reconciliation import *

source = load_data("data/source_transactions.csv")
target = load_data("data/warehouse_transactions.csv")

def test_record_count():
    assert record_count_match(source, target)

def test_amount_total():
    assert amount_match(source, target)