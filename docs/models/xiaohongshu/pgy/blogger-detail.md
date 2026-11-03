# Xiaohongshu (RED) PGY Blogger Details API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID. Returns creator metrics and account details.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-detail", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-detail', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-detail", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-detail", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID, obtainable from blogger list results or PGY blogger page URL  |

## Details

Returns a PGY profile record for one Xiaohongshu (RED) blogger. It needs the blogger's `user_id`. The record holds follower counts, 30-day cooperation and impression figures, and estimated ad cost metrics.

### Use cases

- Check a creator's current follower count before adding them to a campaign shortlist.
- Compare estimated picture and video CPM across several bloggers to plan an ad budget.
- Check 30-day follower growth and cooperation note counts to see how active a creator is in brand work.
- Pull a creator's profile record into your own influencer database, keyed by `user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID, obtainable from blogger list results or PGY blogger page URL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "accumCommonImpMedinNum30d": 0,
    "accumCoopImpMedinNum30d": 0,
    "accumPicCommonImpMedinNum30d": 0,
    "accumVideoCommonImpMedinNum30d": 0,
    "activityList": null,
    "algoRecommendReasons": null,
    "authorityList": null,
    "avgAgmv90d": 0.0,
    "avgLiveViewerNum": 0.0,
    "businessNoteCount": 0,
    "buyerType": 1,
    "classifyCode": null
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.fansCount / data.fansNum` | Number of followers the blogger has. Both fields show the same value in this response. |
| `data.fans30GrowthNum / data.fans30GrowthRate` | Follower growth over the last 30 days, as a count and as a rate. The rate can be `null`. |
| `data.coopNoteNum30d` | Number of cooperation notes the blogger published in the last 30 days. |
| `data.accumCoopImpMedinNum30d / data.accumCommonImpMedinNum30d` | Median impression figures over 30 days, for cooperation notes and for regular notes. |
| `data.accumPicCommonImpMedinNum30d / data.accumVideoCommonImpMedinNum30d` | 30-day median impression figures for regular picture notes and regular video notes. |
| `data.estimatePictureCpm / data.estimateVideoCpm` | Estimated cost per thousand impressions for picture notes and for video notes. |
| `data.estimatePictureEngageCost / data.estimateVideoEngageCost` | Estimated cost per engagement for picture notes and for video notes. |
| `data.estimatePictureCpmCompare / data.estimateVideoCpmCompare` | Comparison values for the CPM estimates above. |
| `data.businessNoteCount` | Number of business notes counted for this blogger. |
| `data.avgLiveViewerNum / data.avgAgmv90d` | Average live viewer count, and an average `agmv` figure over 90 days. |

### Notes

- Get `user_id` from the blogger list results in [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list), or from the PGY blogger page URL.
- Many fields are `null` or `0` when the PGY platform has no value for that blogger.
- For follower history, call [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history). For an account-level summary, call [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history): Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-detail.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-detail
