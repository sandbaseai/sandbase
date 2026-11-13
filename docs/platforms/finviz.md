# Finviz API: 5 endpoints with pricing and code examples

Call 5 Finviz endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`finviz/insider-trading`](../models/finviz/insider-trading.md) | List recent insider transactions in US stocks from Finviz with insider, relationship, transaction type, shares, price and value, filtered… | $0.01 per call |
| [`finviz/market-movers`](../models/finviz/market-movers.md) | List today's US stock market movers on Finviz such as top gainers, top losers, new highs and unusual volume, with price, change and volume. | $0.01 per call |
| [`finviz/news-sentiment`](../models/finviz/news-sentiment.md) | Get recent news headlines for a US ticker from Finviz with source, time and a sentiment score for each headline. | $0.01 per call |
| [`finviz/screener`](../models/finviz/screener.md) | Screen US stocks on Finviz with filter codes for valuation, performance, technicals and fundamentals, returning matching tickers with… | $0.01 per call |
| [`finviz/ticker-sectors`](../models/finviz/ticker-sectors.md) | Get the sector, industry and multi-period performance of a list of US tickers from Finviz. | $0.01 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "finviz/insider-trading"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
