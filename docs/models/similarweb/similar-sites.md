# Similarweb SimilarSites API: pricing, parameters and code examples

`similarweb/similar-sites` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.375 per call · **Modes:** sync

Get websites similar to a domain, with affinity score, category and global rank. The date range must span exactly 3 months.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.375 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/similar-sites", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-07"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/similar-sites', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-07'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/similar-sites", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "limit": 1,
  "start_date": "2026-07"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/similar-sites", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-07",
})
```

Same call via the path form: `POST /v1/api/similarweb/similar-sites` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `domain` | string | yes | domain  |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | End month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09.  |
| `start_date` | string | yes | Start month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09.  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly` |
| `traffic_source` | string |  | traffic_source  |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Returns websites similar to a given domain, with an affinity score, category, global rank and an AdSense flag for each. It needs a `domain` and a `start_date` and `end_date` that span exactly 3 months.

### Use cases

- Build a competitor list for a news site such as `cnn.com`.
- Find lookalike sites to target when planning ad placements.
- Group related sites by `category` to map a market segment.
- Rank similar sites by `rank` to pick the biggest competitors to track.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/similar-sites" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "cnn.com", "start_date": "2026-07", "end_date": "2026-09", "limit": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | End month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09. |
| `limit` | integer | Yes | limit |
| `start_date` | string | Yes | Start month (YYYY-MM). The range must span exactly 3 months, e.g. 2026-07 to 2026-09. |
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
      "affinity": 1.0,
      "category": "News_and_Media",
      "domain": "cnbc.com",
      "has_adsense": true,
      "rank": 588
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
      "category": null,
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "metrics": [
        "rank"
      ],
      "start_date": "2026-07-01"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].domain` | The similar website's domain. |
| `data[].affinity` | Similarity score between the similar site and the requested domain. The top result in this example has `1.0`. |
| `data[].category` | Category of the similar site, written with underscores, for example `News_and_Media`. |
| `data[].rank` | Global rank of the similar site. A lower number means a higher rank. |
| `data[].has_adsense` | `true` if the similar site uses AdSense. |
| `meta.last_updated` | Date of the most recent data, in `YYYY-MM-DD` format. |
| `meta.query.limit / meta.query.offset` | The pagination values applied to this call. |
| `meta.request.start_date / meta.request.end_date` | The full date range used for the query. The API expanded the months you sent to the first and last day. |
| `meta.status` | `success` when the call worked. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM`. The range must cover exactly 3 months, such as `2026-07` to `2026-09`.
- Use `limit` (1 to 20) and `offset` to page through results.
- `country` accepts only `ww` (worldwide), and `granularity` accepts only `monthly`.
- To compare traffic for a similar site you find, call [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement) with its `domain`.

### Pricing

Billed at the actual cost of each call, about $0.375 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/similar-sites.json`](../../../catalog/models/similarweb/similar-sites.json) · Store page: https://www.sandbase.ai/model/similarweb/similar-sites
