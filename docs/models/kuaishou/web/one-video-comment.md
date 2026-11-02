# Kuaishou Video Comments (Web) API: pricing, parameters and code examples

`kuaishou/web/one-video-comment` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns root comments for a specified Kuaishou video, including author details, content, and like counts. Queries require a video ID and support cursor pagination.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/one-video-comment", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/one-video-comment', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/one-video-comment", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/one-video-comment", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/one-video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Retrieve root comments for a specific Kuaishou video using `photo_id`. Page through additional comment results using the optional `pcursor` parameter.

### Use cases

- Analyze viewer feedback and discussions on specific Kuaishou videos.
- Track comment engagement metrics such as like counts.
- Extract user feedback and reply interactions for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/one-video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes | — |
| `pcursor` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "rootComments": [
    {
      "authorArea": "江西",
      "authorVerified": false,
      "author_id": 1727775365,
      "author_liked": false,
      "author_name": "<user>",
      "comment_id": 1137733188081,
      "content": "回复 挽风：枕头垫高，不要醒来[呆住][呆住][呆住]。",
      "likedCount": 0,
      "photo_id": 5193494945927590140,
      "replyToUserName": "挽风",
      "profilePagePrefetchInfo": {
        "profilePageType": 1
      }
    }
  ]
}
```

### Notes

- Requires `photo_id` to identify the video.
- Use `pcursor` to control pagination across comment pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/model/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/model/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/model/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/one-video-comment.json`](../../../../catalog/models/kuaishou/web/one-video-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/one-video-comment
