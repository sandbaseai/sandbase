# Yahoo! Auctions Japan API: 4 endpoints with pricing and code examples

Call 4 Yahoo! Auctions Japan endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`yahoo-auctions-jp/compare-market-price`](../models/yahoo-auctions-jp/compare-market-price.md) | Compound endpoint that identifies active listings priced significantly below the 180-day market average (less than 80% of average). | $0.03 per call |
| [`yahoo-auctions-jp/completed-listing-evidence`](../models/yahoo-auctions-jp/completed-listing-evidence.md) | Read the public Yahoo Auctions item page for one listing and return the price, timing and status facts exactly as the page states them,… | $0.03 per call |
| [`yahoo-auctions-jp/search-completed-listings`](../models/yahoo-auctions-jp/search-completed-listings.md) | Search completed/sold listings to get historical market price data. Returns items with final sold prices and 180-day market statistics… | $0.03 per call |
| [`yahoo-auctions-jp/search-listings`](../models/yahoo-auctions-jp/search-listings.md) | Search active auction and fixed-price listings by keyword and category. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-auctions-jp/compare-market-price", "query": "iPhone"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
