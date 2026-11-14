# Opoint API: 3 endpoints with pricing and code examples

Call 3 Opoint endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`opoint/search`](../models/opoint/search.md) | Search global news by keyword, phrase, or boolean query with filters. | $0.06 per call |
| [`opoint/search-headlines`](../models/opoint/search-headlines.md) | Search global news and return headlines only, without article text. | $0.06 per call |
| [`opoint/suggest`](../models/opoint/suggest.md) | Translate a country, site, language, or media name into a search filter id. | from $0 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "opoint/search", "searchterm": "electric vehicles"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
