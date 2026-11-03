# TikTok Hashtag Video List API: pricing, parameters and code examples

`tiktok/app-v3/hashtag-video-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos associated with a specific hashtag on TikTok. Filter results by region and paginate through records using cursor controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/hashtag-video-list", "ch_id": "7551"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/hashtag-video-list', {'ch_id': '7551'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/hashtag-video-list", {
  "ch_id": "7551"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/hashtag-video-list", sandbase.Params{
	"ch_id": "7551",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/hashtag-video-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | string | yes | Hashtag id  |
| `count` | integer |  | Number default `10` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `region` | string |  | Region, supports US, GB, FR, JP, VN, SG, default US default `"US"` |

## Details

Fetch a feed of videos associated with a specific TikTok hashtag using `ch_id`. Results can be scoped to specific countries using `region` and paginated via `cursor`.

### Use cases

- Explore videos categorized under a specific TikTok hashtag.
- Monitor hashtag performance and content across different supported regions.
- Collect video metadata for hashtag-driven topic analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/hashtag-video-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "7551"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | string | Yes | Hashtag id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |
| `region` | string | No | Region, supports US, GB, FR, JP, VN, SG, default US |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "author_user_id": 7504868055664722986,
      "aweme_id": "7556191047316032823",
      "aweme_type": 0,
      "bodydance_score": 0,
      "content_level": 1,
      "content_original_type": 1,
      "content_size_type": 1,
      "content_type": "video",
      "create_time": 1759312979,
      "desc": "Cat core #cat #cats #funnypets #funnyanimals #catlover #foryoupage #fyp #viral",
      "added_sound_music_info": {
        "audition_duration": 94,
        "author": "funnypets_11",
        "author_deleted": false,
        "binded_challenge_id": 0,
        "commercial_right_type": 2,
        "create_time": 1759312983
      },
      "aigc_info": {
        "aigc_label_type": 0
      },
      "animated_image_info": {
        "type": 0
      },
      "author": {
        "apple_account": 0,
        "authority_status": 0,
        "aweme_count": 0,
        "comment_filter_status": 0,
        "create_time": 0,
        "favoriting_count": 0
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the first page, and pass the cursor value returned in the previous response for subsequent pages.
- The `region` parameter supports US, GB, FR, JP, VN, and SG, defaulting to US.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/hashtag-video-list.json`](../../../../catalog/models/tiktok/app-v3/hashtag-video-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/hashtag-video-list
