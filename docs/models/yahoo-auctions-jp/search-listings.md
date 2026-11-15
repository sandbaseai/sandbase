# Yahoo! Auctions Japan Search Listings API: pricing, parameters and code examples

`yahoo-auctions-jp/search-listings` · data API · Yahoo! Auctions Japan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search active auction and fixed-price listings by keyword and category.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-auctions-jp/search-listings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-auctions-jp/search-listings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-auctions-jp/search-listings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-auctions-jp/search-listings", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/yahoo-auctions-jp/search-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort field default `"new"` |
| `limit` | integer |  | Number of results per page (max 50) default `50` |
| `order` | string |  | Sort order default `"d"` |
| `query` | string |  | Search keyword  |
| `auccat` | string |  | Category ID  |
| `offset` | integer |  | Pagination offset (starts at 1, increments by limit) default `1` |
| `condition` | string |  | Item condition filter  |
| `max_price` | integer |  | Maximum price in Yen  |
| `min_price` | integer |  | Minimum price in Yen  |

## Details

Search active auction and fixed-price listings by keyword and category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yahoo-auctions-jp/search-listings", "sort": "new", "limit": 5, "order": "a", "query": "Nintendo Switch", "offset": 1, "condition": "new", "max_price": 50000, "min_price": 1000}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `auccat` | string | No | Category ID |
| `condition` | string | No | Item condition filter |
| `limit` | integer | No | Number of results per page (max 50) |
| `max_price` | integer | No | Maximum price in Yen |
| `min_price` | integer | No | Minimum price in Yen |
| `offset` | integer | No | Pagination offset (starts at 1, increments by limit) |
| `order` | string | No | Sort order |
| `query` | string | No | Search keyword |
| `sort` | string | No | Sort field |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-auctions-jp/search-listings.json`](../../../catalog/models/yahoo-auctions-jp/search-listings.json) · Store page: https://www.sandbase.ai/model/yahoo-auctions-jp/search-listings
