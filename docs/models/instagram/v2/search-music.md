# Instagram Music Search API: pricing, parameters and code examples

`instagram/v2/search-music` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Search available music tracks on Instagram using a keyword. Returns matching audio items with audio IDs, track titles, duration, and licensing details.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/search-music", "keyword": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/search-music', {'keyword': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/search-music", {
  "keyword": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/search-music", sandbase.Params{
	"keyword": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/search-music` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |

## Details

Returns Instagram audio tracks that match a search keyword. Each item has an audio ID, title, artist, duration, cover artwork and download URLs. The only input is `keyword`.

### Use cases

- Find licensed tracks on Instagram that match a brand, topic or mood keyword.
- Collect audio IDs to look up posts that use a given track.
- Compare track duration and suggested highlight start times when picking music for a short video.
- Check whether a track is marked explicit or has lyrics before you use it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/search-music" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "openai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 10,
    "items": [
      {
        "allows_saving": false,
        "audio_id": "961546178588254",
        "cover_artwork_thumbnail_uri": "https://scontent-bru2-1.cdninstagram.com/v/t39.30808-6/425966279_183450367700017…",
        "cover_artwork_uri": "https://scontent-bru2-1.cdninstagram.com/v/t39.30808-6/425966279_183450367700017…",
        "dark_message": null,
        "display_artist": "Worldwide Shine",
        "duration_in_ms": 257306,
        "fast_start_progressive_download_url": "https://scontent-bru2-1.cdninstagram.com/o1/v/t2/f2/m69/AQNeIv8QuImCenq2wIo8qoC5…",
        "has_lyrics": false,
        "highlight_start_times_in_ms": [
          59000
        ],
        "id": "920581052455716",
        "is_eligible_for_audio_effects": false
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.count` | Number of audio items in the response. |
| `data.items[].audio_id` | ID of the audio track. Use it to find posts that use this sound. |
| `data.items[].id` | A second ID for the item. It differs from `audio_id` in the response, so store both. |
| `data.items[].title / data.items[].display_artist` | Track title and the artist name shown on Instagram. |
| `data.items[].duration_in_ms` | Track length in milliseconds. |
| `data.items[].highlight_start_times_in_ms` | List of start offsets in milliseconds for the suggested highlight part of the track. Some tracks have one value and some have several. |
| `data.items[].is_explicit / data.items[].has_lyrics` | Boolean flags that show whether the track is marked explicit and whether it has lyrics. |
| `data.items[].licensed_music_subtype` | Licensing subtype of the track. The sample items show `DEFAULT`. |
| `data.items[].allows_saving / data.items[].is_eligible_for_audio_effects / data.items[].is_eligible_for_vinyl_sticker` | Boolean flags for what Instagram allows with the track, such as saving, audio effects and the vinyl sticker. |
| `data.items[].cover_artwork_uri / data.items[].cover_artwork_thumbnail_uri / data.items[].progressive_download_url` | URLs for the cover image, a smaller thumbnail and the audio file. `web_30s_preview_download_url` can be `null`. |

### Notes

- Send a single `keyword` string. The API has no pagination parameter in its schema.
- Use `audio_id` as the input when you look up content that uses a track, for example with [Instagram Music Posts (V2)](/apis/instagram/v2/music-posts).
- Media URLs in the response are full links. Download or cache the files you need.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/search-music.json`](../../../../catalog/models/instagram/v2/search-music.json) · Store page: https://www.sandbase.ai/model/instagram/v2/search-music
