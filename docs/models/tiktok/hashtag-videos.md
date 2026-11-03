# TikTok Hashtag Videos API: pricing, parameters and code examples

`tiktok/hashtag-videos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List recent TikTok videos for a hashtag (creator, caption, views, likes, shares).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/hashtag-videos", "hashtag": "cooking"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/hashtag-videos', {'hashtag': 'cooking'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/hashtag-videos", {
  "hashtag": "cooking"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/hashtag-videos", sandbase.Params{
	"hashtag": "cooking",
})
```

Same call via the path form: `POST /v1/api/tiktok/hashtag-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). range 1–20 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of videos.  |
| `hashtag` | string | yes | TikTok hashtag to fetch videos for, without the # prefix (e.g. booktok).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `playCount`, and it is served only by a source that returns every…  |

## Details

Returns a page of recent TikTok videos posted under a hashtag. Each video includes the creator, caption, hashtags, sound, and view, like, comment, share and save counts. The only required input is the `hashtag`, written without the # prefix.

### Use cases

- Track which creators and videos get the most views under a niche hashtag such as `cooking`.
- Collect captions and co-used hashtags to find related tags for a content plan.
- Compare `playCount` and `likeCount` across videos to spot posts that perform well for a topic.
- Find which sounds are used most often in a hashtag's videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/hashtag-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "hashtag": "cooking"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | TikTok hashtag to fetch videos for, without the # prefix (e.g. booktok). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of videos. |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `playCount`, and it is served only by a source that returns every one  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "authorFollowers": 251600,
        "authorHandle": "gisellecooks_",
        "authorImage": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/a9c98a411138142ad07…",
        "authorName": "gisellecooks",
        "authorUserId": "6853687020456412166",
        "authorVerified": false,
        "collectCount": 477771,
        "commentCount": 4304,
        "createdUtc": 1789585739,
        "durationSeconds": 60,
        "hashtags": [
          "smores"
        ],
        "id": "7686212146052549902"
      }
    ],
    "nextCursor": "cur_5xH-mglA6e0Rvv0_mI_L-w"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id / data.items[].url` | The video ID and the link to the video page on TikTok. |
| `data.items[].text` | The video caption, including its hashtags. |
| `data.items[].hashtags[]` | Hashtag names used on the video, without the # prefix. The list can be empty. |
| `data.items[].playCount / likeCount / commentCount / shareCount / collectCount` | Engagement counts for the video: plays, likes, comments, shares and saves. Values for large videos can be rounded. |
| `data.items[].authorHandle / authorName / authorUserId` | The creator's handle, display name and numeric user ID. |
| `data.items[].authorFollowers / authorVerified` | The creator's follower count and whether the account is verified. |
| `data.items[].createdUtc / durationSeconds` | When the video was posted, as a Unix timestamp in seconds, and its length in seconds. |
| `data.items[].soundTitle / soundAuthor / soundClipId` | The title, author and ID of the sound used in the video. |
| `data.items[].videoUrl / image / authorImage` | Links to the video file, the cover image and the creator's avatar. |
| `data.nextCursor` | Cursor for the next page of videos. |

### Notes

- Pass `hashtag` without the # prefix, for example `cooking`.
- To get more videos, send `data.nextCursor` as `cursor` in the next request. `limit` accepts 1 to 20.
- `requireFields` limits serving to a source that returns every field you name, such as `playCount` or `soundClipId`. It can raise the price of the call.
- For a single video in more detail, use [TikTok Video Details](/apis/tiktok/app-v3/one-video). For tag-level stats, use [TikTok Hashtag Detail](/apis/tiktok/app-v3/hashtag-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/hashtag-videos.json`](../../../catalog/models/tiktok/hashtag-videos.json) · Store page: https://www.sandbase.ai/model/tiktok/hashtag-videos
