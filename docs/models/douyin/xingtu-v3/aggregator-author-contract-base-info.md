# Douyin Xingtu Creator Contract Base Info API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-contract-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) contract-related baseline information for a creator over a selectable 30- or 90-day period. Use it to review creator contract context during campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-contract-base-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-contract-base-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-contract-base-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-contract-base-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-contract-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns contract and order baseline data for one creator on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId` and takes an optional `range` of `DAY_30` or `DAY_90`.

### Use cases

- Check a creator's credit scores before you add them to a campaign shortlist.
- Compare how many orders a creator has taken with how many are still in progress.
- See which industries a creator's past orders and video views came from.
- Screen creators by positive rating rate and message reply rate.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-contract-base-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `range` | string | No | Time range. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "credit_score": "100",
  "industry_order_distribution": "[{\"key\":\"1933\",\"rate\":\"0.4286\",\"value\":\"3\"},{\"key\":\"1916\",\"rate\":\"0.1429\",\"value…",
  "industry_vv_distribution": "[{\"key\":\"1901\",\"rate\":\"0.5773\",\"value\":\"82816203\"},{\"key\":\"1933\",\"rate\":\"0.2658\"…",
  "max_process_order_cnt": "3",
  "message_reply_rate": "0",
  "modify_time": "1793685800",
  "new_credit_score": 72,
  "order_cnt": "7",
  "positive_rating_rate": "1",
  "process_order_cnt": "3"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `credit_score / new_credit_score` | Two credit score values for the creator. `credit_score` is returned as a string (`100` in this sample) and `new_credit_score` as a number (`72`). The response does not explain how they differ. |
| `order_cnt` | Number of orders for the creator, returned as a string. The sample value is `7`. |
| `process_order_cnt / max_process_order_cnt` | Count of orders in progress, and a second count with a maximum in its name. The sample values are `3` and `3`. |
| `positive_rating_rate` | Share of positive ratings, returned as a decimal string. `1` in this sample. |
| `message_reply_rate` | Reply rate for messages, returned as a decimal string. `0` in this sample. |
| `industry_order_distribution` | A JSON string holding a list of objects. Each object has an industry code in `key`, the order count in `value` and its share in `rate`. Parse the string before you use it. |
| `industry_vv_distribution` | A JSON string holding a list of objects. Each object has an industry code in `key`, a view count in `value` and its share in `rate`. Parse the string before you use it. |
| `modify_time` | Timestamp of the last update, as a Unix time in seconds in a string. |
| `base_resp.status_code / base_resp.status_message` | Request status. `0` with an empty message means the call succeeded. |

### Notes

- Most numbers come back as strings, so convert them to numbers in your code.
- Industry codes in `key` are numeric IDs such as `1933`. The response does not include industry names.
- Find a creator's `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For more creator order detail, call [Douyin Xingtu Creator Order Experience](/apis/douyin/xingtu-v3/aggregator-author-order-experience).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-contract-base-info.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-contract-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-contract-base-info
