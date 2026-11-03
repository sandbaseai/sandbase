# Douyin Xingtu Author Content Hot Keywords API: pricing, parameters and code examples

`douyin/xingtu-v2/author-content-hot-keywords` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending content keywords for a Douyin creator. Filter results by creator ID and specify an optional keyword type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-content-hot-keywords", "author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-content-hot-keywords', {'author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-content-hot-keywords", {
  "author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-content-hot-keywords", sandbase.Params{
	"author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-content-hot-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `author_id` | string | yes | Creator/author ID  |
| `keyword_type` | integer |  | Keyword type, default 0  |

## Details

Returns a set of content keywords for one Douyin creator on Xingtu, each paired with a number. It needs the creator's `author_id` and accepts an optional `keyword_type`.

### Use cases

- Check which product and topic words a creator uses, such as tablets, laptops or charging cables, before a brand pitch.
- Compare keyword sets from several creators to find ones whose content matches a product category.
- Build a keyword tag list for a creator profile in an influencer database.
- Spot sales-related words like `直播间` or `砍一刀` to see how a creator frames promotions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-content-hot-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7146074596666507300"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Creator/author ID |
| `keyword_type` | integer | No | Keyword type, default 0 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "keyword_item_distribution": {
    "平板": 1,
    "平板电脑": 1,
    "店铺": 1,
    "电脑": 1,
    "笔记本": 1
  },
  "keyword_map": {
    "一口价": 1,
    "保护壳": 2,
    "卡针": 2,
    "国货": 2,
    "小型": 1,
    "平板": 2,
    "平板电脑": 2,
    "店铺": 2,
    "快充线": 2,
    "数码科技": 2,
    "新款": 1,
    "民族品牌": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `keyword_map` | Object that maps each keyword to an integer, for example `平板电脑` or `快充线`. The key is the keyword text in Chinese. This is the main and longest keyword list. |
| `keyword_item_distribution` | Object with the same shape as `keyword_map`, with fewer keywords, for example `笔记本` or `店铺`. Each key is a keyword and each value is an integer. |
| `base_resp.status_code` | Status of the call. `0` means the call succeeded. |
| `base_resp.status_message` | Text message that goes with the status. It is an empty string in this response. |

### Notes

- The keywords are dynamic object keys, not a list. Read each key as the keyword text and each value as its number.
- `keyword_type` is optional and defaults to `0`. The example request omitted it.
- Get the creator ID from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator), or convert a Douyin ID with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id).
- For comment words instead of content words, call [Douyin Xingtu Author Hot Comment Tokens (Xingtu V2)](/apis/douyin/xingtu-v2/author-hot-comment-tokens).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-content-hot-keywords.json`](../../../../catalog/models/douyin/xingtu-v2/author-content-hot-keywords.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-content-hot-keywords
