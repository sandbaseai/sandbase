# Zillow Property Details API: pricing, parameters and code examples

`zillow/property-details` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0008 per call (free daily quota) · **Modes:** sync

Fetch full details for a single Zillow property listing by URL (price, facts and features, photos, and price/tax history).

## Pricing

- **$0.0008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/property-details", "url": "https://www.zillow.com/homedetails/4510-Secure-Ln-Austin-TX-78725/83126034_zpid/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/property-details', {'url': 'https://www.zillow.com/homedetails/4510-Secure-Ln-Austin-TX-78725/83126034_zpid/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/property-details", {
  "url": "https://www.zillow.com/homedetails/4510-Secure-Ln-Austin-TX-78725/83126034_zpid/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/property-details", sandbase.Params{
	"url": "https://www.zillow.com/homedetails/4510-Secure-Ln-Austin-TX-78725/83126034_zpid/",
})
```

Same call via the path form: `POST /v1/api/zillow/property-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Zillow property details URL (e.g. https://www.zillow.com/homedetails/123-Main-St-Anytown-CA-90210/12345678_zpid/).  |

## Details

Fetch full details for a single Zillow property listing by URL (price, facts and features, photos, and price/tax history).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "zillow/property-details", "url": "https://www.zillow.com/homedetails/4510-Secure-Ln-Austin-TX-78725/83126034_zpid/"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Zillow property details URL (e.g. https://www.zillow.com/homedetails/123-Main-St-Anytown-CA-90210/12345678_zpid/). |

### Pricing

Flat $0.0008 per call. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/zillow/property-details.json`](../../../catalog/models/zillow/property-details.json) · Store page: https://www.sandbase.ai/model/zillow/property-details
