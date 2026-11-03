# Similarweb Popular Pages API: pricing, parameters and code examples

`similarweb/popular-pages` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.225 per call · **Modes:** sync

Get a website's most visited pages with each page's traffic share and change.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.225 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/popular-pages", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/popular-pages', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/popular-pages", {
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
run, err := c.Run(ctx, "similarweb/popular-pages", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/popular-pages` with the body above minus `model`.

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

Returns the most visited pages of a website on Similarweb, with each page's traffic share and change. It needs a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Find which pages on a news site draw the most visits in a given month.
- Track how the traffic share of a site's top pages shifts between periods.
- Compare the page mix of a competitor's site against your own.
- Spot pages whose traffic is rising fast and review their content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/popular-pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 1, "granularity": "monthly"}'
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
      "change": 9.767841558207868,
      "page": "cnn.com",
      "share": 0.6095348868374078
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
      "classify": "all",
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "metrics": [
        "share"
      ],
      "page": null,
      "start_date": "2026-09-01",
      "utm": false,
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One row per popular page, ordered as returned. The number of rows follows `limit`. |
| `data[].page` | The page this row describes. The value `cnn.com` in the sample is the site's root page. |
| `data[].share` | The page's share of the domain's traffic. In the sample, `0.6095` is a fraction, so it reads as about 61%. |
| `data[].change` | The change in the page's traffic for the period. The response does not state the unit or the comparison period. |
| `meta.status` | Shows `success` when the call worked. |
| `meta.last_updated` | Date of the latest data, such as `2026-09-30`. |
| `meta.request.start_date / meta.request.end_date` | The date range used. The month inputs are expanded to the first and last day of the month. |
| `meta.request.web_source` | The device filter applied. The sample shows `total`. |
| `meta.query.limit / meta.query.offset` | The page size and start position used for the result list. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM`. The response shows them as full dates.
- Use `limit` (1 to 20) and `offset` to page through the results.
- `country` accepts only `ww` (worldwide). `web_source` accepts `desktop`, `mobile_web` or `total`.
- For domain-wide traffic totals, call [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement). For where visitors come from, call [Similarweb Website Top Geographies](/apis/similarweb/website-top-geographies).

### Pricing

Billed at the actual cost of each call, about $0.225 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/popular-pages.json`](../../../catalog/models/similarweb/popular-pages.json) · Store page: https://www.sandbase.ai/model/similarweb/popular-pages
