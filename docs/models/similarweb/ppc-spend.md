# Similarweb PPC Spend API: pricing, parameters and code examples

`similarweb/ppc-spend` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get a website's estimated monthly paid-search (PPC) ad spend in USD.

## Pricing

- Depends on parameters (`params.end_date`, `params.start_date`).

Formula: `0.075 * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/ppc-spend", "domain": "cnn.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/ppc-spend', {'domain': 'cnn.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/ppc-spend", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/ppc-spend", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/ppc-spend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |
| `main_domain_only` | boolean |  | main_domain_only default `true` |

## Details

Returns the estimated monthly paid-search (PPC) ad spend in USD for a website on Similarweb. You send a `domain` and a `start_date` and `end_date` in `YYYY-MM` format. The response has one row per month in the range.

### Use cases

- Track how much a competitor spends on paid search each month.
- Compare the PPC budget of a news site against its peers before planning an ad campaign.
- Spot spending spikes around events by checking month-by-month values.
- Add a PPC spend column to a domain research report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/ppc-spend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "currency": "usd",
      "date": "2026-09-01",
      "ppc_spend": 552114.74
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "request": {
      "country": "ww",
      "currency": "usd",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "main_domain_only": true,
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
| `data[].ppc_spend` | Estimated paid-search ad spend for the month. In the example, `552114.74` is the figure for `cnn.com`. |
| `data[].currency` | Currency of `ppc_spend`. The example returns `usd`. |
| `data[].date` | First day of the month the row covers, such as `2026-09-01`. |
| `meta.status` | Result of the call. The example returns `success`. |
| `meta.last_updated` | Date shown for the last update of the data, such as `2026-09-30`. |
| `meta.request.start_date / meta.request.end_date` | The date range the call used, expanded to full dates. `2026-09` became `2026-09-01` and `2026-09-30`. |
| `meta.request.web_source` | Traffic source the figure covers. The example shows `total` when `web_source` is not sent. |
| `meta.request.main_domain_only` | Shows whether data covers the main domain only. The example shows `true`. |

### Notes

- Send `start_date` and `end_date` as `YYYY-MM`. The `data[].date` values come back as `YYYY-MM-01`.
- Set `web_source` to `desktop`, `mobile_web` or `total`. The example response used `total`.
- `country` accepts only `ww` (worldwide) and `granularity` accepts only `monthly`.
- To see which keywords drive the paid traffic, call [Similarweb Website Keywords](/apis/similarweb/search-website-keywords). For the ad networks involved, call [Similarweb Ad Networks](/apis/similarweb/ad-networks).

### Pricing

Billed at the actual cost of each call, about $0.075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/ppc-spend.json`](../../../catalog/models/similarweb/ppc-spend.json) · Store page: https://www.sandbase.ai/model/similarweb/ppc-spend
