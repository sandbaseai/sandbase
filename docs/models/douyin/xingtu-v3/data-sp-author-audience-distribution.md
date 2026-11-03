# Douyin Xingtu Audience Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-audience-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) audience-distribution data for a creator, content channel, and selected relationship stage. Use it to assess audience fit for campaign targeting.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-audience-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-audience-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-audience-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-audience-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-audience-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `linkType` | string |  | Link type filter. one of: `CONNECTED`, `AWARE`, `INTERESTED`, `LIKE`, `FOLLOW`; default `"CONNECTED"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns Douyin Xingtu audience-distribution data for one creator. It needs the creator's `oAuthorId`, and you can also pick a content channel with `platform` and a relationship stage with `linkType`.

### Use cases

- Check whether a creator's audience leans toward the interests your campaign targets, such as parenting or anime.
- Compare the city-tier mix of two creators before you pick one for a regional campaign.
- Match a creator's audience segments, such as small-town middle-aged or urban silver-age users, to your product's buyer profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-audience-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `linkType` | string | No | Link type filter. |
| `platform` | string | No | Platform type. |

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
      "description": "分布最多的3个兴趣随拍(61%),亲子(7%),二次元(7%)",
      "distribution_list": [
        {
          "distribution_key": "随拍",
          "distribution_value": "266514601"
        }
      ],
      "image": [
        "随拍,亲子,二次元居多"
      ],
      "origin_type": 6,
      "type": 64,
      "type_display": "兴趣分布"
    }
  ],
  "last_update_time": "1793691173"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One audience breakdown per entry. The response shows interest, eight-segment audience and city-tier breakdowns. |
| `distributions[].type_display` | Name of the breakdown, for example `兴趣分布` (interest) or `城市等级分布` (city tier). |
| `distributions[].description` | Short text summary of the top groups in this breakdown, with percentages. |
| `distributions[].distribution_list[].distribution_key` | Label of one group in the breakdown, such as an interest or a city tier. |
| `distributions[].distribution_list[].distribution_value` | Value for that group, returned as a string of digits. Convert it to a number before you compare groups. |
| `distributions[].image[]` | Short text label that names the leading group in this breakdown. |
| `distributions[].type / origin_type` | Numeric codes that identify the breakdown type. |
| `last_update_time` | Timestamp of the data as a string of digits. The value looks like a Unix timestamp in seconds. |
| `base_resp.status_code` | `0` in the sample response. `status_message` is empty. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `platform` accepts `SHORT_VIDEO` (default), `LIVE_STREAMING`, `PICTURE_TEXT` and `SHORT_DRAMA`. `linkType` accepts `CONNECTED` (default), `AWARE`, `INTERESTED`, `LIKE` and `FOLLOW`.
- For the follower side of the audience, call [Douyin Xingtu Follower Distribution](/apis/douyin/xingtu-v3/data-sp-author-fans-distribution).
- Text values such as `distribution_key` and `description` are in Chinese.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-audience-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-audience-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-audience-distribution
