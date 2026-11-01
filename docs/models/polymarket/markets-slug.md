# Polymarket Get market by slug

`polymarket/markets-slug` · api · Polymarket

Get market by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets-slug", "slug": "xi-jinping-out-before-2027"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets-slug', {'slug': 'xi-jinping-out-before-2027'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets-slug", {
  "slug": "xi-jinping-out-before-2027"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets-slug", sandbase.Params{
	"slug": "xi-jinping-out-before-2027",
})
```

Same call via the path form: `POST /v1/api/polymarket/markets-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_tag` | boolean |  | include_tag  |

## Details

Get market by slug from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "xi-jinping-out-before-2027"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `include_tag` | boolean | No | include_tag |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/markets-slug.json`](../../../catalog/models/polymarket/markets-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/markets-slug
