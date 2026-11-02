# Nasdaq API: 17 endpoints with pricing and code examples

Call 17 Nasdaq endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`nasdaq/cryptocurrency-quote`](../models/nasdaq/cryptocurrency-quote.md) | Real-time cryptocurrency price and daily change. Coverage limited to major coins supported by Nasdaq (confirmed: BTC, ETH). | $0.01 per call (free daily quota) |
| [`nasdaq/earnings-calendar`](../models/nasdaq/earnings-calendar.md) | Earnings calendar for a specified date. Past dates include actual EPS and surprise; future dates include EPS forecasts and analyst… | $0.01 per call (free daily quota) |
| [`nasdaq/etf-quote`](../models/nasdaq/etf-quote.md) | Real-time quote and details for an ETF including price, net change, percentage change, volume, and market status. | $0.01 per call (free daily quota) |
| [`nasdaq/index-detail`](../models/nasdaq/index-detail.md) | Detailed quote data for a specific market index including price, net change, percentage change, volume, and daily high/low. | $0.01 per call (free daily quota) |
| [`nasdaq/market-indices`](../models/nasdaq/market-indices.md) | Current values for the NASDAQ Composite index (COMP) including last price, net change, percentage change, volume, and daily high/low. | $0.01 per call (free daily quota) |
| [`nasdaq/mutual-fund-quote`](../models/nasdaq/mutual-fund-quote.md) | Quote and details for a mutual fund including NAV and daily change. Mutual funds show isRealTime=false and have no bid/ask/volume data. | $0.01 per call (free daily quota) |
| [`nasdaq/retail-trading-activity`](../models/nasdaq/retail-trading-activity.md) | Retail Trading Activity Tracker (RTAT) showing the top 5 stocks by percent of retail equity flow, with activity percentage change and… | $0.01 per call (free daily quota) |
| [`nasdaq/search-symbols`](../models/nasdaq/search-symbols.md) | Full-text search across stocks, ETFs, funds, and indices by symbol or company name. Returns scored results with metadata (exchange, asset… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-dividend-history`](../models/nasdaq/stock-dividend-history.md) | Dividend history for a stock including ex-dividend date, current yield, annualized dividend, payout ratio, and historical dividend payment… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-earnings`](../models/nasdaq/stock-earnings.md) | Earnings data for a stock: EPS history (previous and upcoming quarters with consensus vs actual) and upcoming earnings date with analyst… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-financials`](../models/nasdaq/stock-financials.md) | Financial statements for a stock: Income Statement, Balance Sheet, Cash Flow, and Financial Ratios. Returns 4 periods of data (annual or… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-historical-quotes`](../models/nasdaq/stock-historical-quotes.md) | Historical OHLCV price data for a symbol. Without explicit date range, defaults to one year ending today. | $0.01 per call (free daily quota) |
| [`nasdaq/stock-institutional-holdings`](../models/nasdaq/stock-institutional-holdings.md) | Institutional holdings data for a stock: ownership summary, active/new/sold-out position counts, and individual holder transactions sorted… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-news`](../models/nasdaq/stock-news.md) | Latest news headlines for a stock symbol. Returns articles where the symbol appears as primary or related symbol, with title, publisher,… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-quote`](../models/nasdaq/stock-quote.md) | Real-time quote for a single equity including last sale price, net change, percentage change, bid/ask, volume, 52-week range, and market… | $0.01 per call (free daily quota) |
| [`nasdaq/stock-screener`](../models/nasdaq/stock-screener.md) | Screen stocks by exchange and market capitalization. Returns paginated results with symbol, name, last sale, change, and market cap. | $0.01 per call (free daily quota) |
| [`nasdaq/stock-sec-filings`](../models/nasdaq/stock-sec-filings.md) | SEC filings for a stock symbol including 10-K, 10-Q, 8-K, and other filing types. Returns filing metadata with links to view documents. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/cryptocurrency-quote", "symbol": "BTC"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
