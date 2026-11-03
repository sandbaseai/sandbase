# Similarweb Keyword Competitors API: pricing, parameters and code examples

`similarweb/search-keyword-competitors` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get the websites that compete with a domain for the same search keywords, with a competition score and shared-keyword ratio.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.ceil(Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0) * 30000.0 / 1000000.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/search-keyword-competitors", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/search-keyword-competitors', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/search-keyword-competitors", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "limit": 1,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/search-keyword-competitors", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/search-keyword-competitors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly` |
| `traffic_source` | string |  | traffic_source  |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Returns a list of websites that compete with a given domain for the same search keywords. Each row has a competition score and a shared-keyword ratio. The API needs a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Find which sites compete with your domain in search results for the same keywords.
- Rank competitors by `score` to decide which ones to study first.
- Check how much of a rival's keyword set overlaps with your own domain.
- Build a competitor list to feed into keyword or traffic research for each rival.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/search-keyword-competitors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `offset` | integer | No | offset |
| `traffic_source` | string | No | traffic_source |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "score": 18.24179458618164,
      "shared_keywords": 0.4459056258201599,
      "url": "robinhood.com"
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
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "main_domain_only": false,
      "metrics": [
        "score"
      ],
      "start_date": "2026-09-01",
      "traffic_source": "organic",
      "web_source": "desktop"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One competing website per row. The list holds up to `limit` rows. |
| `data[].url` | Domain name of the competing website, such as `robinhood.com`. |
| `data[].score` | Competition score for this site against the requested domain. A higher value means stronger competition, and the scale is not shown in the response. |
| `data[].shared_keywords` | Share of keywords the competitor has in common with the requested domain. It is a ratio, so `0.4459` reads as about 45%. |
| `meta.request.traffic_source / meta.request.web_source` | The traffic source and device type the query used. The sample call ran with `organic` and `desktop`. |
| `meta.request.start_date / meta.request.end_date` | The full date range the query covered. Short `YYYY-MM` inputs expand to the first and last day of the month. |
| `meta.request.main_domain_only` | Whether the query was limited to main domains. It was `false` in this call. |
| `meta.query.limit / meta.query.offset` | The page size and start position applied to the list. |
| `meta.last_updated` | Date shown as the last update of the data, in `YYYY-MM-DD` format. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM`. The response echoes them as full dates.
- Page through results with `limit` (1 to 20) and `offset`.
- `country` accepts only `ww` (worldwide), and `granularity` accepts only `monthly`.
- To see the keywords behind a competitor, call [Similarweb Website Keywords](/apis/similarweb/search-website-keywords). For sites with a similar audience, use [Similarweb SimilarSites](/apis/similarweb/similar-sites).

### Pricing

Billed at the actual cost of each call, about $0.075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/search-keyword-competitors.json`](../../../catalog/models/similarweb/search-keyword-competitors.json) · Store page: https://www.sandbase.ai/model/similarweb/search-keyword-competitors
