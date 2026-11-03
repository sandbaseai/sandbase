# Douyin Creator Activity Details API: pricing, parameters and code examples

`douyin/creator/creator-activity-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specific Douyin creator activity. Queries campaign details using a designated activity identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-activity-detail", "activity_id": "7545335931785450534"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-activity-detail', {'activity_id': '7545335931785450534'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-activity-detail", {
  "activity_id": "7545335931785450534"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-activity-detail", sandbase.Params{
	"activity_id": "7545335931785450534",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-activity-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `activity_id` | string | yes | Activity ID (obtained from activity list interface)  |

## Details

This API returns the details of one Douyin creator activity, such as its name, status, topic tags, run dates and reward rules. It needs one input, the `activity_id` of the activity.

### Use cases

- Show the name, cover image and run dates of a Douyin creator campaign in a creator dashboard.
- Read the required topic tag and participation steps before posting a video for an activity.
- Check whether an activity is still open by comparing `publish_start_time` and `publish_end_time` with today's date.
- Collect the topic names and topic IDs tied to an activity so you can track videos posted under them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-activity-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"activity_id": "7545335931785450534"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `activity_id` | string | Yes | Activity ID (obtained from activity list interface) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activity_description": "点击查看活动主页，发布视频带话题 #超能下蛋鸭，挂载《超能下蛋鸭》抖音小游戏摇杆，即可成功参与活动。",
  "activity_info": {
    "activity_id": "7545335931785450534",
    "activity_level": 3,
    "activity_name": "超能下蛋鸭视频激励活动",
    "activity_status": 2,
    "activity_type": 1,
    "challenge": null,
    "challenge_ids": [
      7507489617000532000
    ],
    "collect_id": 2522,
    "collect_status": false,
    "cover_image": "https://lf-gaia-dy.douyinstatic.com/obj/gaia-dy/1708322328af3a8a9d54f9ce683d1e1d…",
    "game_id": "",
    "hot_score": 1125
  },
  "demo_videos": null,
  "my_publish_videos": null,
  "other_publish_videos": null,
  "publish_end_time": "2025.10.14",
  "publish_start_time": "2025.09.02",
  "reward_rules": "{\"text\":\"按投稿贡献排名，奖励详情请点击参与查看。\",\"anchorText\":\"\",\"anchorUri\":\"\"}",
  "status_code": 0,
  "topics": [
    "超能下蛋鸭"
  ],
  "topics_ids": [
    "7507489617000532018"
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `activity_info.activity_name` | Name of the activity. |
| `activity_info.activity_id` | ID of the activity. It matches the `activity_id` you sent. |
| `activity_description` | Text that explains how to join the activity, including the topic tag and the item to attach to the video. |
| `activity_info.activity_status / activity_info.activity_type / activity_info.activity_level / activity_info.reward_type` | Numeric codes for the status, type, level and reward type of the activity. The response does not include a label for each code. |
| `publish_start_time / publish_end_time` | First and last day of the activity period, in `YYYY.MM.DD` format. |
| `activity_info.show_start_time / activity_info.show_end_time` | Dates between which the activity is shown, in `YYYY.MM.DD` format. |
| `reward_rules` | A JSON string. Its `text` key holds the reward rule in plain text. Parse the string before you read it. |
| `topics[] / topics_ids[]` | Names and IDs of the topics linked to the activity. Both lists are in the same order. |
| `activity_info.hot_score` | Numeric score for the activity's popularity. |
| `activity_info.cover_image` | URL of the activity cover image. |

### Notes

- Get `activity_id` from [Douyin Activity List](/apis/douyin/creator/creator-activity-list).
- `activity_info.challenge_ids[]` holds large numbers, while `topics_ids[]` holds IDs as strings. Treat IDs as strings to avoid rounding.
- `demo_videos`, `my_publish_videos` and `other_publish_videos` came back as `null` for this activity.
- `status_code` is `0` in the sample response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.
- [Douyin Creator Content Courses](/apis/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-activity-detail.json`](../../../../catalog/models/douyin/creator/creator-activity-detail.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-activity-detail
