# TikTok User Playlists API: pricing, parameters and code examples

`tiktok/web/user-play-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the public playlists or mixes associated with a TikTok user using their secure user ID. Includes playlist metadata, video counts, and creator details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-play-list", "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-play-list', {'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-play-list", {
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-play-list", sandbase.Params{
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-play-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page default `30` |
| `cursor` | integer |  | Page cursor default `0` |
| `secUid` | string | yes | User secUid  |

## Details

Returns the public playlists (mixes) on a TikTok account. Each playlist includes its name, cover image, video count and creator details. The input is the user's `secUid`.

### Use cases

- List the playlists a TikTok creator has published on their profile.
- Compare `videoCount` across playlists to see which series hold the most videos.
- Collect playlist IDs to feed into a mix video lookup.
- Show a creator's playlist names and covers in a profile dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-play-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "cursor": "5",
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103154431181FE96A9F411504D026",
    "now": 1793691871000
  },
  "hasMore": false,
  "log_pb": {
    "impr_id": "20261103154431181FE96A9F411504D026"
  },
  "playList": [
    {
      "cover": "https://p16-common-sign.tiktokcdn.com/tos-useast8-p-0068-tx2/o8UZ7AA11Ciogu5XByi…",
      "creator": {
        "avatarLarger": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
        "avatarMedium": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
        "avatarThumb": "https://p16-common-sign.tiktokcdn.com/tos-maliva-avt-0068/ba67b11de451691939223e…",
        "ftc": false,
        "id": "107955",
        "isADVirtual": false,
        "nickname": "TikTok",
        "openFavorite": false
      },
      "id": "7681171537575824159",
      "mixId": "7681171537575824159",
      "mixName": "Songs Of The Summer 2026",
      "name": "Songs Of The Summer 2026",
      "videoCount": 3
    }
  ],
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "0k5cdiqY…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `playList[]` | List of playlists (mixes) on the account. |
| `playList[].id / playList[].mixId` | ID of the playlist. Both keys hold the same value in this response. |
| `playList[].mixName / playList[].name` | Display name of the playlist. |
| `playList[].videoCount` | Number of videos in the playlist. |
| `playList[].cover` | URL of the playlist cover image. The URL carries an `x-expires` query value, so save the image if you need it later. |
| `playList[].creator.id` | ID of the account that owns the playlist. |
| `playList[].creator.nickname` | Display name of the creator. |
| `playList[].creator.avatarLarger / playList[].creator.avatarMedium / playList[].creator.avatarThumb` | Creator avatar image URLs in three sizes. |
| `hasMore` | Tells you whether more pages remain. `false` means this was the last page. |
| `cursor` | Cursor value returned for this page, as a string. |

### Notes

- Get the `secUid` for a profile from [TikTok Profile Sec User ID](/apis/tiktok/web/sec-user-id) or [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id).
- Paginate with `count` (default `30`) and `cursor` (default `0`). Pass the returned `cursor` into the next request while `hasMore` is `true`.
- Use a playlist `id` with [TikTok User Mix Video List](/apis/tiktok/web/user-mix) to see the videos inside it.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-play-list.json`](../../../../catalog/models/tiktok/web/user-play-list.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-play-list
