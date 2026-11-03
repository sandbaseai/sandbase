# Facebook Group Posts API: pricing, parameters and code examples

`facebook/group-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch recent posts from any public Facebook group by URL: text, author, reactions, and comment counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/group-posts", "url": "https://www.facebook.com/groups/instantpotcommunity/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/group-posts', {'url': 'https://www.facebook.com/groups/instantpotcommunity/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/group-posts", {
  "url": "https://www.facebook.com/groups/instantpotcommunity/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/group-posts", sandbase.Params{
	"url": "https://www.facebook.com/groups/instantpotcommunity/",
})
```

Same call via the path form: `POST /v1/api/facebook/group-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The URL of a public Facebook group to fetch posts from (e.g. https://www.facebook.com/groups/instantpotcommunity/).  |
| `sort` | string |  | Ordering for the returned posts (e.g. TOP_POSTS). one of: `TOP_POSTS`, `RECENT_ACTIVITY`, `CHRONOLOGICAL`, `CHRONOLOGICAL_LISTINGS` |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |

## Details

Returns a page of posts from a public Facebook group, including post text, author, reaction counts, comment count, and a link to each post. It needs the group's URL as `url`.

### Use cases

- Track what members of a niche group ask about, such as recipes or product problems.
- Find the most reacted posts in a group by requesting `TOP_POSTS` order.
- Collect post permalinks from a group, then pull comments on the ones that get replies.
- Compare engagement across several groups by reading `reactionCount` and `commentCount`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/group-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/groups/instantpotcommunity/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of a public Facebook group to fetch posts from (e.g. https://www.facebook.com/groups/instantpotcommunity/). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `sort` | string | No | Ordering for the returned posts (e.g. TOP_POSTS). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_VcavPYzyva1DYFhA9pw7Jg",
    "posts": [
      {
        "authorId": "1020320894",
        "authorName": "Barbara Schieving",
        "commentCount": 0,
        "id": "29304905819176694",
        "image": "https://scontent-ord5-1.xx.fbcdn.net/v/t15.5256-10/245892761_817229948955627_562…",
        "publishTime": 1793657938,
        "reactionCount": 3,
        "reactions": {
          "angry": 0,
          "care": 0,
          "haha": 0,
          "like": 3,
          "love": 0,
          "sad": 0,
          "wow": 0
        },
        "text": "",
        "url": "https://www.facebook.com/groups/InstantPotCommunity/permalink/29304905819176694/"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[].id` | ID of the post. |
| `data.posts[].url` | Permalink to the post inside the group. |
| `data.posts[].text` | Text of the post. It can be an empty string when the post only has an image. |
| `data.posts[].authorName / data.posts[].authorId` | Display name and ID of the member who wrote the post. The ID is numeric for some authors and a `pfbid...` string for others. |
| `data.posts[].publishTime` | Time the post was published, as a Unix timestamp in seconds. |
| `data.posts[].reactionCount` | Total number of reactions on the post. |
| `data.posts[].reactions.like / data.posts[].reactions.love / data.posts[].reactions.care / data.posts[].reactions.haha / data.posts[].reactions.wow / data.posts[].reactions.sad / data.posts[].reactions.angry` | Count of each reaction type on the post. |
| `data.posts[].commentCount` | Number of comments on the post. |
| `data.posts[].image` | URL of an image attached to the post. |
| `data.nextCursor` | Cursor for the next page of posts. |

### Notes

- Pass `data.nextCursor` as `cursor` in the next request to get the following page.
- Use `sort` with `TOP_POSTS`, `RECENT_ACTIVITY`, `CHRONOLOGICAL`, or `CHRONOLOGICAL_LISTINGS` to change the order of posts.
- Post `id` values are numeric strings. Author `authorId` values can be numeric or start with `pfbid`.
- To read the comments on a post, call [Facebook Post Comments](/apis/facebook/post-comments). For full details on one post, call [Facebook Post](/apis/facebook/post).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/group-posts.json`](../../../catalog/models/facebook/group-posts.json) · Store page: https://www.sandbase.ai/model/facebook/group-posts
