# Douyin Author Daily Fan Trend API: pricing, parameters and code examples

`douyin/xingtu-v2/author-daily-fans` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns daily follower trend data for a specified Douyin creator. Supports filtering by date range, author type, and platform source.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-daily-fans", "author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-daily-fans', {'author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-daily-fans", {
  "author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-daily-fans", sandbase.Params{
	"author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-daily-fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_date` |  |  | End date, format YYYYMMDD, optional  |
| `author_id` | string | yes | Creator ID  |
| `start_date` |  |  | Start date, format YYYYMMDD, optional  |
| `author_type` |  |  | Author type, optional  |
| `platform_source` | integer |  | Platform source, default 1  |

## Details

Retrieve daily follower trend metrics for a creator using `author_id`. Filter the historical records by specifying `start_date` and `end_date`.

### Use cases

- Track daily follower growth and fluctuations for target creators.
- Analyze audience trend patterns over custom date intervals.
- Evaluate creator audience performance across different platform sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-daily-fans" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7146074596666507300"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Creator ID |
| `end_date` | string | No | End date, format YYYYMMDD, optional |
| `start_date` | string | No | Start date, format YYYYMMDD, optional |
| `author_type` | string | No | Author type, optional |
| `platform_source` | integer | No | Platform source, default 1 |

### Notes

- Provide `start_date` and `end_date` in YYYYMMDD format.
- `platform_source` defaults to 1 if not specified.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-daily-fans.json`](../../../../catalog/models/douyin/xingtu-v2/author-daily-fans.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-daily-fans
