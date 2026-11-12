# JD.com Product Price API: pricing, parameters and code examples

`jd/item/price` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get current JD.com prices for up to 10 product IDs in one call; pass the IDs comma-separated. One call costs the same for 1 or 10 IDs.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/item/price", "itemIds": "100012043978,100207440191"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/item/price', {'itemIds': '100012043978,100207440191'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/item/price", {
  "itemIds": "100012043978,100207440191"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/item/price", sandbase.Params{
	"itemIds": "100012043978,100207440191",
})
```

Same call via the path form: `POST /v1/api/jd/item/price` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemIds` | string | yes | Between 1 and 10 numeric JD.com item IDs, separated by commas without spaces.  |

## Details

Get current JD.com prices for up to 10 product IDs in one call; pass the IDs comma-separated. One call costs the same for 1 or 10 IDs.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/item/price" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemIds": "100012043978,100207440191"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemIds` | string | Yes | Between 1 and 10 numeric JD.com item IDs, separated by commas without spaces. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/jd/item/price.json`](../../../../catalog/models/jd/item/price.json) · Store page: https://www.sandbase.ai/model/jd/item/price
