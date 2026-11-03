# Instagram Music Posts (V1) API: pricing, parameters and code examples

`instagram/v1/music-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Reels and posts associated with a specific audio track using either an audio ID or URL. Supports cursor pagination to browse results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/music-posts"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/music-posts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/music-posts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/music-posts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v1/music-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `music_id` | string |  | Music ID (alternative to music_url)  |
| `music_url` | string |  | Music URL, ID will be extracted automatically (alternative to music_id)  |

## Details

Returns Reels that use a given Instagram audio track, plus details about the track itself. You pass either `music_id` or `music_url`, and you can page through results with `max_id`.

### Use cases

- Count how many Reels use a song with `media_count.clips_count` or `formatted_media_count`.
- Page through the Reels that use a track to see which creators picked it.
- Find the Spotify track behind an Instagram audio page with `spotify_track_metadata`.
- Check whether an audio page is restricted before you build a report on it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/music-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "564058920086577", "music_url": "https://www.instagram.com/reels/audio/564058920086577"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `max_id` | string | No | Pagination cursor, omit for first request |
| `music_id` | string | No | Music ID (alternative to music_url) |
| `music_url` | string | No | Music URL, ID will be extracted automatically (alternative to music_id) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "67",
  "audio_page_reporting_id": "18404542084110335",
  "audio_page_segments": [],
  "audio_ranking_info": {
    "best_audio_cluster_id": "25883770477923057"
  },
  "auto_created_reels_preview_metadata": [],
  "available_tabs": [
    "clips"
  ],
  "formatted_media_count": "389K reels",
  "is_music_page_restricted": false,
  "items": [
    {
      "media": {
        "are_remixes_crosspostable": true,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boost_unavailable_reason_v2": null,
        "can_see_insights_as_brand": false,
        "can_view_more_preview_comments": false,
        "can_viewer_reshare": true,
        "can_viewer_save": true
      }
    }
  ],
  "media_count": {
    "clips_count": 389789,
    "photos_count": 0
  },
  "metadata": {
    "additional_audio_info": null,
    "music_info": {
      "music_asset_info": {
        "allows_saving": true,
        "artist_id": "545138078499840",
        "audio_asset_id": "2111814179306968",
        "audio_cluster_id": "564058920086577",
        "cover_artwork_thumbnail_uri": "https://instagram.fbcn2-1.fna.fbcdn.net/v/t39.30808-6/649199056_71060828927069_1…",
        "cover_artwork_uri": "https://instagram.fbcn2-1.fna.fbcdn.net/v/t39.30808-6/649199056_71060828927069_1…",
        "dark_message": null,
        "dash_manifest": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011…"
      },
      "music_canonical_id": 18404542084110335,
      "music_consumption_info": {
        "allow_media_creation_with_music": true,
        "audio_asset_start_time_in_ms": 2500,
        "audio_filter_infos": [],
        "audio_muting_info": {
          "allow_audio_editing": false,
          "mute_audio": false,
          "mute_reason_str": "",
          "show_muted_audio_toast": false
        },
        "contains_lyrics": null,
        "derived_content_id": null,
        "display_labels": null,
        "formatted_clips_media_count": "389K reels"
      }
    },
    "original_sound_info": null
  },
  "music_canonical_id": "18404542084110335"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].media` | One Reel or post that uses the audio. The trimmed sample shows flags such as `can_viewer_reshare` and `can_viewer_save` inside each `media` object. |
| `media_count.clips_count / media_count.photos_count` | Number of Reels and photo posts that use the audio. In this response the Reel count is 389789 and the photo count is 0. |
| `formatted_media_count` | Reel count as a short display string, for example `389K reels`. |
| `metadata.music_info.music_asset_info.audio_cluster_id` | ID of the audio cluster. It matches the `music_id` sent in this request. |
| `metadata.music_info.music_asset_info.cover_artwork_uri` | URL of the cover artwork image for the track. |
| `metadata.music_info.music_consumption_info.allow_media_creation_with_music` | Whether new media can be created with this audio. |
| `spotify_track_metadata.spotify_track_id / spotify_track_metadata.spotify_listen_uri` | Spotify track ID and a link to listen to the track on Spotify. |
| `is_music_page_restricted` | `true` if the music page is restricted. It is `false` in this response. |
| `paging_info.max_id` | Cursor for the next page. Send it as `max_id` in the next request. |
| `paging_info.more_available` | `true` when more results can be fetched with the cursor. |

### Notes

- Send either `music_id` or `music_url`. The ID is the number at the end of a URL like `https://www.instagram.com/reels/audio/564058920086577`.
- Omit `max_id` on the first request. For the next page, copy `paging_info.max_id` into `max_id` and repeat until `paging_info.more_available` is `false`.
- To get full details for a single item, use [Instagram Post Details by ID](/apis/instagram/v1/post-by-id) or [Instagram Post Details by URL](/apis/instagram/v1/post-by-url).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/music-posts.json`](../../../../catalog/models/instagram/v1/music-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/music-posts
