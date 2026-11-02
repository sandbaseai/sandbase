# Brave POI Descriptions API: pricing, parameters and code examples

`brave/local-descriptions` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

POI Descriptions from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/local-descriptions", "ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/local-descriptions', {'ids': ['loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA=']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/local-descriptions", {
  "ids": [
    "loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/local-descriptions", sandbase.Params{
	"ids": []any{"loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="},
})
```

Same call via the path form: `POST /v1/api/brave/local-descriptions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ids` | array | yes | A list of unique identifiers for the location. The ids are valid only for 8 hours.  |

## Details

POI Descriptions from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/local-descriptions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ids": ["loc4DFZ5OEXSZVDUAEEDV6PMTFK6YDFANIHQIRRVKLA="]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | array | Yes | A list of unique identifiers for the location. The ids are valid only for 8 hours. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/local-descriptions.json`](../../../catalog/models/brave/local-descriptions.json) · Store page: https://www.sandbase.ai/model/brave/local-descriptions
