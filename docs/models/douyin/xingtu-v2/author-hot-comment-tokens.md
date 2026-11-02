# Douyin Xingtu Author Hot Comment Tokens (Xingtu V2) API: pricing, parameters and code examples

`douyin/xingtu-v2/author-hot-comment-tokens` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending comment tokens and keywords for a Douyin creator. Queries metrics by author ID with options to exclude emojis and adjust token count.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-hot-comment-tokens", "author_id": "7146074596666507300"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-hot-comment-tokens', {'author_id': '7146074596666507300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-hot-comment-tokens", {
  "author_id": "7146074596666507300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-hot-comment-tokens", sandbase.Params{
	"author_id": "7146074596666507300",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-hot-comment-tokens` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Number of hot tokens, default 10  |
| `author_id` | string | yes | Creator/author ID  |
| `without_emoji` | boolean |  | Whether to exclude emoji, default True  |

## Details

Retrieve top comment keywords and hot rates for a Douyin author by supplying `author_id`. You can configure the result size with `num` and filter out emojis using `without_emoji`.

### Use cases

- Analyze popular topics and discussion themes in an author's comment section.
- Assess audience sentiment and trending keywords across creator posts.
- Benchmark audience engagement topics across multiple Xingtu creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-hot-comment-tokens" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7146074596666507300"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Creator/author ID |
| `num` | integer | No | Number of hot tokens, default 10 |
| `without_emoji` | boolean | No | Whether to exclude emoji, default True |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "hot_comment_tokens": [
    {
      "hot_rate": 1335
    }
  ]
}
```

### Notes

- `num` defaults to 10 tokens.
- `without_emoji` defaults to true.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-hot-comment-tokens.json`](../../../../catalog/models/douyin/xingtu-v2/author-hot-comment-tokens.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-hot-comment-tokens
