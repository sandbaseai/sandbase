# DataForSEO Google Trends

`dataforseo/v3/keywords_data/google_trends/explore/live` · api · DataForSEO

Get Google Trends interest over time for up to 5 keywords by location, language and time range, with weekly values on a 0–100 scale.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_trends/explore/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_trends/explore/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_trends/explore/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_trends/explore/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_trends/explore/live` with the body above minus `model`.

## Details

Send up to five keywords and get Google Trends interest-over-time data, the same 0–100 index shown on trends.google.com, for any location and time range.

### Use cases

- Compare interest in brands, products or topics.
- Detect seasonality and emerging trends.
- Add trend data to SEO and content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_trends/explore/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. Common fields:

| Name | Type | Description |
|---|---|---|
| `keywords` | array | Up to 5 keywords to compare. |
| `location_code` | integer | DataForSEO location code, e.g. 2840 for the United States. |
| `language_code` | string | Language code, e.g. "en". |
| `time_range` | string | Preset range, e.g. past_hour, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 20000,
  "tasks": [
    {
      "status_message": "Ok.",
      "result": [
        {
          "keywords": [
            "openai"
          ],
          "location_code": 2840,
          "language_code": "en",
          "datetime": "2026-10-06 09:02:28 +00:00",
          "items": [
            {
              "type": "google_trends_graph",
              "keywords": [
                "openai"
              ],
              "data": [
                {
                  "date_from": "2025-10-05",
                  "date_to": "2025-10-11",
                  "missing_data": false,
                  "timestamp": 1759622400,
                  "values": [
                    19
                  ]
                },
                {
                  "date_from": "2025-10-12",
                  "date_to": "2025-10-18",
                  "missing_data": false,
                  "timestamp": 1760227200,
                  "values": [
                    12
                  ]
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### Notes

- Use `date_from` / `date_to` instead of `time_range` for a custom window.

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Google Ads Keyword Search Volume](/model/dataforseo/v3/keywords_data/google_ads/search_volume/live): Get Google Ads search volume, CPC, competition and 12-month trend for up to 1,000 keywords per request, by location and language.
- [DataForSEO Website Screenshot](/model/dataforseo/v3/on_page/page_screenshot): Capture a full-page or viewport screenshot of any URL in desktop, mobile or tablet view.
- [DataForSEO Google SERP (Advanced)](/model/dataforseo/v3/serp/google/organic/live/advanced): Get live Google organic search results for any keyword, location and language, including AI Overviews, featured snippets, People Also Ask and other SERP featur…

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_trends/explore/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_trends/explore/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_trends/explore/live
