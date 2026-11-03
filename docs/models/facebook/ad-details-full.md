# Facebook Ad Creative Details API: pricing, parameters and code examples

`facebook/ad-details-full` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00462 per call · **Modes:** sync

Pull one Meta Ad Library ad with its creative: every carousel variant, image and video URL, headline, body, and call to action.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00462**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-details-full", "id": "962050096457659"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ad-details-full', {'id': '962050096457659'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ad-details-full", {
  "id": "962050096457659"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ad-details-full", sandbase.Params{
	"id": "962050096457659",
})
```

Same call via the path form: `POST /v1/api/facebook/ad-details-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Meta Ad Library ad ID - the numeric id in an Ad Library URL (e.g. "962050096457659" from https://www.facebook.com/ads/library/?id=962050096457659).  |

## Details

This API returns one ad from the Meta Ad Library, including the page that runs it and every creative variant. You send the Ad Library ad ID in `id`. The response has the ad text, call to action, image and video URLs, platforms, and run dates.

### Use cases

- Archive the full carousel of a competitor ad, with each card's title, image, and landing page link.
- Check which platforms an ad runs on and whether it is still active.
- Collect the landing page URLs and call to action types used in a brand's ads.
- Record when an ad started and ended to build a timeline of a campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ad-details-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "962050096457659"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Meta Ad Library ad ID - the numeric id in an Ad Library URL (e.g. "962050096457659" from https://www.facebook.com/ads/library/?id=962050096457659). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "active": true,
    "adArchiveId": "962050096457659",
    "body": "Free Depop Shipping just dropped. Go find something you love.",
    "caption": "itunes.apple.com",
    "categories": [
      "UNKNOWN"
    ],
    "creatives": [
      {
        "body": "Free Depop Shipping just dropped. Go find something you love.",
        "caption": "itunes.apple.com",
        "ctaText": "Download",
        "ctaType": "DOWNLOAD",
        "image": "https://scontent.frst1-1.fna.fbcdn.net/v/t39.35426-6/706317255_2037222576909248_…",
        "imageResized": "https://scontent.frst1-1.fna.fbcdn.net/v/t39.35426-6/706317255_2037222576909248_…",
        "linkDescription": "Download Depop - Buy & Sell Clothes by Depop Ltd on the App Store. See screensho…",
        "linkUrl": "https://www.depop.com/products/coachellana-coachella-2018-cardi-b-cropped/",
        "title": "Coach Women's Hoodie"
      }
    ],
    "ctaText": "Download",
    "ctaType": "DOWNLOAD",
    "displayFormat": "DPA",
    "endedUtc": 1793606400,
    "images": [],
    "isReshared": false
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the ad ID was found. A missing ad returns `found: false`. |
| `data.active` | Whether the ad is marked active. |
| `data.startedUtc / data.endedUtc` | Start and end of the ad run as Unix timestamps in seconds. |
| `data.platforms` | Platforms the ad is shown on, such as `FACEBOOK`, `INSTAGRAM`, and `MESSENGER`. |
| `data.displayFormat` | Ad format. This ad shows `DPA`. |
| `data.creatives[].title / data.creatives[].body` | Headline and body text of each creative variant. A title can be a template placeholder such as `{{product.name}}` at the top level. |
| `data.creatives[].image / data.creatives[].imageResized` | Full image URL and a smaller resized image URL for each variant. |
| `data.creatives[].ctaText / data.creatives[].ctaType` | Call to action label and its type code for each variant. |
| `data.creatives[].linkUrl` | Landing page URL for each variant. |
| `data.pageName / data.pageId / data.pageUrl / data.pageLikes` | Name, ID, Facebook URL, and like count of the page that runs the ad. |

### Notes

- Take the `id` from the `id=` value in an Ad Library URL. The response `sourceUrl` shows the same URL.
- `data.images` and `data.videos` are empty lists for this ad. Card images sit in `data.creatives[]` instead.
- To list the ads of a page first, use [Facebook Company Ads](/apis/facebook/company-ads). To find ads by keyword, use [Facebook Ad Search](/apis/facebook/ads-search).

### Pricing

Billed at the actual cost of each call, about $0.00462 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/ad-details-full.json`](../../../catalog/models/facebook/ad-details-full.json) · Store page: https://www.sandbase.ai/model/facebook/ad-details-full
