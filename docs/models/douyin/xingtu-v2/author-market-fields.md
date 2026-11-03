# Douyin Author Market Fields API: pricing, parameters and code examples

`douyin/xingtu-v2/author-market-fields` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns all filter field options available within the Douyin creator marketplace. Accepts an optional marketplace scene identifier to tailor field choices.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-market-fields"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-market-fields', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-market-fields", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-market-fields", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-market-fields` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `market_scene` | integer |  | Market scene, 1=default default `1` |

## Details

Returns the filter options that the Douyin Xingtu creator marketplace offers for finding authors. The response lists ranges, category lists, audience labels and sort keys. It takes one optional input, `market_scene`, which defaults to `1`.

### Use cases

- Build a creator search form with the same fan count and price brackets that Xingtu offers.
- Map numeric filter values such as `watcher_age` codes to their labels before you send a search.
- List the industry, content and style tags a creator can be filtered by.
- Check which sort keys the marketplace supports for ranking authors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-market-fields" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `market_scene` | integer | No | Market scene, 1=default |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "成功"
  },
  "data": {
    "author_gpm": "[{\"author_gpm__ge\":150},{\"author_gpm__ge\":100,\"author_gpm__le\":150},{\"author_gpm…",
    "avg_sale_amount": "[{\"avg_sale_amount__ge\":100000000},{\"avg_sale_amount__ge\":50000000,\"avg_sale_amo…",
    "aweme_label": "[{\"value\":669,\"label\":\"财经\"},{\"value\":313,\"label\":\"其他\"},{\"value\":312,\"label\":\"户外\"…",
    "content_label": "[{\"label\":\"妆容妆造\",\"value\":\"妆容妆造\",\"children\":[{\"label\":\"淡妆教程\",\"value\":\"淡妆教程\"},{\"la…",
    "content_tag_v2": "[{\"second\":[{\"2\":\"美妆教程\"},{\"3\":\"妆容展示\"},{\"4\":\"护肤保养\"},{\"5\":\"美妆测评种草\"}],\"first\":{\"1\":…",
    "download_category_type": "[{\"second\":[{\"900401\":\"武侠仙侠\"},{\"900402\":\"都市\"},{\"900403\":\"魔幻\"},{\"900404\":\"西游\"},{\"…",
    "ecom_video_num_30d": "[{\"ecom_video_num_30d__ge\":20},{\"ecom_video_num_30d__ge\":10},{\"ecom_video_num_30…",
    "expected_cpm": "[{\"expected_cpm__le\":10},{\"expected_cpm__le\":20},{\"expected_cpm__le\":30},{\"expec…",
    "expected_play_num": "[{\"expected_play_num__ge\":10000000},{\"expected_play_num__le\":10000000,\"expected_…",
    "fans": "[{\"fans_min\":10000000},{\"fans_min\":5000000,\"fans_max\":10000000},{\"fans_min\":3000…",
    "fans_category": "[\"玩具乐器\",\"二手商品\",\"服饰内衣\",\"个护家清\",\"礼品文创\",\"智能家居\",\"生鲜\",\"美妆\",\"母婴宠物\",\"鲜花园艺\",\"本地生活\",\"食品饮料\"…",
    "fans_max": "50000000"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.fans / data.price / data.author_gpm` | Range brackets for follower count, price and author GPM. Each bracket uses min/max style keys such as `fans_min`, `fans_max`, `price_min` or `author_gpm__ge`. |
| `data.fans_max / data.price_max` | The highest follower count (`50000000`) and the highest price (`1000000`) in the filter ranges. |
| `data.order_by` | Sort options as arrays of key, label and a number. Examples are `follower`, `avg_play`, `ecom_video_num_30d` and `avg_sale_amount`. |
| `data.content_tag_v2 / data.tag` | Two-level content category tree. Each entry has a `first` category and a list of `second` categories, each mapped from an ID to a name. |
| `data.industry_tag_v2` | Two-level industry tree with numeric IDs for the `first` and `second` levels, such as `1901` for 3C及电器. |
| `data.watcher_age / data.watcher_city / data.watcher_device / data.watcher_gender` | Audience filter options. Each entry pairs a `value` code with a `label`, such as `一线城市居多` or `苹果居多`. |
| `data.live_watcher_age / data.live_watcher_city / data.live_watcher_device / data.live_watcher_gender` | Audience filter options for live streams, with their own `value` codes that differ from the `watcher_*` codes. |
| `data.main_category / data.fans_category` | Lists of e-commerce category names, such as 美妆 and 食品饮料. |
| `data.marketing_target` | Marketing goals as `key` and `value` pairs: 品牌传播 is `1` and 电商卖货 is `2`. |
| `data.location` | Object that maps each province or city name to a list of district names. |

### Notes

- Most values in `data` are JSON strings. Parse them again to get arrays or objects.
- Use the `value` codes from this response as filter values, and do not mix the `watcher_*` and `live_watcher_*` codes.
- To search authors with these filters, call [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- For another set of search options, see [Douyin Search Field Options](/apis/douyin/xingtu-v2/search-field-options).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-market-fields.json`](../../../../catalog/models/douyin/xingtu-v2/author-market-fields.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-market-fields
