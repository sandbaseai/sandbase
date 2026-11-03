# Facebook Company Ads API: pricing, parameters and code examples

`facebook/company-ads` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List the Meta Ad Library ads a company is running by page ID or company name (creative text, format, platforms, and run dates) with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/company-ads"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/company-ads', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/company-ads", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/company-ads", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/facebook/company-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |
| `pageId` | string |  | Company's Ad Library page ID. Provide either pageId or companyName.  |
| `sortBy` | string |  | Sort order: impressions (highest first, the default) or recent (most recent). one of: `impressions`, `recent` |
| `status` | string |  | Ad status filter. Defaults to ACTIVE. one of: `ALL`, `ACTIVE`, `INACTIVE` |
| `country` | string |  | Two-letter country code to scope results. Defaults to all countries.  |
| `endDate` | string |  | Filter to ads with impressions on or before this date, in YYYY-MM-DD format.  |
| `language` | string |  | Two-letter language code to filter ads (e.g. "EN", "ES", "FR").  |
| `mediaType` | string |  | Creative media type filter. one of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE` |
| `startDate` | string |  | Filter to ads with impressions on or after this date, in YYYY-MM-DD format.  |
| `companyName` | string |  | Company name to search (e.g. "nike"). Exact-match and case-sensitive against the Meta Ad Library index; an advertiser with no indexed page returns found:false.  |

## Details

Returns the Meta Ad Library ads a company runs, with ad text, display format, platforms, and start and end dates. You pass either a `pageId` or a `companyName`. Results come in pages with a cursor.

### Use cases

- Track the newest ads a competitor launches by sorting with `sortBy: recent`.
- Collect the headline, body text, and call-to-action wording a brand uses in its ads.
- Check which platforms (Facebook, Instagram, WhatsApp) a brand targets with each ad.
- Pull image and video URLs from a brand's ads to review its creative style.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/company-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pageId": "15087023444", "sortBy": "recent"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `companyName` | string | No | Company name to search (e.g. "nike"). Exact-match and case-sensitive against the Meta Ad Library index; an advertiser with no indexed page returns found:false. |
| `country` | string | No | Two-letter country code to scope results. Defaults to all countries. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `endDate` | string | No | Filter to ads with impressions on or before this date, in YYYY-MM-DD format. |
| `language` | string | No | Two-letter language code to filter ads (e.g. "EN", "ES", "FR"). |
| `mediaType` | string | No | Creative media type filter. |
| `pageId` | string | No | Company's Ad Library page ID. Provide either pageId or companyName. |
| `sortBy` | string | No | Sort order: impressions (highest first, the default) or recent (most recent). |
| `startDate` | string | No | Filter to ads with impressions on or after this date, in YYYY-MM-DD format. |
| `status` | string | No | Ad status filter. Defaults to ACTIVE. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "active": true,
        "adCount": 1,
        "caption": "nike.in",
        "categories": [
          "UNKNOWN"
        ],
        "creatives": [
          {
            "body": "Race the Night Away in The Nike After Dark Tour Collection",
            "ctaText": "Shop Now",
            "ctaType": "SHOP_NOW",
            "image": "https://scontent-bos5-1.xx.fbcdn.net/v/t39.35426-6/867290372_1407183714905230_32…",
            "linkUrl": "https://www.nike.in/styles-for-after-dark-tour/c/118363",
            "title": "Step To The Starting Line."
          }
        ],
        "ctaText": "Shop now",
        "ctaType": "SHOP_NOW",
        "currency": "",
        "displayFormat": "DCO",
        "endDate": 1793606400,
        "id": "2006384856715426",
        "isReshared": false
      }
    ],
    "nextCursor": "cur_9-LwAOFGJDpFAVSYrocbjQ",
    "totalResults": 3053
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].id` | ID of the ad in the Ad Library. |
| `data.ads[].text / data.ads[].title` | Main body text and headline of the ad. |
| `data.ads[].displayFormat` | Format of the ad, such as `DCO` or `VIDEO`. |
| `data.ads[].platforms` | List of platforms the ad runs on, such as `FACEBOOK`, `INSTAGRAM`, `WHATSAPP`. |
| `data.ads[].startDate / data.ads[].endDate` | Start and end of the ad run as Unix timestamps in seconds. |
| `data.ads[].active` | `true` when the ad is currently active. |
| `data.ads[].ctaText / data.ads[].ctaType / data.ads[].linkUrl` | Call-to-action button label, its type code (for example `SHOP_NOW`), and the landing page URL. |
| `data.ads[].creatives[]` | Creative variants of the ad. Each has `body`, `title`, `image`, `ctaText`, and `linkUrl`. The list can be empty, as for video ads. |
| `data.ads[].media[]` | Media files of the ad. Each has a `type` (`photo` or `video`) and a `url`. Video items also have `videoUrl`. |
| `data.ads[].pageId / data.ads[].pageName / data.ads[].pageLikes` | ID, name, and like count of the advertiser's Facebook page. |
| `data.totalResults` | Total number of ads matching the request. |

### Notes

- Pass `data.nextCursor` as `cursor` in the next request to get the next page of ads.
- `status` defaults to `ACTIVE`. Set it to `ALL` or `INACTIVE` to see ended ads.
- `companyName` must match exactly and is case-sensitive. If no page matches, the response has `found: false`. Use [Facebook Company Search](/apis/facebook/search-companies) to find a page ID.
- To inspect a single ad in more detail, call [Facebook Ad Details](/apis/facebook/ad-details) with the ad `id`.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/company-ads.json`](../../../catalog/models/facebook/company-ads.json) · Store page: https://www.sandbase.ai/model/facebook/company-ads
