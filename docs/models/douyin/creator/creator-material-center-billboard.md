# Douyin Creator Material Center Billboard API: pricing, parameters and code examples

`douyin/creator/creator-material-center-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending billboard items from the Douyin Creator Material Center with interaction metrics. Supports filtering by time, billboard tag, and sorting order.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key default `1` |
| `time_filter` | integer |  | Time filter default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Returns a list of trending videos from the Douyin Creator Material Center billboard, with play, like, comment and share counts for each. All inputs are optional integers: `billboard_tag`, `order_key` and `time_filter`.

### Use cases

- Rank the most played Douyin videos in a billboard category.
- Compare `hot_score` with `like_count` and `share_count` to find videos that spread faster than they are liked.
- Collect `key_words` from trending titles to spot themes before planning new content.
- Build a list of top authors by reading `author_name` and `author_link` across billboard items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-billboard" \
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
      "author_link": "https://www.iesdouyin.com/share/user/58600794821?sec_uid=MS4wLjABAAAADdBKgoN-VYy…",
      "author_name": "张百乔",
      "aweme_list": null,
      "collection_count": 0,
      "comment_count": 37658,
      "cover": {
        "url_list": [
          "https://p5-ex-gddgtc-sign.douyinpic.com/tos-cn-i-0813/ocAAfDQIECArh8o8eRWMo7DeQ9…"
        ]
      },
      "duration": 19534,
      "hot_involve_ratio": "",
      "hot_involve_type": "",
      "hot_onboard_time": 0,
      "hot_score": 428224,
      "item_id": "7703486126555902874"
    }
  ],
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[]` | One trending video on the billboard. |
| `item_list[].item_id / item_list[].sec_item_id` | Identifiers for the video. `item_id` is a numeric string. `sec_item_id` is a longer encoded string. |
| `item_list[].title` | Video caption text. It can include hashtags. |
| `item_list[].author_name / item_list[].author_link` | Display name of the author and a link to the author's Douyin share page. |
| `item_list[].play_count / item_list[].like_count` | Total plays and likes for the video. |
| `item_list[].comment_count / item_list[].share_count` | Total comments and shares for the video. |
| `item_list[].hot_score` | Hotness score the billboard gives the video. Higher values mean a hotter item. |
| `item_list[].key_words` | Short list of keywords taken from the video. |
| `item_list[].duration` | Video length as an integer. The values suggest milliseconds, but the response does not state the unit. |
| `item_list[].cover.url_list[]` | Cover image URLs for the video. Each entry points to the same image on a different host. |

### Notes

- Set `billboard_tag` to `0` for all categories. To get other tag values, call [Douyin Material Center Configuration](/apis/douyin/creator/creator-material-center-config).
- The request has no page parameter. Use `order_key` and `time_filter` to change which items come back.
- Several fields, such as `publish_count`, `show_count`, `shoot_count` and `collection_count`, are `0` in this response. `aweme_list` and `related_item_ids` are `null`.
- To see related videos for an item, try [Douyin Material Center Related Videos](/apis/douyin/creator/creator-material-center-related).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-billboard.json`](../../../../catalog/models/douyin/creator/creator-material-center-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-billboard
