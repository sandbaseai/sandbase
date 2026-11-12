# Taobao Product Description Images API: pricing, parameters and code examples

`taobao/item/description-images` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the description HTML and the list of description images for a Taobao or Tmall product by item ID, for catalog preparation and listing content review.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/item/description-images", "itemId": "920640959876"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/item/description-images', {'itemId': '920640959876'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/item/description-images", {
  "itemId": "920640959876"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/item/description-images", sandbase.Params{
	"itemId": "920640959876",
})
```

Same call via the path form: `POST /v1/api/taobao/item/description-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Unique product identifier on Taobao/Tmall (item ID).  |

## Details

Get the description HTML and the list of description images for a Taobao or Tmall product by item ID, for catalog preparation and listing content review.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/item/description-images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "920640959876"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Unique product identifier on Taobao/Tmall (item ID). |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/taobao/item/description-images.json`](../../../../catalog/models/taobao/item/description-images.json) · Store page: https://www.sandbase.ai/model/taobao/item/description-images
