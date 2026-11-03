# Xiaohongshu Pugongying Cost Effectiveness Analysis API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v2-cost-effective` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Xiaohongshu Pugongying cost-effectiveness analysis for a known creator. Use it to assess cooperation efficiency when comparing creators for a campaign.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v2-cost-effective", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v2-cost-effective', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v2-cost-effective", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v2-cost-effective", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v2-cost-effective` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |

## Details

This API returns cost-effectiveness figures for one Xiaohongshu Pugongying creator. It covers estimated CPM, engagement cost and read cost for picture notes and video notes. It needs the creator's `userId`.

### Use cases

- Compare the estimated CPM of several shortlisted creators before you book a campaign.
- Check whether a creator is cheaper for picture notes or for video notes.
- Rank creators by `videoSurpassRate` or `pictureSurpassRate` to find the ones that beat most peers on cost.
- Pair the cost figures with follower and note metrics to build a creator scorecard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v2-cost-effective" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "date": null,
  "estimatePictureCpm": 20.004835835649338,
  "estimatePictureCpmCompare": 0.29824561403508776,
  "estimatePictureEngageCost": 0.5015363730895643,
  "estimatePictureEngageCostCompare": 0.29239766081871343,
  "estimateVideoCpm": 14.239646993455175,
  "estimateVideoCpmCompare": 0.8771929824561403,
  "estimateVideoEngageCost": 0.5981385926995191,
  "estimateVideoEngageCostCompare": 0.8771929824561403,
  "pictureCase": 0,
  "pictureReadCost": "0.40",
  "pictureSurpassRate": 37.59
}
```

### Response fields

| Field | Meaning |
|---|---|
| `estimatePictureCpm / estimateVideoCpm` | Estimated CPM for picture notes and for video notes. A lower value means a lower estimated cost per thousand impressions. |
| `estimatePictureEngageCost / estimateVideoEngageCost` | Estimated cost per engagement for picture notes and for video notes. |
| `estimatePictureCpmCompare / estimateVideoCpmCompare` | Comparison values for the CPM of each note type, given as decimals between 0 and 1 in this response. |
| `estimatePictureEngageCostCompare / estimateVideoEngageCostCompare` | Comparison values for the engagement cost of each note type, given as decimals between 0 and 1 in this response. |
| `pictureReadCost / videoReadCost` | Read cost for picture notes and for video notes. The values are strings, such as `0.40` and `1.58`. |
| `pictureSurpassRate / videoSurpassRate` | Surpass rate for each note type, such as `37.59` and `90.45`. A higher number means the creator surpasses more peers on this measure. |
| `pictureCase / videoCase` | Case counts for picture and video notes. Both are `0` in this response. |
| `date` | Date value for the data. It is `null` in this response. |

### Notes

- Pass the creator's Pugongying user ID as `userId`. You can find it with [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- Numeric cost fields come as numbers, while `pictureReadCost` and `videoReadCost` come as strings. Convert them before you sort.
- For follower and performance data on the same creator, call [Xiaohongshu Pugongying Creator Core Metrics](/apis/xiaohongshu/pgy-v2/data-core-data) or [Xiaohongshu Pugongying Note Performance Metrics](/apis/xiaohongshu/pgy-v2/data-v3-notes-rate).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v2-cost-effective.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v2-cost-effective.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v2-cost-effective
