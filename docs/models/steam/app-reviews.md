# Steam App Reviews API: pricing, parameters and code examples

`steam/app-reviews` · data API · Steam · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get user reviews for a Steam product with filtering and cursor-based pagination. Returns reviews with author info (playtime, games owned), vote data, and a cursor for fetching subsequent pages. First page uses cursor '*'.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "steam/app-reviews", "appid": "570"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('steam/app-reviews', {'appid': '570'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("steam/app-reviews", {
  "appid": "570"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "steam/app-reviews", sandbase.Params{
	"appid": "570",
})
```

Same call via the path form: `POST /v1/api/steam/app-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `appid` | string | yes | Steam application ID  |
| `cursor` | string |  | Pagination cursor ('*' for first page, then use returned cursor for next pages)  |
| `filter` | string |  | Sort filter for reviews default `"recent"` |
| `language` | string |  | Review language filter default `"english"` |
| `day_range` | integer |  | Filter reviews to within N days  |
| `review_type` | string |  | Filter by review sentiment default `"all"` |
| `num_per_page` | integer |  | Number of reviews per page (max 100) default `20` |

## Details

Get user reviews for a Steam product with filtering and cursor-based pagination. Returns reviews with author info (playtime, games owned), vote data, and a cursor for fetching subsequent pages. First page uses cursor '*'.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "steam/app-reviews", "appid": "570", "cursor": "*", "filter": "recent", "language": "english", "day_range": 365, "review_type": "all", "num_per_page": 5, "purchase_type": "all"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `appid` | string | Yes | Steam application ID |
| `cursor` | string | No | Pagination cursor ('*' for first page, then use returned cursor for next pages) |
| `day_range` | integer | No | Filter reviews to within N days |
| `filter` | string | No | Sort filter for reviews |
| `language` | string | No | Review language filter |
| `num_per_page` | integer | No | Number of reviews per page (max 100) |
| `review_type` | string | No | Filter by review sentiment |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/steam/app-reviews.json`](../../../catalog/models/steam/app-reviews.json) · Store page: https://www.sandbase.ai/model/steam/app-reviews
