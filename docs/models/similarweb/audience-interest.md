# Similarweb Audience Interest API: pricing, parameters and code examples

`similarweb/audience-interest` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.375 per call · **Modes:** sync

Get the other websites a site's audience also visits, with affinity and audience overlap scores.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.375 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/audience-interest", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/audience-interest', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/audience-interest", {
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
run, err := c.Run(ctx, "similarweb/audience-interest", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/audience-interest` with the body above minus `model`.

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

Returns a list of other websites that the audience of a given domain also visits. Each row has an affinity score, an audience overlap share, a period-over-period change and an ad flag. You send a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Find websites that share an audience with a competitor to plan media buys.
- Build a list of sites to approach for partnerships or link placements around a topic.
- Check which sites draw the same readers as `cnn.com` to study how a news audience splits its attention.
- Track the `pop_change` value of related sites between periods to spot rising or falling audience ties.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/audience-interest" \
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
      "affinity": 100.0,
      "domain": "bbc.com",
      "has_adsense": true,
      "overlap": 0.11716861665468993,
      "pop_change": -0.011031223932006734
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
        "affinity"
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
| `data[]` | One website that the audience of the requested domain also visits. The list holds up to `limit` rows. |
| `data[].domain` | Domain of the related website, for example `bbc.com`. |
| `data[].affinity` | Affinity score for the related site. The top row in the sample shows `100.0`. |
| `data[].overlap` | Audience overlap between the requested domain and the related site, as a decimal value such as `0.117`. |
| `data[].pop_change` | Change in the related site's value compared with the previous period, as a decimal. A negative value means a decrease. |
| `data[].has_adsense` | `true` when the related site is flagged as using AdSense. |
| `meta.last_updated` | Date of the latest data behind the response, in `YYYY-MM-DD` format. |
| `meta.request.start_date / meta.request.end_date` | The full date range that the API applied. Month inputs like `2026-09` expand to the first and last day of the month. |
| `meta.request.web_source` | Traffic source scope that the API applied. The sample shows `total`. |
| `meta.request.metrics` | List of metrics returned per row: `affinity`, `overlap` and `pop_change`. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM` values. `granularity` accepts `monthly` and `country` accepts `ww`.
- Use `limit` (1 to 20) and `offset` to page through results. The response echoes both under `meta.query`.
- `web_source` accepts `desktop`, `mobile_web` or `total`.
- For sites with similar content rather than shared audience, call [Similarweb SimilarSites](/apis/similarweb/similar-sites). For direct audience overlap between sites, see [Similarweb Audience Overlap](/apis/similarweb/audience-overlap).

### Pricing

Billed at the actual cost of each call, about $0.375 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/audience-interest.json`](../../../catalog/models/similarweb/audience-interest.json) · Store page: https://www.sandbase.ai/model/similarweb/audience-interest
