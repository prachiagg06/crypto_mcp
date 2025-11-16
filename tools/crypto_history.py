
import ccxt
from datetime import datetime
from tools.exceptions import CryptoAPIException

def get_historical_data(symbol, days, exchange_name):
    try:
        ex = getattr(ccxt, exchange_name)()
        since = ex.milliseconds() - days * 24 * 60 * 60 * 1000
        ohlcv = ex.fetch_ohlcv(f"{symbol}/USDT", "1d", since=since)
        return [
            {
                "timestamp": c[0],
                "date": datetime.utcfromtimestamp(c[0] / 1000).strftime("%Y-%m-%d"),
                "open": c[1], "high": c[2], "low": c[3], "close": c[4], "volume": c[5]
            }
            for c in ohlcv
        ]
    except:
        raise CryptoAPIException("History fetch failed")
