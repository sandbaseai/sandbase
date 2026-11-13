# Foreplay Ad Search API: pricing, parameters and code examples

`foreplay/ad-search` · data API · Foreplay · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0525 per call · **Modes:** sync

Search the Foreplay library of live and past social ads from Facebook, Instagram, TikTok, YouTube and more by keyword, format, platform, niche, language and run time, with creative, copy and landing page.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0525**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "foreplay/ad-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('foreplay/ad-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("foreplay/ad-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "foreplay/ad-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/foreplay/ad-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `live` | string |  | Filter ads by live status. `true` means currently active ads, `false` means inactive ads. Leave empty to include both.  |
| `limit` | integer |  | Number of results (1-20). Each returned item is billed at about $0.0175, so this caps the cost of one call. default `10`; range –20 |
| `order` | string |  | Order of results: 'newest' (default), 'oldest', 'longest_running', or 'most_relevant'. Sorts ads by creation date, longest running duration, or relevance to the search query. one of: `newest`, `oldest`, `longest_running`, `most_relevant`; default `"newest"` |
| `query` | string |  | Search text for ad name or description. Leave empty to search all ads with filters only.  |
| `cursor` | string |  | Cursor for pagination. Use the cursor value from the previous response's metadata to get the next page of results.  |
| `niches` | string |  | Filter by one or more niches. Available niches: accessories, app/software, beauty, business/professional, education, entertainment, fashion, food/drink, health/wellness, home/garden, jewelry/watches, other, parenting,…  |
| `end_date` | string |  | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for…  |
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

Search the Foreplay library of live and past social ads from Facebook, Instagram, TikTok, YouTube and more by keyword, format, platform, niche, language and run time, with creative, copy and landing page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/foreplay/ad-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "running shoes", "limit": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Pagination limit (max 250). Controls the number of ads returned per request. |
| `query` | string | No | Search text for ad name or description. Leave empty to search all ads with filters only. |
| `cursor` | string | No | Cursor for pagination. Use the cursor value from the previous response's metadata to get the next page of results. |
| `display_format` | string | No | Filter by one or more display formats. Available formats (11): carousel, dco, dpa, event, image, multi_images, multi_medias, multi_videos, page_like, text, video Example: `?display_format=video&display_format=carousel` |
| `end_date` | string | No | End date (inclusive). Format: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', or 'YYYY-MM-DD HH:MM:SS'. If you provide only the date (e.g. '2024-11-12'), it will be interpreted as '2024-11-12 00:00:00'. To include all results for a |
| `languages` | string | No | Filter by languages. Accepts various language formats: 'french', 'FR', 'romanian', 'ro', 'english', 'en', etc. Example: `?languages=en&languages=fr` |
| `live` | string | No | Filter ads by live status. `true` means currently active ads, `false` means inactive ads. Leave empty to include both. |
| `market_target` | string | No | Filter by market target. Available targets: b2b (business-to-business), b2c (business-to-consumer) Example: `?market_target=b2b` |
| `niches` | string | No | Filter by one or more niches. Available niches: accessories, app/software, beauty, business/professional, education, entertainment, fashion, food/drink, health/wellness, home/garden, jewelry/watches, other, parenting, pe |
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
Machine-readable: [`catalog/models/foreplay/ad-search.json`](../../../catalog/models/foreplay/ad-search.json) · Store page: https://www.sandbase.ai/model/foreplay/ad-search
