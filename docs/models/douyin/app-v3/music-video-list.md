# Douyin Music Video List API: pricing, parameters and code examples

`douyin/app-v3/music-video-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of Douyin videos that feature a specified audio track, identified by its music ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-video-list", "music_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-video-list', {'music_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-video-list", {
  "music_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-video-list", sandbase.Params{
	"music_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `music_id` | string | yes | Music id  |

## Details

Retrieve videos associated with a specific Douyin audio track using `music_id`.

### Use cases

- Track video posts associated with a specific music track on Douyin.
- Monitor user adoption and content trends for audio identifiers.
- Retrieve video metadata and author details linked to a background track.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "7348905216869174025"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "activity_video_type": 0,
      "author_user_id": 4055412235572862,
      "aweme_id": "7357708701425224997",
      "aweme_type": 68,
      "bodydance_score": 0,
      "boost_status": 0,
      "caption": "永远这词 我只信你 我的朋友",
      "caption_template_id": 0,
      "category_da": 16,
      "cf_assets_type": 0,
      "author": {
        "account_cert_info": "{}",
        "authority_status": 0,
        "comment_filter_status": 0,
        "follow_status": 0,
        "follower_status": 0,
        "live_status": 0
      },
      "comment_permission_info": {
        "comment_permission_status": 0
      },
      "commerce_info": {
        "ad_type": 0
      },
      "component_control": {
        "data_source_url": "/aweme/v1/music/aweme/"
      }
    }
  ]
}
```

### Notes

- Use `cursor` for pagination, starting with 0 and passing the subsequent cursor returned by the prior response.
- Retain the default value for `count` to prevent issues.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-video-list.json`](../../../../catalog/models/douyin/app-v3/music-video-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-video-list
