# Douban Movie Reviews API: pricing, parameters and code examples

`douban/movie-reviews` · data API · Douban · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get paginated Douban long-form reviews for a movie or TV subject, ordered by time or popularity. Use it to browse in-depth audience reviews for a known subject.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/movie-reviews", "subjectId": "1292052"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douban/movie-reviews', {'subjectId': '1292052'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douban/movie-reviews", {
  "subjectId": "1292052"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douban/movie-reviews", sandbase.Params{
	"subjectId": "1292052",
})
```

Same call via the path form: `POST /v1/api/douban/movie-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `time`, `hotest`; default `"time"` |
| `subjectId` | string | yes | The unique ID for a movie or TV subject on Douban.  |

## Details

Get paginated Douban long-form reviews for a movie or TV subject, ordered by time or popularity. Use it to browse in-depth audience reviews for a known subject.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douban/movie-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subjectId": "1292052"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subjectId` | string | Yes | The unique ID for a movie or TV subject on Douban. |
| `sort` | string | No | Sort order for the result set. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douban/movie-reviews.json`](../../../catalog/models/douban/movie-reviews.json) · Store page: https://www.sandbase.ai/model/douban/movie-reviews
