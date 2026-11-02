# Douban Review Details API: pricing, parameters and code examples

`douban/movie-review-detail` · data API · Douban · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get a single Douban long-form review by its review ID. Use it to inspect a known review after discovering it in a subject's review list.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/movie-review-detail", "reviewId": "37660136"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/movie-review-detail', {'reviewId': '37660136'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/movie-review-detail", {
  "reviewId": "37660136"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/movie-review-detail", sandbase.Params{
	"reviewId": "37660136",
})
```

Same call via the path form: `POST /v1/api/douban/movie-review-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `reviewId` | string | yes | The unique ID for a specific review on Douban.  |

## Details

Get a single Douban long-form review by its review ID. Use it to inspect a known review after discovering it in a subject's review list.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/movie-review-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"reviewId": "1000369"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `reviewId` | string | Yes | The unique ID for a specific review on Douban. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douban/movie-review-detail.json`](../../../catalog/models/douban/movie-review-detail.json) · Store page: https://www.sandbase.ai/model/douban/movie-review-detail
