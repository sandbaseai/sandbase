# Xiaohongshu (RED) PGY Blogger Data Summary API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-data-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-data-summary", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-data-summary', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-data-summary", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-data-summary", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-data-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |

## Details

Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform. It needs the blogger's `user_id`. The response covers activity, note counts, reads, engagement, estimated cost metrics and content tags.

### Use cases

- Screen a blogger's recent reads and engagement before sending a collaboration invite.
- Compare estimated picture-note cost metrics such as `estimatePictureCpm` against peer benchmarks for campaign budgeting.
- Check whether a blogger is active and how many invites they have received.
- Group bloggers by their main content tags to build a shortlist for a category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-data-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5c668b3e0000000012021605"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "activeDayInLast7": 7,
    "dateKey": "2026-11-02",
    "easyConnect": true,
    "estimatePictureCpm": 294.50076456929264,
    "estimatePictureCpmCompare": 34.64,
    "estimatePictureCpuv": 0,
    "estimatePictureCpuvCompare": 0,
    "estimatePictureEngageCost": 8.227848101265822,
    "estimatePictureEngageCostCompare": 41.41,
    "estimateVideoCpm": 0,
    "estimateVideoCpmCompare": 0,
    "estimateVideoCpuv": 0
  },
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.isActive / data.activeDayInLast7` | Whether the blogger is active, and the number of active days in the last 7 days. |
| `data.noteNumber` | Number of notes counted in this summary. |
| `data.readMedian / data.interactionMedian` | Median reads and median interactions per note. |
| `data.mAccumImpNum / data.mValidRawReadFeedNum / data.mEngagementNum` | Accumulated impressions, valid reads from the feed, and engagement count. The matching `Compare` fields hold a comparison value for each. |
| `data.estimatePictureCpm / data.estimatePictureEngageCost` | Estimated cost metrics for picture notes: CPM and cost per engagement. The `Compare` versions hold the matching comparison values. Video fields such as `estimateVideoCpm` return 0 for this blogger. |
| `data.fans30GrowthRate / data.fans30GrowthBeyondRate` | Follower growth rate over 30 days, and the share of bloggers it beats. Both are strings. |
| `data.interactionBeyondRate / data.pictureReadBeyondRate` | Share of bloggers this account beats on interaction and on picture-note reads. Both are strings. |
| `data.kolAdvantage / data.kolAdvantageHover` | Label for the blogger's strength, with a short explanation of why it was assigned. Both are in Chinese. |
| `data.noteType[].contentTag / data.noteType[].percent` | Content tag and the percentage of notes under that tag. |
| `data.inviteNum` | Number of invites the blogger has received. |

### Notes

- Pass the blogger's PGY user ID as `user_id`, for example `5c668b3e0000000012021605`. You can find IDs with [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list).
- `data.dateKey` is formatted as `YYYY-MM-DD`.
- For follower history, call [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history). For profile details, call [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) Blogger Core Data](/apis/xiaohongshu/pgy/blogger-core-data): Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.
- [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history): Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-data-summary.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-data-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-data-summary
