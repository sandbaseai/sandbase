# StockAnalysis API: 6 endpoints with pricing and code examples

Call 6 StockAnalysis endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`stockanalysis/market-movers-premarket`](../models/stockanalysis/market-movers-premarket.md) | Top gainers, losers, and most active stocks in the pre-market session. Each category contains query metadata and a data array of stock… | $0.01 per call (free daily quota) |
| [`stockanalysis/search-stocks`](../models/stockanalysis/search-stocks.md) | Full-text search for stocks and ETFs by company name or ticker symbol. Returns matches across multiple global exchanges including US,… | $0.01 per call (free daily quota) |
| [`stockanalysis/stock-financials-income`](../models/stockanalysis/stock-financials-income.md) | Detailed income statement for a stock. Returns annual financial data including revenue, gross profit, operating income, net income, EPS,… | $0.01 per call (free daily quota) |
| [`stockanalysis/stock-list`](../models/stockanalysis/stock-list.md) | Stocks from a curated stock list by URL slug. Returns the list title, description, stock count, and an array of stock entries with symbol,… | $0.01 per call (free daily quota) |
| [`stockanalysis/stock-overview`](../models/stockanalysis/stock-overview.md) | Real-time quote overview for a stock symbol. Returns current price, change, volume, exchange, market status, 52-week range, and… | $0.01 per call (free daily quota) |
| [`stockanalysis/stock-statistics`](../models/stockanalysis/stock-statistics.md) | Comprehensive statistics for a stock organized into categorized sections. Each section contains a text summary and a data array of… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/market-movers-premarket"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
