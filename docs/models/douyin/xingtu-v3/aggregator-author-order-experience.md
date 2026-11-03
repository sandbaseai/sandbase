# Douyin Xingtu Creator Order Experience API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-order-experience` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) creator order-experience information for the last 30 or 90 days. Use it to review marketplace order history during creator evaluation.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-order-experience", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-order-experience', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-order-experience", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-order-experience", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-order-experience` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | Time period. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the industries and product categories a Douyin Xingtu creator has taken marketplace orders in, with the share of orders for each. It needs the creator's `oAuthorId` and an optional `period` of `DAY_30` or `DAY_90`.

### Use cases

- Check whether a creator has real order history in your product industry before you book them.
- Compare the order mix of two creators to see which one focuses on a narrower category.
- Spot creators who spread orders across many industries and may lack a clear niche.
- Add industry share data to a creator scorecard for brand campaign planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-order-experience" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `period` | string | No | Time period. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "order_experience_industries": [
    {
      "first_category": [
        {
          "name": "家庭护理品",
          "rate": 1
        }
      ],
      "industry": {
        "name": "日化",
        "rate": 0.6667
      },
      "second_category": []
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code / base_resp.status_message` | Request status. `0` with an empty message means the call succeeded. |
| `order_experience_industries[]` | One entry per industry the creator has taken orders in. Each entry holds the industry and its category breakdown. |
| `order_experience_industries[].industry.name` | Name of the industry, in Chinese, for example `日化`. |
| `order_experience_industries[].industry.rate` | Share of the creator's orders in this industry, as a decimal. In the sample, `0.6667` and `0.3333` add up to 1. |
| `order_experience_industries[].first_category[].name` | Name of a first-level category inside the industry, for example `个人护理`. |
| `order_experience_industries[].first_category[].rate` | Share of this first-level category within the industry, as a decimal. |
| `order_experience_industries[].second_category[].name / order_experience_industries[].second_category[].rate` | Name and share of a second-level category within the industry. The list can be empty when no finer breakdown exists. |

### Notes

- Set `period` to `DAY_30` or `DAY_90`. If you leave it out, it defaults to `DAY_30`.
- Category names are returned in Chinese. Map them to your own labels if you need another language.
- Get the `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For more creator detail, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-order-experience.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-order-experience.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-order-experience
