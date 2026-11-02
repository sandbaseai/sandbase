# Douyin Brand Hot Search List Detail API: pricing, parameters and code examples

`douyin/app-v3/brand-hot-search-list-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed brand hot search list data from Douyin for a specific category. Requires a category identifier to filter the ranking results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/brand-hot-search-list-detail", "category_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/brand-hot-search-list-detail', {'category_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/brand-hot-search-list-detail", {
  "category_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/brand-hot-search-list-detail", sandbase.Params{
	"category_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/brand-hot-search-list-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category_id` | integer | yes | Category id  |

## Details

Call this endpoint with `category_id` to retrieve brand hot search list details from Douyin.

### Use cases

- Tracking trending brands across specific Douyin categories.
- Analyzing brand search popularity and rankings on the platform.
- Monitoring competitive brand visibility by category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/brand-hot-search-list-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": "<category_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | Category id |

### Notes

- Requires `category_id` to specify the brand category.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.
- [Douyin Video Share QR Code](/model/douyin/app-v3/generate-video-share-qrcode): Returns a Douyin share QR code for a designated target.

---
Machine-readable: [`catalog/models/douyin/app-v3/brand-hot-search-list-detail.json`](../../../../catalog/models/douyin/app-v3/brand-hot-search-list-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/brand-hot-search-list-detail
