# Toutiao Post Comments API: pricing, parameters and code examples

`toutiao/app/comments` · data API · Toutiao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns user comments and interaction metrics for a specific Toutiao post. Results can be paginated through comment batches using an offset index.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "toutiao/app/comments", "group_id": "7453372680222523931", "offset": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('toutiao/app/comments', {'group_id': '7453372680222523931', 'offset': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("toutiao/app/comments", {
  "group_id": "7453372680222523931",
  "offset": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "toutiao/app/comments", sandbase.Params{
	"group_id": "7453372680222523931",
	"offset": "0",
})
```

Same call via the path form: `POST /v1/api/toutiao/app/comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string | yes | Offset, used for pagination, default is 0, then add 20 each time  |
| `group_id` | string | yes | Post ID, can be obtained from the link  |

## Details

Returns a page of comments for a Toutiao post, plus paging data and post-level comment settings. It needs the post's `group_id` and an `offset` value.

### Use cases

- Collect the first pages of comments on a Toutiao post to review reader feedback.
- Track how many `bury_count` votes each comment on a post receives.
- Page through all comments of a post by repeating the call until `has_more` is false.
- Check whether commenting is turned off on a post using `ban_comment`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/toutiao/app/comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"group_id": "7453372680222523931", "offset": "0"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `group_id` | string | Yes | Post ID, can be obtained from the link |
| `offset` | string | Yes | Offset, used for pagination, default is 0, then add 20 each time |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "at_user_guide_info": null,
  "ban_ai_polish": true,
  "ban_audio_comment": true,
  "ban_comment": false,
  "ban_comment_reason": "写评论",
  "ban_comment_toast": "",
  "ban_face": false,
  "ban_gif_suggest": 0,
  "ban_pic_comment": 0,
  "bottom_tips": null,
  "comment_activity": null,
  "comment_classify_detail": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | List of comment cells. Each item holds one comment and its `id`. |
| `data[].id` | ID of the comment cell. It is a long number. |
| `data[].comment.bury_count` | Number of bury votes on the comment. |
| `data[].comment.aid` | App ID value attached to the comment. The response does not explain its meaning. |
| `data[].cell_type` | Type code of the list item. Items in this response all have the value `1`. |
| `has_more` | `true` when more comments are available after this page. |
| `offset` | Offset value for the next page. The sample response returns `20` after a request with `0`. |
| `next_comment_since_ts` | Unix-style timestamp number returned for the next comment batch. |
| `ban_comment / ban_pic_comment / ban_audio_comment` | Flags that show whether commenting, picture comments or audio comments are blocked on this post. |
| `group.group_id` | ID of the post the comments belong to. |

### Notes

- Take `group_id` from the Toutiao post link.
- Start with `offset` set to `0`, then add 20 for each next page, as the parameter description states.
- Stop paging when `has_more` is `false`.
- To get details about the post itself, call [Toutiao Article Details (App)](/apis/toutiao/app/article-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Toutiao Article Details (App)](/apis/toutiao/app/article-info): Returns details and interface settings for a specified Toutiao post.
- [Toutiao Profile User ID](/apis/toutiao/app/user-id): Resolves a Toutiao user profile URL into numeric and secure user identifiers.
- [Toutiao User Profile](/apis/toutiao/app/user-info): Get a Toutiao (Jinri Toutiao) user profile by user ID: name, bio, avatar, follower, following and like counts, and content tabs.

---
Machine-readable: [`catalog/models/toutiao/app/comments.json`](../../../../catalog/models/toutiao/app/comments.json) · Store page: https://www.sandbase.ai/model/toutiao/app/comments
