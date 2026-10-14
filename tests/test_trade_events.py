
def test_valid_trade_event_has_required_data():
    event = {
        "event_id": "EVT001",
        "trade_id": "T101",
        "instrument_id": "AAPL",
        "quantity": 100,
        "price": 150.25,
        "event_type": "TRADE_EXECUTED"
    }

    assert event["event_id"] is not None
    assert event["trade_id"] is not None
    assert event["instrument_id"] is not None
    assert event["quantity"] > 0
    assert event["price"] > 0
    assert event["event_type"] == "TRADE_EXECUTED"


def test_duplicate_trade_events_are_detected():
    events = [
        {"event_id": "EVT001", "trade_id": "T101"},
        {"event_id": "EVT001", "trade_id": "T101"},
    ]

    event_ids = [event["event_id"] for event in events]

    assert len(event_ids) != len(set(event_ids))
