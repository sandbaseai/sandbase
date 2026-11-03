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

Returns the most frequent comment tokens (keywords) found in a Douyin creator's comment sections on Xingtu, each with a `hot_rate` score. It needs a Xingtu `author_id`. You can set the number of tokens with `num` and drop emojis with `without_emoji`.

### Use cases

- Find the words and topics that audiences repeat most in a creator's comments.
- Spot recurring complaints or product mentions in a creator's comment section before a brand deal.
- Compare the top comment tokens of several creators to see which audiences talk about similar topics.
- Feed the token list into a dashboard or word cloud for a creator report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-hot-comment-tokens" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "7146074596666507300"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `author_id` | string | Yes | Creator/author ID |
| `num` | integer | No | Number of hot tokens, default 10 |
| `without_emoji` | boolean | No | Whether to exclude emoji, default True |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "hot_comment_tokens": [
    {
      "comment_token": "平板",
      "hot_rate": 1335
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hot_comment_tokens[]` | List of hot comment tokens for the creator. Each item is one token with its score. |
| `hot_comment_tokens[].comment_token` | The keyword or token found in the creator's comments, such as `平板` or `电脑`. |
| `hot_comment_tokens[].hot_rate` | Score for how hot the token is. A higher number ranks the token higher in the list. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with `Success` means the request worked. |

### Notes

- Pass the Xingtu creator ID as `author_id`. If you only have a Douyin ID or `sec_user_id`, look up the creator ID first with [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) or [Douyin XingTu kolId by sec_user_id (V2)](/apis/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id).
- `num` sets how many tokens come back (default 10). `without_emoji` defaults to `true`; set it to `false` to keep emoji tokens.
- For keywords from the creator's own content instead of comments, call [Douyin Xingtu Author Content Hot Keywords](/apis/douyin/xingtu-v2/author-content-hot-keywords).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-hot-comment-tokens.json`](../../../../catalog/models/douyin/xingtu-v2/author-hot-comment-tokens.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-hot-comment-tokens
