# 1688 Shop Categories API: pricing, parameters and code examples

`1688/shop/categories` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

List all product categories of a 1688 shop by shop URL or seller member ID.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/shop/categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/shop/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/shop/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/shop/categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/shop/categories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shopUrl` | string |  | 1688 shop homepage URL. Supply shopUrl or memberId.  |
| `memberId` | string |  | Seller member ID. Supply memberId or shopUrl.  |

## Details

Returns the list of product categories that a 1688 shop has set up, with a product count for each category. Send either the shop homepage URL as `shopUrl` or the seller ID as `memberId`.

### Use cases

- Map the full catalog structure of a competitor shop on 1688.
- Find which categories hold the most products in a supplier's shop.
- Collect category IDs for a shop before you pull the products in each category.
- Check how a seller groups its products, for example by phone case type.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/shop/categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"memberId": "b2b-3945631662b7581"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `memberId` | string | No | Seller member ID. Supply memberId or shopUrl. |
| `shopUrl` | string | No | 1688 shop homepage URL. Supply shopUrl or memberId. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "is_custom": true,
  "list": [
    {
      "children": [],
      "count": 16,
      "full_name": "折叠屏转轴保护套",
      "id": 169945812,
      "name": "折叠屏转轴保护套"
    }
  ],
  "member_id": "b2b-3945631662b7581"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `member_id` | The seller member ID the categories belong to. It matches the `memberId` you sent. |
| `is_custom` | Boolean flag on the category list. It is `true` in this response. The key name does not say more, so treat the exact meaning as unconfirmed. |
| `list[]` | One entry per shop category. |
| `list[].id` | Numeric ID of the category. |
| `list[].name / list[].full_name` | Category name, and its full name. Both show the same text for these top-level categories. |
| `list[].count` | Number of products in the category. |
| `list[].children` | List of sub-categories. It is empty for the categories shown here. |

### Notes

- Supply `shopUrl` or `memberId`. You only need one of them.
- Category names are returned in Chinese, as set by the seller.
- Use [1688 Category Products](/apis/1688/category/items) to list products in a category, and [1688 Category Info](/apis/1688/category/info) for category details.
- Use [1688 Shop Info](/apis/1688/shop/info) to get details about the shop itself.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/shop/categories.json`](../../../../catalog/models/1688/shop/categories.json) · Store page: https://www.sandbase.ai/model/1688/shop/categories
