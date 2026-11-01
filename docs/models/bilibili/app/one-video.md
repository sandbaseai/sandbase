# Bilibili App Single Video Details

`bilibili/app/one-video` · api · Bilibili

Returns detailed video metadata for a specific Bilibili video. Looks up video information using either an AV ID or a BV ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync, async (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/one-video", "bv_id": "BV1dVbC6WE6p"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/one-video', {'bv_id': 'BV1dVbC6WE6p'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/one-video", {
  "bv_id": "BV1dVbC6WE6p"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/one-video", sandbase.Params{
	"bv_id": "BV1dVbC6WE6p",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/bilibili/app/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `av_id` | string |  | AV ID (choose one of av_id or bv_id)  |
| `bv_id` | string |  | BV ID (choose one of av_id or bv_id)  |

## Details

Retrieve detailed information for a single Bilibili video by providing either `av_id` or `bv_id`.

### Use cases

- Look up metadata and stats for a specific Bilibili video.
- Monitor video engagement metrics across different video IDs.
- Integrate Bilibili video info into internal media tracking dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `av_id` | string | No | AV ID (choose one of av_id or bv_id) |
| `bv_id` | string | No | BV ID (choose one of av_id or bv_id) |

### Notes

- Requires either `av_id` or `bv_id` as the video identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/one-video.json`](../../../../catalog/models/bilibili/app/one-video.json) · Store page: https://www.sandbase.ai/model/bilibili/app/one-video
