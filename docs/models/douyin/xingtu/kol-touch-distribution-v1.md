# Douyin Xingtu KOL Touch Distribution API: pricing, parameters and code examples

`douyin/xingtu/kol-touch-distribution-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns touch distribution data for a Douyin Xingtu creator using their unique KOL identifier. Helps evaluate audience contact points and reach patterns.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-touch-distribution-v1", "kolId": "7048929565493690398"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-touch-distribution-v1', {'kolId': '7048929565493690398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-touch-distribution-v1", {
  "kolId": "7048929565493690398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-touch-distribution-v1", sandbase.Params{
	"kolId": "7048929565493690398",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-touch-distribution-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns touch distribution data for a Douyin Xingtu creator. You send the creator's `kolId` and get back a list of touch categories with a count for each one.

### Use cases

- Check which touch categories appear in a creator's video touch data before you pick the creator for a campaign.
- Compare the `cnt` values of touch categories across several creators.
- Add creator touch data to a Xingtu creator report next to profile and audience data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-touch-distribution-v1" \
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
  "video_touch": [
    {
      "distribution_data": {
        "cnt": 2,
        "id": "0",
        "name": "个人"
      },
      "second_distribution": []
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code / base_resp.status_message` | Status of the call. `status_code` is `0` in the sample response and `status_message` is empty. |
| `video_touch[]` | List of touch groups for the creator's videos. Each item holds one category and its sub-breakdown. |
| `video_touch[].distribution_data.name` | Name of the touch category. The sample value is `个人`. |
| `video_touch[].distribution_data.id` | ID of the touch category, returned as a string. The sample value is `0`. |
| `video_touch[].distribution_data.cnt` | Count for the touch category. The sample value is `2`. |
| `video_touch[].second_distribution[]` | Second-level breakdown of the category. It is an empty list in the sample response. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- `kolId` is a numeric string such as `7048929565493690398`.
- `second_distribution` can be an empty list, so check its length before you read items from it.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-touch-distribution-v1.json`](../../../../catalog/models/douyin/xingtu/kol-touch-distribution-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-touch-distribution-v1
