# Douyin Xingtu Content Keyword Analysis API: pricing, parameters and code examples

`douyin/xingtu-v3/gauthor-author-content-hot-keywords` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) content keyword analysis for a specified creator. Use it to identify recurring content themes during creator positioning research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/gauthor-author-content-hot-keywords", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/gauthor-author-content-hot-keywords', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/gauthor-author-content-hot-keywords", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/gauthor-author-content-hot-keywords", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/gauthor-author-content-hot-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the keywords found in a creator's content on Douyin Creator Marketplace (Xingtu), with a number for each keyword. It needs one input, the creator's `oAuthorId`.

### Use cases

- Check which themes a creator repeats before you pick them for a skincare or men's grooming campaign.
- Compare the `keyword_map` of several creators to find the ones whose content matches a product angle.
- Spot niche terms such as travel photography or lab testing that describe a creator's style.
- Screen out creators whose keywords do not match your brand category during positioning research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/gauthor-author-content-hot-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "keyword_item_distribution": {
    "干燥": 1,
    "控油": 1,
    "旅拍": 1,
    "油脂": 1,
    "男士": 1
  },
  "keyword_map": {
    "不干净": 2,
    "仪器": 2,
    "实验室": 2,
    "干燥": 2,
    "护肤": 2,
    "控油": 2,
    "旅拍": 2,
    "松弛": 2,
    "油脂": 3,
    "油脂分泌": 2,
    "泡沫": 2,
    "洗的干净": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword_map` | Object where each key is a content keyword in Chinese and each value is a number for that keyword. In this sample `油脂` and `男士` have 3, and most other keywords have 2. |
| `keyword_item_distribution` | Object with the same shape as `keyword_map`, but with fewer keywords. In this sample every value is 1, and all five keywords also appear in `keyword_map`. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. In this sample `status_code` is `0` and `status_message` is an empty string. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square) or from [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).
- Keywords are object keys, not list items. Read them by iterating over the keys of `keyword_map`.
- To see what the audience says instead of what the creator posts, call [Douyin Xingtu Comment Keyword Analysis](/apis/douyin/xingtu-v3/data-author-hot-comment-tokens).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/gauthor-author-content-hot-keywords.json`](../../../../catalog/models/douyin/xingtu-v3/gauthor-author-content-hot-keywords.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/gauthor-author-content-hot-keywords
