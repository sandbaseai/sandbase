# Similarweb Ad Networks API: pricing, parameters and code examples

`similarweb/ad-networks` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.225 per call · **Modes:** sync

Get the ad networks behind a website's display-ad traffic, with each network's traffic share and change over the selected months.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.225 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/ad-networks", "domain": "cnn.com", "end_date": "2026-09", "limit": 1, "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/ad-networks', {'domain': 'cnn.com', 'end_date': '2026-09', 'limit': 1, 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/ad-networks", {
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
run, err := c.Run(ctx, "similarweb/ad-networks", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"limit": 1,
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/ad-networks` with the body above minus `model`.

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

Returns the ad networks that send display-ad traffic to a website, with each network's traffic share and change over the selected months. It needs a `domain`, a `start_date`, an `end_date` and a `limit`.

### Use cases

- Find which ad networks drive the most display-ad traffic to a publisher such as cnn.com.
- Compare a competitor's ad network mix with your own to spot networks you do not use.
- Track which ad networks are gaining or losing share on a site from month to month.
- Build a list of ad networks to approach when you sell ad inventory or ad tech services.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/ad-networks" \
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
      "ad_network": "Zeta Global",
      "change": 0.14955310891417808,
      "share": 0.48691075625418256
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
      "ad_network_type": "incoming",
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "main_domain_only": false,
      "metrics": [
        "share"
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
| `data[].ad_network` | Name of the ad network, for example `Zeta Global`. |
| `data[].share` | The network's share of the site's display-ad traffic, as a decimal fraction. A value of `0.4869` means about 48.7%. |
| `data[].change` | Change in the network's share compared with the earlier period, as a decimal. A positive value means the network grew. |
| `meta.request.ad_network_type` | Type of ad traffic the rows describe. The sample shows `incoming`. |
| `meta.request.web_source` | Device scope used for the query. The sample shows `total`. |
| `meta.request.start_date / meta.request.end_date` | Full date range the query covered. The month inputs are expanded to the first and last day of the month. |
| `meta.query.limit / meta.query.offset` | Page size and starting position used for this response. |
| `meta.last_updated` | Date shown as the last update for the data, in `YYYY-MM-DD` format. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM` months. Set both to the same month to get one month of data.
- `limit` accepts 1 to 20. Use `offset` to page through more networks.
- `country` accepts only `ww` (worldwide). `web_source` accepts `desktop`, `mobile_web` or `total`.
- To see where a site's other traffic comes from, call [Similarweb Referrals](/apis/similarweb/referrals) or [Similarweb Marketing Channel Sources](/apis/similarweb/marketing-channel-sources-legacy).

### Pricing

Billed at the actual cost of each call, about $0.225 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/ad-networks.json`](../../../catalog/models/similarweb/ad-networks.json) · Store page: https://www.sandbase.ai/model/similarweb/ad-networks
