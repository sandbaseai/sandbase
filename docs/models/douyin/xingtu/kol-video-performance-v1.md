# Douyin XingTu KOL Video Performance API: pricing, parameters and code examples

`douyin/xingtu/kol-video-performance-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get a Douyin KOL's video performance from XingTu: interaction and play benchmarks versus peers, plus recent videos with likes, plays, comments and shares.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-video-performance-v1", "kolId": "7038603512770461703", "onlyAssign": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-video-performance-v1', {'kolId': '7038603512770461703', 'onlyAssign': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-video-performance-v1", {
  "kolId": "7038603512770461703",
  "onlyAssign": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-video-performance-v1", sandbase.Params{
	"kolId": "7038603512770461703",
	"onlyAssign": false,
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-video-performance-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `onlyAssign` | boolean | yes | Whether to display only assigned works, the specific parameters are as follows: false: Show all, including personal works and assigned works, default value; true: Only display assigned works from XingTu  |

## Details

This API returns performance data for one Douyin creator listed on XingTu. It gives interaction, play and view-rate benchmarks, plus the creator's latest videos and latest XingTu-assigned videos with likes, plays, comments and shares. It needs a XingTu `kolId` and an `onlyAssign` flag.

### Use cases

- Check whether a creator's interaction rate sits above or below the average of peers before you book a campaign.
- Compare the plays and likes of recent organic videos with the plays and likes of XingTu-assigned videos.
- Read the titles and hashtags of recent videos to see which brands and topics a creator has promoted.
- Track play, like and share counts per video to spot which formats and durations get the most reach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-video-performance-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703", "onlyAssign": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |
| `onlyAssign` | boolean | Yes | Whether to display only assigned works, the specific parameters are as follows: false: Show all, including personal works and assigned works, default value; true: Only display assigned works from XingTu |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "data_description": {
    "interaction": {
      "compare_author": 0.92,
      "compare_avg": 0.0756,
      "rate": 0.1285
    },
    "interaction_enrollment": {
      "compare_author": 0,
      "compare_avg": -0.0806,
      "rate": 0
    },
    "play_medium": {
      "compare_author": 0.75,
      "compare_avg": -0.8962107426137736,
      "rate": 1585
    },
    "play_medium_enrollment": {
      "compare_author": 0,
      "compare_avg": -1,
      "rate": 0
    },
    "video_view_rate": {
      "compare_author": 0.71,
      "compare_avg": 0.0348,
      "rate": 0.1853
    },
    "video_view_rate_enrollment": {
      "compare_author": 0,
      "compare_avg": -0.1214,
      "rate": 0
    }
  },
  "latest_item_info": [
    {
      "comment": 34,
      "core_user_id": "93153724393",
      "create_time": 1793616450,
      "create_timestamp": 1793616450,
      "duration": 8,
      "duration_min": 0,
      "head_image_uri": "tos-cn-p-0015/owC066G9lEq5AacAEqGgioDfFlfBABkKHI2o4Q",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-p-0015/owC066G9lEq5AacAEqGgioDfFlfBABkKHI2o4Q",
      "item_cover": "tos-cn-p-0015/owC066G9lEq5AacAEqGgioDfFlfBABkKHI2o4Q",
      "item_date": "2026-11-02"
    }
  ],
  "latest_item_statics_antispam": {},
  "latest_star_item_info": [
    {
      "comment": 372,
      "core_user_id": "93153724393",
      "create_time": 1792834253,
      "create_timestamp": 1792834253,
      "duration": 20,
      "duration_min": 0,
      "head_image_uri": "tos-cn-i-dy/b04028c0571c419688a86e266e409abc",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-i-dy/b04028c0571c419688a86e266e409abc",
      "item_cover": "tos-cn-i-dy/b04028c0571c419688a86e266e409abc",
      "item_date": "2026-10-24"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data_description.interaction.rate` | The creator's interaction rate, shown as a ratio (for example `0.1285`). |
| `data_description.interaction.compare_author / data_description.interaction.compare_avg` | Comparison values for the interaction rate. `compare_author` is a score between 0 and 1. `compare_avg` is a signed difference from the average, where a negative number means below average. |
| `data_description.play_medium.rate` | The creator's median play count for the period, for example `1585`. |
| `data_description.video_view_rate.rate` | The creator's video view rate as a ratio. The `compare_author` and `compare_avg` fields beside it work like the interaction ones. |
| `data_description.interaction_enrollment / data_description.play_medium_enrollment / data_description.video_view_rate_enrollment` | The same three metrics with an `_enrollment` suffix, each with `rate`, `compare_author` and `compare_avg`. In this response the rates are `0`. |
| `latest_item_info[].item_title` | Title of a recent video, including its hashtags. |
| `latest_item_info[].play / like / comment / share` | Play, like, comment and share counts for the video. |
| `latest_item_info[].item_date / create_timestamp` | Publish date as `YYYY-MM-DD` and as a Unix timestamp in seconds. |
| `latest_item_info[].duration` | Video length. The values (8, 10, 20) fit seconds, but the response does not state the unit. |
| `latest_star_item_info[]` | Recent XingTu-assigned videos, with the same fields as `latest_item_info[]` (`item_id`, `item_title`, `play`, `like`, `comment`, `share`, `item_date`). |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- Set `onlyAssign` to `false` to include personal and assigned works. Set it to `true` to show only works assigned through XingTu.
- Each video has an `item_id` and a `video_id`. The `url` field is a share link to the video on Douyin.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/apis/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-video-performance-v1.json`](../../../../catalog/models/douyin/xingtu/kol-video-performance-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-video-performance-v1
