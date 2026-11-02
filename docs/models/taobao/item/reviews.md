# Taobao Product Reviews API: pricing, parameters and code examples

`taobao/item/reviews` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get Taobao and Tmall product reviews by item ID with pagination, sorted by latest or default, for customer feedback analysis.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/reviews", "itemId": "920640959876"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/reviews', {'itemId': '920640959876'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/reviews", {
  "itemId": "920640959876"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/reviews", sandbase.Params{
	"itemId": "920640959876",
})
```

Same call via the path form: `POST /v1/api/taobao/item/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |
| `orderType` | string |  | Sort order for the result set. one of: `feedbackdate`, `general`; default `"feedbackdate"` |

## Details

Get Taobao and Tmall product reviews by item ID with pagination, sorted by latest or default, for customer feedback analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "920640959876"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |
| `orderType` | string | No | Sort order for the result set. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/item/reviews.json`](../../../../catalog/models/taobao/item/reviews.json) · Store page: https://www.sandbase.ai/model/taobao/item/reviews
