# X-Rates API: 7 endpoints with pricing and code examples

Call 7 X-Rates endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`x-rates/24h-percent-changes`](../models/x-rates/24h-percent-changes.md) | Extracts the 'Percent Change in the Last 24 Hours' widget data for major currency pairs from the homepage. Returns ~8 major pairs with… | $0.03 per call |
| [`x-rates/convert-currency`](../models/x-rates/convert-currency.md) | Performs a currency conversion from one currency to another for a given amount. Returns the converted value and a text representation.… | $0.03 per call |
| [`x-rates/current-rates-table`](../models/x-rates/current-rates-table.md) | Fetches the current exchange rates table for a given base currency against all other supported currencies. Returns rate and inverse rate… | $0.03 per call |
| [`x-rates/graph-data`](../models/x-rates/graph-data.md) | Returns exchange rate trend data points for a currency pair for the current year, suitable for generating graphs. Each data point contains… | $0.03 per call |
| [`x-rates/historical-rates-table`](../models/x-rates/historical-rates-table.md) | Fetches historical exchange rates for a base currency against all supported currencies on a specific date. The date must be in ISO… | $0.03 per call |
| [`x-rates/monthly-average`](../models/x-rates/monthly-average.md) | Retrieves monthly average exchange rates for a specific currency pair for a given year. Returns up to 12 monthly data points with the… | $0.03 per call |
| [`x-rates/supported-currencies`](../models/x-rates/supported-currencies.md) | Retrieves the full list of supported currencies and their codes from x-rates.com. Returns approximately 54 currencies with their display… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/24h-percent-changes"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
