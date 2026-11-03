# Douyin Xingtu Live Statistics API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-live-statistics` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) live-stream statistics for a creator, with live-room, period, marketplace-order, and flow filters. Use it to compare live-streaming creators for campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-live-statistics", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-live-statistics', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-live-statistics", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-live-statistics", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-live-statistics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | Live data time period. one of: `DAY_30`, `DAY_90` |
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE` |
| `liveType` | string |  | Live room type filter. one of: `ALL`, `GAME`, `ECOMMERCE`, `OTHER` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyStarOrder` | boolean |  | Whether to include only Xingtu marketplace orders. default `false` |

## Details

Returns live-stream statistics for one creator on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId` and accepts optional filters for live room type, time period, marketplace orders, and flow type.

### Use cases

- Compare average viewers and peak viewers across live-streaming creators before a campaign.
- Check how engaged a creator's live audience is using the like, comment, and interact rates.
- Screen creators by how many live sessions they ran in the chosen period.
- Check whether a creator sells products in live rooms before you plan an e-commerce campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-live-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `flowType` | string | No | Flow type filter. |
| `liveType` | string | No | Live room type filter. |
| `onlyStarOrder` | boolean | No | Whether to include only Xingtu marketplace orders. |
| `period` | string | No | Live data time period. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "live_aa_statistics": {},
  "live_convert_statistics": {},
  "live_ecom_statistics": {
    "avg_ecom_product_price_range": "0",
    "avg_gmv_range": "0",
    "avg_gpm_range": "0",
    "ecom_live_product_num": "0"
  },
  "live_room_statistics": {
    "acu": "7054",
    "acu_precede_percent": 0.07668231611893583,
    "comment_rate_avg": 0.0062,
    "fans_watch_rate": 0.5692,
    "finish_order_cnt": "1",
    "follow_ucnt_avg": "426",
    "in_process_order_cnt": "0",
    "interact_rate_avg": 0.1518,
    "like_rate_avg": 0.0055,
    "pcu": "49271",
    "room_cnt": "38",
    "watch_cnt_avg": "358128"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `live_room_statistics.room_cnt` | Number of live rooms counted in the statistics. |
| `live_room_statistics.acu / live_room_statistics.pcu` | `acu` is the average concurrent viewer count. `pcu` is the peak concurrent viewer count. |
| `live_room_statistics.acu_precede_percent` | Share value that shows how this creator's `acu` ranks against others. It is a ratio between 0 and 1. |
| `live_room_statistics.watch_cnt_avg / live_room_statistics.watch_ucnt_avg` | Average watch count and average unique watcher count per live room. |
| `live_room_statistics.watch_duration_avg` | Average watch duration per viewer. The unit is not stated in the response. |
| `live_room_statistics.like_rate_avg / live_room_statistics.comment_rate_avg / live_room_statistics.interact_rate_avg` | Average like, comment, and overall interaction rates, given as ratios. |
| `live_room_statistics.fans_watch_rate` | Ratio of viewers who are followers of the creator. |
| `live_room_statistics.follow_ucnt_avg` | Average number of new followers gained per live room. |
| `live_room_statistics.finish_order_cnt / live_room_statistics.in_process_order_cnt` | Count of finished marketplace orders and count of orders still in progress. |
| `live_ecom_statistics.ecom_live_product_num` | Number of products sold in e-commerce live rooms. `avg_gmv_range`, `avg_gpm_range` and `avg_ecom_product_price_range` sit beside it in the same object. |

### Notes

- Most numbers in `live_room_statistics` arrive as strings, such as `"acu": "7054"`. Rates arrive as numbers.
- `live_aa_statistics` and `live_convert_statistics` came back as empty objects for this creator. `live_ecom_statistics` values were `"0"`, so this creator had no e-commerce live data.
- Use [Douyin Xingtu Live Watch Distribution](/apis/douyin/xingtu-v3/aggregator-author-live-watch-distribution) to see who watches this creator's lives, and [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info) for profile details.
- Find an `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-live-statistics.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-live-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-live-statistics
