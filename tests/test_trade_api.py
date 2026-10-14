
import requests
import responses


@responses.activate
def test_trade_api_returns_success():
    # Simulate a successful trade API response
    responses.add(
        responses.GET,
        "https://api.example.com/trades/T101",
        json={
            "trade_id": "T101",
            "instrument_id": "AAPL",
            "quantity": 100,
            "price": 150.25,
            "currency": "USD",
            "status": "FILLED"
        },
        status=200
    )

    response = requests.get(
        "https://api.example.com/trades/T101",
        timeout=5
    )

    assert response.status_code == 200

    trade = response.json()
    assert trade["trade_id"] == "T101"
    assert trade["instrument_id"] == "AAPL"
    assert trade["quantity"] == 100
    assert trade["price"] == 150.25
    assert trade["currency"] == "USD"
    assert trade["status"] == "FILLED"


@responses.activate
def test_trade_api_rejects_missing_trade_id():
    responses.add(
        responses.GET,
        "https://api.example.com/trades/T102",
        json={
            "instrument_id": "MSFT",
            "quantity": 200,
            "price": 300.50,
            "currency": "USD",
            "status": "FILLED"
        },
        status=200
    )

    response = requests.get(
        "https://api.example.com/trades/T102",
        timeout=5
    )

    assert response.status_code == 200

    trade = response.json()
    assert "trade_id" not in trade





@responses.activate
def test_trade_api_returns_not_found():
    responses.add(
        responses.GET,
        "https://api.example.com/trades/T999",
        json={"error": "Trade not found"},
        status=404
    )

    response = requests.get(
        "https://api.example.com/trades/T999",
        timeout=5
    )

    assert response.status_code == 404
    assert response.json()["error"] == "Trade not found"





