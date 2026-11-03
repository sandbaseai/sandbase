# Douyin Xingtu Author Show Items API: pricing, parameters and code examples

`douyin/xingtu-v2/author-show-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a video list for a specified Douyin Xingtu author. Filter results by author ID via o_author_id, flow type, platform source, or restrict results to assigned Xingtu videos.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-show-items", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-show-items', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-show-items", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-show-items", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-show-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `flow_type` | integer |  | Flow type, default 0  |
| `o_author_id` | string | yes | Creator/author ID  |
| `only_assign` | boolean |  | Only show assigned videos (only for XingTu videos), default False  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns a list of recent videos for a Douyin Xingtu author. The response splits videos into `latest_item_info` and `latest_star_item_info`, with title, play, like, comment and share counts for each video. It needs the author ID in `o_author_id`.

### Use cases

- Review an author's recent posts and their play counts before booking a campaign.
- Compare views and likes between an author's regular videos and their Xingtu videos.
- Pull video titles and hashtags to see which brands and products an author promotes.
- Build a link list of an author's videos using `item_id` and `url`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-show-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator/author ID |
| `flow_type` | integer | No | Flow type, default 0 |
| `only_assign` | boolean | No | Only show assigned videos (only for XingTu videos), default False |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "data_description": {
    "interaction": {},
    "interaction_enrollment": {},
    "play_medium": {},
    "play_medium_enrollment": {},
    "video_view_rate": {},
    "video_view_rate_enrollment": {}
  },
  "latest_item_info": [
    {
      "comment": 0,
      "core_user_id": "1113181577281568",
      "create_time": 1793587703,
      "create_timestamp": 1793587703,
      "duration": 80,
      "duration_min": 1,
      "head_image_uri": "tos-cn-i-dy/5ee00ee2c66f4b27a12a6ce2a6c40edd",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-i-dy/5ee00ee2c66f4b27a12a6ce2a6c40edd",
      "item_cover": "tos-cn-i-dy/5ee00ee2c66f4b27a12a6ce2a6c40edd",
      "item_date": "2026-11-02"
    }
  ],
  "latest_item_statics_antispam": {},
  "latest_star_item_info": [
    {
      "comment": 59,
      "core_user_id": "1113181577281568",
      "create_time": 1792826328,
      "create_timestamp": 1792826328,
      "duration": 100,
      "duration_min": 1,
      "head_image_uri": "tos-cn-i-dy/ebbf065864914a1e8aa0768fb2a44a0b",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-i-dy/ebbf065864914a1e8aa0768fb2a44a0b",
      "item_cover": "tos-cn-i-dy/ebbf065864914a1e8aa0768fb2a44a0b",
      "item_date": "2026-10-24"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `latest_item_info[]` | The author's latest videos. Each entry holds the video's title, publish date, counts and cover. |
| `latest_star_item_info[]` | A second list of videos for the same author, with the same fields as `latest_item_info[]`. The name suggests these are Xingtu videos. |
| `latest_item_info[].item_id / latest_item_info[].video_id` | Two IDs for the video. `item_id` is a numeric string and `video_id` is an alphanumeric string. |
| `latest_item_info[].title / latest_item_info[].item_title` | The video caption, including hashtags. |
| `latest_item_info[].play` | Play count of the video. |
| `latest_item_info[].like / latest_item_info[].comment / latest_item_info[].share` | Like, comment and share counts of the video. |
| `latest_item_info[].create_time / latest_item_info[].item_date` | When the video was created. `create_time` is a Unix timestamp in seconds and `item_date` is a date string in `YYYY-MM-DD` format. |
| `latest_item_info[].duration` | Video length. The values (such as 80 and 54) match `duration_min` values of 1 and 0, so the unit looks like seconds. |
| `latest_item_info[].url` | Share link to the video on Douyin. The link in the response is cut at a long query string. |
| `latest_item_info[].item_cover` | Cover image path for the video. It is a storage path, not a full URL. |

### Notes

- Pass the author's Xingtu ID as `o_author_id`. Look it up with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator) if you only have a name.
- Set `only_assign` to `true` to restrict results to assigned Xingtu videos.
- The response has no pagination fields, and the request has no page parameters.
- For a different view of an author's videos, try [Douyin Xingtu Author Homepage Videos](/apis/douyin/xingtu-v2/author-homepage-videos).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-show-items.json`](../../../../catalog/models/douyin/xingtu-v2/author-show-items.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-show-items
