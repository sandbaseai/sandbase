# LinkedIn Ad Search API: pricing, parameters and code examples

`linkedin/ads-search` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search the LinkedIn Ad Library by company or keyword and list matching ads (advertiser, headline, creative text, format, CTA, and run dates) with pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/ads-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/ads-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/ads-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/ads-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/linkedin/ads-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company` | string |  | Company name to search (e.g. "microsoft").  |
| `endDate` | string |  | Search end date in YYYY-MM-DD format. Today or a later date is moved back to yesterday in UTC when your range overlaps LinkedIn's accepted dates. When you send startDate without endDate, the search ends yesterday in…  |
| `keyword` | string |  | Keyword term for the ad search.  |
| `companyId` | string |  | LinkedIn company identifier.  |
| `countries` | string |  | Comma-separated two-letter country codes (e.g. "US,CA,MX").  |
| `startDate` | string |  | Search start date in YYYY-MM-DD format. An earlier date is moved up to one year ago in UTC when your range overlaps LinkedIn's accepted dates.  |
| `paginationToken` | string |  | Opaque pagination token from a previous response's nextCursor.  |

## Details

This API searches the LinkedIn Ad Library and returns a page of matching ads. Each ad includes the advertiser, headline, body text, format, call to action, run dates and impression range. Send a `company` name, a `companyId` or a `keyword`, and optionally narrow the results by country and date range.

### Use cases

- Track which ads a competitor runs on LinkedIn and how their messaging changes over time.
- Collect ad creative text and headlines for a swipe file or messaging research.
- Check which countries and date ranges a company targets by filtering with `countries`, `startDate` and `endDate`.
- Compare the ad formats a brand uses, such as single image and carousel ads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/ads-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company": "microsoft"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company` | string | No | Company name to search (e.g. "microsoft"). |
| `companyId` | string | No | LinkedIn company identifier. |
| `countries` | string | No | Comma-separated two-letter country codes (e.g. "US,CA,MX"). |
| `endDate` | string | No | Search end date in YYYY-MM-DD format. Today or a later date is moved back to yesterday in UTC when your range overlaps LinkedIn's accepted dates. When you send startDate without endDate, the search ends yesterday in UTC, |
| `keyword` | string | No | Keyword term for the ad search. |
| `paginationToken` | string | No | Opaque pagination token from a previous response's nextCursor. |
| `startDate` | string | No | Search start date in YYYY-MM-DD format. An earlier date is moved up to one year ago in UTC when your range overlaps LinkedIn's accepted dates. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "adType": "Single Image Ad",
        "advertiser": "Microsoft",
        "advertiserLinkedinPage": "https://www.linkedin.com/company/1035",
        "advertiserLogo": "https://media.licdn.com/dms/image/v2/D560BAQH32RJQCl3dDQ/company-logo_100_100/B5…",
        "cta": "Registrieren",
        "description": "Nehmen Sie am 10. November beim Microsoft Frontier Transformation Day in Wien te…",
        "destinationUrl": "https://msevents.microsoft.com/event?id=4123375389&wt.mc_id=3084764_QSG_PD_SCL_6…",
        "endDate": "2026-11-03T00:00:00.000Z",
        "headline": "Frontier Transformation Day | 10. Nov.",
        "id": "1624217084",
        "startDate": "2026-10-30T00:00:00.000Z",
        "totalImpressions": "10k-20k"
      }
    ],
    "nextCursor": "1624207074-1793359876270",
    "totalAds": 26901
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].id` | Ad ID. Use it to build or look up the ad detail page. |
| `data.ads[].url` | Link to the ad's page in the LinkedIn Ad Library. |
| `data.ads[].advertiser` | Name of the advertiser running the ad. |
| `data.ads[].advertiserLinkedinPage` | URL of the advertiser's LinkedIn company page. The number at the end is the LinkedIn company ID. |
| `data.ads[].adType` | Ad format, for example `Single Image Ad` or `Carousel Ad`. |
| `data.ads[].headline / data.ads[].description / data.ads[].cta` | Headline, body text and call-to-action label of the ad. They are in the ad's own language and can be empty strings. |
| `data.ads[].destinationUrl` | Landing page URL the ad links to. It is empty for some ads. |
| `data.ads[].startDate / data.ads[].endDate` | ISO 8601 timestamps for when the ad ran. They are empty strings when the library shows no dates. |
| `data.ads[].totalImpressions` | Impression range as a text bucket, for example `10k-20k`. It is empty when not shown. |
| `data.nextCursor` | Token for the next page of results. |
| `data.totalAds` | Total number of ads that match the search. |

### Notes

- Send `data.nextCursor` as `paginationToken` in the next request to get the following page.
- Dates use the `YYYY-MM-DD` format in requests. Ad dates in the response are full ISO timestamps.
- Some ads return empty strings for `headline`, `cta`, `endDate` and `totalImpressions`, so check for blanks before you use them.
- To get more detail on a single ad, pass its `id` to [LinkedIn Ad Details](/apis/linkedin/ad).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/ads-search.json`](../../../catalog/models/linkedin/ads-search.json) · Store page: https://www.sandbase.ai/model/linkedin/ads-search
