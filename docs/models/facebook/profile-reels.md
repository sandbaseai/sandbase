# Facebook Profile Reels API: pricing, parameters and code examples

`facebook/profile-reels` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a Facebook page's reels by URL with cursor pagination (caption, view count, permalink, thumbnail).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-reels", "url": "https://www.facebook.com/nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-reels', {'url': 'https://www.facebook.com/nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-reels", {
  "url": "https://www.facebook.com/nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-reels", sandbase.Params{
	"url": "https://www.facebook.com/nike",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Facebook page/profile URL.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `feedbackId` or `authorVerified`, and it is served only by a source…  |

## Details

Returns a list of reels published by a Facebook page, with caption, view count, permalink, thumbnail and author details for each reel. It needs the full page or profile URL, for example `https://www.facebook.com/nike`.

### Use cases

- Track which reels from a brand page get the most views.
- Collect captions and hashtags from a competitor's reels to study their content themes.
- Build a catalog of reel permalinks and thumbnails for a media monitoring dashboard.
- Sort a page's reels by `createdUtc` to see how often it posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/nike"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Facebook page/profile URL. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `feedbackId` or `authorVerified`, and it is served only by a source th |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_Y0DHHLlEwg5FrmrjAWioUg",
    "reels": [
      {
        "authorId": "100044541544829",
        "authorImage": "https://scontent-phl2-1.xx.fbcdn.net/v/t39.30808-1/284964043_10159903868513445_7…",
        "authorName": "Nike",
        "authorVerified": true,
        "caption": "Leave your limits at the surface. #JustDoIt",
        "comments": null,
        "createdUtc": 1757952115,
        "durationSeconds": 30.025,
        "feedbackId": "ZmVlZGJhY2s6cGZiaWQwMzNLUmdTcnd1RWZ0b3p1OU5CU012MW16YXpZTFJzQXBHa2dhUGlGMmZUa0pu…",
        "id": "1393461115481927",
        "likes": null,
        "shares": null
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.reels[].url` | Permalink to the reel on Facebook. |
| `data.reels[].caption` | Text the page posted with the reel, including hashtags. |
| `data.reels[].views` | View count of the reel as a number. |
| `data.reels[].createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.reels[].durationSeconds` | Length of the reel in seconds. |
| `data.reels[].thumbnail` | Image URL for the reel's cover frame. |
| `data.reels[].videoUrl` | Direct URL of the video file. |
| `data.reels[].authorName / data.reels[].authorId / data.reels[].authorVerified` | Name and ID of the page that posted the reel, and whether it is verified. |
| `data.reels[].id / data.reels[].videoId` | Identifiers for the reel. `videoId` is the same value that appears in the reel `url`. |
| `data.nextCursor` | Cursor that fetches the next page of reels. |

### Notes

- Pass `data.nextCursor` as `cursor` in the next request to get more reels.
- `likes`, `comments` and `shares` can come back as `null`. Add them to `requireFields` if you need them, which may change the price.
- Use the page's full Facebook URL. If you only have a page name, try [Facebook Page Search](/apis/facebook/search-pages) to find it.
- For regular posts instead of reels, call [Facebook Get Profile Posts](/apis/facebook/profile-posts).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-reels.json`](../../../catalog/models/facebook/profile-reels.json) · Store page: https://www.sandbase.ai/model/facebook/profile-reels
