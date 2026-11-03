# YouTube Channel Community Posts API: pricing, parameters and code examples

`youtube/channel-community-posts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a YouTube channel's community posts by handle or channel ID with cursor pagination (text, likes, image, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-community-posts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-community-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-community-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-community-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-community-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |

## Details

Returns a list of community posts for a YouTube channel, with the post text, like count, image links and publish time. You pass a channel `handle` such as `@MrBeast` or a `channelId`.

### Use cases

- Track what a creator announces in community posts, such as new video releases.
- Compare `likeCount` across posts to see which posts get the most engagement.
- Archive post text and image links for a channel.
- Build a feed of recent posts from a list of channels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-community-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@MrBeast"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `handle` | string | No | YouTube channel handle. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_VMouee4IpseKyQo6IPoYVg",
    "posts": [
      {
        "channelHandle": "MrBeast",
        "channelId": "UCX6OQ3DkcsbYNE6H8uQQuVA",
        "channelTitle": "MrBeast",
        "content": "We spent $7,000,000 making the new MrBeast Lab animation series, and EPISODE 1 I…",
        "createdUtc": 1793605689,
        "id": "UgkxvMrKTpUbvqLPjv-lVi7N0wn68DV_NCBQ",
        "image": "",
        "likeCount": 9000,
        "publishedTime": "1 day ago",
        "url": "https://www.youtube.com/post/UgkxvMrKTpUbvqLPjv-lVi7N0wn68DV_NCBQ"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[]` | List of community posts for the channel, as returned on this page. |
| `data.posts[].id` | ID of the post. It also appears at the end of the post `url`. |
| `data.posts[].content` | Text of the post. Long text can end with an ellipsis. |
| `data.posts[].likeCount` | Number of likes on the post, as a whole number. |
| `data.posts[].createdUtc` | Time the post was created, as a Unix timestamp in seconds. |
| `data.posts[].publishedTime` | Relative publish time as shown on YouTube, for example `2 weeks ago`. |
| `data.posts[].image / data.posts[].images[]` | Image attached to the post. `image` is an empty string when the post has no image. `images` appears on posts that have images. |
| `data.posts[].url` | Link to the post on YouTube. |
| `data.posts[].channelHandle / data.posts[].channelId / data.posts[].channelTitle` | Handle, ID and display name of the channel that made the post. |
| `data.nextCursor` | Token for the next page of posts. Send it as `cursor`. |

### Notes

- Send either `handle` or `channelId`. The handle in the response (`channelHandle`) has no leading `@`.
- For the next page, repeat the request with `cursor` set to the `data.nextCursor` value.
- To get details for one post, use the post `id` or `url` with [YouTube Community Post](/apis/youtube/community-post).
- To get the channel ID from a handle first, call [YouTube Channel](/apis/youtube/channel).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/channel-community-posts.json`](../../../catalog/models/youtube/channel-community-posts.json) · Store page: https://www.sandbase.ai/model/youtube/channel-community-posts
