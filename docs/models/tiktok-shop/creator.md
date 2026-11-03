# TikTok Shop Creator API: pricing, parameters and code examples

`tiktok-shop/creator` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0055 per call · **Modes:** sync

TikTok Shop creator performance by handle: GMV range, promoted product count, brand collaborations, follower age/gender/location demographics, category GMV split, and video versus live engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0055**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/creator", "handle": "golinutrition"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/creator', {'handle': 'golinutrition'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/creator", {
  "handle": "golinutrition"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/creator", sandbase.Params{
	"handle": "golinutrition",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/creator` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | TikTok handle of the creator or shop account, without the @ (e.g. golinutrition).  |
| `region` | string |  | Country code of the TikTok Shop market. Only the US market is served; creators in other markets are not available. one of: `us`, `US`; default `"us"` |

## Details

Returns TikTok Shop performance data for one creator or shop account in the US market. You send a TikTok `handle` without the @, and the API returns a GMV range, follower audience breakdowns, content stats, and categories.

### Use cases

- Vet a creator before an affiliate outreach by checking `gmvRange`, `promotedProducts`, and `brandCollaborations`.
- Match a creator to your target buyers using the audience age, gender, and state breakdowns.
- Compare how a creator performs in short videos versus live streams using the engagement and average view fields.
- Check which TikTok Shop categories a creator sells in before you pitch a product.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/creator" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "golinutrition"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | TikTok handle of the creator or shop account, without the @ (e.g. golinutrition). |
| `region` | string | No | Country code of the TikTok Shop market. Only the US market is served; creators in other markets are not available. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "audienceAge": [
      {
        "bucket": "25-34",
        "sharePct": 27.55
      }
    ],
    "audienceGender": [
      {
        "gender": "male",
        "sharePct": 33.49
      }
    ],
    "audienceLocations": [
      {
        "followers": 124600,
        "state": "TEXAS"
      }
    ],
    "avgCommissionRange": "",
    "avgLiveLikes": 19734,
    "avgLiveViews": 146572,
    "avgVideoComments": 0,
    "avgVideoLikes": 0,
    "avgVideoViews": 281,
    "bio": "Making Health Delicious and Simple✨\nVegan. Gluten-Free. Non-GMO.",
    "brandCollaborations": 1,
    "categories": [
      {
        "categoryId": "700645",
        "name": "Health"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the handle was found. A lookup that finds nothing returns `false`. |
| `data.gmvRange` | Range of gross merchandise value for the creator, as text such as `$25K-$60K`. |
| `data.promotedProducts / data.brandCollaborations` | Number of products the creator promotes and number of brand collaborations. |
| `data.followers / data.videoCount / data.liveCount` | Follower count, number of videos, and number of live streams for the account. |
| `data.audienceAge[].bucket / data.audienceAge[].sharePct` | Follower age range and the percentage of the audience in that range. |
| `data.audienceGender[].gender / data.audienceGender[].sharePct` | Follower gender and the percentage of the audience of that gender. |
| `data.audienceLocations[].state / data.audienceLocations[].followers` | US state name and the number of followers located there. |
| `data.videoEngagementRate / data.liveEngagementRate` | Engagement rate for video content and for live streams. |
| `data.avgVideoViews / data.avgLiveViews / data.avgLiveLikes` | Average views per video, average views per live, and average likes per live. |
| `data.categories[].categoryId / data.categories[].name` | Category ID and name for the categories the creator is listed in. |

### Notes

- Use the TikTok username without the @ as `handle`. Only the US market is served, so `region` accepts `us` or `US`.
- Some fields can come back empty or `null`, such as `avgCommissionRange`, `gpm`, and `rating`. Some averages can be `0`.
- To see what the creator sells, call [TikTok Shop User Showcase](/apis/tiktok-shop/user-showcase). For a shop account's catalog, use [TikTok Shop Store Products](/apis/tiktok-shop/shop-products).
- Use the `categoryId` values with [TikTok Shop Categories](/apis/tiktok-shop/categories) to look up category details.

### Pricing

Billed at the actual cost of each call, about $0.0055 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/creator.json`](../../../catalog/models/tiktok-shop/creator.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/creator
