# Bilibili Video Comments (App) API: pricing, parameters and code examples

`bilibili/app/video-comments` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns user comments for a specified Bilibili video by AV or BV identifier. Supports sorting comments by popularity or post time, with cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/video-comments", "bv_id": "BV19uhb6mEWd", "next_offset": 3}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/video-comments', {'bv_id': 'BV19uhb6mEWd', 'next_offset': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/video-comments", {
  "bv_id": "BV19uhb6mEWd",
  "next_offset": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/video-comments", sandbase.Params{
	"bv_id": "BV19uhb6mEWd",
	"next_offset": 3,
})
```

Same call via the path form: `POST /v1/api/bilibili/app/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mode` | integer |  | Sort mode (3=hot, 2=time) default `3` |
| `av_id` | string |  | AV ID (choose one of av_id or bv_id)  |
| `bv_id` | string |  | BV ID (choose one of av_id or bv_id)  |
| `next_offset` | integer |  | Pagination cursor default `1` |

## Details

Retrieve comments on a Bilibili video using either `bv_id` or `av_id`. Configure comment ordering and traverse pages via `next_offset`.

### Use cases

- Analyze viewer sentiment and reactions across top video comments.
- Track discussion timelines on videos sorted by post time.
- Collect popular viewer feedback to measure engagement trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mode` | integer | No | Sort mode (3=hot, 2=time) |
| `av_id` | string | No | AV ID (choose one of av_id or bv_id) |
| `bv_id` | string | No | BV ID (choose one of av_id or bv_id) |
| `next_offset` | integer | No | Pagination cursor |

### Notes

- Specify either `av_id` or `bv_id` to identify the target video.
- Set `mode` to 3 for top comments or 2 for chronological order.
- Advance through result pages using `next_offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/video-comments.json`](../../../../catalog/models/bilibili/app/video-comments.json) · Store page: https://www.sandbase.ai/model/bilibili/app/video-comments
