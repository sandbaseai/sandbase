# TikTok Ad Library Ad API: pricing, parameters and code examples

`tiktok/ad-library-ad` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch full details for a single TikTok ad (brand, title, spend, CTR, objectives, landing page, and video info).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-library-ad", "adId": "7648493525660270600"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-library-ad', {'adId': '7648493525660270600'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-library-ad", {
  "adId": "7648493525660270600"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-library-ad", sandbase.Params{
	"adId": "7648493525660270600",
})
```

Same call via the path form: `POST /v1/api/tiktok/ad-library-ad` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `adId` | string | yes | TikTok Top Ads material/ad ID, or a Top Ads detail URL (e.g. 7648493525660270600).  |

## Details

This API returns details for one TikTok ad from the Top Ads library. You pass the ad ID or a Top Ads detail URL in `adId`. The response includes the ad title, target countries, click-through rate, objective, landing page, and video details.

### Use cases

- Check the landing page and campaign objective of an ad you found in a search.
- Compare the `ctr` of different ads in the same industry.
- Download the cover image and video link of an ad for a creative review.
- See which countries an ad ran in.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-library-ad" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"adId": "7648493525660270600"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adId` | string | Yes | TikTok Top Ads material/ad ID, or a Top Ads detail URL (e.g. 7648493525660270600). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "adId": "7648493525660270600",
    "adTitle": "New Captain Tsubasa Game Arrives!",
    "brandName": "",
    "comments": 0,
    "cost": 0,
    "countries": [
      "US"
    ],
    "coverUrl": "https://p16-common-sign.tiktokcdn.com/tos-alisg-p-0051c001-sg/os0IwlEEv5Y9Ao1jzi…",
    "ctr": 0.87,
    "durationSeconds": 6.016,
    "height": 1280,
    "industry": "label_25100000000",
    "landingPage": "https://captaintsubasa-mg11.com/zh-tw/?utm_source=tiktok&utm_medium=cpc&utm_camp…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the ad exists. A lookup that finds nothing returns `false`. |
| `data.adId / data.adTitle` | The ID of the ad and its title text. |
| `data.brandName` | Name of the brand. It can be an empty string, as in this example. |
| `data.countries[]` | Country codes where the ad ran, such as `US`, `SG` and `TW`. |
| `data.ctr` | Click-through rate of the ad. The example value is `0.87`. |
| `data.objective` | Campaign objective as a label, such as `campaign_objective_conversion`. |
| `data.industry` | Industry label code, such as `label_25100000000`. The response gives the code only, not a readable name. |
| `data.landingPage` | The URL the ad sends users to, including its tracking parameters. |
| `data.likes / data.comments / data.shares / data.cost` | Counts of likes, comments and shares, and a `cost` value. All can be `0`. |
| `data.videoUrl / data.coverUrl / data.durationSeconds / data.width / data.height` | Links to the video file and cover image, plus the video length in seconds and its size in pixels. |

### Notes

- The result is returned in `outputs[0].data`. If the ad is not found, the call still succeeds and returns `found: false`.
- `adId` accepts a numeric Top Ads ID such as `7648493525660270600`, or a Top Ads detail URL.
- To find ad IDs first, use [TikTok Ad Library Search](/apis/tiktok/ad-library-search) or [TikTok Creative Center Ad Search](/apis/tiktok/ads/search-ads).
- For another view of the same ad, try [TikTok Ad Detail](/apis/tiktok/ads/ads-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/ad-library-ad.json`](../../../catalog/models/tiktok/ad-library-ad.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-library-ad
