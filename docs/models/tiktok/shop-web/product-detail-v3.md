# TikTok Shop Product Detail (V3) API: pricing, parameters and code examples

`tiktok/shop-web/product-detail-v3` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-detail-v3", "product_id": "1732108663255959373"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-detail-v3', {'product_id': '1732108663255959373'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-detail-v3", {
  "product_id": "1732108663255959373"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-detail-v3", sandbase.Params{
	"product_id": "1732108663255959373",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-detail-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"SG"` |
| `product_id` | string | yes | Product ID (required)  |

## Details

Returns the TikTok Shop product page configuration for one product. The response holds A/B test page settings and a list of page components. It needs a `product_id` and accepts an optional `region`.

### Use cases

- Read which components a TikTok Shop product page loads, such as the header and the app popup.
- Check the page-level `page_id` that TikTok Shop assigns to a product page.
- Compare the page configuration of one product across regions by changing `region`.
- Confirm that a `product_id` returns a page before you call other product APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-detail-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1732108663255959373"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "product_data": {
    "ab_test": {
      "page_level": {
        "page_id": "1107184653723596687",
        "params": {},
        "vids": []
      },
      "user_level": {}
    },
    "page_config": {
      "components_map": [
        {
          "component_name": "user_info",
          "component_type": "user_info",
          "fe_config": {}
        }
      ],
      "global_fe_config": {}
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `product_data.page_config.components_map[].component_name` | Name of a component on the product page, for example `user_info` or `page_header`. |
| `product_data.page_config.components_map[].component_type` | Type of the component. In this response it matches `component_name`. |
| `product_data.page_config.components_map[].fe_config` | Front-end settings for that component. For `page_header` it holds `disable_search`, and for `call_app_bottom_popup` it holds `target`. |
| `product_data.page_config.components_map[].fe_config.disable_search` | Set to `true` when search is turned off in the page header. |
| `product_data.page_config.components_map[].fe_config.target` | Page element that the app popup attaches to. The value here is `wrapper_pdp`. |
| `product_data.page_config.global_fe_config` | Front-end settings that apply to the whole page. It is an empty object in this response. |
| `product_data.ab_test.page_level.page_id` | ID of the product page used for A/B testing, as a string. |
| `product_data.ab_test.page_level.params / product_data.ab_test.page_level.vids` | A/B test parameters and variant IDs for the page. Both are empty in this response. |
| `product_data.ab_test.user_level` | A/B test settings tied to the user. It is an empty object in this response. |

### Notes

- `product_id` is a long numeric string, for example `1732108663255959373`. If you only have a share link, call [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link) first.
- `region` takes `US`, `GB`, `SG`, `MY`, `PH`, `TH`, `VN` or `ID`. The default is `SG`.
- This response for the sample product holds page configuration only. For other product data, try [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2) or [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/apis/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link): Returns the TikTok Shop product identifier extracted from a provided product share link.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-detail-v3.json`](../../../../catalog/models/tiktok/shop-web/product-detail-v3.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-detail-v3
