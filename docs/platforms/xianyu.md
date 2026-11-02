# Xianyu API: 2 endpoints with pricing and code examples

Call 2 Xianyu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`xianyu/item/detail`](../models/xianyu/item/detail.md) | Get a Xianyu (Goofish) second-hand listing by item ID: title, price, description, images, seller and location. | $0.028571 per call |
| [`xianyu/search/items`](../models/xianyu/search/items.md) | Search Xianyu (Goofish) second-hand listings by keyword, sorted by activity, recency, seller credit or price. | $0.028571 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xianyu/item/detail", "itemId": "1043659406022"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
