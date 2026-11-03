# Xiaohongshu Pugongying Similar Creators API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/kol-similar-kol` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get paginated Xiaohongshu Pugongying creators similar to a known creator. Use it to expand a campaign shortlist from an existing reference account.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/kol-similar-kol", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/kol-similar-kol', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/kol-similar-kol", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/kol-similar-kol", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/kol-similar-kol` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `pageNum` | integer |  | Page number for results. default `1` |

## Details

Returns a page of Xiaohongshu Pugongying creators that resemble a reference creator. Each creator comes with follower counts, note counts, level and cooperation fields. You pass the reference creator's `userId`.

### Use cases

- Expand a campaign shortlist by finding creators similar to one account you already trust.
- Compare follower size across lookalike creators to pick candidates in a target audience range.
- Filter similar creators by `cooperateState` before you reach out.
- Rank candidates by `businessNoteCount` to see who already publishes sponsored content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/kol-similar-kol" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `pageNum` | integer | No | Page number for results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "highlightWords": [],
  "kols": [
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
      "businessNoteCount": 73,
      "buyerType": 2,
      "classifyCode": null
    }
  ],
  "redirect2NickSearch": false,
  "resultType": 0,
  "total": 8,
  "trackId": "kolSimilar_6df6cc54eceb4c13a94facae835ed2a5"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `kols[]` | List of similar creators on this page. |
| `kols[].fansCount / kols[].fansNum` | Follower count of the creator. Both fields hold the same value in this response. |
| `kols[].businessNoteCount` | Number of sponsored (business) notes recorded for the creator. |
| `kols[].coopNoteNum30d` | Number of cooperation notes in the last 30 days, as the key name says. |
| `kols[].clickMidNum / kols[].clickMidNumMcn` | Click-related metric for the creator. The two fields carry the same number in this response. |
| `kols[].currentLevel` | Creator level on the platform. A value of `-1` appears for a creator with no level. |
| `kols[].cooperateState / kols[].cooperType` | Numeric codes for the creator's cooperation status and cooperation type. The response does not explain what each code means. |
| `kols[].fans30GrowthNum / kols[].fans30GrowthRate` | Follower growth over 30 days, as a count and as a rate. The rate can be `null`. |
| `kols[].clothingIndustryPrice.picturePrice / kols[].clothingIndustryPrice.videoPrice` | Price fields for picture and video notes in the clothing industry. They are `0` for the creators shown. |
| `total` | Total number of similar creators found for the reference creator. |
| `trackId` | Identifier of this similar-creator request. |

### Notes

- Send `pageNum` to move through pages. It defaults to `1`.
- Many numeric fields are `0` and many others are `null` for some creators, so check values before you rely on them.
- To read more about a creator in the list, call [Xiaohongshu Pugongying Creator Profile](/apis/xiaohongshu/pgy-v2/blogger-user-id) or [Xiaohongshu Pugongying Creator Core Metrics](/apis/xiaohongshu/pgy-v2/data-core-data).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/kol-similar-kol.json`](../../../../catalog/models/xiaohongshu/pgy-v2/kol-similar-kol.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/kol-similar-kol
