# MarketBeat API: 13 endpoints with pricing and code examples

Call 13 MarketBeat endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`marketbeat/analyst-ratings`](../models/marketbeat/analyst-ratings.md) | Get historical monthly analyst rating counts and breakdown. Returns time series data with buy, hold, sell, strong buy counts and total… | $0.02 per call |
| [`marketbeat/competitors`](../models/marketbeat/competitors.md) | Get competitor comparison data for a stock. Returns multiple comparison tables covering earnings/valuation, profitability, and analyst… | $0.01 per call (free daily quota) |
| [`marketbeat/earnings`](../models/marketbeat/earnings.md) | Get earnings estimates and historical earnings data including EPS estimates (low, high, average), number of analyst estimates, revenue… | $0.01 per call (free daily quota) |
| [`marketbeat/financial-statements`](../models/marketbeat/financial-statements.md) | Get financial statements including annual and quarterly income statements, cash flow statements, balance sheets, and metrics/ratios. Each… | $0.02 per call |
| [`marketbeat/insider-trades`](../models/marketbeat/insider-trades.md) | Get recent insider transactions for a stock including transaction dates, insider names, buy/sell actions, share counts, average share… | $0.01 per call (free daily quota) |
| [`marketbeat/institutional-ownership`](../models/marketbeat/institutional-ownership.md) | Get institutional ownership data including top institutional holders, their share positions, market value, portfolio percentage, quarterly… | $0.01 per call (free daily quota) |
| [`marketbeat/marketrank`](../models/marketbeat/marketrank.md) | Get MarketRank scores and component details for a stock. Includes overall percentile score and individual category scores for Analyst… | $0.01 per call (free daily quota) |
| [`marketbeat/profitability-metrics`](../models/marketbeat/profitability-metrics.md) | Get key profitability, valuation, debt, and other financial metrics for a stock. Returns a flat key-value mapping of metrics including… | $0.01 per call (free daily quota) |
| [`marketbeat/search-stocks`](../models/marketbeat/search-stocks.md) | Search for stock tickers by company name or symbol. Returns matching stocks with ticker, exchange, name, and URL path. | $0.01 per call (free daily quota) |
| [`marketbeat/short-interest`](../models/marketbeat/short-interest.md) | Get short interest statistics and historical short interest data for a stock. Summary includes current short interest, change vs previous… | $0.01 per call (free daily quota) |
| [`marketbeat/stock-forecast`](../models/marketbeat/stock-forecast.md) | Get analyst forecast data including consensus rating breakdown over time periods, consensus comparison against sector and S&P 500, and a… | $0.01 per call (free daily quota) |
| [`marketbeat/stock-headlines`](../models/marketbeat/stock-headlines.md) | Get recent news headlines for a stock from various sources. Each headline includes the title, URL, relative date, and source domain. | $0.01 per call (free daily quota) |
| [`marketbeat/stock-overview`](../models/marketbeat/stock-overview.md) | Get comprehensive stock overview including current price, day change, key stats, company description, and company calendar for a given… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "marketbeat/analyst-ratings", "ticker": "AAPL"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
