# 1688 Product Description Images API: pricing, parameters and code examples

`1688/item/description-images` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the description images of a 1688 product listing by item ID, for catalog preparation and product research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/description-images", "itemId": "857511694718"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/description-images', {'itemId': '857511694718'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/description-images", {
  "itemId": "857511694718"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/description-images", sandbase.Params{
	"itemId": "857511694718",
})
```

Same call via the path form: `POST /v1/api/1688/item/description-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | 1688 product ID.  |

## Details

Returns the description images of a 1688 product listing, plus the raw description HTML. It needs one input: the 1688 product ID in `itemId`.

### Use cases

- Download the description images of a listing to prepare catalog entries for a resale store.
- Review the detail-page artwork of a competing product during product research.
- Extract image URLs from the description HTML to check which images a listing embeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/description-images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "857511694718"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | 1688 product ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "detail_html": "<div id=\"offer-template-0\"></div><div style=\"width: 790.0px;\"><img style=\"displa…",
  "detail_imgs": [
    "https://cbu01.alicdn.com/img/ibank/O1CN01RgFJeQ2MFztOKMuBj_!!3534549799-0-cib.jp…"
  ],
  "item_id": 857511694718
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_id` | The numeric 1688 product ID of the listing. It matches the `itemId` you sent. |
| `detail_imgs[]` | Image URLs taken from the product description. Each entry is one image link. |
| `detail_html` | The raw HTML of the product description. It contains `<img>` tags with `src` links to the description images, plus layout styles. |

### Notes

- Send `itemId` as a string. The response returns `item_id` as a number.
- Use `detail_imgs` when you only need image links. Parse `detail_html` when you also need the order of the images in the description.
- For other data about the same listing, call [1688 Product Details](/apis/1688/item/detail) with the same ID.
- If you only have a product link, use [1688 Product Details by URL](/apis/1688/item/detail-by-url).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/item/description-images.json`](../../../../catalog/models/1688/item/description-images.json) · Store page: https://www.sandbase.ai/model/1688/item/description-images
