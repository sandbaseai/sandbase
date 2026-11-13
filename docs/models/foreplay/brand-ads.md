# Foreplay Brand Ads API: pricing, parameters and code examples

`foreplay/brand-ads` · data API · Foreplay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0525 per call · **Modes:** sync

List the social ads a brand has run by Foreplay brand ID, with creative, copy, platforms, run dates and landing page, filtered by format, platform and run time.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0525**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "foreplay/brand-ads", "brand_ids": ["3YfFtyvZ3viTAbbLaWLV"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('foreplay/brand-ads', {'brand_ids': ['3YfFtyvZ3viTAbbLaWLV']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("foreplay/brand-ads", {
  "brand_ids": [
    "3YfFtyvZ3viTAbbLaWLV"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "foreplay/brand-ads", sandbase.Params{
	"brand_ids": []any{"3YfFtyvZ3viTAbbLaWLV"},
})
```

Same call via the path form: `POST /v1/api/foreplay/brand-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `live` | string |  | Filter ads by live status. `true` means currently active ads, `false` means inactive ads. Leave empty to include both.  |
| `limit` | integer |  | Number of results (1-20). Each returned item is billed at about $0.0175, so this caps the cost of one call. default `10`; range –20 |
| `order` | string |  | Order of results: 'newest' (default), 'oldest', 'longest_running', or 'most_relevant'. Sorts ads by creation date, longest running duration, or relevance to the search query. one of: `newest`, `oldest`, `longest_running`, `most_relevant`; default `"newest"` |
| `cursor` | string |  | Cursor for pagination. Use the cursor value from the previous response's metadata to get the next page of results.  |
| `niches` | string |  | Filter by one or more niches. Available niches: travel, food, fashion, beauty, health, technology, automotive, finance, education, entertainment, sports, home, pets, business, other Example:…  |
| `collect` | string |  | Best-effort live fallback. If the cached results are empty and `collect=true`, the API translates each brand id to its Meta page id (`adlibraryid`), kicks off a live fetch through our Spyder pipeline, and polls for ~30… default `"false"` |
| `end_date` | string |  | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for…  |
| `brand_ids` | array | yes | Brand ID(s) to search for. Can be a single ID or multiple IDs separated by commas.  |
| `languages` | string |  | Filter by languages. Accepts various language formats: 'french', 'FR', 'romanian', 'ro', 'english', 'en', etc. Example: `?languages=en&languages=fr`  |
| `start_date` | string |  | Start date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To get all ads from a…  |
| `market_target` | string |  | Filter by market target. Available targets: b2b (business-to-business), b2c (business-to-consumer) Example: `?market_target=b2b`  |
| `display_format` | string |  | Filter by one or more display formats. Available formats (11): carousel, dco, dpa, event, image, multi_images, multi_medias, multi_videos, page_like, text, video Example: `?display_format=video&display_format=carousel` one of: `carousel`, `dco`, `dpa`, `event`, `image`, `multi_images`, `multi_medias`, `multi_videos`, `page_like`, `text`, `video` |
| `publisher_platform` | string |  | Filter by one or more publisher platforms. Available platforms: facebook, instagram, audience_network, messenger, tiktok, youtube, linkedin, threads, whatsapp Example:… one of: `facebook`, `instagram`, `audience_network`, `messenger`, `tiktok`, `youtube`, `linkedin`, `threads`, `whatsapp` |
| `video_duration_max` | string |  | Filter ads by maximum video duration in seconds. Only applies to video ads.  |
| `video_duration_min` | string |  | Filter ads by minimum video duration in seconds. Only applies to video ads.  |
| `running_duration_max_days` | string |  | Filter ads by maximum running duration in days. Must be a positive integer.  |
| `running_duration_min_days` | string |  | Filter ads by minimum running duration in days. Must be a positive integer.  |

## Details

List the social ads a brand has run by Foreplay brand ID, with creative, copy, platforms, run dates and landing page, filtered by format, platform and run time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/foreplay/brand-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"brand_ids": ["3YfFtyvZ3viTAbbLaWLV"], "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `brand_ids` | array | Yes | Brand ID(s) to search for. Can be a single ID or multiple IDs separated by commas. |
| `limit` | integer | No | Pagination limit (max 250). Controls the number of ads returned per request. |
| `collect` | string | No | Best-effort live fallback. If the cached results are empty and `collect=true`, the API translates each brand id to its Meta page id (`adlibraryid`), kicks off a live fetch through our Spyder pipeline, and polls for ~30 s |
| `cursor` | string | No | Cursor for pagination. Use the cursor value from the previous response's metadata to get the next page of results. |
| `display_format` | string | No | Filter by one or more display formats. Available formats (11): carousel, dco, dpa, event, image, multi_images, multi_medias, multi_videos, page_like, text, video Example: `?display_format=video&display_format=carousel` |
| `end_date` | string | No | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for a |
| `languages` | string | No | Filter by languages. Accepts various language formats: 'french', 'FR', 'romanian', 'ro', 'english', 'en', etc. Example: `?languages=en&languages=fr` |
| `live` | string | No | Filter ads by live status. `true` means currently active ads, `false` means inactive ads. Leave empty to include both. |
| `market_target` | string | No | Filter by market target. Available targets: b2b (business-to-business), b2c (business-to-consumer) Example: `?market_target=b2b` |
| `niches` | string | No | Filter by one or more niches. Available niches: travel, food, fashion, beauty, health, technology, automotive, finance, education, entertainment, sports, home, pets, business, other Example: `?niches=travel&niches=fashio |
| `order` | string | No | Order of results: 'newest' (default), 'oldest', 'longest_running', or 'most_relevant'. Sorts ads by creation date, longest running duration, or relevance to the search query. |
| `publisher_platform` | string | No | Filter by one or more publisher platforms. Available platforms: facebook, instagram, audience_network, messenger, tiktok, youtube, linkedin, threads, whatsapp Example: `?publisher_platform=facebook&publisher_platform=ins |
| `running_duration_max_days` | string | No | Filter ads by maximum running duration in days. Must be a positive integer. |
| `running_duration_min_days` | string | No | Filter ads by minimum running duration in days. Must be a positive integer. |
| `start_date` | string | No | Start date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To get all ads from a spec |
| `video_duration_max` | string | No | Filter ads by maximum video duration in seconds. Only applies to video ads. |
| `video_duration_min` | string | No | Filter ads by minimum video duration in seconds. Only applies to video ads. |

### Pricing

Billed at the actual upstream cost of each call (about $0.0525 for the request above). Failed calls are not charged.

---
Machine-readable: [`catalog/models/foreplay/brand-ads.json`](../../../catalog/models/foreplay/brand-ads.json) · Store page: https://www.sandbase.ai/model/foreplay/brand-ads
