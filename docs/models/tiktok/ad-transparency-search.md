# TikTok Ad Transparency Search API: pricing, parameters and code examples

`tiktok/ad-transparency-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Search TikTok's EU Commercial Content Library by keyword or advertiser ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-transparency-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-transparency-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-transparency-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-transparency-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ad-transparency-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `days` | integer |  | Number of days of Commercial Content Library history to search, from 1 to 365. Defaults to 30. default `30`; range 1–365 |
| `sort` | string |  | Sort expression. Defaults to last_shown_date,desc. default `"last_shown_date,desc"` |
| `limit` | integer |  | Maximum number of ads to return, from 1 to 50. Defaults to 20. Billing is flat per request. default `20`; range 1–50 |
| `query` | string |  | Keyword to search in TikTok's EU Commercial Content Library. Provide query or advertiserId.  |
| `cursor` | string |  | Search cursor from a previous response's nextCursor.  |
| `offset` | integer |  | Zero-based result offset. Defaults to 0. default `0`; range 0– |
| `region` | string |  | Region code for the transparency search. Defaults to DE. default `"DE"` |
| `advertiserId` | string |  | TikTok Commercial Content Library advertiser ID. Provide advertiserId or query.  |

## Details

This API searches TikTok's EU Commercial Content Library and returns a list of ads. Each ad includes its title, advertiser name, audience estimate, show dates, and media links. Send a keyword in `query` or a library advertiser ID in `advertiserId`.

### Use cases

- Track which ads a brand such as Nike runs on TikTok in Germany.
- Check how long a campaign has been running by comparing its first and last shown dates.
- Collect ad videos and images from competitors for creative research.
- List all ads from one advertiser by passing its `advertiserId`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-transparency-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"days": 30, "limit": 20, "query": "nike", "region": "DE"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiserId` | string | No | TikTok Commercial Content Library advertiser ID. Provide advertiserId or query. |
| `cursor` | string | No | Search cursor from a previous response's nextCursor. |
| `days` | integer | No | Number of days of Commercial Content Library history to search, from 1 to 365. Defaults to 30. |
| `limit` | integer | No | Maximum number of ads to return, from 1 to 50. Defaults to 20. Billing is flat per request. |
| `offset` | integer | No | Zero-based result offset. Defaults to 0. |
| `query` | string | No | Keyword to search in TikTok's EU Commercial Content Library. Provide query or advertiserId. |
| `region` | string | No | Region code for the transparency search. Defaults to DE. |
| `sort` | string | No | Sort expression. Defaults to last_shown_date,desc. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "adTitle": "Neue Winterausrüstung in Nike Factory Stores.",
        "advertiserName": "NIKE Retail B.V.",
        "estimatedAudience": "300K-400K",
        "firstShownUtc": 1792454400,
        "format": "2",
        "id": "1879578150853922",
        "image": "https://p16-common-sign.tiktokcdn.com/ad-site-i18n-sg/20261013c7c72a61615657cc4f…",
        "lastShownUtc": 1793577600,
        "status": "1",
        "videoUrl": "https://library.tiktok.com/api/v1/cdn/1793691828/video/aHR0cHM6Ly92MTZtLnRpa3Rva…"
      }
    ],
    "hasMore": false,
    "nextCursor": "cur_r-MF0Us35pN_wCPP3qHT6Q",
    "offset": 0,
    "region": "DE",
    "total": 4448
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].id` | ID of the ad in the Commercial Content Library, returned as a string. |
| `data.ads[].adTitle` | Text title of the ad. |
| `data.ads[].advertiserName` | Name of the advertiser that ran the ad. |
| `data.ads[].estimatedAudience` | Estimated audience size as a range string, for example `300K-400K`. |
| `data.ads[].firstShownUtc / data.ads[].lastShownUtc` | Unix timestamps in seconds for the first and last day the ad was shown. |
| `data.ads[].videoUrl / data.ads[].image` | Links to the ad video and the ad image. |
| `data.ads[].format / data.ads[].status` | Coded values for the ad format and ad status, returned as strings such as `2` and `1`. |
| `data.total` | Total number of ads that match the search. |
| `data.hasMore / data.nextCursor` | `hasMore` tells you if more results exist. `nextCursor` is the value to send as `cursor` in the next request. |
| `data.region` | Region code used for the search. |

### Notes

- Send either `query` or `advertiserId`. Use `limit` (1 to 50) and `offset` to page through results.
- To get the next page, pass `data.nextCursor` as `cursor` in the next request.
- A search with no match returns `found: false`.
- For details on a single ad, try [TikTok Ad Library Ad](/apis/tiktok/ad-library-ad). For another ad search, see [TikTok Ad Library Search](/apis/tiktok/ad-library-search).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/ad-transparency-search.json`](../../../catalog/models/tiktok/ad-transparency-search.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-transparency-search
