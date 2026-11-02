# JD.com Product Comments API: pricing, parameters and code examples

`jd/item/comments` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get paginated customer comments for a JD.com product by item ID, for buyer feedback and product quality research.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/item/comments", "itemId": "100207440191"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/item/comments', {'itemId': '100207440191'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/item/comments", {
  "itemId": "100207440191"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/item/comments", sandbase.Params{
	"itemId": "100207440191",
})
```

Same call via the path form: `POST /v1/api/jd/item/comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for paginated comments.  |
| `itemId` | string | yes | A unique product identifier on JD.com (item ID).  |

## Details

Get paginated customer comments for a JD.com product by item ID, for buyer feedback and product quality research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/item/comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "100207440191"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on JD.com (item ID). |
| `page` | string | No | Page number for paginated comments. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/jd/item/comments.json`](../../../../catalog/models/jd/item/comments.json) · Store page: https://www.sandbase.ai/model/jd/item/comments
