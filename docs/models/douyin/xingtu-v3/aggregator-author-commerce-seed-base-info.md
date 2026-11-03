# Douyin Xingtu Commerce Seeding Base Info API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-commerce-seed-base-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) commerce-seeding baseline information for a creator over a selectable 30- or 90-day period. Use it to research creators for product-seeding campaigns.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-commerce-seed-base-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-commerce-seed-base-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-commerce-seed-base-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-commerce-seed-base-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-commerce-seed-base-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `range` | string |  | Time range. one of: `DAY_30`, `DAY_90`; default `"DAY_90"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns commerce-seeding baseline metrics for one Douyin creator on Xingtu, the Douyin Creator Marketplace. Send the creator's `oAuthorId` and optionally a `range` of `DAY_30` or `DAY_90`. The metrics cover post-view search behavior and A3 audience growth.

### Use cases

- Compare a creator's search-after-view rate against other creators before choosing who receives product samples.
- Check how a creator's own content performs against their wider seeding results using the `personal_` fields.
- Screen a shortlist of creators by their percentile rank for A3 audience growth.
- Compare the 30-day and 90-day windows to see whether a creator's search impact is changing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-commerce-seed-base-info" \
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
  "avg_a3_incr_cnt": "20,000 - 100,000",
  "avg_a3_incr_cnt_rank_percent": "0.9",
  "avg_search_after_view_cnt": ">15,000",
  "avg_search_after_view_cnt_rank_percent": "0.9",
  "avg_search_after_view_rate": "0.25% - 0.5%",
  "avg_search_after_view_rate_rank_percent": "0.5",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "modify_time": "1793656399",
  "personal_avg_search_after_view_cnt": "5,000 - 15,000",
  "personal_avg_search_after_view_cnt_rank_percent": "0.9",
  "personal_avg_search_after_view_rate": "0.02% - 0.1%",
  "personal_avg_search_after_view_rate_rank_percent": "0.75"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `avg_a3_incr_cnt` | Average A3 audience increase, returned as a range string such as `20,000 - 100,000`. |
| `avg_a3_incr_cnt_rank_percent` | Rank percentile for `avg_a3_incr_cnt`, returned as a string such as `0.9`. |
| `avg_search_after_view_cnt / avg_search_after_view_rate` | Average number of searches after viewing, and the rate of searches after viewing. Both are returned as range strings. |
| `avg_search_after_view_cnt_rank_percent / avg_search_after_view_rate_rank_percent` | Rank percentiles for the two `avg_search_after_view` fields. |
| `personal_avg_search_after_view_cnt / personal_avg_search_after_view_rate` | The same search-after-view measures with a `personal_` prefix. Compare them with the `avg_` fields to see how the creator's own content differs. |
| `personal_avg_search_after_view_cnt_rank_percent / personal_avg_search_after_view_rate_rank_percent` | Rank percentiles for the `personal_` search-after-view fields. |
| `search_word_ctr / personal_search_word_ctr` | Click-through rate on search words, returned as range strings such as `1% - 1.5%`. The `personal_` field is the creator's own value. |
| `modify_time` | Unix timestamp in seconds, returned as a string. It most likely shows when the record was last changed. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means success. |

### Notes

- Most metric values are strings holding ranges or bands, such as `>15,000` or `0.25% - 0.5%`, not single numbers. Parse them as text.
- `range` accepts `DAY_30` or `DAY_90` and defaults to `DAY_90`.
- Find an `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For conversion data on the same creator, call [Douyin Xingtu Conversion Analysis](/apis/douyin/xingtu-v3/data-sp-author-convert-ability).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-commerce-seed-base-info.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-commerce-seed-base-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-commerce-seed-base-info
