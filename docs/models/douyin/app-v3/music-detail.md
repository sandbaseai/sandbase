# Douyin Music Details API: pricing, parameters and code examples

`douyin/app-v3/music-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified Douyin audio track using its unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/music-detail", "music_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/music-detail', {'music_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/music-detail", {
  "music_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/music-detail", sandbase.Params{
	"music_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/music-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `music_id` | string | yes | Music id  |

## Details

Returns metadata for one Douyin audio track, including its title-side details, author name, duration, cover and avatar images, and flags such as original sound. It needs a `music_id`, the numeric ID of the track.

### Use cases

- Check whether a Douyin sound is marked as original sound before using it in a campaign.
- Download the cover and avatar images of a track to show it in a music trend report.
- Confirm the author name and duration of a sound when you only have its ID from a video.
- Check restriction and deletion flags to see if a track is still usable.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/music-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "7348905216869174025"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "detail_page_labels": null,
  "disable_music_activity_setting": false,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153135C29678542B1D715AD79F",
    "now": 1793691096000,
    "scenes": null
  },
  "feature_data": {},
  "follow_shoot_buttons": null,
  "log_pb": {
    "impr_id": "20261103153135C29678542B1D715AD79F"
  },
  "lora_model_ids": null,
  "msg": "success",
  "music_activity_resource_infos": null,
  "music_info": {
    "album": "",
    "artist_user_infos": null,
    "artists": [],
    "audition_duration": 29,
    "author": "KD_B Music",
    "author_deleted": false,
    "author_position": null,
    "author_status": 1,
    "avatar_large": {
      "height": 720,
      "uri": "1080x1080/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACgeCH1nztAM9h0AfAArgAzpkId",
      "url_list": [
        "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKA…"
      ],
      "width": 720
    },
    "avatar_medium": {
      "height": 720,
      "uri": "720x720/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACgeCH1nztAM9h0AfAArgAzpkId",
      "url_list": [
        "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACg…"
      ],
      "width": 720
    },
    "avatar_thumb": {
      "height": 720,
      "uri": "100x100/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACgeCH1nztAM9h0AfAArgAzpkId",
      "url_list": [
        "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_oMDhlc4OEhKACg…"
      ],
      "width": 720
    },
    "binded_challenge_id": 0
  },
  "rec_list": [],
  "related_effects": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `music_info.id_str / music_info.mid` | The track ID as a string. Use these when your tools cannot hold a 64-bit number safely. |
| `music_info.author` | Display name of the track's author, for example `KD_B Music`. |
| `music_info.duration / music_info.audition_duration` | Track length and audition length. Both are `29` in this response. |
| `music_info.is_original_sound / music_info.is_original / music_info.is_pgc / music_info.is_commerce_music` | Boolean flags that describe the type of the track. Here `is_original_sound` is `true` and the other three are `false`. |
| `music_info.is_restricted / music_info.is_del_video / music_info.author_deleted` | Boolean flags for restriction and deletion state of the track and its author. |
| `music_info.cover_large.url_list[] / music_info.cover_medium.url_list[] / music_info.cover_thumb.url_list[]` | Image URLs for the track cover in large, medium and thumbnail sizes. Each list holds a `.webp` and a `.jpeg` link. |
| `music_info.avatar_large.url_list[] / music_info.avatar_medium.url_list[] / music_info.avatar_thumb.url_list[]` | Image URLs for the author avatar in three sizes. |
| `music_info.luna_song.luna_song_id_str` | ID of the linked Luna song, with `luna_copyright` showing whether copyright is flagged `true`. |
| `music_info.music_caption_url` | Link to a caption file for the track. The URL carries `x-expires` and `x-signature` query values. |
| `status_code / msg` | Request result. `0` and `success` mean the lookup worked. |

### Notes

- Take `music_id` from the music field of a video, for example from [Douyin Single Video Details](/apis/douyin/app-v3/one-video), or from a music list such as [Douyin Music Hot Search List](/apis/douyin/app-v3/music-hot-search-list).
- To list videos that use this sound, call [Douyin Music Video List](/apis/douyin/app-v3/music-video-list) with the same ID.
- Many top-level fields such as `related_musics`, `rec_list` and `trends_infos` come back empty or `null` for this track.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/music-detail.json`](../../../../catalog/models/douyin/app-v3/music-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/music-detail
