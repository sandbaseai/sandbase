# JD.com Product Description Images API: pricing, parameters and code examples

`jd/item/description-images` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Get the description images and product attributes of a JD.com product by item ID.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/item/description-images", "itemId": "100344885578"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/item/description-images', {'itemId': '100344885578'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/item/description-images", {
  "itemId": "100344885578"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/item/description-images", sandbase.Params{
	"itemId": "100344885578",
})
```

Same call via the path form: `POST /v1/api/jd/item/description-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | A unique product identifier on JD.com (item ID).  |

## Details

Get the description images and product attributes of a JD.com product by item ID.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/item/description-images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "100344885578"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | A unique product identifier on JD.com (item ID). |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/jd/item/description-images.json`](../../../../catalog/models/jd/item/description-images.json) · Store page: https://www.sandbase.ai/model/jd/item/description-images
