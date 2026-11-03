# Douyin Xingtu Marketing Metrics API: pricing, parameters and code examples

`douyin/xingtu-v3/author-author-marketing-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) marketing information for a specified creator and content channel. Use it to compare creator commercial offerings during campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/author-author-marketing-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/author-author-marketing-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/author-author-marketing-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/author-author-marketing-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/author-author-marketing-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the commercial offerings of one Douyin Xingtu creator for one content channel. The response lists price items, industry tags, and activity and ranking lists. It needs the creator's `oAuthorId`, and `platform` is optional.

### Use cases

- Compare the fixed prices a creator charges for different video formats before booking a campaign.
- Check which price items are open and active for a creator.
- Screen creators by their `industry_tags` to match them to a brand category.
- Check whether a creator has a discount or platform activity attached to a price item.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/author-author-marketing-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

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
    "美妆-面部洗护"
  ],
  "price_info": [
    {
      "activity_info": [],
      "author_id": "6870161898013196295",
      "desc": "短直明星种草",
      "do_fold": false,
      "enable": true,
      "end_time": "2145916800",
      "field": "price",
      "has_discount": false,
      "is_open": true,
      "need_price": true,
      "online_status": 1,
      "origin_price": 50000
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `price_info[]` | One row per priced offering the creator sells on the chosen channel. Each row has its own price, dates, and settlement terms. |
| `price_info[].desc` | Name of the offering, such as `短直明星种草` or `视频(定金模式)`. |
| `price_info[].price / price_info[].origin_price` | Current price and original price of the offering. In this response both are `50000`. The response does not state the currency or unit. |
| `price_info[].has_discount` | Shows whether the offering carries a discount. |
| `price_info[].enable / price_info[].is_open` | Show whether the offering is enabled and open for orders. |
| `price_info[].settlement_desc / price_info[].settlement_type` | Settlement method as text and as a code. `固定价格` means fixed price and goes with `settlement_type` `2`. |
| `price_info[].start_time / price_info[].end_time` | Start and end of the offering's validity period, as Unix timestamps in seconds stored as strings. |
| `price_info[].video_type` | Numeric code for the video format of the offering. The response does not explain the code values. |
| `industry_tags` | List of industry categories the creator is tagged with, written as category and subcategory such as `美妆-面部洗护`. |
| `activity_info / hot_list_ranks` | Lists of platform activities and hot list rankings for the creator. Both are empty in this response. |

### Notes

- Pass `oAuthorId` as a string. It is a long numeric ID, and the same value appears as `price_info[].author_id`.
- Set `platform` to `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`. The default is `SHORT_VIDEO`.
- To find an `oAuthorId` by name, use [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- For the creator's profile data, call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/author-author-marketing-info.json`](../../../../catalog/models/douyin/xingtu-v3/author-author-marketing-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/author-author-marketing-info
