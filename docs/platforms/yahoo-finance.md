# Yahoo Finance API: 6 endpoints with pricing and code examples

Call 6 Yahoo Finance endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yahoo-finance/closing-price`](../models/yahoo-finance/closing-price.md) | Return the official daily closing price for a single ticker on one specific calendar date, interpreted in the listing exchange's local… | $0.05 per call |
| [`yahoo-finance/company-profile`](../models/yahoo-finance/company-profile.md) | Obtain a detailed company profile including business summary, key executives, sector, industry, and financial metrics such as revenue,… | $0.05 per call |
| [`yahoo-finance/historical-data`](../models/yahoo-finance/historical-data.md) | Extract historical OHLCV price data for a single ticker over a configurable date range and interval. Returns timestamped records suitable… | $0.05 per call |
| [`yahoo-finance/quote`](../models/yahoo-finance/quote.md) | Retrieve real-time stock quotes including current price, bid/ask, volume, market cap, and market status for one or more tickers. Supports… | $0.05 per call |
| [`yahoo-finance/search-tickers`](../models/yahoo-finance/search-tickers.md) | Search for stock tickers and companies by name or keyword. Returns matching equities, ETFs, and other instruments across global exchanges… | $0.05 per call |
| [`yahoo-finance/stock-news`](../models/yahoo-finance/stock-news.md) | Gather the latest financial news articles related to a specified stock ticker. Returns headlines, publishers, links, publish timestamps,… | $0.05 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/closing-price", "date": "2026-10-01", "symbol": "AAPL"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
