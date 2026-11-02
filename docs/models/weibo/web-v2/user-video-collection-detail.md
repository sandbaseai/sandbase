# Weibo User Video Collection Detail API: pricing, parameters and code examples

`weibo/web-v2/user-video-collection-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves detailed information and video listings for a specified Weibo video collection. Supports sorting by default, hottest, or latest videos, alongside cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-video-collection-detail", "cid": "<cid>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-video-collection-detail', {'cid': '<cid>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-video-collection-detail", {
  "cid": "<cid>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-video-collection-detail", sandbase.Params{
	"cid": "<cid>",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-video-collection-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cid` | string | yes | Collection ID (required, get from fetch_user_video_collection_list)  |
| `cursor` | string |  | Pagination cursor, pass empty for first request, use returned cursor for subsequent  |
| `tab_code` | integer |  | Sort type (0=default, 1=hottest, 2=latest)  |

## Details

Retrieve detailed video listings and information from a specific Weibo video collection using its `cid`.

### Use cases

- Retrieve full video playlists from a specific user collection.
- Display collections sorted by latest or hottest video items.
- Paginate through large video collections using cursor tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-video-collection-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cid": "<cid>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cid` | string | Yes | Collection ID (required, get from fetch_user_video_collection_list) |
| `cursor` | string | No | Pagination cursor, pass empty for first request, use returned cursor for subsequent |
| `tab_code` | integer | No | Sort type (0=default, 1=hottest, 2=latest) |

### Notes

- Obtain the required `cid` from the user video collection list endpoint.
- Use `tab_code` to sort videos by default (0), hottest (1), or latest (2).
- Leave `cursor` empty for the initial query and pass the returned token for subsequent requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-video-collection-detail.json`](../../../../catalog/models/weibo/web-v2/user-video-collection-detail.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-video-collection-detail
