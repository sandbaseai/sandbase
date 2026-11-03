# TikTok Song Videos API: pricing, parameters and code examples

`tiktok/song-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** sync

List TikTok videos that use a given song or sound (with descriptions, authors, and engagement stats).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/song-videos", "clipId": "7439295283975702544"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/song-videos', {'clipId': '7439295283975702544'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/song-videos", {
  "clipId": "7439295283975702544"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/song-videos", sandbase.Params{
	"clipId": "7439295283975702544",
})
```

Same call via the path form: `POST /v1/api/tiktok/song-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `clipId` | string | yes | The song ID found in TikTok music URLs (e.g. 7439295283975702544).  |
| `cursor` | string |  | Pagination cursor for retrieving the next page of results.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |

## Details

Returns a page of TikTok videos that use a given song or sound. Each video includes its description, author, hashtags, engagement counts and links. The input is the song ID (`clipId`) from a TikTok music URL.

### Use cases

- Track how far a new song spreads by listing the videos that use it and their `playCount` values.
- Find the most viral videos on a sound by sorting on `likeCount` or `shareCount`.
- Build a list of creators who use a track, using `authorHandle` and `authorUserId`.
- Collect the hashtags that appear alongside a sound to see which topics it is tied to.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/song-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"clipId": "7439295283975702544"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `clipId` | string | Yes | The song ID found in TikTok music URLs (e.g. 7439295283975702544). |
| `cursor` | string | No | Pagination cursor for retrieving the next page of results. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hasMore": 1,
    "nextCursor": "cur_H6EK-BtRQfER3uDYk3o7KA",
    "videos": [
      {
        "authorHandle": "sza",
        "authorImage": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/42b31651a14a0f…",
        "authorName": "SZA",
        "authorUserId": "7486547994222740523",
        "collectCount": 13557,
        "commentCount": 1640,
        "createTime": 1746917771,
        "description": "THANK YOU KENDRICK FOR COMING TO YESTERDAY’S @NotBeauty POP UP !!!! 🪲⛺️🫶🏾 @Ameri…",
        "durationSeconds": 23,
        "hashtags": [],
        "image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-p-0068-tx2/oMAj6PIBJAreJfqx…",
        "likeCount": 228029
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videos[].videoId / data.videos[].url` | The ID of the video and its public TikTok page link. |
| `data.videos[].description` | The caption text of the video, including mentions and emoji. |
| `data.videos[].hashtags[]` | Hashtags from the caption, without the `#` sign. The list is empty when the caption has none. |
| `data.videos[].authorHandle / data.videos[].authorName` | The handle and the display name of the creator who posted the video. |
| `data.videos[].authorUserId` | The numeric ID of the creator's account. |
| `data.videos[].playCount / data.videos[].likeCount / data.videos[].commentCount / data.videos[].shareCount / data.videos[].collectCount` | Engagement counts for the video: plays, likes, comments, shares and saves (collects). |
| `data.videos[].createTime` | When the video was posted, as a Unix timestamp in seconds. |
| `data.videos[].durationSeconds` | Length of the video in seconds. |
| `data.videos[].image / data.videos[].videoUrl / data.videos[].authorImage` | Links to the video cover image, the video file and the author's avatar. |
| `data.hasMore / data.nextCursor` | `hasMore` is `1` when more videos exist. `nextCursor` is the value to pass as `cursor` to get the next page. |

### Notes

- Find the song ID in a TikTok music URL. It is the long number at the end of the URL.
- To get the next page, send the same `clipId` with `cursor` set to the `data.nextCursor` value from the previous response.
- Add `requireFields: ["nextCursor"]` if you need every response to be able to return a next-page cursor. This can raise the price of the call.
- For details about the song itself, use [TikTok Music Details](/apis/tiktok/app-v3/music-detail). A similar video list is also available from [TikTok Music Video List](/apis/tiktok/app-v3/music-video-list).

### Pricing

Billed at the actual cost of each call, about $0.0006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/song-videos.json`](../../../catalog/models/tiktok/song-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/song-videos
