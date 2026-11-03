# Douyin Xingtu Live Watch Distribution API: pricing, parameters and code examples

`douyin/xingtu-v3/aggregator-author-live-watch-distribution` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) live audience or follower watch-distribution data for a creator and selected live-room type. Use it to assess live audience fit for a campaign.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/aggregator-author-live-watch-distribution", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/aggregator-author-live-watch-distribution', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/aggregator-author-live-watch-distribution", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/aggregator-author-live-watch-distribution", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/aggregator-author-live-watch-distribution` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `liveType` | string |  | Live room type filter. one of: `ALL`, `GAME`, `ECOMMERCE`, `OTHER` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `liveCrowdType` | string |  | Live audience profile type. one of: `AUDIENCE`, `FANS` |

## Details

Returns watch-distribution breakdowns for a creator's Douyin live streams on Xingtu, such as city, city tier and audience segment. It needs the creator's `oAuthorId`. You can choose the audience type (`liveCrowdType`) and the live room type (`liveType`).

### Use cases

- Check which cities and city tiers a creator's live viewers come from before booking a regional campaign.
- Compare the audience segments of a creator's live viewers with a brand's target customer group.
- Run the call once with `AUDIENCE` and once with `FANS` to see how live viewers differ from followers.
- Compare `ECOMMERCE` and `GAME` live rooms for the same creator to pick the right live format.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/aggregator-author-live-watch-distribution" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `liveCrowdType` | string | No | Live audience profile type. |
| `liveType` | string | No | Live room type filter. |

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
      "description": "分布最多的1个城市北京(4%)",
      "distribution_list": [
        {
          "distribution_key": "北京",
          "distribution_value": "2203379"
        }
      ],
      "image": [
        "北京居多"
      ],
      "origin_type": 8,
      "type": 256,
      "type_display": "城市分布"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `distributions[]` | One entry per breakdown type. Each entry holds a summary text and a list of values. |
| `distributions[].type_display` | Name of the breakdown, such as 城市分布 (city distribution), 八大人群分布 (eight-segment audience distribution) or 城市等级分布 (city tier distribution). |
| `distributions[].description` | Short text that names the top group and its share, for example 新锐白领居多,占比20%. |
| `distributions[].distribution_list[].distribution_key` | Label of one group in the breakdown, such as a city name, a city tier or an audience segment. |
| `distributions[].distribution_list[].distribution_value` | Value for that group, returned as a string of digits. Convert it to a number before you sort or add values. |
| `distributions[].image[]` | Short label text for the top group, such as 北京居多. |
| `distributions[].type / origin_type` | Numeric codes for the breakdown type. Use `type` to match the same breakdown across calls. |
| `base_resp.status_code / base_resp.status_message` | Status of the request. `0` with an empty message appears in this response. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `liveCrowdType` accepts `AUDIENCE` or `FANS`. `liveType` accepts `ALL`, `GAME`, `ECOMMERCE` or `OTHER`. Both are optional.
- For non-live follower data, call [Douyin Xingtu Follower Distribution](/apis/douyin/xingtu-v3/data-sp-author-fans-distribution).
- For live performance numbers, call [Douyin Xingtu Live Statistics](/apis/douyin/xingtu-v3/aggregator-author-live-statistics).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/aggregator-author-live-watch-distribution.json`](../../../../catalog/models/douyin/xingtu-v3/aggregator-author-live-watch-distribution.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/aggregator-author-live-watch-distribution
