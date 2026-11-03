# Douyin Xingtu Creator Link Metrics API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-link-info` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) creator-link metrics for a specified creator, content channel, and industry category. Use it to review creator link information in an industry context.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-link-info", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-link-info', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-link-info", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-link-info", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-link-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `industryTag` | string |  | Industry tag. one of: `ALL`, `ELECTRONICS_AND_APPLIANCES`, `SHOPPING`, `FOOD_AND_BEVERAGE`, `CLOTHING_AND_ACCESSORIES`, `HEALTHCARE_AND_MEDICAL`, `MEDICAL_INSTITUTIONS`, `HOME_AND_BUILDING_MATERIALS`, `LOCAL_SERVICES`, `BUSINESS_SERVICES`, `CULTURE_SPORTS_ENTERTAINMENT`, `BEAUTY_SERVICES` …; default `"ALL"` |

## Details

This API returns six link index scores for a Douyin Xingtu creator. Each score comes with the average value, rank, and change against the previous period. It needs the creator's `oAuthorId`, and you can narrow the result with `platform` and `industryTag`.

### Use cases

- Compare a creator's shopping and conversion scores against the average before you book a sponsored post.
- Shortlist creators in one industry by sorting on `rank_percent` for a given index.
- Check whether a creator's link scores are rising or falling using `link_relative_ratio`.
- Check cost performance and cooperation scores for a creator before a budget review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-link-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `industryTag` | string | No | Industry tag. |
| `platform` | string | No | Platform type. |

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
    "rank": "147420",
    "rank_percent": 0.0674,
    "value": 75.63
  },
  "cp_index": {
    "avg_value": 64.1,
    "link_relative_ratio": 0,
    "rank": "51080",
    "rank_percent": 0.0233,
    "value": 68.6
  },
  "link_convert_index": {
    "avg_value": 55.24,
    "link_relative_ratio": -0.0275,
    "rank": "2093",
    "rank_percent": 0.001,
    "value": 95.91
  },
  "link_shopping_index": {
    "avg_value": 53.3,
    "link_relative_ratio": -0.0028,
    "rank": "288",
    "rank_percent": 0.0001,
    "value": 98.66
  },
  "link_spread_index": {
    "avg_value": 53.1,
    "link_relative_ratio": -0.0053,
    "rank": "600",
    "rank_percent": 0.0003,
    "value": 98.09
  },
  "link_star_index": {
    "avg_value": 56.19,
    "link_relative_ratio": -0.0079,
    "rank": "175",
    "rank_percent": 0.0001,
    "value": 87.38
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `link_shopping_index.value` | The creator's score for the shopping link index. Compare it with `avg_value` to see how far above or below average the creator sits. |
| `link_convert_index.value` | The creator's score for the conversion link index. |
| `link_spread_index.value / link_star_index.value` | The creator's scores for the spread link index and the star link index. |
| `cooperate_index.value / cp_index.value` | The creator's cooperation index score and cp index score. |
| `link_shopping_index.avg_value / link_convert_index.avg_value / link_spread_index.avg_value / link_star_index.avg_value` | The average score for the same index. Use it as a baseline for the creator's `value`. |
| `link_shopping_index.rank / link_convert_index.rank / cp_index.rank` | The creator's rank for that index, returned as a string. A smaller number means a better position. |
| `link_shopping_index.rank_percent / link_convert_index.rank_percent / cp_index.rank_percent` | The creator's rank as a fraction of the ranked group. For example, `0.0001` is about 0.01%. |
| `link_convert_index.link_relative_ratio / link_shopping_index.link_relative_ratio` | The relative change in the index compared with the previous period. A negative number means the index fell. |
| `base_resp.status_code` | Status of the call. `0` means success, and `status_message` is empty in that case. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`. It defaults to `SHORT_VIDEO`.
- `industryTag` defaults to `ALL`. Set a value such as `AUTOMOTIVE` or `BEAUTY_AND_COSMETICS` to read the scores for one industry.
- For the creator's cost performance details, call [Douyin Xingtu Cost Performance Analysis](/apis/douyin/xingtu-v3/data-sp-author-cp-info).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-link-info.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-link-info.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-link-info
