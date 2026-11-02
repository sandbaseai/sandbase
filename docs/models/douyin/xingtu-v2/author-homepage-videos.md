# Douyin Xingtu Author Homepage Videos API: pricing, parameters and code examples

`douyin/xingtu-v2/author-homepage-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Retrieves homepage video records for a specified Douyin Xingtu creator. Filters results by post time range, pagination, and star item status.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-homepage-videos", "o_author_id": "7029342444797820939"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-homepage-videos', {'o_author_id': '7029342444797820939'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-homepage-videos", {
  "o_author_id": "7029342444797820939"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-homepage-videos", sandbase.Params{
	"o_author_id": "7029342444797820939",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-homepage-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default 1  |
| `end_time` |  |  | Publish end time, unix seconds, optional  |
| `start_time` |  |  | Publish start time, unix seconds, optional  |
| `o_author_id` | string | yes | Creator ID  |
| `is_star_item` |  |  | 1=star items only, 0=non-star only, omit=all  |

## Details

Fetch a list of homepage videos for a creator using their `o_author_id`. Filter the results by date range using `start_time` and `end_time` or filter by star collaboration status.

### Use cases

- Track video releases from a specific Douyin creator.
- Filter a creator's portfolio to inspect Xingtu star collaboration items.
- Inspect creator video activity across specific Unix timestamp ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-homepage-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "<o_author_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `page` | integer | No | Page number, default 1 |
| `end_time` | string | No | Publish end time, unix seconds, optional |
| `start_time` | string | No | Publish start time, unix seconds, optional |
| `is_star_item` | string | No | 1=star items only, 0=non-star only, omit=all |

### Notes

- Requires `o_author_id` to specify the creator.
- Set `is_star_item` to 1 for star items only, 0 for non-star items, or omit to view all.
- Supports pagination through `page`, which defaults to 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-homepage-videos.json`](../../../../catalog/models/douyin/xingtu-v2/author-homepage-videos.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-homepage-videos
