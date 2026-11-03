# YouTube Channel Playlists API: pricing, parameters and code examples

`youtube/channel-playlists` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a YouTube channel's playlists by handle or channel ID with cursor pagination (title, video count, thumbnail).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-playlists"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-playlists', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-playlists", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-playlists", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-playlists` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |

## Details

Returns the playlists of a YouTube channel, with each playlist's title, video count, thumbnail and links. It needs a channel `handle` such as `@veritasium` or a `channelId`.

### Use cases

- Build a table of contents for a creator's content by listing every playlist and its size.
- Find a channel's topic series, such as Biology or Computing, to group its videos by subject.
- Collect playlist URLs to feed into a playlist tracker or a content audit.
- Show playlist cover images in a channel directory or a recommendation widget.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-playlists" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@veritasium"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `handle` | string | No | YouTube channel handle. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": null,
    "playlists": [
      {
        "id": "PLkahZjV5wKe8w9GC_n2yyhx6Wj-NKzzeE",
        "playlistUrl": "https://www.youtube.com/playlist?list=PLkahZjV5wKe8w9GC_n2yyhx6Wj-NKzzeE",
        "thumbnail": "https://i.ytimg.com/vi/AaZ_RSt0KP8/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwk…",
        "title": "Computing",
        "videoCount": 5,
        "videoId": "AaZ_RSt0KP8",
        "videoUrl": "https://www.youtube.com/watch?v=AaZ_RSt0KP8"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.playlists[].id` | The playlist ID. It starts with `PL` and works as the `list` value in the playlist URL. |
| `data.playlists[].title` | The playlist name, for example `Computing`. |
| `data.playlists[].videoCount` | The number of videos in the playlist. |
| `data.playlists[].playlistUrl` | A direct link to the playlist page on YouTube. |
| `data.playlists[].thumbnail` | The thumbnail image URL for the playlist. |
| `data.playlists[].videoId / data.playlists[].videoUrl` | The ID and watch link of the video that supplies the thumbnail. This is the video shown as the playlist cover. |
| `data.nextCursor` | The token for the next page of playlists. It is `null` when there are no more pages. |
| `found` | `true` when the channel was found. |

### Notes

- Send either `handle` (with the leading `@`) or `channelId`. The example request uses `handle`.
- To page through results, pass the `data.nextCursor` value as `cursor` in the next request. Stop when it is `null`.
- To list the videos in a playlist, pass its `id` to [YouTube Playlist](/apis/youtube/playlist).
- To get the channel's own uploads, use [YouTube Channel Videos](/apis/youtube/channel-videos).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/channel-playlists.json`](../../../catalog/models/youtube/channel-playlists.json) · Store page: https://www.sandbase.ai/model/youtube/channel-playlists
