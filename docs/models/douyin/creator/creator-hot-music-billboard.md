# Douyin Creator Hot Music Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-music-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending music rankings from the Douyin creator platform. Filters allow sorting by view metrics, like counts, popularity, or submission volumes across customizable time ranges.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-music-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-music-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-music-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-music-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-music-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) default `1` |
| `time_filter` | integer |  | Time filter (1=24 hours, 2=7 days, 3=30 days) default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Returns a ranked list of trending music tracks from the Douyin creator platform. Each item has play, like, comment, share and submission counts. All inputs are optional: `order_key` sets the sort, `time_filter` sets the time window, and `billboard_tag` picks a chart category.

### Use cases

- Pick sounds that are rising on Douyin before you plan a new video.
- Rank tracks by `like_count` or `play_count` over the last 24 hours, 7 days or 30 days.
- Compare how many videos use each sound with `publish_count` to find sounds that are not yet crowded.
- Store the `item_id` of top tracks and watch how the chart changes between days.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-music-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `billboard_tag` | integer | No | Billboard tag, 0=all, other values can be obtained through config interface |
| `order_key` | integer | No | Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) |
| `time_filter` | integer | No | Time filter (1=24 hours, 2=7 days, 3=30 days) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_list": [
    {
      "aweme_list": null,
      "collection_count": 0,
      "comment_count": 37658,
      "cover": {
        "url_list": [
          "https://p5-ex-gddgtc-sign.douyinpic.com/tos-cn-i-dy/d133d42bf424ce44cd12d17622d0…"
        ]
      },
      "hot_involve_ratio": "",
      "hot_involve_type": "",
      "hot_onboard_time": 0,
      "hot_score": 428224,
      "item_id": "7703486029906348850",
      "key_words": null,
      "like_count": 2285417,
      "play_count": 118052061
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[]` | One ranked music entry on the billboard. The list follows the order set by `order_key`. |
| `item_list[].title` | Name of the sound. Many entries are original sounds, shown as the creator's handle followed by the text for "original sound". |
| `item_list[].item_id / item_list[].query_id` | Identifiers for the track. Both are strings of digits. |
| `item_list[].play_count` | Total play count for the sound. |
| `item_list[].like_count / item_list[].comment_count / item_list[].share_count` | Like, comment and share totals for the sound. |
| `item_list[].hot_score` | Popularity score for the track. The `order_key` value 4 sorts by popularity. |
| `item_list[].publish_count` | Number of submissions that use the sound. The `order_key` value 5 sorts by submissions. It is 0 for some entries. |
| `item_list[].cover.url_list[]` | Cover image URLs for the track. Each URL is signed and carries an `x-expires` value. |
| `status_code / status_msg` | Status of the call. A `status_code` of 0 with an empty `status_msg` is the success case in this response. |

### Notes

- `order_key` values: 1 for highest views, 2 for most likes, 4 for highest popularity, 5 for most submissions.
- `time_filter` values: 1 for 24 hours, 2 for 7 days, 3 for 30 days.
- Leave `billboard_tag` at 0 for all categories. Other values come from a config interface. For related Douyin creator data, see [Douyin Creator Hot Topic Billboard](/apis/douyin/creator/creator-hot-topic-billboard).
- Fields such as `aweme_list`, `key_words`, `related_item_ids`, `show_count` and `shoot_count` were empty or 0 in the sample response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-music-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-music-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-music-billboard
