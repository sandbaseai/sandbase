# Weibo User Video Collection List API: pricing, parameters and code examples

`weibo/web-v2/user-video-collection-list` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the video collection list belonging to a specified Weibo user. Provide the target account identifier using the uid parameter to retrieve their curated video playlists.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-video-collection-list", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-video-collection-list', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-video-collection-list", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-video-collection-list", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-video-collection-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Returns the video collections (playlists) that a Weibo user has set up on their profile. It needs one input, the user's numeric `uid`. The response also carries a few profile video display settings.

### Use cases

- Check whether a Weibo creator has published any video playlists.
- Collect playlist entries from a creator profile before pulling the videos inside each one.
- Track a list of accounts and flag when one starts to organize its videos into collections.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-video-collection-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attitude_msg": "",
  "attitude_visible": 1,
  "icon": "https://h5.sinaimg.cn/upload/1011/55/2023/02/08/svideo_profile_video_like.png",
  "playlists": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `playlists` | List of video collections for the user. It is empty (`[]`) when the account has no collections. |
| `attitude_visible` | Flag with value `1` in the sample. The name suggests it controls whether the like tab on the profile video page is shown. |
| `attitude_msg` | Message text tied to the like tab. It is an empty string in the sample. |
| `icon` | URL of an icon image. The file name suggests it is the profile video like icon. |

### Notes

- Pass the Weibo user ID as a string in `uid`, for example `8431518763`. Use [Weibo User Search](/apis/weibo/web-v2/user-search) to find an account if you do not have the ID.
- This API takes no pagination parameter. The only input is `uid`.
- An empty `playlists` list means the account has no collections. Call [Weibo User Video List](/apis/weibo/web-v2/user-video-list) to see the user's videos instead.
- To open a single collection, use [Weibo User Video Collection Detail](/apis/weibo/web-v2/user-video-collection-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-video-collection-list.json`](../../../../catalog/models/weibo/web-v2/user-video-collection-list.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-video-collection-list
