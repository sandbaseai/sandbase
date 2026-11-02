# TikTok User Repost Videos API: pricing, parameters and code examples

`tiktok/app-v3/user-repost-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of videos reposted by a specific TikTok user based on their user ID. Supports result pagination through count and offset parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-repost-videos", "user_id": 107955}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-repost-videos', {'user_id': 107955})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-repost-videos", {
  "user_id": 107955
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-repost-videos", sandbase.Params{
	"user_id": 107955,
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-repost-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `21` |
| `offset` | integer |  | Offset default `0` |
| `user_id` | integer | yes | User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response.  |

## Details

Retrieve videos reposted by an account using their `user_id`. Supports navigating through results via `count` and `offset`.

### Use cases

- Track videos shared or reposted by a specific creator.
- Analyze content amplification and sharing trends across targeted accounts.
- Collect reposted media metadata for audience research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-repost-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": 107955}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | integer | Yes | User id, which can be obtained through the handler_user_profile endpoint, with the keyword uid in the response. |
| `count` | integer | No | Number |
| `offset` | integer | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_list": [
    {
      "author_user_id": 6653919748492099589,
      "aweme_id": "7691036284428635423",
      "aweme_type": 0,
      "bodydance_score": 0,
      "content_desc": "[\"This @TikTok TikTok ad campaign is live right now — and it’s airing on major national T…",
      "content_level": 1,
      "content_original_type": 1,
      "content_size_type": 1,
      "content_type": "video",
      "create_time": 1790708957,
      "added_sound_music_info": {
        "audition_duration": 15,
        "author": "Christopher Sbrocco",
        "author_deleted": false,
        "binded_challenge_id": 0,
        "commercial_right_type": 2,
        "create_time": 1790708962
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

- Obtain `user_id` from the `handler_user_profile` endpoint response via the `uid` field.
- Paginate through results using `count` and `offset`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-repost-videos.json`](../../../../catalog/models/tiktok/app-v3/user-repost-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-repost-videos
