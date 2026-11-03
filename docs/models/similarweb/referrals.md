# Similarweb Referrals API: pricing, parameters and code examples

`similarweb/referrals` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.3 per call · **Modes:** sync

Get the websites a site's referral traffic comes from, with visits, share and change for each referrer.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.3 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/referrals", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/referrals', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/referrals", {
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
run, err := c.Run(ctx, "similarweb/referrals", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/referrals` with the body above minus `model`.

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

Returns the websites that send referral traffic to a given domain, with visits, share and change for each referrer. It needs a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- List the sites that send the most referral visits to a competitor's domain.
- Spot referrers whose traffic to a site dropped or grew from the prior period.
- Find partner or publisher sites to approach based on the share of referral traffic they send.
- Compare desktop and mobile web referrals by setting `web_source`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/referrals" \
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
      "change": -0.3251058721471521,
      "domain": "drudgereport.com",
      "share": 0.07414256683760033,
      "visits": 601755.1926150493
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
      "referral_type": "incoming",
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
| `data[].domain` | The referring website that sends traffic to the requested domain. |
| `data[].visits` | Estimated number of visits that came from this referrer in the requested period. |
| `data[].share` | This referrer's share of the domain's referral traffic, as a fraction. A value of `0.074` means about 7.4%. |
| `data[].change` | Change in visits for this referrer compared with the previous period, as a fraction. A negative value means a drop. |
| `meta.status` | Shows `success` when the call worked. |
| `meta.last_updated` | Date of the latest data for this response, such as `2026-09-30`. |
| `meta.query.limit / meta.query.offset` | The page size and start position that were applied to the list. |
| `meta.request.web_source` | The device filter that was applied. The sample response shows `total`. |
| `meta.request.referral_type` | The kind of referrals returned. The sample response shows `incoming`. |
| `meta.request.start_date / meta.request.end_date` | The full date range that was queried, expanded to day precision. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM` values. The response echoes them as full dates such as `2026-09-01` and `2026-09-30`.
- `limit` accepts 1 to 20. Use `offset` to move through further referrers.
- `country` accepts only `ww` (worldwide), and `granularity` accepts only `monthly`.
- Set `main_domain_only` to `true` or `false` to control how referrers are grouped. The sample request left it unset, and the response shows `false`.

### Pricing

Billed at the actual cost of each call, about $0.3 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/referrals.json`](../../../catalog/models/similarweb/referrals.json) · Store page: https://www.sandbase.ai/model/similarweb/referrals
