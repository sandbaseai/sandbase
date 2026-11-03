# Similarweb Keywords Overview API: pricing, parameters and code examples

`similarweb/keywords-overview` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $1.275 per call · **Modes:** sync

Get search metrics for keywords: clicks, volume, CPC, competition, intent and SERP features such as AI Overviews.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `1.275 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/keywords-overview", "end_date": "2026-09", "granularity": "monthly", "keywords": "running shoes", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/keywords-overview', {'end_date': '2026-09', 'granularity': 'monthly', 'keywords': 'running shoes', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/keywords-overview", {
  "end_date": "2026-09",
  "granularity": "monthly",
  "keywords": "running shoes",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/keywords-overview", sandbase.Params{
	"end_date": "2026-09",
	"granularity": "monthly",
	"keywords": "running shoes",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/keywords-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `keywords` | string | yes | keywords  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Returns monthly search metrics for a keyword: clicks, search volume, CPC bids, competition, difficulty, intent volumes and click splits by SERP type. It needs a `keywords` value, a `start_date` and `end_date` in `YYYY-MM` format, a `granularity` and a `limit`.

### Use cases

- Compare organic and paid click shares for a keyword before planning a search budget.
- Check the CPC bid range for a keyword to estimate ad costs.
- Measure how many searches end without a click to judge the value of ranking for a term.
- Check whether a keyword triggers an AI Overview.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/keywords-overview" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "keywords": "running shoes", "limit": 1, "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | end_date |
| `granularity` | string | Yes | granularity |
| `keywords` | string | Yes | keywords |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `format` | string | No | format |
| `main_domain_only` | boolean | No | main_domain_only |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "ai_overview": [
        "running shoes"
      ],
      "classic_organic_clicks": 58280.955131874034,
      "clicks": 142689.35058397474,
      "competition": 100,
      "cpc_high_bid": 6400000,
      "cpc_low_bid": 10000,
      "date": "2026-09-01",
      "difficulty": 24,
      "informational_intent_volume": 0.0,
      "job_search_intent_volume": 0.0,
      "local_intent_volume": 688559.0,
      "navigational_intent_volume": 0.0
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "query": {
      "asc": null,
      "limit": 1,
      "offset": 0,
      "sort": null
    },
    "request": {
      "country": "ww",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "is_keyword_group": false,
      "keyword": "running shoes",
      "metrics": [
        "clicks"
      ],
      "start_date": "2026-09-01",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].volume` | Search volume for the keyword in the month. |
| `data[].clicks` | Total clicks the keyword produced in the month. |
| `data[].classic_organic_clicks / paid_clicks` | Clicks that went to classic organic results and to paid results. |
| `data[].search_ads_clicks / pla_clicks` | Paid clicks split into text search ads and product listing ads (PLA). |
| `data[].organic_serp_features_clicks` | Clicks that went to organic SERP features rather than classic results. |
| `data[].zero_clicks` | Searches that ended without a click on any result. |
| `data[].cpc_low_bid / cpc_high_bid` | Low and high CPC bid values for the keyword. The response does not show the unit. |
| `data[].competition / difficulty` | Competition and difficulty scores for the keyword. |
| `data[].local_intent_volume / transactional_intent_volume` | Volume tied to each search intent. Other intents are `informational_intent_volume`, `navigational_intent_volume` and `job_search_intent_volume`. |
| `data[].ai_overview` | List of keywords that trigger an AI Overview. |

### Notes

- `data[].date` is the first day of the month, for example `2026-09-01`.
- `limit` accepts 1 to 20. The response `meta.query` shows `limit` and `offset`.
- Use [Similarweb Keyword Competitors](/apis/similarweb/search-keyword-competitors) to see which domains compete for the keyword.
- Use [Similarweb SERP Players - Aggregated](/apis/similarweb/search-serp-players-aggregated) to see who earns the clicks.

### Pricing

Billed at the actual cost of each call, about $1.275 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/keywords-overview.json`](../../../catalog/models/similarweb/keywords-overview.json) · Store page: https://www.sandbase.ai/model/similarweb/keywords-overview
