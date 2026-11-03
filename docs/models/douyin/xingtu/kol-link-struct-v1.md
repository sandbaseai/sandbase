# Douyin Xingtu KOL Link Structure API: pricing, parameters and code examples

`douyin/xingtu/kol-link-struct-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns the link structure data for a Douyin Xingtu creator. Queries the platform structure by specifying the creator's KOL identifier.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-link-struct-v1", "kolId": "7048929565493690398"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-link-struct-v1', {'kolId': '7048929565493690398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-link-struct-v1", {
  "kolId": "7048929565493690398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-link-struct-v1", sandbase.Params{
	"kolId": "7048929565493690398",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-link-struct-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns the link structure for one Douyin Xingtu creator. The response has a link type label and five numbered entries with values, proportions and same-industry comparisons. The only input is the creator's `kolId`.

### Use cases

- Check the `author_link_type` label of a creator before adding them to a Xingtu shortlist.
- Compare the `proportion` split across entries 1 to 4 for different creators.
- Compare a creator's `same_industry_median` numbers with the industry medians for the same entries.
- Pull `rank_percent` for entry 5 to sort a list of candidate creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-link-struct-v1" \
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
  "author_link_type": "种草",
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "link_struct": {
    "1": {
      "proportion": 0.3,
      "same_industry_median": 7393,
      "value": 3
    },
    "2": {
      "proportion": 0.2,
      "same_industry_median": 1913,
      "value": 2
    },
    "3": {
      "proportion": 0.5,
      "same_industry_median": 653,
      "value": 5
    },
    "4": {
      "proportion": 0,
      "same_industry_median": 0,
      "value": 0
    },
    "5": {
      "rank_percent": 0.9634,
      "relative_ratio": -0.2308,
      "value": 10
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `author_link_type` | Text label for the creator's link type. The sample value is the Chinese label `种草`. |
| `link_struct.1.value / link_struct.2.value / link_struct.3.value / link_struct.4.value` | Number for each of entries 1 to 4. In the sample they are 3, 2, 5 and 0. |
| `link_struct.1.proportion / link_struct.2.proportion / link_struct.3.proportion / link_struct.4.proportion` | Share of each entry as a decimal. In the sample they are 0.3, 0.2, 0.5 and 0, and they add up to 1. |
| `link_struct.1.same_industry_median / link_struct.2.same_industry_median / link_struct.3.same_industry_median / link_struct.4.same_industry_median` | Median for creators in the same industry, for each entry. Use it as a benchmark next to the creator's own numbers. |
| `link_struct.5.value` | Number for entry 5. In the sample it is 10, which equals the sum of the values in entries 1 to 4. |
| `link_struct.5.rank_percent` | Rank percentile for entry 5 as a decimal. The sample value is `0.9634`. |
| `link_struct.5.relative_ratio` | Relative ratio for entry 5. The value can be negative, as in the sample `-0.2308`. |
| `base_resp.status_code / base_resp.status_message` | Status of the request. A `status_code` of `0` with an empty `status_message` appears in the sample response. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- `kolId` is a numeric string, for example `7048929565493690398`.
- The keys inside `link_struct` are the strings `1` to `5`. Entries 1 to 4 share one field set, and entry 5 uses `rank_percent` and `relative_ratio` instead.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-link-struct-v1.json`](../../../../catalog/models/douyin/xingtu/kol-link-struct-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-link-struct-v1
