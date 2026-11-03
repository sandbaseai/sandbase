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

Returns a paged list of homepage videos for one Douyin Xingtu creator. Each item has the title, publish time, duration, play and interaction counts, and rates such as finish rate. The only required input is the creator ID in `o_author_id`.

### Use cases

- Pull a creator's latest videos with play, like and comment counts to review recent performance.
- Limit results to a publish window with `start_time` and `end_time` to compare a creator's output across campaign periods.
- Set `is_star_item` to separate Xingtu star item videos from regular posts.
- Rank a creator's videos by `finish_rate` or `interact_rate` to find which content held viewers best.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-homepage-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7029342444797820939"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `end_time` | string | No | Publish end time, unix seconds, optional |
| `is_star_item` | string | No | 1=star items only, 0=non-star only, omit=all |
| `page` | integer | No | Page number, default 1 |
| `start_time` | string | No | Publish start time, unix seconds, optional |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "items": [
    {
      "comment_cnt": "8215",
      "content_theme_labels": [],
      "cover_uri": "tos-cn-i-dy/ab08db17659849f58dbeb878ee1e65a2",
      "create_time": "1792486908",
      "duration": 789.664,
      "finish_rate": 0.026315,
      "interact_rate": 0.0254,
      "item_id": "7698612187585203482",
      "like_cnt": "100531",
      "title": "今天在泰山当挑山工，挑战日入一千！#华哥带你练  #挑山工",
      "url": "https://www.iesdouyin.com/share/video/7698612187585203482/?region=CN&mid=7698612…",
      "video_id": "v0d00fg10000dbbfbqfog65mpv6gq99g"
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 20,
    "page": 1,
    "total_count": 73
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].item_id / items[].video_id` | Identifiers for the video. `item_id` is the numeric ID that also appears in the share `url`. |
| `items[].title` | Video caption, including any hashtags. |
| `items[].create_time` | Publish time as a Unix timestamp in seconds, returned as a string. |
| `items[].duration` | Video length. The value is a decimal number, for example `789.664`. |
| `items[].watch_cnt / items[].like_cnt / items[].comment_cnt` | Play, like and comment counts for the video. They arrive as strings. |
| `items[].finish_rate / items[].interact_rate` | Decimal rates for the video. `finish_rate` is a completion rate and `interact_rate` is an interaction rate. |
| `items[].content_theme_labels` | List of content theme labels for the video. It can be empty. |
| `items[].url` | Share link for the video on Douyin. |
| `pagination.has_more / pagination.total_count` | `has_more` shows whether more pages exist. `total_count` is the total number of matching videos. |
| `pagination.page / pagination.limit` | Current page number and the number of items per page (`20` in this response). |

### Notes

- Get the creator ID for `o_author_id` from a search API such as [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- Increase `page` while `pagination.has_more` is `true` to read the next page.
- `start_time` and `end_time` take Unix seconds, the same format as `items[].create_time`.
- Set `is_star_item` to `1` for star items only or `0` for non-star items. Omit it to get all videos.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-homepage-videos.json`](../../../../catalog/models/douyin/xingtu-v2/author-homepage-videos.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-homepage-videos
