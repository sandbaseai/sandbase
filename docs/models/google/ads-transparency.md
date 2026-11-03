# Google Ads Transparency Center API: pricing, parameters and code examples

`google/ads-transparency` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Ads an advertiser is running on Google, from the Ads Transparency Center: creatives, formats, first and last shown dates.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/ads-transparency"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/ads-transparency', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/ads-transparency", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/ads-transparency", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google/ads-transparency` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | results to return; default 40. Unlike engine=google, `num` IS documented here  |
| `text` | string |  | free-text advertiser or domain to search for. Supply either this OR advertiser_id — neither is individually mandatory but one is needed  |
| `region` | string |  | geographic region the search originates from. REQUIRED when political_ads is true  |
| `end_date` | string |  | YYYYMMDD  |
| `platform` | string |  | where the ad ran: PLAY \| MAPS \| SEARCH \| SHOPPING \| YOUTUBE  |
| `start_date` | string |  | YYYYMMDD  |
| `advertiser_id` | string |  | a specific advertiser id, or several comma-separated  |
| `political_ads` | boolean |  | restrict to political advertising; forces `region` to be set  |
| `creative_format` | string |  | text \| image \| video  |
| `next_page_token` | string |  | cursor from the previous response's serpapi_pagination  |

## Details

Returns a list of ad creatives shown on Google for an advertiser or domain, taken from the Google Ads Transparency Center. Each creative includes the advertiser, format, first and last shown timestamps, and a preview link. Send a domain or advertiser name in `text`, or one or more IDs in `advertiser_id`.

### Use cases

- Check which advertisers run ads that point to your own domain.
- Monitor a competitor's ad creatives and see how long each one has been running.
- Filter a domain's ads by `creative_format` to review only video or text ads.
- Collect `advertiser_id` values to look up one advertiser's full ad history.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/ads-transparency" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "apple.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `advertiser_id` | string | No | a specific advertiser id, or several comma-separated |
| `creative_format` | string | No | text / image / video |
| `end_date` | string | No | YYYYMMDD |
| `next_page_token` | string | No | cursor from the previous response's serpapi_pagination |
| `num` | integer | No | results to return; default 40. Unlike engine=google, `num` IS documented here |
| `platform` | string | No | where the ad ran: PLAY / MAPS / SEARCH / SHOPPING / YOUTUBE |
| `political_ads` | boolean | No | restrict to political advertising; forces `region` to be set |
| `region` | string | No | geographic region the search originates from. REQUIRED when political_ads is true |
| `start_date` | string | No | YYYYMMDD |
| `text` | string | No | free-text advertiser or domain to search for. Supply either this OR advertiser_id — neither is individually mandatory but one is needed |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_creatives": [
    {
      "ad_creative_id": "CR01913929004390285313",
      "advertiser": "Optimum Media Direction (Thailand) Co., Ltd",
      "advertiser_id": "AR03550249516248596481",
      "details_link": "https://adstransparency.google.com/advertiser/AR03550249516248596481/creative/CR…",
      "first_shown": 1792688520,
      "format": "video",
      "last_shown": 1793690110,
      "link": "https://displayads-formats.googleusercontent.com/ads/preview/content.js?client=a…",
      "target_domain": "apple.com",
      "total_days_shown": 12
    }
  ],
  "search_information": {
    "total_results": 300000
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ad_creatives[]` | List of ad creatives that match the search. |
| `ad_creatives[].ad_creative_id` | Identifier of one creative. It starts with `CR`. |
| `ad_creatives[].advertiser / ad_creatives[].advertiser_id` | Name of the advertiser that ran the ad and its ID, which starts with `AR`. Use the ID in `advertiser_id` for later searches. |
| `ad_creatives[].format` | Creative type, such as `video` or `text`. |
| `ad_creatives[].first_shown / ad_creatives[].last_shown` | Unix timestamps in seconds for when the creative was first and last shown. |
| `ad_creatives[].total_days_shown` | Number of days the creative was shown. |
| `ad_creatives[].target_domain` | Domain the ad is tied to, such as `apple.com`. |
| `ad_creatives[].details_link` | Link to the creative's page in the Ads Transparency Center. |
| `ad_creatives[].image / ad_creatives[].link / ad_creatives[].width / ad_creatives[].height` | Preview image URL or preview content URL for the creative, with pixel size when given. Text and image creatives carry `image`, `width` and `height`. The video creative carries `link`. |
| `search_information.total_results` | Total number of creatives that match the search. |

### Notes

- Send either `text` or `advertiser_id`. One of the two is needed.
- Set `region` when `political_ads` is `true`.
- Use `num` to set how many results to return. Pass `next_page_token` from the previous response's pagination data to get the next page.
- Pass `start_date` and `end_date` as `YYYYMMDD`.

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/ads-transparency.json`](../../../catalog/models/google/ads-transparency.json) · Store page: https://www.sandbase.ai/model/google/ads-transparency
