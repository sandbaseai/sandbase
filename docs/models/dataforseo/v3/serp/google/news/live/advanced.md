# DataForSEO Google News SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/news/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.002 per call · **Modes:** sync

Get live Google News results for any keyword, location and language: headlines, sources, URLs, dates and rank.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/news/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/news/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/news/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/news/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/news/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | string |  | Number of results to return.  |
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

Returns live Google News results for a keyword, location and language. Each result has its source domain, a text snippet, a publish time, an image URL and its rank. Send `keyword`, `location_code` and `language_code`.

### Use cases

- Track which news sites appear for a brand name or product term in a given country.
- Collect recent news snippets about a topic to feed a summary or alert.
- Compare the Google News results for the same keyword in different locations or languages.
- Check how high a specific publisher ranks for a news query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/news/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `depth` | string | No | Number of results to return. |
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | DataForSEO location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "serp",
        "device": "desktop",
        "function": "live",
        "keyword": "running shoes",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030829-1614-0139-0000-75eda89264ed",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/search?q=running%20shoes&num=10&hl=en&gl=US&gws_rd=cr&tbm…",
          "datetime": "2026-11-03 08:29:31 +00:00",
          "includes_non_news_search_results": false,
          "item_types": [
            "news_search"
          ],
          "items": [
            {
              "domain": "google.com",
              "image_url": "https://api.dataforseo.com/cdn/i/11030829-1614-0139-0000-75eda89264ed:0",
              "rank_absolute": 1,
              "rank_group": 1,
              "rectangle": null,
              "snippet": "New Balance FuelCell Rebel Trail review: We think New Balance made a questionabl…",
              "time_published": "17 hours ago",
              "timestamp": "2026-11-02 15:29:29 +00:00"
            }
          ],
          "items_count": 10,
          "keyword": "running shoes",
          "language_code": "en"
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "3.8170 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "4.0184 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].domain` | Domain of the site that published the news result. |
| `tasks[].result[].items[].snippet` | Short text excerpt shown for the news result. |
| `tasks[].result[].items[].rank_group / rank_absolute` | Position of the result in the news list, starting at `1`. |
| `tasks[].result[].items[].time_published` | Publish time as relative text, such as `17 hours ago`. |
| `tasks[].result[].items[].timestamp` | Publish time as a date and time with a UTC offset, such as `2026-11-02 15:29:29 +00:00`. |
| `tasks[].result[].items[].image_url` | URL of the thumbnail image for the result. |
| `tasks[].result[].items_count` | Number of news items in the result. |
| `tasks[].result[].check_url` | The Google News search URL for this query, location and language. |
| `tasks[].result[].datetime` | Date and time of the result set, in UTC. |
| `tasks[].data.keyword / location_code / language_code` | The query settings that were used for the search. |

### Notes

- Results sit in `tasks[].result[].items[]`. Check `status_code` (`20000` means `Ok.`) at the top level and inside each task.
- Use `location_code` for the country or area, for example `2840` for the United States. Use `language_code` for the language, for example `en`.
- Use `depth` to ask for more results. It is a string in the request schema.
- `timestamp` uses the format `YYYY-MM-DD HH:MM:SS +00:00`, so you can sort results by date.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Historical Search Volume](/apis/dataforseo/v3/dataforseo_labs/google/historical_search_volume/live): Get historical Google search volume for keywords from DataForSEO Labs: monthly searches, CPC, competition and keyword properties by location and language.
- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/news/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/news/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/news/live/advanced
