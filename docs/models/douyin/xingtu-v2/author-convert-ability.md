# Douyin Xingtu Author Conversion Ability API: pricing, parameters and code examples

`douyin/xingtu-v2/author-convert-ability` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns creator conversion ability metrics including GMV, clicks, and conversion rate ranges filtered by creator, time range, and industry.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-convert-ability", "o_author_id": "7029342444797820939"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-convert-ability', {'o_author_id': '7029342444797820939'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-convert-ability", {
  "o_author_id": "7029342444797820939"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-convert-ability", sandbase.Params{
	"o_author_id": "7029342444797820939",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-convert-ability` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `time_range` | integer |  | Time range tier, default 2  |
| `industry_id` | integer |  | Industry ID, 0=unlimited, default 0  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns conversion ability metrics for one Douyin Xingtu creator, such as sales amount, GPM, click and CPC ranges, plus video and product counts. It needs the creator ID in `o_author_id`. Optional filters set the industry, time range and platform.

### Use cases

- Check a creator's `gpm_range` and `avg_sales_amount_range` before shortlisting them for a sales campaign.
- Compare `component_click_cnt_range` and `component_click_rate_range` across several creators.
- Read `video_vv_median` to see the typical view count of a creator's videos.
- Check `rec_product_cnt` and `related_video_cnt` to see how many products and videos the metrics rest on.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-convert-ability" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7029342444797820939"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `industry_id` | integer | No | Industry ID, 0=unlimited, default 0 |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |
| `time_range` | integer | No | Time range tier, default 2 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "avg_sales_amount_range": "-",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "component_click_cnt_range": "-",
  "component_click_rate_range": "-",
  "gpm_range": "-",
  "rec_product_cnt": {
    "value": "0"
  },
  "rec_product_price_range": "-",
  "related_cpc_range": "-",
  "related_video_cnt": {
    "value": "1"
  },
  "video_vv_median": {
    "value": "4621348"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `avg_sales_amount_range` | Range for the creator's average sales amount. The value is `-` when no range is available, as in the sample. |
| `gpm_range` | Range for the creator's GPM. The value is `-` when no range is available. |
| `component_click_cnt_range / component_click_rate_range` | Ranges for the number of clicks and the click rate on the creator's video components. Both are `-` when empty. |
| `related_cpc_range` | Range for the related CPC value. The value is `-` when empty. |
| `rec_product_cnt.value` | Count of recommended products, returned as a string. The sample shows `0`. |
| `rec_product_price_range` | Price range of the recommended products. The value is `-` when empty. |
| `related_video_cnt.value` | Count of related videos, returned as a string. The sample shows `1`. |
| `video_vv_median.value` | Median video view count, returned as a string. The sample shows `4621348`. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `status_code` is `0` and `status_message` is empty in the sample. |

### Notes

- Many range fields return `-` when the creator has no data for the chosen filters. The count fields stay filled, so check them first.
- Numeric values in `rec_product_cnt`, `related_video_cnt` and `video_vv_median` come as strings inside a `value` key.
- Find the creator ID with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator) or [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).
- For the videos or products behind these metrics, call [Douyin Xingtu Creator Conversion Details](/apis/douyin/xingtu-v2/author-convert-videos-or-products).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-convert-ability.json`](../../../../catalog/models/douyin/xingtu-v2/author-convert-ability.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-convert-ability
