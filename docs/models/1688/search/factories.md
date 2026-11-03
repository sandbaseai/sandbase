# 1688 Factory Search API: pricing, parameters and code examples

`1688/search/factories` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search 1688 factories and manufacturers by keyword, sorted by default order or repurchase rate.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/factories", "keyword": "phone case"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/factories', {'keyword': 'phone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/factories", {
  "keyword": "phone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/factories", sandbase.Params{
	"keyword": "phone case",
})
```

Same call via the path form: `POST /v1/api/1688/search/factories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Factory sort order. one of: `default`, `repurchase_rate`; default `"default"` |
| `keyword` | string | yes | Factory search keyword.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |

## Details

Returns a list of 1688 factories and manufacturers that match a keyword. Each item has the company name, factory level, product tags, service tags and a factory card link. The only required input is `keyword`.

### Use cases

- Build a supplier shortlist for a product type such as phone cases by reading `product_tags` and `service_tags`.
- Filter factories that hold certifications such as ISO 9001 by checking `service_tags`.
- Rank factories by `response_rate` to find suppliers that reply to buyers.
- Sort by `repurchase_rate` to compare factories that buyers order from again.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/factories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "phone case"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Factory search keyword. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Factory sort order. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "items": [
    {
      "company_name": "广州贝利塑料制品有限公司",
      "factory_level": "无牌工厂",
      "factory_url": "https://sale.1688.com/factory/card.html?__existtitle__=1&__removesafearea__=1&me…",
      "invoice_available": false,
      "is_factory": true,
      "location": {
        "city": null
      },
      "member_id": "b2b-3945631662b7581",
      "product_tags": [
        "iPhone保护套"
      ],
      "response_rate": "0.89",
      "service_tags": [
        "ISO 9001认证"
      ],
      "shop_repurchase_rate": null,
      "super_factory": false
    }
  ],
  "keywords": "phone case",
  "page": 1,
  "page_size": 20,
  "sort": "default",
  "total_count": 1000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].company_name` | Registered company name of the factory, in Chinese. |
| `items[].member_id / items[].user_id` | Identifiers for the factory account. `member_id` is a string that starts with `b2b-`. `user_id` is a number. |
| `items[].factory_url` | Link to the factory card page on 1688. |
| `items[].factory_level` | Factory level label. The sample shows `无牌工厂`, which means a factory with no level badge. |
| `items[].is_factory / items[].super_factory` | Flags that show whether the seller is marked as a factory and whether it is marked as a super factory. |
| `items[].product_tags` | List of product categories the factory makes, such as `iPhone保护套`. |
| `items[].service_tags` | List of service and certification labels, such as `ISO 9001认证`, `CCC认证` and `包工包料`. |
| `items[].response_rate` | Reply rate of the factory, returned as a string such as `0.89`. |
| `items[].shop_repurchase_rate` | Repurchase rate of the shop. It is `null` when the factory has no value. |
| `items[].invoice_available / items[].tp_member / items[].tp_year` | Flag for invoice availability, flag for TrustPass membership, and the membership year. `tp_year` is `null` when the factory is not a member. |
| `total_count` | Total number of matching factories reported for the query. |

### Notes

- Pass `page` to move through results. `page` starts at 1.
- `pageSize` sets the requested items per page. The number of returned items may differ.
- Set `sort` to `default` or `repurchase_rate`. The response echoes the value in `sort`.
- Use `items[].factory_url` to open the factory card. Call [1688 Shop Info](/apis/1688/shop/info) for more shop details.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/search/factories.json`](../../../../catalog/models/1688/search/factories.json) · Store page: https://www.sandbase.ai/model/1688/search/factories
