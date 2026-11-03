# Facebook Post API: pricing, parameters and code examples

`facebook/post` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch a single Facebook post by URL with its text and engagement counts (likes, comments, shares, views).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/post", "url": "https://www.facebook.com/reel/2166091230582141/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/post', {'url': 'https://www.facebook.com/reel/2166091230582141/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/post", {
  "url": "https://www.facebook.com/reel/2166091230582141/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/post", sandbase.Params{
	"url": "https://www.facebook.com/reel/2166091230582141/",
})
```

Same call via the path form: `POST /v1/api/facebook/post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Facebook post URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoId` or `views`, and it is served only by a source that returns…  |

## Details

Returns one Facebook post or reel as JSON, with its text, author, engagement counts, reaction breakdown, and video details. It needs the full post URL in `url`.

### Use cases

- Track the views, likes, and shares of a brand's reel after it goes live.
- Compare reaction mixes such as `love` and `angry` across competitor posts.
- Save the caption, author, and video link of a post for a content archive.
- Check whether a post still resolves from a URL stored in a report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/reel/2166091230582141/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Facebook post URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoId` or `views`, and it is served only by a source that returns e |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorId": "100044541544829",
    "authorImage": "https://scontent-phx1-1.xx.fbcdn.net/v/t39.30808-1/284964043_10159903868513445_7…",
    "authorName": "Nike",
    "authorVerified": true,
    "comments": 2737,
    "createdUtc": 1757952115,
    "durationSeconds": 30.025,
    "feedbackId": "ZmVlZGJhY2s6cGZiaWQwMzNLUmdTcnd1RWZ0b3p1OU5CU012MW16YXpZTFJzQXBHa2dhUGlGMmZUa0pu…",
    "id": "1393461115481927",
    "image": "https://scontent-phx1-1.xx.fbcdn.net/v/t51.82787-10/549104239_18565912819020081_…",
    "likes": 8541,
    "reactions": {
      "angry": 36,
      "care": 142,
      "haha": 32,
      "like": 7062,
      "love": 1218,
      "sad": 5,
      "wow": 46
    }
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.text` | Caption or body text of the post. |
| `data.authorName / data.authorId` | Display name and numeric ID of the page or profile that posted. |
| `data.authorVerified` | `true` when the author shows as verified. |
| `data.likes / data.comments / data.shares / data.views` | Engagement counts for the post. |
| `data.reactions.like / love / care / haha / wow / sad / angry` | Count of each reaction type on the post. |
| `data.createdUtc` | Creation time of the post as a Unix timestamp in seconds. |
| `data.durationSeconds` | Length of the video in seconds. |
| `data.videoId / data.videoUrl` | ID of the video and a direct link to the video file. |
| `data.feedbackId` | Identifier for the post's feedback object, which holds its reactions and comments. |
| `found` | `true` when the post was found. |

### Notes

- Pass the full post or reel URL in `url`, for example `https://www.facebook.com/reel/2166091230582141/`.
- Set `requireFields` to names such as `views`, `reactions`, `videoUrl`, or `authorVerified` when your code needs them. A dearer source may then serve the call.
- To read the comments on a post, call [Facebook Post Comments](/apis/facebook/post-comments).
- To get the spoken text of a video post, call [Facebook Post Transcript](/apis/facebook/post-transcript).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/post.json`](../../../catalog/models/facebook/post.json) · Store page: https://www.sandbase.ai/model/facebook/post
