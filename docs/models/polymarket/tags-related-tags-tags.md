# Polymarket Get tags related to a tag id

`polymarket/tags-related-tags-tags` · api · Polymarket

Get tags related to a tag id from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-related-tags-tags", "id": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-related-tags-tags', {'id': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-related-tags-tags", {
  "id": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-related-tags-tags", sandbase.Params{
	"id": 2,
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-related-tags-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | integer | yes | id  |
| `status` | string |  | status one of: `active`, `closed`, `all` |
| `omit_empty` | boolean |  | omit_empty  |

## Details

Get tags related to a tag id from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-related-tags-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | integer | Yes | id |
| `omit_empty` | boolean | No | omit_empty |
| `status` | string | No | status |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/tags-related-tags-tags.json`](../../../catalog/models/polymarket/tags-related-tags-tags.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-related-tags-tags
