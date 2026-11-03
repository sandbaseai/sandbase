# 1688 Shop Info API: pricing, parameters and code examples

`1688/shop/info` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get 1688 shop information by shop URL or seller member ID: company, location, ratings and business type.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/shop/info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/shop/info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/shop/info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/shop/info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/1688/shop/info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shopUrl` | string |  | 1688 shop homepage URL. Supply shopUrl or memberId.  |
| `memberId` | string |  | Seller member ID. Supply memberId or shopUrl.  |

## Details

This API returns profile data for a 1688 shop, including company name, location, service ratings and business type flags. It needs either a `shopUrl` (the shop homepage URL) or a `memberId` (the seller member ID).

### Use cases

- Check a supplier's company name and city before you place a sourcing order.
- Compare service ratings such as logistics and dispute resolution across several 1688 sellers.
- Filter suppliers by flags like `is_factory` or `is_super_factory` when you build a supplier list.
- Map a seller `member_id` to a `company_id` and company name to match records in your own database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/shop/info" \
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
  "chat_url": "",
  "company_id": "36968811",
  "company_name": "广州贝利塑料制品有限公司",
  "contact_info": {},
  "favorite_count": "295",
  "is_factory": false,
  "is_flagship_shop": false,
  "is_industry_brand": false,
  "is_super_factory": false,
  "is_tp": true,
  "location": {
    "city": "广州市",
    "province": "广东省",
    "street": ""
  },
  "location_str": "广东省 广州市"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `company_name / shop_name` | Registered company name and shop name. Both hold the same value in this response. |
| `company_id / member_id` | Identifiers for the company and the seller. `member_id` matches the value you can send as `memberId`. |
| `location.province / location.city / location.street` | Province, city and street of the seller. `street` can be an empty string. |
| `location_str` | Province and city joined in one string, ready to display. |
| `shop_ratings[].title` | Name of the rating category, shown in Chinese. |
| `shop_ratings[].score` | Score for that category, returned as a string such as `5.0`. |
| `shop_ratings[].type` | Machine-readable rating code, such as `purchase_consultation`, `logistics` or `dispute_resolution`. |
| `is_factory / is_super_factory / is_flagship_shop / is_industry_brand` | Boolean flags for the shop's business type and status. |
| `is_tp / tp_year` | `is_tp` flags a TP shop. `tp_year` is a string with a number of years, `9` in this response. |
| `favorite_count` | Number of favorites for the shop, returned as a string. |

### Notes

- Send either `shopUrl` or `memberId`. The example uses `memberId` with a value like `b2b-3945631662b7581`.
- Some fields can come back empty, such as `chat_url`, `shop_logo`, `shop_url` and `contact_info`. `seller_id` can be `null`.
- Numbers like `favorite_count`, `company_id` and `tp_year` are returned as strings.
- To list the products of a shop, call [1688 Shop Products by URL](/apis/1688/shop/items-by-url). For its product groups, call [1688 Shop Categories](/apis/1688/shop/categories).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/1688/shop/info.json`](../../../../catalog/models/1688/shop/info.json) · Store page: https://www.sandbase.ai/model/1688/shop/info
