# TikTok Song API: pricing, parameters and code examples

`tiktok/song` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

Fetch details for a TikTok song or sound (title, author, duration, cover art, and how many videos use it).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/song", "clipId": "7439295283975702544"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/song', {'clipId': '7439295283975702544'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/song", {
  "clipId": "7439295283975702544"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/song", sandbase.Params{
	"clipId": "7439295283975702544",
})
```

Same call via the path form: `POST /v1/api/tiktok/song` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `clipId` | string | yes | The clip identifier for the song, found in TikTok music URLs (e.g. 7439295283975702544).  |

## Details

Returns details for one TikTok song or sound: title, author, album, duration, cover image URL, and the number of videos that use it. It needs the `clipId` from a TikTok music URL.

### Use cases

- Check how many TikTok videos use a track to see how widely it has spread.
- Pull the title, author, and album for a sound ID to label it in a music tracking sheet.
- Tell original sounds apart from licensed tracks using the `isOriginal` flag.
- Save the cover image and share link to show a sound in a dashboard or report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/song" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"clipId": "7439295283975702544"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `clipId` | string | Yes | The clip identifier for the song, found in TikTok music URLs (e.g. 7439295283975702544). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "album": "GNX",
    "author": "Kendrick Lamar & SZA",
    "coverUrl": "https://p16-common.tiktokcdn-us.com/tos-alisg-v-2774/ooCBAEtE4DqIfBLAjADiRIneQAT…",
    "duration": 59,
    "isOriginal": false,
    "shareUrl": "https://www.tiktok.com/music/-7439295283975702544",
    "songId": "7439295283975702544",
    "title": "luther",
    "videoCount": 1425960
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the song exists. A lookup that finds nothing returns `false`. |
| `data.title` | Name of the song or sound, for example `luther`. |
| `data.author` | Artist or creator credited for the sound, for example `Kendrick Lamar & SZA`. |
| `data.album` | Album the track belongs to, for example `GNX`. |
| `data.duration` | Length of the sound. The example value is `59`. |
| `data.videoCount` | Number of TikTok videos that use this sound. |
| `data.isOriginal` | Whether the sound is marked as an original sound. It is `false` for this track. |
| `data.songId` | ID of the song, the same value as the `clipId` in the request. |
| `data.coverUrl` | URL of the cover image for the song. |
| `data.shareUrl` | Link to the song's page on TikTok. |

### Notes

- Take `clipId` from the number at the end of a TikTok music URL, such as `7439295283975702544`.
- Check `found` before reading `data`.
- To list videos that use this sound, call [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list).
- For a second view of a song, call [TikTok Music Details](/apis/tiktok/app-v3/music-detail).

### Pricing

Billed at the actual cost of each call, about $0.0006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/song.json`](../../../catalog/models/tiktok/song.json) · Store page: https://www.sandbase.ai/model/tiktok/song
