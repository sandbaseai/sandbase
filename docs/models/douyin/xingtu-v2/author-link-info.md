# Douyin Xingtu Creator Link Indices API: pricing, parameters and code examples

`douyin/xingtu-v2/author-link-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Returns Xingtu link indices for a Douyin creator, including cooperation, CP, conversion, and shopping indices filtered by industry tag.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-link-info", "o_author_id": "7589271892177518598"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-link-info', {'o_author_id': '7589271892177518598'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-link-info", {
  "o_author_id": "7589271892177518598"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-link-info", sandbase.Params{
	"o_author_id": "7589271892177518598",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-link-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `industy_tag` | integer |  | Industry tag, 0=unlimited, default 0  |
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, default 1  |
| `platform_channel` | integer |  | Platform channel, default 1  |

## Details

Returns Xingtu link indices for one Douyin creator: cooperation, CP, conversion, shopping, spread and star. Each index comes with the creator's value, the average value, and the creator's rank. The only required input is the creator ID in `o_author_id`.

### Use cases

- Compare a creator's `link_shopping_index` with the average before choosing a creator for a product campaign.
- Check `link_convert_index` and its `link_relative_ratio` to see whether conversion is rising or falling.
- Screen a list of creators by `rank_percent` on the cooperation and CP indices.
- Re-run the call with `industy_tag` to see how a creator scores within one industry.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-link-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7589271892177518598"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `industy_tag` | integer | No | Industry tag, 0=unlimited, default 0 |
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
  "cooperate_index": {
    "avg_value": 75.55,
    "link_relative_ratio": 0,
    "rank": "138415",
    "rank_percent": 0.0632,
    "value": 75.71
  },
  "cp_index": {
    "avg_value": 64.1,
    "link_relative_ratio": 0,
    "rank": "84302",
    "rank_percent": 0.0385,
    "value": 67.06
  },
  "link_convert_index": {
    "avg_value": 55.24,
    "link_relative_ratio": -0.0902,
    "rank": "409688",
    "rank_percent": 0.1872,
    "value": 36.81
  },
  "link_shopping_index": {
    "avg_value": 53.3,
    "link_relative_ratio": 0.2556,
    "rank": "93389",
    "rank_percent": 0.0427,
    "value": 69.16
  },
  "link_spread_index": {
    "avg_value": 53.1,
    "link_relative_ratio": 0.1397,
    "rank": "144503",
    "rank_percent": 0.066,
    "value": 63.72
  },
  "link_star_index": {
    "avg_value": 56.19,
    "link_relative_ratio": 0.062,
    "rank": "149014",
    "rank_percent": 0.0681,
    "value": 62.49
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cooperate_index.value / cp_index.value` | The creator's score on the cooperation index and the CP index. |
| `link_convert_index.value / link_shopping_index.value` | The creator's score on the conversion index and the shopping index. |
| `link_spread_index.value / link_star_index.value` | The creator's score on the spread index and the star index. |
| `cooperate_index.avg_value / cp_index.avg_value` | The average score for the same index. Compare it with `value` to see if the creator is above or below average. The same field exists in each of the other indices. |
| `link_convert_index.link_relative_ratio` | Relative change for the conversion index. In the sample it is `-0.0902`, a negative change. The same field exists in each of the other indices. |
| `link_shopping_index.rank` | The creator's rank for the shopping index, returned as a string such as `93389`. The same field exists in each of the other indices. |
| `link_shopping_index.rank_percent` | The rank as a fraction, such as `0.0427`. A smaller number means a better position. The same field exists in each of the other indices. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message is the success result in the sample. |

### Notes

- Get the creator ID for `o_author_id` from a lookup such as [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) or [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- `industy_tag` defaults to `0`, which means no industry filter. The parameter name is spelled this way in the schema.
- `platform_source` and `platform_channel` both default to `1`.
- For more creator detail, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-link-info.json`](../../../../catalog/models/douyin/xingtu-v2/author-link-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-link-info
