# Yellow Pages Check Pos Technology API: pricing, parameters and code examples

`yellowpages/check-pos-technology` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Check a business website for POS (Point of Sale) technology signals by scanning the page HTML for mentions of specific software platforms (MICROS Simphony, MICROS 3700, Oracle Hospitality). Returns whether any POS technology was detected and the list of detected technologies.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/check-pos-technology", "website_url": "https://www.rotorooter.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/check-pos-technology', {'website_url': 'https://www.rotorooter.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/check-pos-technology", {
  "website_url": "https://www.rotorooter.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/check-pos-technology", sandbase.Params{
	"website_url": "https://www.rotorooter.com",
})
```

Same call via the path form: `POST /v1/api/yellowpages/check-pos-technology` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `website_url` | string | yes | Business website URL to check (e.g., 'https://www.example.com')  |

## Details

Check a business website for POS (Point of Sale) technology signals by scanning the page HTML for mentions of specific software platforms (MICROS Simphony, MICROS 3700, Oracle Hospitality). Returns whether any POS technology was detected and the list of detected technologies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/check-pos-technology", "website_url": "https://www.rotorooter.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `website_url` | string | Yes | Business website URL to check (e.g., 'https://www.example.com') |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/check-pos-technology.json`](../../../catalog/models/yellowpages/check-pos-technology.json) · Store page: https://www.sandbase.ai/model/yellowpages/check-pos-technology
