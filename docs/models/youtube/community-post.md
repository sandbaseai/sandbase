# YouTube Community Post API: pricing, parameters and code examples

`youtube/community-post` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a single YouTube community post by URL (text, images, channel, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/community-post", "url": "https://www.youtube.com/post/Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/community-post', {'url': 'https://www.youtube.com/post/Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/community-post", {
  "url": "https://www.youtube.com/post/Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/community-post", sandbase.Params{
	"url": "https://www.youtube.com/post/Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e",
})
```

Same call via the path form: `POST /v1/api/youtube/community-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of the YouTube community post.  |

## Details

Returns one YouTube community post: its text, image URLs, like count, publish time and the channel that posted it. It needs the full URL of the post in the `url` parameter.

### Use cases

- Archive the text and images of a creator announcement before it is edited or deleted.
- Track the like count of a single community post over time.
- Match a post URL from a mention or report to its channel handle and channel ID.
- Pull the image URL from a post to show a preview in a monitoring dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/community-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/post/Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of the YouTube community post. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "channelHandle": "MrBeast",
    "channelId": "UCX6OQ3DkcsbYNE6H8uQQuVA",
    "channelTitle": "MrBeast",
    "content": "All the YouTube Play Buttons",
    "createdUtc": 1783064892,
    "id": "Ugkx1LonSRBBUqASv-J8j9_FesxwlMAhT3_e",
    "image": "https://yt3.ggpht.com/GuMi512thU6CHTFw1kYlRISWYQmCyn90qa9JmrV2p6oj0K8v05z-omlruh…",
    "images": [
      "https://yt3.ggpht.com/GuMi512thU6CHTFw1kYlRISWYQmCyn90qa9JmrV2p6oj0K8v05z-omlruh…"
    ],
    "likeCount": 2000000,
    "publishedTime": "4 months ago"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the post exists. A lookup that finds nothing returns `false`. |
| `data.id` | ID of the community post. It is the last part of the post URL. |
| `data.content` | Text of the post. |
| `data.image / images[]` | URL of the post image, and the list of all image URLs attached to the post. |
| `data.likeCount` | Number of likes on the post. |
| `data.createdUtc` | Creation time of the post as a Unix timestamp. Compare it with `publishedTime` before you rely on it. |
| `data.publishedTime` | Relative publish time as YouTube shows it, for example `4 months ago`. |
| `data.channelId / channelHandle / channelTitle` | ID, handle and display name of the channel that posted. |

### Notes

- Pass a post URL in the form `https://www.youtube.com/post/<id>`. The `id` in the response matches the last part of this URL.
- Use `channelId` with [YouTube Channel](/apis/youtube/channel) to get details about the posting channel.
- To list more posts from the same channel, call [YouTube Channel Community Posts](/apis/youtube/channel-community-posts).
- To read the replies to a post, call [YouTube Community Post Comments](/apis/youtube/web-v2/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/community-post.json`](../../../catalog/models/youtube/community-post.json) · Store page: https://www.sandbase.ai/model/youtube/community-post
