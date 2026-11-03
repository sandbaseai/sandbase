# Douyin Xingtu Comment Keyword Analysis API: pricing, parameters and code examples

`douyin/xingtu-v3/data-author-hot-comment-tokens` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) comment keyword analysis for a specified creator. Use it to identify recurring audience discussion themes during creator research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-author-hot-comment-tokens", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-author-hot-comment-tokens', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-author-hot-comment-tokens", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-author-hot-comment-tokens", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-author-hot-comment-tokens` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns the keywords that appear most often in comments on a Douyin creator's content, as listed in Xingtu (Douyin Creator Marketplace). It needs one input: the creator's author ID in `oAuthorId`.

### Use cases

- Check which brands and topics the audience of a creator mentions most before you start a sponsorship pitch.
- Compare comment themes across several candidate creators during creator research.
- Spot unexpected words in the comments that may signal audience reactions to ads.
- Combine the keywords with content keyword data to see how a creator's topics line up with audience talk.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-author-hot-comment-tokens" \
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
    "status_message": "Success"
  },
  "hot_comment_tokens": [
    {
      "comment_token": "广告",
      "hot_rate": 548
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hot_comment_tokens[]` | List of keywords found in the creator's comments. Items appear to be ordered from the highest `hot_rate` to the lowest. |
| `hot_comment_tokens[].comment_token` | The keyword text, such as `广告` (advertisement) or a brand name. |
| `hot_comment_tokens[].hot_rate` | A number that shows how prominent the keyword is in the comments. A higher value means the keyword is more prominent. The response does not state the unit. |
| `base_resp.status_code` | Result code of the call. `0` means success. |
| `base_resp.status_message` | Text description of the result, for example `Success`. |

### Notes

- Get `oAuthorId` from a creator search such as [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `oAuthorId` is a numeric string, for example `6870161898013196295`. Send it as a string.
- For keywords from the creator's own content instead of the comments, call [Douyin Xingtu Content Keyword Analysis](/apis/douyin/xingtu-v3/gauthor-author-content-hot-keywords).
- To see who the audience is, call [Douyin Xingtu Audience Distribution](/apis/douyin/xingtu-v3/data-sp-author-audience-distribution).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-author-hot-comment-tokens.json`](../../../../catalog/models/douyin/xingtu-v3/data-author-hot-comment-tokens.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-author-hot-comment-tokens
