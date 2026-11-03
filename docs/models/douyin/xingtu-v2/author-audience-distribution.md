# Douyin Xingtu Author Audience Distribution API: pricing, parameters and code examples

`douyin/xingtu-v2/author-audience-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel options.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-audience-distribution", "link_type": 5, "o_author_id": "7029342444797820939"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-audience-distribution', {'link_type': 5, 'o_author_id': '7029342444797820939'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-audience-distribution", {
  "link_type": 5,
  "o_author_id": "7029342444797820939"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-audience-distribution", sandbase.Params{
	"link_type": 5,
	"o_author_id": "7029342444797820939",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-audience-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `link_type` |  | yes | Link type, optional  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns audience profile distributions for a Douyin Xingtu creator, such as city tier, age group and phone brand. It needs the creator ID in `o_author_id` and a `link_type` value.

### Use cases

- Check whether a creator's audience skews to the age group a brand wants to reach.
- Compare city tier splits across several candidate creators before a campaign.
- Filter creators by phone brand mix when the product targets specific device owners.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-audience-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7029342444797820939", "link_type": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `link_type` | string | Yes | Link type, optional |
| `o_author_id` | string | Yes | Creator ID |
| `platform_channel` | integer | No | Platform channel, default 1 |
| `platform_source` | integer | No | Platform source, default 1 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "distributions": [
    {
      "description": "一线居多,占比29%",
      "distribution_list": [
        {
          "distribution_key": "五线",
          "distribution_value": "12004884"
        }
      ],
      "image": [
        "一线居多"
      ],
      "origin_type": 5,
      "type": 32,
      "type_display": "城市等级分布"
    }
  ],
  "last_update_time": "1793691158"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One audience dimension per item, such as city tier, age or device brand. |
| `distributions[].type_display` | Name of the dimension, for example `城市等级分布` (city tier), `年龄分布` (age) or `设备品牌分布` (device brand). |
| `distributions[].description` | Short text summary of the dominant group in that dimension, including its share as a percentage. |
| `distributions[].distribution_list[].distribution_key` | Label of one group inside the dimension, such as `二线`, `18-23` or `oppo`. |
| `distributions[].distribution_list[].distribution_value` | Numeric value for that group, returned as a string. Compare values within the same dimension to rank groups. |
| `distributions[].image[]` | Short label text for the dominant group in the dimension. |
| `distributions[].type / origin_type` | Numeric codes for the dimension. Use them to match the same dimension across calls. |
| `last_update_time` | Timestamp of the last update, returned as a string in Unix seconds format. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means success. |

### Notes

- Get the creator ID for `o_author_id` from a search call such as [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- `platform_source` and `platform_channel` are optional integers and both default to `1`.
- For follower-based breakdowns of the same creator, see [Douyin Xingtu Author Fan Distribution](/apis/douyin/xingtu-v2/author-fans-distribution).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.
- [Douyin Xingtu Author Content Hot Keywords](/apis/douyin/xingtu-v2/author-content-hot-keywords): Returns trending content keywords for a Douyin creator.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-audience-distribution.json`](../../../../catalog/models/douyin/xingtu-v2/author-audience-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-audience-distribution
