# Ahrefs Ahrefs Domain Rating API: pricing, parameters and code examples

`ahrefs/domain-rating` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.08 per call · **Modes:** sync

Return the Ahrefs Domain Rating (0-100 authority score) and Ahrefs Rank for a target domain on a given date. 4xx/5xx are not charged.

## Pricing

- **$0.08 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/domain-rating", "date": "2026-08-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/domain-rating', {'date': '2026-08-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/domain-rating", {
  "date": "2026-08-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/domain-rating", sandbase.Params{
	"date": "2026-08-01",
	"target": "ahrefs.com",
})
```

Same call via the path form: `POST /v1/api/ahrefs/domain-rating` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Snapshot date in `YYYY-MM-DD` format.  |
| `target` | string | yes | Target domain, e.g. `ahrefs.com`.  |

## Details

Returns the Ahrefs Domain Rating and Ahrefs Rank for one domain on a chosen date. You send the domain in `target` and a snapshot date in `date`.

### Use cases

- Check the authority score of a domain before you buy a guest post or ask for a link.
- Track how a site's Domain Rating changes by calling the API with different `date` values.
- Compare the Domain Rating of several competitor domains in one report.
- Filter a list of prospect domains by minimum Domain Rating in an outreach tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ahrefs/domain-rating" \
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
  "domain_rating": {
    "ahrefs_rank": 620,
    "domain_rating": 91.0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `domain_rating.domain_rating` | The Ahrefs Domain Rating of the target domain on the requested date. The value is on a 0-100 scale, as described in the API description. |
| `domain_rating.ahrefs_rank` | The Ahrefs Rank of the target domain on the requested date. A lower number means a higher position in the ranking. |

### Notes

- Send `target` as a bare domain such as `ahrefs.com`.
- Send `date` as `YYYY-MM-DD`. Both `target` and `date` are required.
- To get more site metrics for the same domain, call [Ahrefs Ahrefs Site Metrics](/apis/ahrefs/metrics).

### Pricing

$0.08 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ahrefs/domain-rating.json`](../../../catalog/models/ahrefs/domain-rating.json) · Store page: https://www.sandbase.ai/model/ahrefs/domain-rating
