# Kuaishou User Video List (V2)

`kuaishou/app/user-post-v2` · api · Kuaishou

Retrieves a list of video feeds posted by a specific Kuaishou user. Supports sorting by latest or hot posts and cursor-based pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/user-post-v2", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/user-post-v2', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/user-post-v2", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/user-post-v2", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/user-post-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort type, latest (default) / hot. one of: `latest`, `hot` |
| `pcursor` | string |  | Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests.  |
| `user_id` | string | yes | 用户ID/User ID  |

## Details

Retrieve posted video feeds for a specific Kuaishou account by passing the `user_id`. Supports sorting by post recency or popularity alongside cursor pagination.

### Use cases

- Track recent video uploads from specific Kuaishou creators.
- Analyze engagement metrics such as comments and saves across a creator profile.
- Sort and display an author top-performing video content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/user-post-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |
| `sort` | string | No | Sort type, latest (default) / hot. |
| `pcursor` | string | No | Video cursor, empty for the first request, and use the pcursor value in the returned response for subsequent requests. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "feeds": [
    {
      "caption": "听说你还在搞什么原创 #李秀妍u #喜爱度激励计划 #素颜",
      "captionToComment": "听说你还在搞什么原创 #李秀妍u #喜爱度激励计划 #素颜",
      "collect_count": 11,
      "comment_count": 6,
      "disableCommentDislike": false,
      "duration": 11616,
      "exp_tag": "1_i/2010168907973245329_p0",
      "fastCommentType": 1,
      "following": 0,
      "forward_count": 0,
      "bottomEntryInfo": {
        "bottomBizType": 14
      },
      "commentGuessSearch": {
        "searchWord": "李秀妍素颜照片",
        "searchWordMD5": "910267cc9d85ae9b8468fe979ef7cc28",
        "searchWordUrl": "kwai://search?keyword=李秀妍素颜照片&sessionId=MzIwXzBfMTc5MTI5MDQ5OTMwMV9fNzU4Ng&source=search_…"
      },
      "ext_params": {
        "mtype": 3
      },
      "photoAreaInfo": {
        "areaName": "发布于湖南"
      }
    }
  ]
}
```

### Notes

- Set `sort` to 'latest' (default) or 'hot' to order the returned feeds.
- Leave `pcursor` empty on the initial call and use the returned `pcursor` value for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/user-post-v2.json`](../../../../catalog/models/kuaishou/app/user-post-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/user-post-v2
