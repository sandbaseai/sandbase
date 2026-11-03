# Douyin Activity List API: pricing, parameters and code examples

`douyin/creator/creator-activity-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-activity-list", "end_time": 1, "start_time": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-activity-list', {'end_time': 1, 'start_time': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-activity-list", {
  "end_time": 1,
  "start_time": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-activity-list", sandbase.Params{
	"end_time": 1,
	"start_time": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-activity-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_time` | integer | yes | End timestamp  |
| `start_time` | integer | yes | Start timestamp  |

## Details

Returns a list of Douyin creator activity and campaign records that fall inside a time window. You send `start_time` and `end_time` as integer Unix timestamps in seconds.

### Use cases

- Build a calendar of Douyin campaigns that run during a given month.
- Find activities with a high `hot_score` to decide which campaign to join.
- Collect `activity_id` values and fetch full details for each activity.
- Pull each activity's cover image and jump link to show campaigns in your own creator dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-activity-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_time": 1759247999, "start_time": 1756656000}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_time` | integer | Yes | End timestamp |
| `start_time` | integer | Yes | Start timestamp |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "list": [
    {
      "activity_id": "7555852683250996270",
      "activity_level": 3,
      "activity_type": 1,
      "challenge_ids": [
        0
      ],
      "creator_id": 2600,
      "crowd_id": "7555781468044364553",
      "game_id": "",
      "head_image": "https://lf-gaia-zb.douyinstatic.com/obj/gaia-zb/0add5e4217e2b0e0f4550bcfa026073e…",
      "highlight_tag": 0,
      "hot_score": 100,
      "jump_link": "https://webcast.amemv.com/magic/eco/runtime/release/68d678defa986f07272121e4?sho…",
      "jump_type": 2
    }
  ],
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[]` | One activity or campaign record. The list holds every activity found in the time window. |
| `list[].activity_id` | ID of the activity, returned as a string. Use it to look up the activity in the detail API. |
| `list[].show_name` | Display title of the activity, such as a campaign or hashtag name. |
| `list[].show_start_time / list[].show_end_time` | Start and end of the period when the activity is shown, as Unix timestamps in seconds. |
| `list[].hot_score` | Popularity score of the activity. All three sample records show `100`. |
| `list[].head_image` | URL of the cover image for the activity. |
| `list[].jump_link` | Link that opens the activity. It can be a web URL, an `aweme://` app link, or an empty string. |
| `list[].challenge_ids[]` | IDs of the challenges (hashtags) linked to the activity. The value `0` appears when none is linked. |
| `list[].activity_type / list[].activity_level / list[].jump_type` | Numeric codes that classify the activity and how its link opens. The response gives no labels for these codes. |
| `status_code` | Status of the call. `0` appears in the sample response. |

### Notes

- `start_time` and `end_time` are both required. They are integer Unix timestamps in seconds, for example `1756656000` and `1759247999`.
- Pass `list[].activity_id` to [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail) to get more information on one activity.
- The request has no pagination parameters. The whole result comes back in `list`.
- Some fields, such as `tag_start_time` and `tag_end_time`, can be `0` when the activity has no tag period.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.
- [Douyin Creator Content Courses](/apis/douyin/creator/creator-content-course): Returns content development courses from the Douyin creator platform for a specified category.

---
Machine-readable: [`catalog/models/douyin/creator/creator-activity-list.json`](../../../../catalog/models/douyin/creator/creator-activity-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-activity-list
