# Xiaohongshu Pugongying Creator Profile API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/blogger-user-id` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a Xiaohongshu Pugongying creator profile and cooperation quote information for a known user ID. Use it to review a creator before campaign outreach or pricing comparison.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/blogger-user-id", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/blogger-user-id', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/blogger-user-id", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/blogger-user-id", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/blogger-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | Blogger's user ID.  |

## Details

Returns a Xiaohongshu Pugongying creator profile for one user ID. The response covers follower counts, cooperation status, note counts and estimated cost metrics. It needs only the creator's `userId`.

### Use cases

- Check a creator's follower count and cooperation state before sending a campaign invitation.
- Compare how many sponsored notes different creators have published using `businessNoteCount`.
- Read the estimated CPM and engagement cost fields to compare pricing across creators.
- Confirm that a creator is open to cooperation before adding them to a shortlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/blogger-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Blogger's user ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "accumCommonImpMedinNum30d": 0,
  "accumCoopImpMedinNum30d": 0,
  "accumPicCommonImpMedinNum30d": 0,
  "accumVideoCommonImpMedinNum30d": 0,
  "activityList": [
    "6adb6413e4b078c833452df1"
  ],
  "algoRecommendReasons": null,
  "authorityList": null,
  "avgAgmv90d": 0.0,
  "avgLiveViewerNum": 0.0,
  "businessNoteCount": 181,
  "buyerType": 1,
  "classifyCode": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fansCount / fansNum` | Total follower count of the creator. Both fields show the same value in this response. |
| `businessNoteCount` | Number of sponsored (business) notes recorded for the creator. |
| `coopNoteNum30d` | Number of cooperation notes in the last 30 days, as the `30d` suffix indicates. |
| `cooperateState / cooperType` | Numeric codes for the creator's cooperation status and cooperation type. The response does not explain what each code means. |
| `currentLevel` | Numeric level of the creator on the platform. The response does not explain the scale. |
| `clickMidNum / clickMidNumMcn` | Median click count figures. In this response both fields hold the same value. |
| `fans30GrowthNum / fans30GrowthRate` | Follower growth over the last 30 days, as a count and as a rate. The rate can be `null`. |
| `estimatePictureCpm / estimateVideoCpm` | Estimated CPM for picture notes and for video notes. A value of `0.0` means no estimate is present. |
| `estimatePictureEngageCost / estimateVideoEngageCost` | Estimated cost per engagement for picture notes and for video notes. |
| `clothingIndustryPrice.picturePrice / clothingIndustryPrice.videoPrice` | Quoted prices for picture and video notes in the clothing industry. The matching `pictureState` and `videoState` fields hold state codes. |

### Notes

- Many fields are `null` or `0` when the platform has no data for that creator, so check for empty values before comparing creators.
- To find a `userId`, search for creators with [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- For deeper analysis of the same creator, call [Xiaohongshu Pugongying Creator Core Metrics](/apis/xiaohongshu/pgy-v2/data-core-data) or [Xiaohongshu Pugongying Follower Distribution](/apis/xiaohongshu/pgy-v2/user-id-fans-profile).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/blogger-user-id.json`](../../../../catalog/models/xiaohongshu/pgy-v2/blogger-user-id.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/blogger-user-id
