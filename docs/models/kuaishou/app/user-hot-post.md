# Kuaishou User Hot Posts

`kuaishou/app/user-hot-post` · api · Kuaishou

Returns popular posts from a specified Kuaishou user profile, including captions and interaction metrics such as comments and collects.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-hot-post", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-hot-post', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-hot-post", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-hot-post", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-hot-post` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 作品游标/Post cursor  |
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Retrieve hot post feeds and engagement statistics for a Kuaishou creator using `user_id`.

### Use cases

- Analyze top-performing video content from a creator.
- Track engagement metrics like comment and collect counts on popular posts.
- Browse a user trending feed history using pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-hot-post" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |
| `pcursor` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "feeds": [
    {
      "caption": "回村往事@李秀妍u(O4489551526) #李秀妍u",
      "captionToComment": "回村往事@李秀妍u(O4489551526) #李秀妍u",
      "collect_count": 8390,
      "comment_count": 4097,
      "disableCommentDislike": false,
      "duration": 129349,
      "exp_tag": "1_i/2006355482836038866_phot",
      "fastCommentType": 1,
      "following": 0,
      "forward_count": 0,
      "bottomEntryInfo": {
        "bottomBizType": 14
      },
      "commentGuessSearch": {
        "searchWord": "李秀妍和榜一大哥的视频",
        "searchWordMD5": "c541e248be165bd097c418eb43aa4a47",
        "searchWordUrl": "kwai://search?keyword=李秀妍和榜一大哥的视频&sessionId=MzIwXzBfMTc5MTI5MDQ5OTE1NV9fOTM1NQ&source=sea…"
      },
      "commentInfo": {
        "commentCountSpecialEffect": true
      },
      "editInfo": {
        "editTime": 1775816488646
      }
    }
  ]
}
```

### Notes

- Specify `user_id` to query hot posts for a specific profile.
- Pass `pcursor` to navigate across paginated feed results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-hot-post.json`](../../../../catalog/models/kuaishou/app/user-hot-post.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-hot-post
