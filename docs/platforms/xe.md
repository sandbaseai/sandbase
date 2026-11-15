# XE API: 7 endpoints with pricing and code examples

Call 7 XE endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`xe/all-rates`](../models/xe/all-rates.md) | Get all mid-market exchange rates relative to USD. Returns a timestamp and a rates object mapping every supported currency code to its… | $0.06 per call |
| [`xe/convert-currency`](../models/xe/convert-currency.md) | Convert a specific amount from source to target currency. Returns the same structure as get_live_exchange_rate with the specified amount… | $0.03 per call |
| [`xe/currency-details`](../models/xe/currency-details.md) | Get the ISO 2-letter country code associated with a specific currency. Useful for mapping currencies to their issuing country. | $0.03 per call |
| [`xe/currency-symbols`](../models/xe/currency-symbols.md) | Get metadata and classification for all supported currencies. Each currency includes flags for obsolete status, crypto classification, and… | $0.03 per call |
| [`xe/historical-chart-data`](../models/xe/historical-chart-data.md) | Retrieve historical exchange rate data points for a currency pair. Returns multiple time-series batches at different intervals (daily,… | $0.03 per call |
| [`xe/live-exchange-rate`](../models/xe/live-exchange-rate.md) | Get the live mid-market exchange rate for a specific currency pair. Computes the cross-rate from USD-based rates. When amount is provided,… | $0.03 per call |
| [`xe/popular-currency-pairings`](../models/xe/popular-currency-pairings.md) | Get popular currency pairings for a base currency with real-time rates and trend data including rate change, percentage change, and… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/all-rates"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
