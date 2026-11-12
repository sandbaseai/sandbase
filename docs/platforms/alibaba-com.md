# Alibaba.com API: 1 endpoints with pricing and code examples

Call 1 Alibaba.com endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`alibaba/search`](../models/alibaba/search.md) | Search Alibaba by keyword and get up to 25 wholesale listings (title, price range, minimum order, and supplier) in one normalized response. | about $0.00231 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/search", "query": "bluetooth speaker"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
