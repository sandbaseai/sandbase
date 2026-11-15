# H&M Similar Items API: pricing, parameters and code examples

`hm/similar-items` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch similar product recommendations for a given article code. Returns multiple recommendation lists (style_with, alternatives, upsell) each containing related products with pricing and availability.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/similar-items", "article_code": "1347416001"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/similar-items', {'article_code': '1347416001'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/similar-items", {
  "article_code": "1347416001"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/similar-items", sandbase.Params{
	"article_code": "1347416001",
})
```

Same call via the path form: `POST /v1/api/hm/similar-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_code` | string | yes | Article code to find similar items for (e.g. '1347416001').  |

## Details

Fetch similar product recommendations for a given article code. Returns multiple recommendation lists (style_with, alternatives, upsell) each containing related products with pricing and availability.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/similar-items", "article_code": "1347416001"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_code` | string | Yes | Article code to find similar items for (e.g. '1347416001'). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/similar-items.json`](../../../catalog/models/hm/similar-items.json) · Store page: https://www.sandbase.ai/model/hm/similar-items
