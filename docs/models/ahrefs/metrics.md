# Ahrefs Ahrefs Site Metrics API: pricing, parameters and code examples

`ahrefs/metrics` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.08 per call · **Modes:** sync

Return core Site Explorer metrics for a target domain on a given date: organic and paid keyword counts, top-3 keyword count, organic traffic, and traffic value. 4xx/5xx are not charged.

## Pricing

- **$0.08 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/metrics", "date": "2026-08-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/metrics', {'date': '2026-08-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/metrics", {
  "date": "2026-08-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/metrics", sandbase.Params{
	"date": "2026-08-01",
	"target": "ahrefs.com",
})
```

Same call via the path form: `POST /v1/api/ahrefs/metrics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Snapshot date in `YYYY-MM-DD` format.  |
| `target` | string | yes | Target domain, e.g. `ahrefs.com`.  |

## Details

Returns Site Explorer metrics for a target domain on a given date. The response covers organic and paid keyword counts, top-3 organic keywords, organic and paid traffic, and cost values. You send a `target` domain and a `date` in `YYYY-MM-DD` format.

### Use cases

- Compare the organic traffic of a competitor domain with your own on the same date.
- Track how many keywords a site ranks for in positions 1 to 3 by calling the API for different dates.
- Check whether a domain runs paid search by reading `metrics.paid_keywords` and `metrics.paid_traffic`.
- Estimate the value of a site's organic traffic with `metrics.org_cost` when screening acquisition targets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ahrefs/metrics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "ahrefs.com", "date": "2026-10-01"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | Snapshot date in `YYYY-MM-DD` format. |
| `target` | string | Yes | Target domain, e.g. `ahrefs.com`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "metrics": {
    "org_cost": 423229931,
    "org_keywords": 36098,
    "org_keywords_1_3": 14678,
    "org_traffic": 2566697,
    "paid_cost": 45844,
    "paid_keywords": 34,
    "paid_pages": 10,
    "paid_traffic": 515
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `metrics.org_keywords` | Number of keywords the target ranks for in organic search. |
| `metrics.org_keywords_1_3` | Number of organic keywords where the target ranks in positions 1 to 3. |
| `metrics.org_traffic` | Organic traffic estimate for the target. |
| `metrics.org_cost` | Cost value of the organic traffic. The response does not show the currency unit. |
| `metrics.paid_keywords` | Number of keywords the target bids on in paid search. |
| `metrics.paid_pages` | Number of pages of the target that appear in paid search results. |
| `metrics.paid_traffic` | Paid traffic estimate for the target. |
| `metrics.paid_cost` | Cost value of the paid traffic. The response does not show the currency unit. |

### Notes

- Both `target` and `date` are required. Pass the domain, for example `ahrefs.com`, and a date such as `2026-10-01`.
- Call the API with different `date` values to build a time series for one domain.
- To see the authority score of the same domain, call [Ahrefs Ahrefs Domain Rating](/apis/ahrefs/domain-rating).

### Pricing

$0.08 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ahrefs/metrics.json`](../../../catalog/models/ahrefs/metrics.json) · Store page: https://www.sandbase.ai/model/ahrefs/metrics
