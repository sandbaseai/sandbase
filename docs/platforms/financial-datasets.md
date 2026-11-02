# Financial Datasets API: 24 endpoints with pricing and code examples

Call 24 Financial Datasets endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`financial-datasets/analyst-estimates`](../models/financial-datasets/analyst-estimates.md) | Get Analyst Estimates from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/company-facts`](../models/financial-datasets/company-facts.md) | Get Company Facts from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/earnings`](../models/financial-datasets/earnings.md) | Get the most recent earnings snapshot for a ticker. Optional change fields are returned only when available. | $0.02 per call |
| [`financial-datasets/filings`](../models/financial-datasets/filings.md) | Get Company SEC Filings from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/filings-items`](../models/financial-datasets/filings-items.md) | Get SEC Filing Items from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/financial-metrics`](../models/financial-datasets/financial-metrics.md) | Get financial metrics for a ticker, including valuation, profitability, efficiency, liquidity, leverage, growth, and per share metrics. | $0.02 per call |
| [`financial-datasets/financial-metrics-snapshot`](../models/financial-datasets/financial-metrics-snapshot.md) | Get the real-time financial metrics snapshot for a stock, including valuation ratios, profitability, efficiency, liquidity, leverage,… | $0.02 per call |
| [`financial-datasets/financials`](../models/financial-datasets/financials.md) | Get Financial Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/financials-balance-sheets`](../models/financial-datasets/financials-balance-sheets.md) | Get Balance Sheets from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/financials-cash-flow-statements`](../models/financial-datasets/financials-cash-flow-statements.md) | Get Cash Flow Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/financials-income-statements`](../models/financial-datasets/financials-income-statements.md) | Get Income Statements from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/financials-search-screener`](../models/financial-datasets/financials-search-screener.md) | Screen US public companies by financial metrics such as revenue, net income or P/E, with gt/lt/eq filters and ticker lists. | $0.02 per call |
| [`financial-datasets/index-funds`](../models/financial-datasets/index-funds.md) | Holdings of an ETF or index fund by ticker, with fund name, asset class, net assets and each holding's weight. | $0.02 per call |
| [`financial-datasets/insider-trades`](../models/financial-datasets/insider-trades.md) | Get insider trades like buys and sells for a ticker by a company insider. | $0.02 per call |
| [`financial-datasets/institutional-holdings`](../models/financial-datasets/institutional-holdings.md) | 13F institutional holdings of a US stock by ticker: holder, shares, value and report period. | $0.02 per call |
| [`financial-datasets/ipos`](../models/financial-datasets/ipos.md) | Recent US IPO and registration filings (S-1, F-1 and amendments) with company, form type and filing links. | $0.16 per call |
| [`financial-datasets/kpi-guidance`](../models/financial-datasets/kpi-guidance.md) | Get structured forward guidance from earnings releases. Returns ranges, point estimates, and directional signals. | $0.02 per call |
| [`financial-datasets/kpi-metrics`](../models/financial-datasets/kpi-metrics.md) | Get sector-specific operational KPIs for a ticker. Includes metrics like load factor, CET1 ratio, same-store sales, FFO per share, and… | $0.02 per call |
| [`financial-datasets/kpi-non-gaap`](../models/financial-datasets/kpi-non-gaap.md) | Get non-GAAP financial metrics with GAAP equivalents and key adjustments. | $0.02 per call |
| [`financial-datasets/macro-interest-rates`](../models/financial-datasets/macro-interest-rates.md) | The daily policy rate of one central bank: one row per calendar day, newest first, 10 rows per page. A rate change appears on the first… | $0.02 per call |
| [`financial-datasets/macro-interest-rates-snapshot`](../models/financial-datasets/macro-interest-rates-snapshot.md) | The newest published policy rate of every central bank we cover, one row per bank with the date it is in effect. Pass bank to get one bank… | $0.02 per call |
| [`financial-datasets/news`](../models/financial-datasets/news.md) | Get recent news articles for a specific company or the broad market. Pass a ticker for company-specific news, or omit the ticker for… | $0.02 per call |
| [`financial-datasets/prices`](../models/financial-datasets/prices.md) | Get Historical Stock Prices from Financial Datasets. Returns the official Financial Datasets API response unchanged. | $0.02 per call |
| [`financial-datasets/prices-snapshot`](../models/financial-datasets/prices-snapshot.md) | Get the real-time price snapshot for a stock, including the current price, day change, and day change percent. | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/analyst-estimates"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
