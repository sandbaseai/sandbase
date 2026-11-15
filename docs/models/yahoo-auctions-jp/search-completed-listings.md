# Yahoo! Auctions Japan Search Completed Listings API: pricing, parameters and code examples

`yahoo-auctions-jp/search-completed-listings` · data API · Yahoo! Auctions Japan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Search completed/sold listings to get historical market price data. Returns items with final sold prices and 180-day market statistics (min, avg, max price). Useful for determining fair market value of items.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-auctions-jp/search-completed-listings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-auctions-jp/search-completed-listings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-auctions-jp/search-completed-listings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-auctions-jp/search-completed-listings", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/yahoo-auctions-jp/search-completed-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results (max 50) default `50` |
| `query` | string |  | Search keyword  |
| `offset` | integer |  | Pagination offset (starts at 1, increments by limit) default `1` |

## Details

Search completed/sold listings to get historical market price data. Returns items with final sold prices and 180-day market statistics (min, avg, max price). Useful for determining fair market value of items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yahoo-auctions-jp/search-completed-listings", "limit": 5, "query": "iPhone", "offset": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Number of results (max 50) |
| `offset` | integer | No | Pagination offset (starts at 1, increments by limit) |
| `query` | string | No | Search keyword |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-auctions-jp/search-completed-listings.json`](../../../catalog/models/yahoo-auctions-jp/search-completed-listings.json) · Store page: https://www.sandbase.ai/model/yahoo-auctions-jp/search-completed-listings
