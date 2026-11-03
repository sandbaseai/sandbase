# Douyin Xingtu Spread Metrics API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-spread-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) spread metrics for a creator, with channel, period, video-type, assignment, and flow filters. Use it to compare creator spread performance during campaign planning.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-spread-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-spread-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-spread-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-spread-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-spread-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Video type. one of: `PERSONAL_VIDEO`, `XINTU_VIDEO`; default `"PERSONAL_VIDEO"` |
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE`; default `"EXCLUDE"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyAssign` | boolean |  | Whether to only include assigned videos. default `false` |

## Details

This API returns spread metrics for one creator on Douyin Creator Marketplace (Xingtu), such as median plays, average likes, comments and shares, and interaction rate. It needs the creator's `oAuthorId`. You can also filter by platform type, time range, video type, assigned-only videos, and flow type.

### Use cases

- Compare median play counts of several creators before choosing who to book for a campaign.
- Check a creator's average likes, comments and shares to estimate how much engagement their videos get.
- Compare `DAY_30` and `DAY_90` results to see whether a creator's spread is steady over time.
- Compare `PERSONAL_VIDEO` and `XINTU_VIDEO` results to see how a creator's own videos differ from Xingtu order videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-spread-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `flowType` | string | No | Flow type filter. |
| `onlyAssign` | boolean | No | Whether to only include assigned videos. |
| `platform` | string | No | Platform type. |
| `range` | string | No | Time range. |
| `type` | string | No | Video type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avg_duration": "9700",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "comment_avg": "25722",
  "expect_cpe": {},
  "expect_cpm": {},
  "interact_rate": {
    "overtake": 8248,
    "value": 248
  },
  "item_num": "420",
  "item_rate": {
    "interact_rate": {},
    "item_num": {
      "label": "",
      "value": 420
    },
    "play_mid": {
      "label": "",
      "overtake": 9996,
      "value": 16933169
    }
  },
  "like_avg": "516411",
  "play_mid": "16933169",
  "play_over_rate": {
    "overtake": 7112,
    "value": 2316
  },
  "play_stability": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `play_mid` | Median play count of the creator's videos in the selected range. It is returned as a string. |
| `like_avg / comment_avg / share_avg` | Average likes, comments and shares per video. Each value is returned as a string. |
| `item_num` | Number of videos counted in the selected range. It is returned as a string. |
| `avg_duration` | Average video duration. The response does not show the unit. |
| `interact_rate.value` | The creator's interaction rate value. |
| `interact_rate.overtake` | Overtake value that goes with the interaction rate. The response does not show how it is scaled. |
| `play_over_rate.value / play_over_rate.overtake` | Play completion style metric and its overtake value. Both are raw numbers, so the scale is not shown. |
| `item_rate.play_mid.value / item_rate.play_mid.overtake` | Median plays and its overtake value, grouped under `item_rate`. |
| `item_rate.item_num.value` | Video count as a number, grouped under `item_rate`. |
| `base_resp.status_code` | Status of the call. `0` means the request succeeded. |

### Notes

- Only `oAuthorId` is required. Other parameters default to `platform` `SHORT_VIDEO`, `range` `DAY_30`, `type` `PERSONAL_VIDEO`, `onlyAssign` `false`, and `flowType` `EXCLUDE`.
- Several objects can come back empty, such as `expect_cpe`, `expect_cpm`, `play_stability`, and `sales_expect_cpm`. Check for empty objects before reading them.
- Use [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square) to find creators, and [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info) for profile details.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-spread-info.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-spread-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-spread-info
