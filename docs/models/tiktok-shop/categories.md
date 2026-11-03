# TikTok Shop Categories API: pricing, parameters and code examples

`tiktok-shop/categories` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List the TikTok Shop category tree for a market: top-level categories with ids, slugs, and images, each with its child categories.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok-shop/categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Country code of the TikTok Shop market whose category tree to list. Only US and VN publish a category tree. one of: `US`, `VN`; default `"US"` |

## Details

Returns the TikTok Shop category tree for one market. Each top-level category comes with its `categoryId`, `name`, `slug`, `image`, and a list of child categories. The only input is `region`, which can be `US` or `VN`.

### Use cases

- Build a category picker or filter menu for a TikTok Shop research tool.
- Map `categoryId` values to readable names when you analyze product data.
- Compare how the US and Vietnam markets group their products.
- Collect category slugs and images to build a catalog of TikTok Shop verticals.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | No | Country code of the TikTok Shop market whose category tree to list. Only US and VN publish a category tree. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "categories": [
      {
        "categoryId": "601450",
        "children": [
          {
            "categoryId": "849032",
            "image": "https://p16-oec-ttp.tiktokcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/dc05090b19cd43e…",
            "isLeaf": false,
            "name": "Hand & Foot Care",
            "slug": "hand-foot-care"
          }
        ],
        "image": "https://lf16-tiktok-common.tiktokcdn-us.com/obj/tiktok-web-common-tx/i18n_ecom_f…",
        "isLeaf": false,
        "name": "Beauty & Personal Care",
        "slug": "beauty-personal-care"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.categories[].categoryId` | ID of a top-level category, returned as a string. |
| `data.categories[].name / data.categories[].slug` | Display name and URL-style slug of the top-level category, such as `Beauty & Personal Care` and `beauty-personal-care`. |
| `data.categories[].image` | URL of the image used for the top-level category. |
| `data.categories[].isLeaf` | Shows whether the category has no deeper categories below it. A value of `false` means it has children. |
| `data.categories[].children[]` | List of child categories under the top-level category. |
| `data.categories[].children[].categoryId` | ID of a child category, returned as a string. |
| `data.categories[].children[].name / data.categories[].children[].slug` | Display name and slug of the child category, such as `Hand & Foot Care` and `hand-foot-care`. |
| `data.categories[].children[].image` | URL of a 200x200 image for the child category. |
| `data.categories[].children[].isLeaf` | Shows whether the child category is a leaf. In this sample, every child has `false`, so the tree may go deeper than this response shows. |
| `found` | `true` when the category tree was found for the requested `region`. |

### Notes

- Only `US` and `VN` publish a category tree. Other `region` values are not accepted.
- `categoryId` values are strings, not numbers. Keep them as strings when you store or compare them.
- To see products and results from TikTok Shop, call [TikTok Shop Search](/apis/tiktok-shop/search) next.
- To look at a single item, use [TikTok Shop Product](/apis/tiktok-shop/product).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/categories.json`](../../../catalog/models/tiktok-shop/categories.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/categories
