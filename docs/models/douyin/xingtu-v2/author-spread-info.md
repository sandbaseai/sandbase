# Douyin Xingtu Author Spread Info API: pricing, parameters and code examples

`douyin/xingtu-v2/author-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Retrieves commercial spread and reach capability data for a specific creator. Accepts filtering by time range, video type, flow type, and assignment status.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-spread-info", "o_author_id": "6677767167234015243", "range": 2, "type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-spread-info', {'o_author_id': '6677767167234015243', 'range': 2, 'type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-spread-info", {
  "o_author_id": "6677767167234015243",
  "range": 2,
  "type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-spread-info", sandbase.Params{
	"o_author_id": "6677767167234015243",
	"range": 2,
	"type": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | integer |  | Video type, 1=personal video  |
| `range` | integer |  | Time range, 2=last 30 days, 3=last 90 days  |
| `flow_type` | integer |  | Flow type, default 0  |
| `o_author_id` | string | yes | Creator/author ID  |
| `only_assign` | boolean |  | Only assigned videos, default False  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns commercial spread metrics for one Douyin Xingtu creator, such as median plays, average likes, comments and shares, and expected CPM and CPE. It needs the creator's `o_author_id`. You can narrow the data by time range, video type, flow type and assigned-only videos.

### Use cases

- Compare the median play count of several creators before picking one for a campaign.
- Estimate campaign cost from the expected CPM and CPE values for 21 to 60 second and 60 second plus videos.
- Check how many videos back a creator's spread stats by reading `item_num`.
- Screen creators on average likes, comments and shares per video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-spread-info" \
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
| `only_assign` | boolean | No | Only assigned videos, default False |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |
| `range` | integer | No | Time range, 2=last 30 days, 3=last 90 days |
| `type` | integer | No | Video type, 1=personal video |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avg_duration": "5800",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "comment_avg": "35",
  "expect_cpe": {
    "cpe_21_60": "6153",
    "cpe_60": "7692"
  },
  "expect_cpm": {
    "cpm_21_60": "776699",
    "cpm_60": "970873"
  },
  "interact_rate": {
    "overtake": 1555,
    "value": 50
  },
  "item_num": "5",
  "item_rate": {
    "interact_rate": {},
    "item_num": {
      "label": "",
      "value": 5
    },
    "play_mid": {
      "label": "",
      "overtake": 7588,
      "value": 986
    }
  },
  "like_avg": "61",
  "play_mid": "986",
  "play_over_rate": {
    "overtake": 1701,
    "value": 185
  },
  "play_stability": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `play_mid` | Median play count of the creator's videos in the selected window. |
| `like_avg / comment_avg / share_avg` | Average likes, comments and shares per video. Values are returned as strings. |
| `avg_duration` | Average video duration. The response does not show the unit. |
| `item_num` | Number of videos counted in these stats. |
| `expect_cpm.cpm_21_60 / expect_cpm.cpm_60` | Expected CPM for videos of 21 to 60 seconds and for videos over 60 seconds. |
| `expect_cpe.cpe_21_60 / expect_cpe.cpe_60` | Expected CPE for the same two video length bands. |
| `sales_expect_cpm.cpm_21_60 / sales_expect_cpm.cpm_60` | Expected CPM in the sales context for the same two video length bands. |
| `interact_rate.value / interact_rate.overtake` | The creator's interaction rate value and an `overtake` figure that shows how the creator ranks against others. |
| `play_over_rate.value / play_over_rate.overtake` | The creator's play-over rate value and its `overtake` ranking figure. |
| `item_rate.play_mid.value / item_rate.play_mid.overtake` | Median plays with its `overtake` ranking figure, grouped under `item_rate`. |

### Notes

- Only `o_author_id` is required. Add `range` (`2` for 30 days, `3` for 90 days) to change the time window.
- Numeric values such as `play_mid` and `like_avg` come back as strings, while `overtake` and `value` inside rate objects are numbers.
- `play_stability` and `item_rate.interact_rate` can come back as empty objects.
- For the individual videos behind these stats, call [Douyin Author Spread Videos](/apis/douyin/xingtu-v2/author-spread-videos).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-spread-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-spread-info
