# Douyin Creator Hot Topic Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-topic-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending creator topic rankings on Douyin with engagement metrics like play, like, comment, and share counts based on time and tag filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-topic-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-topic-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-topic-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-topic-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-topic-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key default `1` |
| `time_filter` | integer |  | Time filter default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Returns a ranked list of trending creator topics on Douyin. Each topic has play, like, comment and share counts plus publish counts. All inputs are optional integers: `billboard_tag`, `order_key` and `time_filter`.

### Use cases

- Find which topics get the most plays and likes so you can pick themes for new Douyin videos.
- Compare `publish_count` and `publish_uv` across topics to spot topics with high reach but few creators posting.
- Rank topics by `share_count` or `comment_count` to see which ones drive the most interaction.
- Pull the billboard for different `billboard_tag` values to compare topic trends by category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-topic-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `billboard_tag` | integer | No | Billboard tag, 0=all, other values can be obtained through config interface |
| `order_key` | integer | No | Order key |
| `time_filter` | integer | No | Time filter |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_list": [
    {
      "aweme_list": null,
      "collection_count": 0,
      "comment_count": 437302,
      "cover": {
        "url_list": [
          "https://p11-sign.douyinpic.com/tos-cn-i-dy/05d329044d5340108ec4bc2f05f4248b~noop…"
        ]
      },
      "hot_involve_ratio": "",
      "hot_involve_type": "",
      "hot_onboard_time": 0,
      "hot_score": 0,
      "item_id": "7495235888088090635",
      "key_words": null,
      "like_count": 10362414,
      "play_count": 932836314
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[].title` | Name of the topic, in Chinese. |
| `item_list[].item_id / item_list[].query_id` | String IDs for the topic entry. Both are returned as strings. |
| `item_list[].play_count` | Total plays recorded for the topic. |
| `item_list[].like_count / item_list[].comment_count / item_list[].share_count` | Total likes, comments and shares recorded for the topic. |
| `item_list[].publish_count` | Number of videos published under the topic. |
| `item_list[].publish_uv` | Number of distinct publishers for the topic, as the key name suggests. |
| `item_list[].cover.url_list[]` | Cover image URLs for the topic. Several URLs are listed for the same image. |
| `item_list[].collection_count / item_list[].hot_score / item_list[].show_count` | Other counters. They were `0` in this response, so do not rely on them for ranking. |
| `status_code / status_msg` | Request status. `status_code` is `0` and `status_msg` is empty on success. |

### Notes

- `billboard_tag` defaults to `0`, which means all tags. Other values come from the config interface.
- The schema does not describe the values for `order_key` and `time_filter`. Both default to `1`.
- The cover URLs are signed and include an `x-expires` value, so download images soon after the call.
- For other Douyin creator rankings, see [Douyin Creator Hot Spot Billboard](/apis/douyin/creator/creator-hot-spot-billboard) and [Douyin Creator Hot Music Billboard](/apis/douyin/creator/creator-hot-music-billboard).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-topic-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-topic-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-topic-billboard
