# Douyin Creator Hot Props Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-props-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending creator prop rankings and performance metrics on Douyin. Supports filtering by sorting sequence, time interval, and prop category tag.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-props-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-props-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-props-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-props-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-props-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key default `1` |
| `time_filter` | integer |  | Time filter default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Returns a ranked list of trending creator props (camera effects and filters) on Douyin, with play, show, shoot and publish counts for each prop. All inputs are optional integers: `billboard_tag`, `order_key` and `time_filter`. An empty request returns the default ranking.

### Use cases

- Track which Douyin props get the most plays and shoots to spot effects that are gaining traction.
- Compare `publish_count` and `shoot_count` across props to see which effects creators actually use in videos.
- Build a prop watchlist for a content team by saving each `item_id` and its `title`.
- Pull the prop cover images to show a visual ranking in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-props-billboard" \
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
      "collection_count": 8270,
      "comment_count": 0,
      "cover": {
        "url_list": [
          "https://lf3-effectcdn-tos.byteeffecttos.com/obj/ies.fe.effect/2d07e44c0a2328be56…"
        ]
      },
      "hot_involve_ratio": "",
      "hot_involve_type": "",
      "hot_onboard_time": 0,
      "hot_score": 0,
      "item_id": "273663451",
      "key_words": null,
      "like_count": 178,
      "play_count": 31241388
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[].item_id` | ID of the prop, returned as a string. |
| `item_list[].title` | Name of the prop as shown on Douyin. |
| `item_list[].cover.url_list[]` | Image URLs for the prop cover. The list holds more than one URL for the same image. |
| `item_list[].play_count` | Number of plays recorded for the prop. |
| `item_list[].show_count` | Number of times the prop was shown. |
| `item_list[].shoot_count` | Number of times creators shot a video with the prop. |
| `item_list[].publish_count` | Number of videos published with the prop. |
| `item_list[].like_count / collection_count` | Like count and collection (favorite) count for the prop. |
| `item_list[].query_id` | Query ID of the prop, returned as a string. |
| `status_code / status_msg` | Request status. `status_code` is `0` and `status_msg` is empty in the sample response. |

### Notes

- `billboard_tag` defaults to `0`, which means all props. Other values come from the config interface.
- `order_key` and `time_filter` are integers with a default of `1`. The schema does not describe their values.
- In the sample response, fields such as `hot_score`, `comment_count`, `share_count` and `publish_uv` are `0`, and `aweme_list` and `key_words` are `null`. Do not rely on them for ranking.
- This API has no pagination parameters in its schema.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-props-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-props-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-props-billboard
