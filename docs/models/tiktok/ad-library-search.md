# TikTok Ad Library Search API: pricing, parameters and code examples

`tiktok/ad-library-search` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Search TikTok's public Ads Library by keyword or advertiser (advertiser, title, audience band, run dates, library link, and video).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ad-library-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ad-library-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ad-library-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ad-library-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ad-library-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string |  | Keyword to search ad titles and content (e.g. spotify). Provide query or advertiserName, never both.  |
| `cursor` | string |  | Opaque cursor from a previous response's nextCursor. Omit it for the first page.  |
| `region` | string |  | Two-letter region code for TikTok's Commercial Content Library, such as DE, FR, GB or IT. Each region holds a different set of ads. Omit it to take the library's own default region, DE. Coverage is the EU and EEA; a…  |
| `advertiserName` | string |  | Advertiser name to list ads for (e.g. Spotify). Provide advertiserName or query, never both.  |

## Details

This API searches TikTok's public Ads Library and returns a page of matching ads. Each ad includes the advertiser name, ad title, an audience band, run dates, a library link and a video link. Send either a `query` keyword or an `advertiserName`, not both.

### Use cases

- Track which ads a brand currently runs on TikTok in a given EU or EEA region.
- Compare ad titles and audience bands for competing advertisers.
- Build a timeline of when a campaign started and last ran from its first and last shown dates.
- Collect library links and video links to review ad creatives.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ad-library-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "spotify"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiserName` | string | No | Advertiser name to list ads for (e.g. Spotify). Provide advertiserName or query, never both. |
| `cursor` | string | No | Opaque cursor from a previous response's nextCursor. Omit it for the first page. |
| `query` | string | No | Keyword to search ad titles and content (e.g. spotify). Provide query or advertiserName, never both. |
| `region` | string | No | Two-letter region code for TikTok's Commercial Content Library, such as DE, FR, GB or IT. Each region holds a different set of ads. Omit it to take the library's own default region, DE. Coverage is the EU and EEA; a non- |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "ads": [
      {
        "adId": "1823872659482674",
        "adTitle": "Pitch to Spotify Playlists",
        "brandName": "SPOTIFY USA INC",
        "coverUrl": "https://p16-common-sign.tiktokcdn.com/tos-alisg-p-0051c001-sg/oUeIxrmUDGrsUgpzfm…",
        "estimatedAudience": "100K-200K",
        "firstShownUtc": 1739404800,
        "format": "2",
        "lastShownUtc": 1793577600,
        "status": "1",
        "url": "https://library.tiktok.com/ads/detail/?ad_id=1823872659482674",
        "videoUrl": "https://library.tiktok.com/api/v1/cdn/1793691827/video/aHR0cHM6Ly92NzcudGlrdG9rY…"
      }
    ],
    "hasMore": false,
    "nextCursor": "cur_uNU1NXRd1LfZ6gD-_NvMGA",
    "total": 5000
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.ads[].adId` | ID of the ad. Pass it to an ad detail API to get more about one ad. |
| `data.ads[].adTitle` | Title text of the ad. |
| `data.ads[].brandName` | Name of the advertiser that ran the ad, such as `SPOTIFY LIMITED`. |
| `data.ads[].estimatedAudience` | Audience size as a range string, such as `100K-200K` or `1M-10M`. |
| `data.ads[].firstShownUtc / data.ads[].lastShownUtc` | Unix timestamps in seconds for the first and last day the ad was shown. |
| `data.ads[].url` | Link to the ad's detail page in TikTok's Ads Library. |
| `data.ads[].videoUrl / data.ads[].coverUrl` | Link to the ad video and link to its cover image. |
| `data.total` | Total count of matching ads reported for the search. |
| `data.hasMore / data.nextCursor` | `hasMore` tells you if another page exists. `nextCursor` is the value to send as `cursor` for the next page. |

### Notes

- Use `region` with a two-letter EU or EEA code such as `DE`, `FR`, `GB` or `IT`. Each region holds a different set of ads, and `DE` is the default.
- To page through results, send the `nextCursor` value from the last response as `cursor`. Stop when `hasMore` is `false`.
- Use [TikTok Ad Library Ad](/apis/tiktok/ad-library-ad) to look up a single ad from its `adId`.

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/ad-library-search.json`](../../../catalog/models/tiktok/ad-library-search.json) · Store page: https://www.sandbase.ai/model/tiktok/ad-library-search
