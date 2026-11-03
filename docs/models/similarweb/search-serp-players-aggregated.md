# Similarweb SERP Players - Aggregated API: pricing, parameters and code examples

`similarweb/search-serp-players-aggregated` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Get the websites that win clicks on search results for given keywords, with clicks, top URL and SERP features, aggregated over the period.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 70000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-serp-players-aggregated", "end_date": "2026-09", "keywords": "running shoes", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-serp-players-aggregated', {'end_date': '2026-09', 'keywords': 'running shoes', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-serp-players-aggregated", {
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
run, err := c.Run(ctx, "similarweb/search-serp-players-aggregated", sandbase.Params{
	"end_date": "2026-09",
	"keywords": "running shoes",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-serp-players-aggregated` with the body above minus `model`.

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

Returns the websites that win clicks on search results for a keyword, aggregated over a date range. You send a `keywords` value, a `start_date` and `end_date` in `YYYY-MM` format, and a `limit`. Each row gives the domain, its estimated clicks, its share of traffic, its top URL and the SERP features it appears in.

### Use cases

- Find which sites take the most clicks for a keyword such as `running shoes`.
- Check whether video results from sites like YouTube compete with your pages on a target keyword.
- Pick the top-ranking URL of a rival domain to study its content for a keyword.
- Compare the share of clicks between domains to size up the competition before you plan SEO work.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-serp-players-aggregated" \
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
      "clicks": 24689.870996804166,
      "domain": "youtube.com",
      "serp_features": [
        "organic"
      ],
      "site": "youtube.com",
      "top_url": "youtube.com/watch?v=Yi8-joojOlc",
      "top_url_position": null,
      "traffic_share": 0.1730323313951437
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
| `data[].domain / data[].site` | The domain that earns clicks on the search results for the keyword. In this response both fields hold the same value. |
| `data[].clicks` | Clicks that the domain receives for the keyword over the selected period. |
| `data[].traffic_share` | The share of the keyword's clicks that goes to this domain, as a decimal. A value of `0.173` means about 17.3%. |
| `data[].top_url` | The URL of the page on the domain that gets the most clicks for the keyword. |
| `data[].top_url_position` | Position of the top URL in the results. It is `null` in this response. |
| `data[].serp_features` | List of SERP feature types in which the domain appears, such as `organic` and `video`. |
| `meta.request.keyword / meta.request.is_keyword_group` | The keyword that was queried, and whether it was treated as a keyword group. |
| `meta.request.start_date / meta.request.end_date` | The full date range that was applied. A month input such as `2026-09` expands to the first and last day of that month. |
| `meta.query.limit / meta.query.offset` | The page size and starting row used for this response. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Set `limit` between 1 and 20 and use `offset` to page through further rows.
- Only `monthly` is accepted for `granularity`, and only `ww` (worldwide) for `country`.
- To see how clicks change month by month, call [Similarweb SERP Players - Clicks over time](/apis/similarweb/search-serp-players-timeseries).
- To find the domains that compete for a keyword set from the website side, try [Similarweb Keyword Competitors](/apis/similarweb/search-keyword-competitors).

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-serp-players-aggregated.json`](../../../catalog/models/similarweb/search-serp-players-aggregated.json) · Store page: https://www.sandbase.ai/model/similarweb/search-serp-players-aggregated
