# Kuaishou Video Comments (App)

`kuaishou/app/video-comment` · api · Kuaishou

Returns comment records for a specified Kuaishou video, including author metadata and like counts. Supports pagination using a cursor.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/video-comment", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/video-comment', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/video-comment", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/video-comment", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Retrieve comments for a specific Kuaishou video by passing `photo_id` and an optional `pcursor` for pagination.

### Use cases

- Analyze audience feedback and sentiment on Kuaishou videos.
- Display top-level video comments and like counts in external dashboards.
- Monitor engagement and author interactions across posted video clips.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/video-comment" \
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
      "authorArea": "山东",
      "authorVerified": false,
      "author_id": 23458411,
      "author_liked": false,
      "author_name": "<user>",
      "comment_id": 938889241499,
      "displaySubCommentCount": true,
      "likedCount": 143,
      "photo_id": 5193494945927590140,
      "recallType": 1,
      "profilePagePrefetchInfo": {
        "profilePageType": 1
      }
    }
  ]
}
```

### Notes

- Specify the target video using `photo_id`.
- Pass `pcursor` to navigate subsequent pages of comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/video-comment.json`](../../../../catalog/models/kuaishou/app/video-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/video-comment
