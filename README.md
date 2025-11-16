🚀 Crypto MCP Server
---
A FastAPI-powered microservice providing real-time crypto prices, historical market data, and latest crypto news through clean, developer-friendly REST endpoints.

🔥 Overview
---
The Crypto MCP Server is a lightweight API service designed to fetch and serve cryptocurrency data such as:

✅ Live Price (via Binance API)

✅ Historical Price Data (via CoinGecko API)

✅ Crypto News (via CryptoCompare API)

Useful for AI agents, dashboards, trading bots, backend integrations, and MCP-based workflows.

🧩 Features
---
📌 1. Real-Time Market Price

Fetches the latest USDT pair price for any symbol

Uses Binance public market API

Fast response, low latency

📌 2. Historical Market Data

Uses CoinGecko market_chart API

Supports custom day ranges

Returns timestamp–price pairs for plotting

📌 3. Latest Crypto News

Pulls top news from CryptoCompare

Clean & minimal response objects

Useful for daily market insights

⚙️ Tech Stack
---
Layer	Technology

Server	FastAPI

HTTP Client	requests

APIs Used	Binance, CoinGecko, CryptoCompare

Language	Python 3.10+
---
📁 Project Structure
crypto-mcp-server/
│
├── server.py               # Main FastAPI application
├── requirements.txt        # Dependencies
├── README.md               # Documentation
└── .env (optional)         # Env variables if needed

🚀 Getting Started
---
1️⃣ Clone the Repository
---
git clone https://github.com/your-username/crypto-mcp-server.git

cd crypto-mcp-server

2️⃣ Install Dependencies
---
pip install -r requirements.txt

3️⃣ Run the Server
---
uvicorn server:app --reload

Your API will now be available at:
---

👉 http://127.0.0.1:8000

📚 API Documentation
---
Once the server is running, interactive API docs are available at:

Swagger UI: /docs

ReDoc: /redoc

🛠️ Development Notes
---
Binance API supports only SYMBOLUSDT pairs

CoinGecko API rate-limits aggressively; caching recommended

CryptoCompare may occasionally deliver slower payloads

📈 Planned Improvements
---
Add support for Open, High, Low, Close candlestick data

Add 24h change, volume, and market cap endpoints

Redis caching to improve speed

Docker deployment

Full MCP tool definition JSON

🤝 Contributing
---
Contributions are welcome!

Fork the repository

Create a feature branch

Submit a PR

🛡️ License
---
This project is released under the MIT License.

👤 Author
---
Prachi Aggarwal
🌐 GitHub: prachiagg06
