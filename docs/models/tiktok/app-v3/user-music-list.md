# TikTok User Music List API: pricing, parameters and code examples

`tiktok/app-v3/user-music-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of audio tracks associated with a specific TikTok user. Queries require the user's `sec_uid` with optional cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-music-list", "sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-music-list', {'sec_uid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-music-list", {
  "sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-music-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-music-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `10` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `sec_uid` | string | yes | User sec_uid  |

## Details

Retrieve audio tracks associated with a user profile by supplying `sec_uid`. Supports cursor pagination via `cursor` and custom page sizes with `count`.

### Use cases

- Track original audio tracks associated with a creator account.
- Browse cataloged songs and audition details for an artist profile.
- Extract song metadata and duration metrics for specific users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-music-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "music": [
    {
      "audition_duration": 60,
      "author": "Chân CaCa",
      "author_deleted": false,
      "binded_challenge_id": 0,
      "commercial_right_type": 3,
      "create_time": 1777489026,
      "duration": 60,
      "id": 7634256818454333457,
      "preview_end_time": 0,
      "preview_start_time": 87,
      "duration_high_precision": {
        "audition_duration_precision": 60,
        "duration_precision": 60,
        "shoot_duration_precision": 60,
        "video_duration_precision": 60
      },
      "matched_song": {
        "author": "Chân CaCa",
        "full_duration": 248861,
        "id": "7634249903032469521",
        "title": "Chữ Vấn Chữ Vương (Huy PT Remix)"
      },
      "music_release_info": {
        "group_release_date": 1777766400
      }
    }
  ]
}
```

### Notes

- Pagination starts at 0 for `cursor`, with subsequent pages using the cursor returned in previous responses.
- `sec_uid` is required to identify the target TikTok user.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-music-list.json`](../../../../catalog/models/tiktok/app-v3/user-music-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-music-list
