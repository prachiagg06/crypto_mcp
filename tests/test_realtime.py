
from tools.crypto_realtime import get_realtime_price

def test_realtime_price():
    price = get_realtime_price("BTC", "binance")
    assert price > 0
