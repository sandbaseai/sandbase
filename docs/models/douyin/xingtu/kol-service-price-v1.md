# Douyin XingTu KOL Price API: pricing, parameters and code examples

`douyin/xingtu/kol-service-price-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-service-price-v1", "kolId": "7038603512770461703", "platformChannel": "_1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-service-price-v1', {'kolId': '7038603512770461703', 'platformChannel': '_1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-service-price-v1", {
  "kolId": "7038603512770461703",
  "platformChannel": "_1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-service-price-v1", sandbase.Params{
	"kolId": "7038603512770461703",
	"platformChannel": "_1",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-service-price-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `platformChannel` | string | yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live  |

## Details

Returns the XingTu rate card of one Douyin KOL: a price for each collaboration type, the settlement type and the industry tags. It needs a XingTu `kolId` and a `platformChannel` that selects Douyin Video or Douyin Live.

### Use cases

- Estimate the cost of a sponsored video before you contact a creator.
- Compare the fixed price of a custom video with the per-play price of the same creator.
- Filter a shortlist of creators by `industry_tags` such as pet life or personal care appliances.
- Store the price list on a schedule to see when a creator changes rates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-service-price-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703", "platformChannel": "_1"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |
| `platformChannel` | string | Yes | Platform channel, supports the following parameters: _1: Douyin Video; _10: Douyin Live |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activity_info": [],
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "hot_list_ranks": [],
  "industry_tags": [
    "3C及电器-个护健康电器"
  ],
  "price_info": [
    {
      "author_id": "7038603512770461703",
      "desc": "植入视频",
      "do_fold": false,
      "enable": true,
      "end_time": "2145916800",
      "field": "long_video_price",
      "is_open": true,
      "need_price": true,
      "online_status": 1,
      "platform_source": 1,
      "price": 13800,
      "price_extra_info": {
        "sku_version": 1
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `price_info[].desc` | Name of the collaboration type, for example `植入视频` (embedded video) or `定制视频` (custom video). |
| `price_info[].price` | Price for that collaboration type. For fixed-price items this is the full price. For the natural-play item it is a small number, so read it together with `price_extra_info`. |
| `price_info[].settlement_desc / price_info[].settlement_type` | How the price is settled. `固定价格` (fixed price) goes with `settlement_type` `2`. `按自然播放量结算` (settled by natural play count) goes with `30`. |
| `price_info[].price_extra_info.floor_price / price_info[].price_extra_info.ceiling_price` | Lower and upper price limits, shown on the play-count settlement item. Values are strings. |
| `price_info[].field` | Name of the price field this row maps to, such as `long_video_price` or `price`. |
| `price_info[].video_type` | Numeric code of the video task type. The codes seen are `2`, `71` and `92`. |
| `price_info[].enable / price_info[].is_open / price_info[].online_status` | Flags that show whether the price item is active and open for orders. |
| `price_info[].start_time / price_info[].end_time` | Unix timestamps in seconds, sent as strings. They mark the period of the price item. |
| `industry_tags[]` | Industry categories of the creator, written as a main category and a subcategory joined by `-`. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- Set `platformChannel` to `_1` for Douyin Video or `_10` for Douyin Live.
- `activity_info` and `hot_list_ranks` came back as empty lists for this KOL.
- `base_resp.status_code` is `0` when the call succeeds.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/apis/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Audience](/apis/douyin/xingtu/kol-fans-portrait-v1): Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-service-price-v1.json`](../../../../catalog/models/douyin/xingtu/kol-service-price-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-service-price-v1
