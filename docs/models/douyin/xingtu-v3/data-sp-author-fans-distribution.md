# Douyin Xingtu Follower Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-fans-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) follower or loyal-follower distribution data for a specified creator. Use it to compare audience-profile distributions during creator selection.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-fans-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-fans-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-fans-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-fans-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-fans-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |
| `authorType` | string |  | Author type filter. one of: `FAN`, `DIE_HARD_FAN`; default `"FAN"` |

## Details

This API returns follower distribution data for one creator on Douyin Creator Marketplace (Xingtu). It needs the creator's `oAuthorId`, and an optional `authorType` switches between all followers and loyal followers.

### Use cases

- Compare the province and city spread of two creators' followers before picking one for a regional campaign.
- Check which phone brands a creator's audience uses to judge device mix and spending level.
- Screen loyal followers (`DIE_HARD_FAN`) against all followers to see how the core audience differs.
- Pull the platform's own audience summary text to paste into a creator shortlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-fans-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `authorType` | string | No | Author type filter. |

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
      "description": "分布最多的3个省份广东(11%),江苏(7%),山东(6%)",
      "distribution_list": [
        {
          "distribution_key": "广西",
          "distribution_value": "4619384"
        }
      ],
      "image": [
        "广东,江苏,山东居多"
      ],
      "origin_type": 2,
      "type": 4,
      "type_display": "省份分布"
    }
  ],
  "last_update_time": "1793691175"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One block per audience dimension. This response includes province, city and device brand blocks. |
| `distributions[].type_display` | Name of the dimension, for example `省份分布` (province), `城市分布` (city) or `设备品牌分布` (device brand). |
| `distributions[].description` | Short summary text written by the platform. It names the top entries and their percentages, for example the top 3 provinces. |
| `distributions[].distribution_list[].distribution_key` | Label of one bucket in the dimension, such as a province, city or phone brand. |
| `distributions[].distribution_list[].distribution_value` | Value for that bucket, returned as a string. It looks like a count, not a percentage, so compare it with the other buckets in the same block. |
| `distributions[].image[]` | Very short tag text that sums up the block, for example `北京居多`. |
| `distributions[].type / origin_type` | Numeric codes for the dimension. Use them to match the same dimension across calls. |
| `last_update_time` | Unix timestamp in seconds, returned as a string. |
| `base_resp.status_code / base_resp.status_message` | Call status from the platform. `0` with an empty message means success. |

### Notes

- Pass `authorType` as `FAN` (default) or `DIE_HARD_FAN` to switch between followers and loyal followers.
- Text in `description`, `image` and `type_display` is in Chinese.
- For the wider audience view, call [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution).
- To see follower growth over time, call [Douyin Xingtu Follower Growth Trend](/apis/douyin/xingtu-v3/data-sp-author-daily-fans).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-fans-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-fans-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-fans-distribution
