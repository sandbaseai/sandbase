# Douyin KOL Xingtu Index API: pricing, parameters and code examples

`douyin/xingtu/kol-xingtu-index-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns Xingtu index metrics for a specific Douyin creator based on their KOL identifier. Useful for tracking creator performance scores.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-xingtu-index-v1", "kolId": "7048929565493690398"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-xingtu-index-v1', {'kolId': '7048929565493690398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-xingtu-index-v1", {
  "kolId": "7048929565493690398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-xingtu-index-v1", sandbase.Params{
	"kolId": "7048929565493690398",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-xingtu-index-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns six Xingtu index scores for one Douyin creator. Each score comes with an average, a rank, a rank percentage and a link relative ratio. The only input is the creator's `kolId`.

### Use cases

- Compare a creator's `link_shopping_index` with its `avg_value` to see whether the creator sells better or worse than the average.
- Screen a list of creators by `cooperate_index.value` before you contact them for a campaign.
- Rank candidate creators by `rank_percent` on the conversion and spread indexes.
- Check `link_relative_ratio` on each index to see how the score moved against the previous period.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-xingtu-index-v1" \
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
    "rank": "155915",
    "rank_percent": 0.0712,
    "value": 65.24
  },
  "link_convert_index": {
    "avg_value": 55.24,
    "link_relative_ratio": 0.054,
    "rank": "441129",
    "rank_percent": 0.2015,
    "value": 33.6
  },
  "link_shopping_index": {
    "avg_value": 53.3,
    "link_relative_ratio": 0.2819,
    "rank": "352635",
    "rank_percent": 0.1611,
    "value": 42.38
  },
  "link_spread_index": {
    "avg_value": 53.1,
    "link_relative_ratio": 0.1457,
    "rank": "412077",
    "rank_percent": 0.1883,
    "value": 36.26
  },
  "link_star_index": {
    "avg_value": 56.19,
    "link_relative_ratio": 0.0659,
    "rank": "361959",
    "rank_percent": 0.1654,
    "value": 50.62
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cooperate_index / cp_index` | Scores for the creator's cooperation index and CP index. `value` is the creator's score and `avg_value` is the average score for comparison. |
| `link_convert_index` | Conversion index. A higher `value` means a higher score on this index. |
| `link_shopping_index` | Shopping index for the creator. Compare `value` with `avg_value` to see how it sits against the average. |
| `link_spread_index` | Spread index for the creator, with the same sub-fields as the other indexes. |
| `link_star_index` | Star index for the creator, with the same sub-fields as the other indexes. |
| `cooperate_index.value / cp_index.value / link_convert_index.value` | The creator's current score on each index, as a number with decimals. |
| `cooperate_index.avg_value / cp_index.avg_value / link_star_index.avg_value` | The average score shown next to the creator's own score for that index. |
| `cooperate_index.rank / cp_index.rank / link_spread_index.rank` | The creator's rank on that index. The value is returned as a string. |
| `cooperate_index.rank_percent / link_convert_index.rank_percent` | The rank as a fraction between 0 and 1. For example, `0.0674` matches a rank of `147420`, so a smaller number means a higher position. |
| `cooperate_index.link_relative_ratio / link_shopping_index.link_relative_ratio` | The link relative ratio for the index. It is `0` when no change is reported. |
| `base_resp.status_code` | Status of the request. `0` with an empty `status_message` means the call succeeded. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- Pass `kolId` as a string, for example `7048929565493690398`.
- `rank` is a string, while `value`, `avg_value` and `rank_percent` are numbers.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-xingtu-index-v1.json`](../../../../catalog/models/douyin/xingtu/kol-xingtu-index-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-xingtu-index-v1
