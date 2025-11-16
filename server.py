
# # from fastapi import FastAPI
# # import requests

# # app = FastAPI(title="Crypto MCP Server")

# # @app.get("/")
# # def home():
# #     return {
# #         "message": "🚀 Crypto MCP Server is running!",
# #         "endpoints": {
# #             "price": "/tools/crypto-price?symbol=BTC",
# #             "history": "/tools/crypto-history?symbol=BTC&days=30",
# #             "news": "/tools/crypto-news",
# #             "docs": "/docs"
# #         }
# #     }

# # # -----------------------
# # # 1) REAL-TIME PRICE
# # # -----------------------

# # @app.get("/tools/crypto-price")
# # def crypto_price(symbol: str = "BTC"):
# #     url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}USDT"
# #     response = requests.get(url).json()

# #     if "price" not in response:
# #         return {"error": "Invalid symbol or price not found"}

# #     return {
# #         "symbol": symbol.upper(),
# #         "price": float(response["price"])
# #     }

# # # -----------------------
# # # 2) HISTORICAL DATA
# # # -----------------------

# # @app.get("/tools/crypto-history")
# # def crypto_history(symbol: str = "BTC", days: int = 30):
# #     url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}/market_chart"
# #     params = {"vs_currency": "usd", "days": days}

# #     response = requests.get(url, params=params).json()

# #     if "prices" not in response:
# #         return {"error": "History not available"}

# #     history = [
# #         {"timestamp": t, "price": p}
# #         for t, p in response["prices"]
# #     ]

# #     return {
# #         "symbol": symbol.upper(),
# #         "days": days,
# #         "history": history
# #     }

# # # -----------------------
# # # 3) CRYPTO NEWS
# # # -----------------------

# # @app.get("/tools/crypto-news")
# # def crypto_news():
# #     url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
# #     response = requests.get(url).json()

# #     news_list = []

# #     for item in response.get("Data", [])[:10]:
# #         news_list.append({
# #             "title": item.get("title"),
# #             "source": item.get("source"),
# #             "url": item.get("url")
# #         })

# #     return {"count": len(news_list), "news": news_list}


# from fastapi import FastAPI
# import requests

# app = FastAPI(title="Crypto MCP Server")

# # -----------------------
# # HOME ENDPOINT
# # -----------------------

# @app.get("/")
# def home():
#     return {
#         "message": "🚀 Crypto MCP Server is running!",
#         "endpoints": {
#             "price": "/tools/crypto-price?symbol=BTC",
#             "history": "/tools/crypto-history?symbol=BTC&days=30",
#             "news": "/tools/crypto-news",
#             "docs": "/docs"
#         }
#     }


# # -----------------------
# # 1) REAL-TIME PRICE
# # -----------------------

# @app.get("/tools/crypto-price")
# def crypto_price(symbol: str = "BTC"):
#     symbol = symbol.upper()
#     url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

#     try:
#         response = requests.get(url).json()
#     except Exception:
#         return {"error": "Failed to fetch price"}

#     if "price" not in response:
#         return {"error": f"Price not found for symbol {symbol}"}

#     return {
#         "symbol": symbol,
#         "price": float(response["price"])
#     }


# # -----------------------
# # 2) HISTORICAL DATA
# # -----------------------

# @app.get("/tools/crypto-history")
# def crypto_history(symbol: str = "BTC", days: int = 30):
#     symbol = symbol.lower()

#     url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
#     params = {"vs_currency": "usd", "days": days}

#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#     }

#     try:
#         response = requests.get(url, params=params, headers=headers).json()
#     except Exception:
#         return {"error": "Failed to fetch history"}

#     # If API returns an error message
#     if "prices" not in response:
#         return {
#             "error": f"Historical data not found for {symbol.upper()}",
#             "details": response
#         }

#     history = [
#         {"timestamp": t, "price": p}
#         for t, p in response["prices"]
#     ]

#     return {
#         "symbol": symbol.upper(),
#         "days": days,
#         "history": history
#     }



# # -----------------------
# # 3) CRYPTO NEWS
# # -----------------------

# @app.get("/tools/crypto-news")
# def crypto_news():
#     url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"

#     try:
#         response = requests.get(url).json()
#     except Exception:
#         return {"error": "Failed to fetch news"}

#     news_entries = response.get("Data", [])

#     if not news_entries:
#         return {"error": "No news available"}

#     news_list = [
#         {
#             "title": item.get("title"),
#             "source": item.get("source"),
#             "url": item.get("url")
#         }
#         for item in news_entries[:10]
#     ]

#     return {
#         "count": len(news_list),
#         "news": news_list
#     }



from fastapi import FastAPI
import requests

app = FastAPI(title="Crypto MCP Server")

# ----------------------------------------------------
# COINGECKO SYMBOL → ID MAPPING (IMPORTANT FIX)
# ----------------------------------------------------
COINGECKO_MAP = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "XRP": "ripple",
    "DOGE": "dogecoin",
    "SOL": "solana",
    "ADA": "cardano",
    "MATIC": "matic-network"
}


# ----------------------------------------------------
# HOME ENDPOINT
# ----------------------------------------------------
@app.get("/")
def home():
    return {
        "message": "🚀 Crypto MCP Server is running!",
        "endpoints": {
            "price": "/tools/crypto-price?symbol=BTC",
            "history": "/tools/crypto-history?symbol=BTC&days=30",
            "news": "/tools/crypto-news",
            "docs": "/docs"
        }
    }


# ----------------------------------------------------
# 1) REAL-TIME PRICE (Binance)
# ----------------------------------------------------
@app.get("/tools/crypto-price")
def crypto_price(symbol: str = "BTC"):
    symbol = symbol.upper()
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

    try:
        response = requests.get(url).json()
    except Exception:
        return {"error": "Failed to fetch price"}

    if "price" not in response:
        return {"error": f"Price not found for symbol {symbol}"}

    return {
        "symbol": symbol,
        "price": float(response["price"])
    }


# ----------------------------------------------------
# 2) HISTORICAL DATA (CoinGecko)
# ----------------------------------------------------
@app.get("/tools/crypto-history")
def crypto_history(symbol: str = "BTC", days: int = 30):

    symbol = symbol.upper()

    # Validate symbol
    if symbol not in COINGECKO_MAP:
        return {"error": f"Symbol {symbol} not supported"}

    coin_id = COINGECKO_MAP[symbol]

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, params=params, headers=headers).json()
    except Exception:
        return {"error": "Failed to fetch historical data"}

    if "prices" not in response:
        return {
            "error": f"Historical data not found for {symbol}",
            "details": response
        }

    history = [
        {"timestamp": t, "price": p}
        for t, p in response["prices"]
    ]

    return {
        "symbol": symbol,
        "days": days,
        "history": history
    }


# ----------------------------------------------------
# 3) CRYPTO NEWS (CryptoCompare)
# ----------------------------------------------------
@app.get("/tools/crypto-news")
def crypto_news():
    url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"

    try:
        response = requests.get(url).json()
    except Exception:
        return {"error": "Failed to fetch news"}

    articles = response.get("Data", [])

    if not articles:
        return {"error": "No news found"}

    news_list = [
        {
            "title": item.get("title"),
            "source": item.get("source"),
            "url": item.get("url")
        }
        for item in articles[:10]
    ]

    return {
        "count": len(news_list),
        "news": news_list
    }
