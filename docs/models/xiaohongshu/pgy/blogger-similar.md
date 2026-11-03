# Xiaohongshu PGY similar bloggers API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-similar` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get PGY similar bloggers on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-similar", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-similar', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-similar", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-similar", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-similar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Target blogger user ID  |
| `page_num` | integer |  | Page default `1` |
| `page_size` | integer |  | Page size, 1-4 default `4` |

## Details

This API returns a list of Xiaohongshu bloggers that PGY marks as similar to a target blogger. It needs the target blogger's `user_id`, and it returns profile, content tag, pricing and cooperation data for each similar blogger.

### Use cases

- Find lookalike creators for a blogger you already work with, to widen an influencer shortlist.
- Compare follower counts and sponsored note counts across similar food or travel bloggers before you pick partners.
- Group similar bloggers by content tags to map a niche on Xiaohongshu.
- Page through the similar list to build a candidate pool for a campaign brief.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-similar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5c668b3e0000000012021605", "page_num": 1, "page_size": 4}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Target blogger user ID |
| `page_num` | integer | No | Page |
| `page_size` | integer | No | Page size, 1-4 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "highlightWords": [],
    "kols": [
      {
        "accumCommonImpMedinNum30d": 0,
        "accumCoopImpMedinNum30d": 0,
        "accumPicCommonImpMedinNum30d": 0,
        "accumVideoCommonImpMedinNum30d": 0,
        "activityList": [],
        "algoRecommendReasons": null,
        "authorityList": null,
        "avgAgmv90d": 0.0,
        "avgLiveViewerNum": 0.0,
        "businessNoteCount": 133,
        "buyerType": 2,
        "classifyCode": null
      }
    ],
    "redirect2NickSearch": false,
    "resultType": 0,
    "total": 8,
    "trackId": "kolSimilar_be353bb575c84f58a9dc3a2bfec5cf2f"
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.kols[]` | One similar blogger per item. The response holds one object for each blogger on the current page. |
| `data.kols[].fansCount / data.kols[].fansNum` | Follower count of the similar blogger. Both keys carry the same number in this response. |
| `data.kols[].contentTags[].taxonomy1Tag` | Top-level content category of the blogger, for example `美食` (food). |
| `data.kols[].contentTags[].taxonomy2Tags[]` | Sub-categories under the top-level tag, for example `美食探店` (food venue reviews). |
| `data.kols[].businessNoteCount` | Number of sponsored notes the blogger has, as the key name indicates. |
| `data.kols[].coopNoteNum30d` | Number of cooperation notes in the last 30 days, as the key name indicates. |
| `data.kols[].clickMidNum` | Median click count for the blogger. The response gives a bare number, so the exact scope is not stated. |
| `data.kols[].clothingIndustryPrice.picturePrice / data.kols[].clothingIndustryPrice.videoPrice` | Price for an image note and a video note in the clothing industry. The value is `0` for all bloggers in this sample. |
| `data.total` | Total number of similar bloggers found for the target. It was `8` in this sample. |
| `data.trackId` | Identifier of this similar-blogger result, starting with `kolSimilar_`. |

### Notes

- Set `page_size` between 1 and 4. The default is `4`.
- Use `page_num` to move through the list. Compare `data.total` with the number of items you have collected to know when to stop.
- Get a `user_id` from [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list). It is a 24-character hex string, such as `5c668b3e0000000012021605`.
- Call [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail) to look deeper at one of the similar bloggers.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-similar.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-similar.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-similar
