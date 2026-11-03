# Xiaohongshu PGY live blogger square API: pricing, parameters and code examples

`xiaohongshu/pgy/live-blogger-list` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY live blogger square on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/live-blogger-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/live-blogger-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/live-blogger-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/live-blogger-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/live-blogger-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ecom` | object |  | E-commerce conversion filters  |
| `fans` | object |  | Fans purchasing power filters  |
| `live` | object |  | Live activity & performance filters  |
| `seed` | integer |  | Paging seed, echo back from previous page default `0` |
| `buyer` | object |  | Buyer group & persona filters  |
| `flags` | object |  | Platform recommendation flags  |
| `category` | object |  | Category filters  |
| `page_num` | integer |  | Page, 1-250 default `1` |
| `nick_name` | string |  | Search by nickname  |
| `page_size` | integer |  | Page size, 1-20 default `20` |

## Details

Returns a paged list of live-stream sellers (distributors) from the Xiaohongshu PGY live blogger square. You can send paging values alone, or add a nickname search and filter objects for category, buyers, e-commerce, live activity, fans and platform flags.

### Use cases

- Build a shortlist of Xiaohongshu live sellers whose average sales amount falls in a target range.
- Find live sellers with a high active fan rate for a brand partnership.
- Page through the square to export candidate sellers into a CRM or spreadsheet.
- Search by `nick_name` to check how a known seller is listed in the square.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/live-blogger-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_num": 1, "page_size": 20, "seed": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `buyer` | object | No | Buyer group & persona filters |
| `category` | object | No | Category filters |
| `ecom` | object | No | E-commerce conversion filters |
| `fans` | object | No | Fans purchasing power filters |
| `flags` | object | No | Platform recommendation flags |
| `live` | object | No | Live activity & performance filters |
| `nick_name` | string | No | Search by nickname |
| `page_num` | integer | No | Page, 1-250 |
| `page_size` | integer | No | Page size, 1-20 |
| `seed` | integer | No | Paging seed, echo back from previous page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "distributor_info_list": [
      {
        "distributor_data_info": {
          "active_fans_rate": 0.8519,
          "atv": "5000-1w",
          "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo320n9uck162eg5qe20btst2n4arn4pcg…",
          "avg_live_viewer_num": "120",
          "avg_sale_amount": "2w-5w",
          "avg_sale_amount_value": 23571.060909090917,
          "bcoo_order_cnt": 0,
          "buyer_activity": []
        },
        "distributor_extra_info": {
          "buyer_bar_list": [],
          "grade": 3,
          "telephone": "AsCoh8eSOTSVJRgpp88+rg==",
          "willing_category": [],
          "willing_commsion": "不限"
        },
        "is_star": false,
        "show_data": 1
      }
    ],
    "page_total": 5000,
    "req_id": "3c0e1f96-e0e7-4ce9-8afa-ea263fb1a337",
    "seed": 0,
    "total": 4872599
  },
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.total` | Total number of sellers that match the request. |
| `data.page_total` | Number of pages reported for the result. |
| `data.seed` | Paging seed for this result. Send it back as `seed` when you request the next page. |
| `data.distributor_info_list[].distributor_data_info.avg_sale_amount / data.distributor_info_list[].distributor_data_info.avg_sale_amount_value` | Average sales amount as a range label (for example `2w-5w`) and as a numeric value. |
| `data.distributor_info_list[].distributor_data_info.atv` | Range label for the seller's `atv`, for example `5000-1w`. |
| `data.distributor_info_list[].distributor_data_info.avg_live_viewer_num` | Average number of viewers per live stream, returned as a string. |
| `data.distributor_info_list[].distributor_data_info.active_fans_rate` | Share of active fans as a decimal, for example `0.8519`. |
| `data.distributor_info_list[].distributor_data_info.avatar` | URL of the seller's avatar image. |
| `data.distributor_info_list[].distributor_extra_info.grade` | Grade number of the seller. |
| `data.distributor_info_list[].distributor_extra_info.willing_commsion` | Commission the seller is willing to accept. `不限` means no limit. |
| `data.distributor_info_list[].is_star` | Whether the seller is flagged as a star. |

### Notes

- Set `page_num` from 1 to 250 and `page_size` from 1 to 20.
- Send the `seed` value from the previous response with each next page request.
- The `telephone` value in `distributor_extra_info` is an encoded string, and it is empty for some sellers.
- Use [Xiaohongshu PGY blogger filter options](/apis/xiaohongshu/pgy/blogger-filter-options) to look up filter choices, and [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail) for a single creator.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/live-blogger-list.json`](../../../../catalog/models/xiaohongshu/pgy/live-blogger-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/live-blogger-list
