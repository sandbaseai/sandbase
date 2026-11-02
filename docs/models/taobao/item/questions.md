# Taobao Product Questions API: pricing, parameters and code examples

`taobao/item/questions` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get buyer questions and answers for a Taobao or Tmall product by item ID, page by page.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/questions", "itemId": "672400567264"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/questions', {'itemId': '672400567264'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/questions", {
  "itemId": "672400567264"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/questions", sandbase.Params{
	"itemId": "672400567264",
})
```

Same call via the path form: `POST /v1/api/taobao/item/questions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |

## Details

Get buyer questions and answers for a Taobao or Tmall product by item ID, page by page.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/questions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "672400567264"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/taobao/item/questions.json`](../../../../catalog/models/taobao/item/questions.json) · Store page: https://www.sandbase.ai/model/taobao/item/questions
