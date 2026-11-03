# Facebook Ad Search API: pricing, parameters and code examples

`facebook/ads-search` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search the Meta Ad Library by keyword and get matching ads (advertiser, creative text, CTA, platforms, and run dates) with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/ads-search", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/ads-search', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/ads-search", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/ads-search", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/ads-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to search the Meta Ad Library for (e.g. "protein powder").  |
| `adType` | string |  | Restrict to all ads (default) or only political and issue ads. one of: `all`, `political_and_issue_ads` |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor.  |
| `sortBy` | string |  | Sort order: impressions (highest first, the default) or recent (most recent). one of: `impressions`, `recent` |
| `status` | string |  | Ad status filter. one of: `ALL`, `ACTIVE`, `INACTIVE`; default `"ACTIVE"` |
| `country` | string |  | Two-letter country code to scope results. Omit for all countries.  |
| `endDate` | string |  | Filter to ads with impressions on or before this date, in YYYY-MM-DD format.  |
| `mediaType` | string |  | Creative media type filter. one of: `ALL`, `IMAGE`, `VIDEO`, `MEME`, `IMAGE_AND_MEME`, `NONE` |
| `startDate` | string |  | Filter to ads with impressions on or after this date, in YYYY-MM-DD format.  |
| `searchType` | string |  | Match mode for the query: loose keyword match (keyword_unordered, the default) or exact phrase (keyword_exact_phrase). one of: `keyword_unordered`, `keyword_exact_phrase` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every…  |

## Details

Returns ads from the Meta Ad Library that match a keyword. Each ad includes the advertiser page, creative text, call to action, platforms, and start and end dates. The only required input is `query`.

### Use cases

- Track which creatives and offers a competitor runs for a brand name.
- Collect ad copy and call-to-action types for a keyword to study how a niche advertises.
- Find the advertiser pages that run ads for a product term, then check their page details.
- Pull image links and landing page URLs for ads that mention a brand.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/ads-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nike", "country": "US", "searchType": "keyword_exact_phrase"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search the Meta Ad Library for (e.g. "protein powder"). |
| `adType` | string | No | Restrict to all ads (default) or only political and issue ads. |
| `country` | string | No | Two-letter country code to scope results. Omit for all countries. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. |
| `endDate` | string | No | Filter to ads with impressions on or before this date, in YYYY-MM-DD format. |
| `mediaType` | string | No | Creative media type filter. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `totalResults`, and it is served only by a source that returns every o |
| `searchType` | string | No | Match mode for the query: loose keyword match (keyword_unordered, the default) or exact phrase (keyword_exact_phrase). |
| `sortBy` | string | No | Sort order: impressions (highest first, the default) or recent (most recent). |
| `startDate` | string | No | Filter to ads with impressions on or after this date, in YYYY-MM-DD format. |
| `status` | string | No | Ad status filter. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "active": true,
        "adCount": null,
        "caption": "play.google.com",
        "categories": [
          "UNKNOWN"
        ],
        "creatives": [],
        "ctaText": "Install now",
        "ctaType": "INSTALL_MOBILE_APP",
        "displayFormat": "IMAGE",
        "endDate": 1793606400,
        "id": "1550534860016399",
        "isReshared": false,
        "linkDescription": ""
      }
    ],
    "nextCursor": "cur_I3725J-mWy22VxKd8YIRew",
    "totalResults": 19895
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].id` | ID of the ad in the Meta Ad Library. `sourceUrl` links to the ad's library page. |
| `data.ads[].pageName / pageId / pageUrl` | Name, ID and Facebook URL of the advertiser page that runs the ad. |
| `data.ads[].text / title` | Main body text and headline of the ad. |
| `data.ads[].ctaText / ctaType` | Button label shown on the ad (such as `Shop now`) and its type code (such as `SHOP_NOW`). |
| `data.ads[].platforms` | List of platforms the ad runs on, such as `FACEBOOK`, `INSTAGRAM`, `MESSENGER` and `AUDIENCE_NETWORK`. |
| `data.ads[].startDate / endDate` | Start and end of the ad run as Unix timestamps in seconds. |
| `data.ads[].active` | `true` when the ad is currently active. |
| `data.ads[].displayFormat` | Creative format, for example `IMAGE` or `DPA`. Ads in `DPA` format carry several items in `creatives`. |
| `data.ads[].creatives[]` | Per-item creatives for multi-item ads. Each has `title`, `body`, `image`, `linkUrl`, `ctaText` and `ctaType`. |
| `data.ads[].media[]` | Media files of the ad. Each has a `type` and a `url`. |
| `data.totalResults` | Total number of ads that match the search. |

### Notes

- Pass `nextCursor` from the response as `cursor` in the next request to get the next page.
- Ad IDs are numeric strings. Use them with [Facebook Ad Details](/apis/facebook/ad-details) to look up one ad.
- To list ads for one advertiser instead of a keyword, use [Facebook Company Ads](/apis/facebook/company-ads).
- `adCount` is `null` for the ads in this sample.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/ads-search.json`](../../../catalog/models/facebook/ads-search.json) · Store page: https://www.sandbase.ai/model/facebook/ads-search
