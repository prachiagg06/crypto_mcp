
import ccxt
from tools.cache import cache
from tools.exceptions import CryptoAPIException

def get_realtime_price(symbol, exchange_name):
    key = f"{symbol}_{exchange_name}"
    cached = cache.get(key)
    if cached:
        return cached
    try:
        exchange = getattr(ccxt, exchange_name)()
        ticker = exchange.fetch_ticker(f"{symbol}/USDT")
        price = ticker["last"]
        cache.set(key, price)
        return price
    except:
        raise CryptoAPIException("Realtime fetch failed")
