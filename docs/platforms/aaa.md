# AAA API: 13 endpoints with pricing and code examples

Call 13 AAA endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`aaa/ev-charging-prices`](../models/aaa/ev-charging-prices.md) | Returns national and per-state EV charging price data including cost per kWh and total charger counts for each state. Data sourced from a… | $0.01 per call (free daily quota) |
| [`aaa/highest-recorded-prices`](../models/aaa/highest-recorded-prices.md) | Returns all-time highest recorded average gas prices for a specific state or nationally. If no state_code is provided, returns national… | $0.01 per call (free daily quota) |
| [`aaa/lowest-metro-prices`](../models/aaa/lowest-metro-prices.md) | Returns metro areas within a state sorted by lowest regular gas price ascending. Useful for finding the cheapest metros within a state. | $0.01 per call (free daily quota) |
| [`aaa/lowest-state-prices`](../models/aaa/lowest-state-prices.md) | Returns all states sorted by lowest average regular gas price ascending. Useful for identifying the cheapest states for gasoline. | $0.01 per call (free daily quota) |
| [`aaa/metro-prices-by-state`](../models/aaa/metro-prices-by-state.md) | Returns gas price data for all metro/city areas within a given state, including current and historical prices (yesterday, week ago, month… | $0.01 per call (free daily quota) |
| [`aaa/national-average`](../models/aaa/national-average.md) | Returns today's AAA national average gas price for all fuel grades (Regular, Mid-Grade, Premium, Diesel) with historical comparisons to… | $0.02 per call |
| [`aaa/news-article-detail`](../models/aaa/news-article-detail.md) | Returns the full content of a specific news article identified by its URL slug. The slug is obtainable from get_news_articles results. | $0.01 per call (free daily quota) |
| [`aaa/news-articles`](../models/aaa/news-articles.md) | Returns recent AAA gas price news articles with pagination support. Results include article title, publication date, excerpt, slug, and… | $0.01 per call (free daily quota) |
| [`aaa/price-change-by-metro`](../models/aaa/price-change-by-metro.md) | Returns price changes for all metro areas within a given state, showing the difference between current and historical prices for each fuel… | $0.01 per call (free daily quota) |
| [`aaa/price-change-by-state`](../models/aaa/price-change-by-state.md) | Returns the price change (delta) for a state between the current price and historical averages (day, week, month, year) for all fuel… | $0.02 per call |
| [`aaa/search-news-articles`](../models/aaa/search-news-articles.md) | Searches the AAA gas price news archive (weekly national reports and state-specific releases going back years) by keyword, optionally… | $0.01 per call (free daily quota) |
| [`aaa/state-gas-prices`](../models/aaa/state-gas-prices.md) | Returns current average gas prices for all 50 US states plus DC across all four fuel grades (Regular, Mid-Grade, Premium, Diesel). States… | $0.01 per call (free daily quota) |
| [`aaa/state-price-details`](../models/aaa/state-price-details.md) | Returns detailed gas price data for a specific state including current prices for all fuel grades, historical averages (yesterday, week… | $0.01 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/ev-charging-prices"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
