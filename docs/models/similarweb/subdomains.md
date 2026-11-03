# Similarweb Website Subdomains API: pricing, parameters and code examples

`similarweb/subdomains` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Get a website's subdomains with each subdomain's share of traffic.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.15 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/subdomains", "domain": "cnn.com", "end_date": "2026-09", "limit": 2, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/subdomains', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 2, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/subdomains", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "limit": 2,
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/subdomains", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 2,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/subdomains` with the body above minus `model`.

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

Returns the subdomains of a website, each with its share of the site's traffic. It needs a `domain`, a `start_date` and `end_date` in `YYYY-MM` format, and a `limit`.

### Use cases

- Check how much of a news site's traffic lands on its main domain versus regional or product subdomains.
- Find which subdomains of a competitor carry the most visits before you study them further.
- Track how traffic moves between subdomains after a site migration or redesign.
- Compare desktop and mobile web subdomain mix by changing `web_source`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/subdomains" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "limit": 2, "granularity": "monthly"}'
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
      "share": 0.7662921167867314,
      "subdomain": "cnn.com"
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "query": {
      "asc": null,
      "limit": 2,
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
      "start_date": "2026-09-01",
      "web_source": "desktop"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One subdomain per row, in the order returned. The number of rows follows `limit`. |
| `data[].subdomain` | Hostname of the subdomain, for example `cnn.com` or `edition.cnn.com`. |
| `data[].share` | Share of the domain's traffic that goes to this subdomain, as a decimal between 0 and 1. A value of `0.766` means about 76.6%. |
| `meta.status` | Shows `success` when the call worked. |
| `meta.last_updated` | Date of the latest data behind this result, such as `2026-09-30`. |
| `meta.query.limit / meta.query.offset` | Page size and start position applied to the list. |
| `meta.request.start_date / meta.request.end_date` | Date range the query used, expanded to full days. A monthly request for `2026-09` shows as `2026-09-01` to `2026-09-30`. |
| `meta.request.web_source` | Device source applied to the query. The sample shows `desktop`. |
| `meta.request.main_domain_only` | Shows whether the result was limited to the main domain. The sample shows `false`. |

### Notes

- Send dates as `YYYY-MM`. The sample request used `2026-09` for both `start_date` and `end_date`.
- `limit` accepts 1 to 20. Add `offset` to page through more subdomains.
- `country` accepts only `ww` (worldwide), and `granularity` accepts only `monthly`.
- `web_source` accepts `desktop`, `mobile_web` or `total`. The sample response shows `desktop` when you do not set it.

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/subdomains.json`](../../../catalog/models/similarweb/subdomains.json) · Store page: https://www.sandbase.ai/model/similarweb/subdomains
