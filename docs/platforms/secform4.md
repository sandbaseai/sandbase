# SECForm4 API: 9 endpoints with pricing and code examples

Call 9 SECForm4 endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`secform4/13d-filings`](../models/secform4/13d-filings.md) | Returns recent Schedule 13D filings showing significant ownership positions (>5%) in public companies. 13D filers are activist investors… | $0.01 per call (free daily quota) |
| [`secform4/13g-filings`](../models/secform4/13g-filings.md) | Returns recent Schedule 13G filings showing passive ownership positions (>5%) in public companies. 13G filers are passive investors who do… | $0.01 per call (free daily quota) |
| [`secform4/company-insider-trading`](../models/secform4/company-insider-trading.md) | Returns the full insider trading history for a specific company identified by its SEC CIK number. Includes all buy, sell, and option… | $0.01 per call (free daily quota) |
| [`secform4/insider-buy-sell-ratios`](../models/secform4/insider-buy-sell-ratios.md) | Returns aggregate insider buy/sell ratio data with daily data points going back to 2003. Includes buy count, sell count, buy dollar… | $0.01 per call (free daily quota) |
| [`secform4/insider-buys`](../models/secform4/insider-buys.md) | Returns recent insider purchase transactions from SEC Form 4 filings. Data is delayed by 6 months for public users. | $0.01 per call (free daily quota) |
| [`secform4/insider-sales`](../models/secform4/insider-sales.md) | Returns recent insider sale transactions from SEC Form 4 filings. Each transaction includes company info, insider relationship, share… | $0.01 per call (free daily quota) |
| [`secform4/search`](../models/secform4/search.md) | Searches for insider trading activity by company ticker symbol, CIK number, or company name. Returns all matching transaction records for… | $0.01 per call (free daily quota) |
| [`secform4/significant-insider-buys`](../models/secform4/significant-insider-buys.md) | Returns insider purchase transactions filtered to significant buys only (larger dollar amounts). Same fields as get_insider_buys but… | $0.01 per call (free daily quota) |
| [`secform4/stock-options`](../models/secform4/stock-options.md) | Returns recent stock option transactions including exercises, awards, grants, conversions, and tax withholdings from SEC Form 4 filings. | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/13d-filings"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
