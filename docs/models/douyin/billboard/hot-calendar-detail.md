# Douyin Billboard Hot Calendar Detail API: pricing, parameters and code examples

`douyin/billboard/hot-calendar-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a Douyin billboard hot calendar event based on the specified activity identifier. Use this endpoint to inspect schedule metadata and billboard campaign details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-calendar-detail", "calendar_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-calendar-detail', {'calendar_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-calendar-detail", {
  "calendar_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-calendar-detail", sandbase.Params{
	"calendar_id": "1",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-calendar-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `calendar_id` | string | yes | Activity id  |

## Details

Returns the details of one Douyin billboard hot calendar event. It needs a `calendar_id`, the activity id of the event. The response includes the event description, category, linked challenge, cover image, and schedule times.

### Use cases

- Read the description and category of a Douyin hot calendar event before planning a campaign around it.
- Check the start and end dates and the publish window of an event to time content.
- Find the challenge name and ID linked to an event, then look up its topic.
- Pull the cover image and title of an event into a marketing dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-calendar-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"calendar_id": "1720"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | string | Yes | Activity id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "activity_desc": "今年过年怎么玩？欢迎分享打卡家乡或者外地的年味聚集地的逛吃故事～",
    "activity_reward": "",
    "category_name": "话题互动",
    "challenge_info": [
      {
        "id": "7452337947140950057",
        "name": "正式开启过年七天乐"
      }
    ],
    "city_name": "",
    "cover_url": "http://p6-dyhot.byteimg.com/tos-cn-i-jid1fmi4d3/93c6a5aa20706aec3be000f68a522319…",
    "end_date": 1738684799,
    "event_ids": null,
    "event_status": -1,
    "example_videos": [],
    "hot_title": "正式开启过年七天乐",
    "id": 1720
  },
  "extra": {
    "now": 1793691106000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hot_title` | Title of the calendar event. It matches the name of the linked challenge in this example. |
| `data.activity_desc` | Text description of the activity and what users are asked to post. |
| `data.category_name` | Category label of the event, such as `话题互动`. |
| `data.challenge_info[].id / data.challenge_info[].name` | ID and name of each challenge linked to the event. |
| `data.start_date / data.end_date` | Start and end of the event as Unix timestamps in seconds. |
| `data.publish_start_time / data.publish_end_time` | Start and end of the publishing window as date-time strings in `YYYY-MM-DD HH:MM:SS` format. |
| `data.publish_cnt` | Number of publications counted for the event. In this example it is `9528`. |
| `data.parent_id` | ID of the parent calendar event. In this example it is `1717`. |
| `data.related_topics[]` | Names of topics related to the event. |
| `data.cover_url` | URL of the event cover image. |

### Notes

- Send the activity ID as the string `calendar_id`, for example `1720`. The same value comes back as `data.id`.
- Several fields can be empty or `null` for some events, such as `data.activity_reward`, `data.city_name`, `data.tags`, `data.example_videos` and `data.timeline`.
- To find other calendar IDs, call [Douyin Billboard Hot Calendar List](/apis/douyin/billboard/hot-calendar-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-calendar-detail.json`](../../../../catalog/models/douyin/billboard/hot-calendar-detail.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-calendar-detail
