# YouTube Playlist API: pricing, parameters and code examples

`youtube/playlist` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List every video in a YouTube playlist (title, length, and channel per video plus playlist owner and totals).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/playlist", "playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/playlist', {'playlistId': 'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/playlist", {
  "playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/playlist", sandbase.Params{
	"playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj",
})
```

Same call via the path form: `POST /v1/api/youtube/playlist` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `playlistId` | string | yes | The playlist ID: the "list" parameter in a playlist URL (e.g. "PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi").  |

## Details

Returns the videos in a YouTube playlist, plus the playlist title, owner, and total video count. It needs one input: the `playlistId` from the `list` parameter of a playlist URL.

### Use cases

- Export a playlist's track list with titles, channels, and durations into a spreadsheet.
- Add up `lengthSeconds` across a playlist to estimate its total running time.
- Check which channels appear in a curated music playlist.
- Collect video IDs from a playlist and pass them to a video details API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/playlist" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"playlistId": "PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `playlistId` | string | Yes | The playlist ID: the "list" parameter in a playlist URL (e.g. "PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi"). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorHandle": "Redlist-JustHits",
    "authorId": "UCs72iRpTEuwV3y6pdWYLgiw",
    "authorUrl": "https://www.youtube.com/@Redlist-JustHits",
    "owner": "Redlist - Just Hits",
    "title": "Pop Music Playlist - Timeless Pop Songs (Updated Weekly 2026)",
    "totalVideos": 200,
    "videos": [
      {
        "channel": "Lady Gaga",
        "id": "kPa7bsKwL-c",
        "lengthSeconds": 253,
        "lengthText": "4:13",
        "thumbnail": "https://i.ytimg.com/vi/kPa7bsKwL-c/hqdefault.jpg?sqp=-oaymwEnCNACELwBSFryq4qpAxk…",
        "title": "Lady Gaga, Bruno Mars - Die With A Smile (Official Music Video)",
        "url": "https://www.youtube.com/watch?v=kPa7bsKwL-c"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the playlist. |
| `data.owner / data.authorHandle` | Display name and @handle of the channel that owns the playlist. |
| `data.authorId / data.authorUrl` | ID and URL of the owner's channel. |
| `data.totalVideos` | Number of videos in the playlist, as reported for the playlist as a whole. |
| `data.videos[].id` | YouTube video ID. It matches the `v` value in `data.videos[].url`. |
| `data.videos[].title` | Title of the video. |
| `data.videos[].channel` | Name of the channel that posted the video. It can differ from the playlist owner. |
| `data.videos[].lengthSeconds / data.videos[].lengthText` | Video length as a number of seconds and as display text such as `4:13`. |
| `data.videos[].url / data.videos[].thumbnail` | Link to the video's watch page and to its thumbnail image. |
| `found` | `true` when the playlist was found. |

### Notes

- Take `playlistId` from the `list` parameter in a playlist URL, for example `PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj`.
- The request has no pagination parameter. Compare `data.totalVideos` with the length of `data.videos` to see how many videos came back.
- Pass a video ID from `data.videos[].id` to [YouTube Video Details](/apis/youtube/video-detail) for more about one video.
- Use [YouTube Channel Playlists](/apis/youtube/channel-playlists) to find playlist IDs for a channel.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/playlist.json`](../../../catalog/models/youtube/playlist.json) · Store page: https://www.sandbase.ai/model/youtube/playlist
