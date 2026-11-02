# CoinGecko API: 22 endpoints with pricing and code examples

Call 22 CoinGecko endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`coingecko/api-volume-chart`](../models/coingecko/api-volume-chart.md) | Get the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange's ID | $0.008 per call (free daily quota) |
| [`coingecko/coins`](../models/coingecko/coins.md) | Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.)… | $0.008 per call (free daily quota) |
| [`coingecko/coins-categories`](../models/coingecko/coins-categories.md) | Get all the coins categories with market data (market cap, volume, ...) on CoinGecko | $0.008 per call (free daily quota) |
| [`coingecko/coins-categories-list`](../models/coingecko/coins-categories-list.md) | Coins Categories List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged. | $0.008 per call (free daily quota) |
| [`coingecko/coins-contract`](../models/coingecko/coins-contract.md) | Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.)… | $0.008 per call (free daily quota) |
| [`coingecko/coins-contract-market-chart`](../models/coingecko/coins-contract-market-chart.md) | Get the historical chart data including time in UNIX, price, market cap and 24hr volume based on asset platform and particular token… | $0.008 per call (free daily quota) |
| [`coingecko/coins-contract-market-chart-range`](../models/coingecko/coins-contract-market-chart-range.md) | Get the historical chart data within certain time range in UNIX along with price, market cap and 24hr volume based on asset platform and… | $0.008 per call (free daily quota) |
| [`coingecko/coins-history`](../models/coingecko/coins-history.md) | Get the historical data (price, market cap, 24hrs volume, ...) at a given date for a coin based on a particular coin ID | $0.008 per call (free daily quota) |
| [`coingecko/coins-list`](../models/coingecko/coins-list.md) | Get all the supported coins on CoinGecko with coins ID, name and symbol | $0.008 per call (free daily quota) |
| [`coingecko/coins-market-chart`](../models/coingecko/coins-market-chart.md) | Get the historical chart data of a coin including time in UNIX, price, market cap and 24hr volume based on particular coin ID | $0.008 per call (free daily quota) |
| [`coingecko/coins-market-chart-range`](../models/coingecko/coins-market-chart-range.md) | Get the historical chart data of a coin within certain time range in UNIX along with price, market cap and 24hr volume based on particular… | $0.008 per call (free daily quota) |
| [`coingecko/coins-markets`](../models/coingecko/coins-markets.md) | Get all the supported coins with price, market cap, volume and market related data | $0.008 per call (free daily quota) |
| [`coingecko/coins-ohlc`](../models/coingecko/coins-ohlc.md) | Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin ID | $0.008 per call (free daily quota) |
| [`coingecko/coins-tickers`](../models/coingecko/coins-tickers.md) | Get the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID | $0.008 per call (free daily quota) |
| [`coingecko/exchanges`](../models/coingecko/exchanges.md) | Get all the supported exchanges with exchanges' data (ID, name, country, ...) that have active trading volumes on CoinGecko | $0.008 per call (free daily quota) |
| [`coingecko/exchanges-by-id`](../models/coingecko/exchanges-by-id.md) | Get exchange's data (name, year established, country, ...), exchange volume in BTC and top 100 tickers based on exchange's ID | $0.008 per call (free daily quota) |
| [`coingecko/exchanges-list`](../models/coingecko/exchanges-list.md) | Exchanges List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged. | $0.008 per call (free daily quota) |
| [`coingecko/exchanges-tickers`](../models/coingecko/exchanges-tickers.md) | Exchange Tickers by ID from CoinGecko. Returns the official CoinGecko API response unchanged. | $0.008 per call (free daily quota) |
| [`coingecko/search-trending`](../models/coingecko/search-trending.md) | This endpoint allows you query trending search coins, NFTs and categories on CoinGecko in the last 24 hours | $0.008 per call (free daily quota) |
| [`coingecko/simple-price`](../models/coingecko/simple-price.md) | Get the prices of one or more coins by using their unique Coin API IDs, symbols, or names | $0.008 per call (free daily quota) |
| [`coingecko/simple-supported-vs-currencies`](../models/coingecko/simple-supported-vs-currencies.md) | Supported Currencies List from CoinGecko. Returns the official CoinGecko API response unchanged. | $0.008 per call (free daily quota) |
| [`coingecko/simple-token-price`](../models/coingecko/simple-token-price.md) | Get one or more token prices using their token contract addresses | $0.008 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/api-volume-chart", "id": "binance", "days": "1"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
