# DataForSEO Google SERP (Regular) API: pricing, parameters and code examples

`dataforseo/v3/serp/google/organic/live/regular` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.002 per run, depending on parameters · **Modes:** sync

Get live Google organic results for any keyword, location and language in a compact format: rank, title, URL, domain and description for each organic result.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.002 |

Formula: `0.002 * Math.ceil(Math.max(params.depth ?? 10.0, 1.0) / 10.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/organic/live/regular", "depth": 10, "keyword": "qwen 3.8 max", "language_code": "en", "location_code": 2840}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/organic/live/regular', {'depth': 10, 'keyword': 'qwen 3.8 max', 'language_code': 'en', 'location_code': 2840})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/organic/live/regular", {
  "depth": 10,
  "keyword": "qwen 3.8 max",
  "language_code": "en",
  "location_code": 2840
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/organic/live/regular", sandbase.Params{
	"depth": 10,
	"keyword": "qwen 3.8 max",
	"language_code": "en",
	"location_code": 2840,
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/organic/live/regular` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `depth` | integer |  | Number of results to return (default 100).  |
| `keyword` | string |  | Search query, e.g. "openai api".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | DataForSEO location code, e.g. 2840 for the United States.  |

## Details

This API returns live Google organic results for one keyword, location and language. Each result has a rank, title, domain, description and URL. Send `keyword`, `location_code` and `language_code`, and set `depth` to choose how many results to fetch.

### Use cases

- Track where your pages rank for a list of keywords.
- List the domains that hold the top spots for a keyword to study competitors.
- Compare results for the same keyword across different `location_code` values.
- Find forum and community pages, such as Reddit threads, that rank for a buying keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/organic/live/regular" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en", "depth": 20}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `depth` | integer | No | Number of results to return (default 100). |
| `keyword` | string | No | Search query, e.g. "openai api". |
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
        "depth": 20,
        "device": "desktop",
        "function": "live",
        "keyword": "running shoes",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows"
      },
      "id": "11030829-1614-0121-0000-2ad640deb040",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/search?q=running%20shoes&hl=en&gl=US&ie=UTF-8&uule=w+CAIQ…",
          "datetime": "2026-11-03 08:29:40 +00:00",
          "item_types": [
            "ai_overview"
          ],
          "items": [
            {
              "breadcrumb": "https://www.roadrunnersports.com › ... › Buying Guides",
              "description": "Oct 9, 2026 — There is no single best running shoe brand. The best brand is the …",
              "domain": "google.com",
              "page": 1,
              "rank_absolute": 2,
              "rank_group": 1,
              "title": "Best Running Shoe Brands for Men and Women (2026)",
              "type": "organic"
            }
          ],
          "items_count": 16,
          "keyword": "running shoes",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "7.4828 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "7.5545 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].keyword / location_code / language_code` | The search query, location and language that Google was checked with. |
| `tasks[].result[].check_url` | The Google search URL that matches this query. Open it to compare with the live page. |
| `tasks[].result[].datetime` | Date and time of the search, with a UTC offset. |
| `tasks[].result[].item_types` | The kinds of elements found on this results page, for example `ai_overview`, `organic` and `images`. |
| `tasks[].result[].items_count` | Number of items returned in `items` for this request. |
| `tasks[].result[].items[].type` | The kind of result. In this API the items are `organic`. |
| `tasks[].result[].items[].rank_group` | Position among results of the same type. The first organic result has `rank_group` 1. |
| `tasks[].result[].items[].rank_absolute` | Position among all elements on the page. It can be higher than `rank_group` when other elements, such as an AI overview, appear above. |
| `tasks[].result[].items[].title / description` | The title and snippet text Google shows for the result. The snippet can contain HTML entities such as `&#39;`. |
| `tasks[].result[].items[].domain` | Domain of the ranking page. |
| `tasks[].result[].items[].breadcrumb` | The path line Google shows under the title. For some results it holds other text, such as a comment count and age. |

### Notes

- `location_code` 2840 is the United States. `language_code` takes a code such as `en`.
- `depth` sets how many results you ask for. In this response `depth` was 20 and `items_count` was 16, so check `items_count` rather than assuming the full depth.
- `page` on each item shows which results page the item came from.
- This API returns organic results only. For AI Overviews, featured snippets or People Also Ask, use the Advanced SERP API.

### Pricing

Billed at the actual cost of each call, about $0.002 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/apis/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Google Trends](/apis/dataforseo/v3/keywords_data/google_trends/explore/live): Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.
- [DataForSEO Website Screenshot](/apis/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/organic/live/regular.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/organic/live/regular.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/organic/live/regular
