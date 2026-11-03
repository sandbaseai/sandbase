# Douyin Xingtu KOL Audience Portrait (V1) API: pricing, parameters and code examples

`douyin/xingtu/kol-audience-portrait-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns audience demographic and portrait insights for a Douyin Xingtu creator. Requires a creator identifier to retrieve detailed follower profile data.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-audience-portrait-v1", "kolId": "6677767167234015243"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-audience-portrait-v1', {'kolId': '6677767167234015243'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-audience-portrait-v1", {
  "kolId": "6677767167234015243"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-audience-portrait-v1", sandbase.Params{
	"kolId": "6677767167234015243",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-audience-portrait-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns audience portrait data for a Douyin Xingtu creator, grouped into distributions such as interests, age and city tier. It needs the creator's Xingtu `kolId`.

### Use cases

- Check which interest categories a creator's audience follows before choosing a campaign theme.
- Compare the age spread of a creator's audience with a target customer group.
- Check the city tier mix of an audience to judge fit for a regional product launch.
- Store the portrait with `last_update_time` to track how a creator's audience profile looks over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-audience-portrait-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7048929565493690398"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |

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
      "description": "分布最多的3个兴趣随拍(30%),亲子(10%),明星(10%)",
      "distribution_list": [
        {
          "distribution_key": "随拍",
          "distribution_value": "3"
        }
      ],
      "image": [
        "随拍,亲子,明星居多"
      ],
      "origin_type": 6,
      "type": 64,
      "type_display": "兴趣分布"
    }
  ],
  "last_update_time": "1793691190"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One block per portrait dimension. Each block holds a text summary, a list of buckets and a dimension label. |
| `distributions[].type_display` | Name of the dimension, for example `兴趣分布` (interest), `年龄分布` (age) and `城市等级分布` (city tier). |
| `distributions[].description` | Short text summary of the dimension, such as the top interests with percentages. The text is in Chinese. |
| `distributions[].distribution_list[].distribution_key` | Label of one bucket, such as an interest name, an age range like `31-40`, or a city tier like `三线`. |
| `distributions[].distribution_list[].distribution_value` | Value for that bucket, returned as a string. Compare it only with other buckets in the same list. |
| `distributions[].image[]` | Short text caption for the dimension, such as `18到23岁居多`. |
| `distributions[].type / distributions[].origin_type` | Numeric codes for the dimension. Use `type` or `type_display` to pick the block you need. |
| `last_update_time` | Unix timestamp in seconds, returned as a string, that marks the last update of this portrait. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means it succeeded. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- The `description` text can cover buckets that are not in `distribution_list`. In the sample, the age description says 18 to 23 is the largest group, but the list shows other ranges.
- Match blocks by `type_display` or `type`, not by array position.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-audience-portrait-v1.json`](../../../../catalog/models/douyin/xingtu/kol-audience-portrait-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-audience-portrait-v1
