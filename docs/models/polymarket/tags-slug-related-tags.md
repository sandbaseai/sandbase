# Polymarket Get related tags (relationships) by tag slug API: pricing, parameters and code examples

`polymarket/tags-slug-related-tags` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get related tags (relationships) by tag slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-slug-related-tags", "slug": "politics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-slug-related-tags', {'slug': 'politics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-slug-related-tags", {
  "slug": "politics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-slug-related-tags", sandbase.Params{
	"slug": "politics",
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-slug-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Get related tags (relationships) by tag slug from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-slug-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "politics"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `omit_empty` | boolean | No | omit_empty |
| `status` | string | No | status |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/tags-slug-related-tags.json`](../../../catalog/models/polymarket/tags-slug-related-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-slug-related-tags
