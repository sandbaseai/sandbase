# Similarweb SERP Players - Clicks over time API: pricing, parameters and code examples

`similarweb/search-serp-players-timeseries` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get month-by-month clicks for the websites that appear on search results for given keywords.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 20000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-serp-players-timeseries", "end_date": "2026-09", "keywords": "running shoes", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-serp-players-timeseries', {'end_date': '2026-09', 'keywords': 'running shoes', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-serp-players-timeseries", {
  "end_date": "2026-09",
  "keywords": "running shoes",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/search-serp-players-timeseries", sandbase.Params{
	"end_date": "2026-09",
	"keywords": "running shoes",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-serp-players-timeseries` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `keywords` | string | yes | keywords  |
| `start_date` | string | yes | start_date  |
| `granularity` | string |  | granularity one of: `monthly` |

## Details

Returns monthly click counts for each website that appears in search results for a keyword. You send a `keywords` value, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Track how many search clicks `youtube.com` gets for "running shoes" from month to month.
- Compare which domains gain or lose search clicks for a keyword over a date range.
- Build a chart of the top sites competing on a keyword for an SEO report.
- Spot new domains that start to capture clicks for a product keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-serp-players-timeseries" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "keywords": "running shoes", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | end_date |
| `keywords` | string | Yes | keywords |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `offset` | integer | No | offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "clicks": 24689,
      "date": "2026-09-01",
      "domain": "youtube.com"
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
      "start_date": "2026-09-01",
      "traffic_source": "all",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].domain` | The website that appeared in search results for the keyword. |
| `data[].date` | The first day of the month the click count belongs to, in `YYYY-MM-DD` format. |
| `data[].clicks` | The number of clicks the domain received from search results for the keyword in that month. |
| `meta.status` | Shows `success` when the call worked. |
| `meta.last_updated` | Date the data was last updated, in `YYYY-MM-DD` format. |
| `meta.query.limit / meta.query.offset` | The page size and starting position applied to the `data` list. |
| `meta.request.keyword` | The keyword the results are for. |
| `meta.request.start_date / meta.request.end_date` | The date range used, expanded to full days. A `2026-09` input becomes `2026-09-01` to `2026-09-30`. |
| `meta.request.granularity` | The time step of the rows. The value `monthly` gives one row per domain per month. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM`. The response echoes them as full dates.
- Use `limit` (1 to 20) and `offset` to page through domains.
- For totals over the whole period instead of month-by-month rows, use [Similarweb SERP Players - Aggregated](/apis/similarweb/search-serp-players-aggregated).
- To see which keywords drive traffic to one site, use [Similarweb Website Keywords](/apis/similarweb/search-website-keywords).

### Pricing

Billed at the actual cost of each call, about $0.075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-serp-players-timeseries.json`](../../../catalog/models/similarweb/search-serp-players-timeseries.json) · Store page: https://www.sandbase.ai/model/similarweb/search-serp-players-timeseries
