
from tools.crypto_history import get_historical_data

def test_history():
    data = get_historical_data("BTC", 3, "binance")
    assert len(data) >= 1
