# TikTok Comment Replies API: pricing, parameters and code examples

`tiktok/post-sub-comment` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get replies to a specific comment on a TikTok post with cursor pagination. Use it to inspect threaded discussions and continue through reply pages for a known post comment.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/post-sub-comment", "awemeId": "7701102965385383199", "commentId": "1650470666299398"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/post-sub-comment', {'awemeId': '7701102965385383199', 'commentId': '1650470666299398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/post-sub-comment", {
  "awemeId": "7701102965385383199",
  "commentId": "1650470666299398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/post-sub-comment", sandbase.Params{
	"awemeId": "7701102965385383199",
	"commentId": "1650470666299398",
})
```

Same call via the path form: `POST /v1/api/tiktok/post-sub-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor. Start with '0'. default `"0"` |
| `awemeId` | string | yes | The unique ID of the TikTok post.  |
| `commentId` | string | yes | The unique ID of the comment to retrieve replies for.  |

## Details

Returns the replies to one comment on a TikTok post. You send the post ID (`awemeId`) and the parent comment ID (`commentId`). Results come in pages, controlled by `cursor`.

### Use cases

- Read the full reply thread under a single TikTok comment.
- Walk through every reply page of a busy comment by passing the cursor forward.
- Check whether a known comment has any replies before you collect more data.
- Archive a threaded discussion for moderation or research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/post-sub-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"awemeId": "7701102965385383199", "commentId": "1650470666299398"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `awemeId` | string | Yes | The unique ID of the TikTok post. |
| `commentId` | string | Yes | The unique ID of the comment to retrieve replies for. |
| `cursor` | string | No | Pagination cursor. Start with '0'. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [],
  "cursor": 0,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074409E041FC3BC7C8170221E3",
    "now": 1793691849000
  },
  "has_more": 0,
  "log_pb": {
    "impr_id": "20261103074409E041FC3BC7C8170221E3"
  },
  "status_code": 0,
  "status_msg": "",
  "total": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments` | List of reply objects for the requested comment. It is an empty list in the sample response, which means that comment had no replies to return. |
| `has_more` | Paging flag. `0` means there are no more reply pages after this one. |
| `cursor` | Cursor value returned with this page. Use it as the `cursor` of your next request when `has_more` is not `0`. |
| `total` | Total count reported with the reply list. It is `0` in the sample response. |
| `status_code / status_msg` | Result status of the call. `status_code` is `0` and `status_msg` is empty in the sample response. |
| `extra.fatal_item_ids` | List of item IDs flagged in the response. It is empty in the sample response. |
| `log_pb.impr_id` | Request identifier. It matches `extra.logid` in the sample response. |

### Notes

- `awemeId` is the ID of the TikTok post. `commentId` is the ID of the parent comment whose replies you want.
- Start with `cursor` set to `"0"`. Send the returned `cursor` on the next call while `has_more` is not `0`.
- A reply-free comment returns `status_code` `0` with an empty `comments` list.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tiktok/post-sub-comment.json`](../../../catalog/models/tiktok/post-sub-comment.json) · Store page: https://www.sandbase.ai/model/tiktok/post-sub-comment
