# Douyin XingTu KOL Audience API: pricing, parameters and code examples

`douyin/xingtu/kol-fans-portrait-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get the audience portrait of a Douyin KOL from XingTu: fan age, gender, region, device and interest distributions.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-fans-portrait-v1", "kolId": "7038603512770461703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-fans-portrait-v1', {'kolId': '7038603512770461703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-fans-portrait-v1", {
  "kolId": "7038603512770461703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-fans-portrait-v1", sandbase.Params{
	"kolId": "7038603512770461703",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-fans-portrait-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |
| `fansType` | string |  | Fans Type, supports the following parameters: _1: Fans Portrait - Default; _2: Fans Group Portrait; _5: Iron Fans Portrait  |

## Details

Returns the audience portrait of a Douyin creator from XingTu. It needs a XingTu `kolId` and returns fan distributions such as age, province and city tier.

### Use cases

- Check whether a creator's fan age range matches your target customers before booking a campaign.
- Compare the province split of several KOLs to pick one for a region-specific promotion.
- Review the city tier mix of a creator's fans to judge fit for a premium or mass-market product.
- Switch `fansType` to compare the general fan base with the fan group or loyal fan portrait.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-fans-portrait-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7038603512770461703"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |
| `fansType` | string | No | Fans Type, supports the following parameters: _1: Fans Portrait - Default; _2: Fans Group Portrait; _5: Iron Fans Portrait |

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
      "description": "18到23岁居多,占比34%",
      "distribution_list": [
        {
          "distribution_key": "50+",
          "distribution_value": "84120"
        }
      ],
      "image": [
        "18到23岁居多"
      ],
      "origin_type": 1,
      "type": 2,
      "type_display": "年龄分布"
    }
  ],
  "last_update_time": "1793691185"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One block per audience dimension. The response shows age, province and city tier blocks. |
| `distributions[].type_display` | Name of the dimension, for example `年龄分布` (age), `省份分布` (province) or `城市等级分布` (city tier). |
| `distributions[].description` | Short text summary of the block, such as which age group or provinces have the largest share and their percentages. |
| `distributions[].distribution_list[].distribution_key` | Label of one bucket, such as an age range like `24-30`, a province name or a city tier like `二线`. |
| `distributions[].distribution_list[].distribution_value` | Value for that bucket, returned as a string. It looks like a fan count, and the buckets can be compared with each other. |
| `distributions[].type / origin_type` | Numeric codes for the dimension. Use them to identify a block without matching on the display text. |
| `distributions[].image[]` | Short label text for the block, such as the top age group or top provinces. |
| `last_update_time` | Timestamp of the portrait as a string of Unix seconds. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message appears on success. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- `fansType` is optional. Use `_1` for the fans portrait (default), `_2` for the fan group portrait and `_5` for the iron fans portrait.
- The `description` and `distribution_key` texts, such as province names, come back in Chinese.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin XingTu KOL Profile](/apis/douyin/xingtu/kol-base-info-v1): Get the XingTu (Douyin creator marketplace) profile of a KOL: followers, location, category tags, online status and available collaboration types.
- [Douyin XingTu KOL Cost Metrics](/apis/douyin/xingtu/kol-cp-info-v1): Get expected campaign metrics for a Douyin KOL from XingTu: expected views, CPM and CPE estimates, and hot-video counts.
- [Douyin XingTu KOL Price](/apis/douyin/xingtu/kol-service-price-v1): Get the XingTu rate card of a Douyin KOL: price per collaboration type (sponsored video, live and more), settlement type and industry tags.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-fans-portrait-v1.json`](../../../../catalog/models/douyin/xingtu/kol-fans-portrait-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-fans-portrait-v1
