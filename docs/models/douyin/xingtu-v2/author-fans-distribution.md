# Douyin Xingtu Author Fan Distribution API: pricing, parameters and code examples

`douyin/xingtu-v2/author-fans-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns audience profile metrics for a Xingtu creator, including gender, age, geographic region, and interests based on creator ID.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-fans-distribution", "o_author_id": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-fans-distribution', {'o_author_id': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-fans-distribution", {
  "o_author_id": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-fans-distribution", sandbase.Params{
	"o_author_id": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-fans-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns the audience profile of a Xingtu creator on Douyin as a list of distributions, such as interests, gender and audience groups. It needs the creator ID in `o_author_id`.

### Use cases

- Check whether a creator's audience is mostly male or female before booking a campaign.
- Compare the top interest categories of a creator's fans with your product category.
- Screen creators by audience group, such as urban blue-collar or senior middle-class, for targeted ads.
- Store the distribution counts to compare several creators side by side.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-fans-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7029342444797820939"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
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
      "description": "分布最多的3个兴趣随拍(53%),体育(9%),社会时政(8%)",
      "distribution_list": [
        {
          "distribution_key": "随拍",
          "distribution_value": "3138780"
        }
      ],
      "image": [
        "随拍,体育,社会时政居多"
      ],
      "origin_type": 6,
      "type": 64,
      "type_display": "兴趣分布"
    }
  ],
  "last_update_time": "1793691160"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One audience breakdown per item. Each item has a type, a description and a list of counts. |
| `distributions[].type_display` | Name of the breakdown, for example `兴趣分布` (interests), `性别分布` (gender) or `八大人群分布` (eight audience groups). |
| `distributions[].type / origin_type` | Numeric codes that identify the breakdown type. Use them to pick a breakdown in code instead of matching the display name. |
| `distributions[].description` | Short summary text of the breakdown, such as which group is largest and its percentage share. |
| `distributions[].distribution_list[].distribution_key` | Label of one category in the breakdown, such as an interest name, `male` or `female`, or an audience group name. |
| `distributions[].distribution_list[].distribution_value` | Count for that category, returned as a string. Divide by the sum of the list to get a share. |
| `distributions[].image[]` | Short text label that restates the main finding of the breakdown. |
| `last_update_time` | Unix timestamp in seconds, returned as a string. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means success. |

### Notes

- Get the creator ID from a search call such as [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- If you only have a Douyin ID, convert it first with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).
- `platform_source` and `platform_channel` are optional integers and both default to `1`.
- For another view of the same audience, call [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-fans-distribution.json`](../../../../catalog/models/douyin/xingtu-v2/author-fans-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-fans-distribution
