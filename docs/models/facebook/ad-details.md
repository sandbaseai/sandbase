# Facebook Ad Details API: pricing, parameters and code examples

`facebook/ad-details` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Look up a single Meta Ad Library ad by ID or URL and get the advertiser, creative text, call-to-action, platforms, and run dates as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ad-details"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ad-details', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ad-details", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ad-details", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/ad-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | Meta Ad Library ad ID (e.g. "702369045530963"). Provide either id or url.  |
| `url` | string |  | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1185617869915074"). Provide either id or url.  |

## Details

This API returns the details of one ad from the Meta Ad Library: the advertiser page, ad text, call-to-action, creatives, platforms, and run dates. It needs either an ad `id` or an Ad Library `url`.

### Use cases

- Check which creatives and call-to-action buttons a competitor uses in a specific ad.
- Record the start and end dates of an ad to track how long a campaign runs.
- Find out which platforms (Facebook, Instagram, Messenger) an ad is shown on.
- Save the advertiser page name, page ID and page URL for an ad you found in the Ad Library.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ad-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "962050096457659"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | Meta Ad Library ad ID (e.g. "702369045530963"). Provide either id or url. |
| `url` | string | No | Meta Ad Library ad URL (e.g. "https://www.facebook.com/ads/library?id=1185617869915074"). Provide either id or url. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "active": true,
    "adArchiveId": "962050096457659",
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
        "image": "https://scontent-bos5-1.xx.fbcdn.net/v/t39.35426-6/706538687_1471950538014143_79…",
        "linkDescription": "Download Depop - Buy & Sell Clothes by Depop Ltd on the App Store. See screensho…",
        "linkUrl": "https://www.depop.com/products/xaznbabyx-open-back-workout-top-cute/",
        "title": "LOFT Women's T-shirt"
      }
    ],
    "ctaText": "Download",
    "currency": "",
    "displayFormat": "DPA",
    "endDate": 1793606400,
    "isReshared": false,
    "linkDescription": "Download Depop - Buy & Sell Clothes by Depop Ltd on the App Store. See screensho…",
    "linkUrl": "http://itunes.apple.com/app/id518684914"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.adArchiveId` | The ID of the ad in the Ad Library. It matches the `id` you sent. |
| `data.active` | Whether the ad is marked as active (`true`) or not. |
| `data.startDate / data.endDate` | Start and end of the ad run as Unix timestamps in seconds. |
| `data.pageName / data.pageId / data.pageUrl` | Name, ID and Facebook URL of the page that runs the ad. |
| `data.pageLikes` | Number of likes on the advertiser page. |
| `data.pageCategories` | Category labels of the advertiser page, such as `Shopping`. |
| `data.platforms` | Platforms the ad runs on, such as `facebook`, `instagram` and `messenger`. |
| `data.text / data.title` | Main ad text and headline. |
| `data.ctaText / data.displayFormat` | Label of the call-to-action button and the ad format (for example `DPA`). |
| `data.creatives[].body / data.creatives[].title / data.creatives[].linkUrl` | Text, headline and destination link of each creative in the ad. Ads with several creatives return one entry per creative. |
| `data.creatives[].ctaType` | Call-to-action type for the creative, such as `DOWNLOAD`. |
| `data.media[].type / data.media[].url` | Type of each media item (for example `photo`) and its file URL. |

### Notes

- Send either `id` or `url`. The `url` has the form `https://www.facebook.com/ads/library?id=<ad id>`.
- If no ad matches, the response has `found: false`.
- To list ads from one advertiser, use [Facebook Company Ads](/apis/facebook/company-ads). To search ads by keyword, use [Facebook Ad Search](/apis/facebook/ads-search).
- For more creative-level data on one ad, try [Facebook Ad Creative Details](/apis/facebook/ad-details-full).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/ad-details.json`](../../../catalog/models/facebook/ad-details.json) · Store page: https://www.sandbase.ai/model/facebook/ad-details
