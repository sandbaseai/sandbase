# TikTok Video API: pricing, parameters and code examples

`tiktok/video` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0004 per call · **Modes:** sync

Fetch a single TikTok video by URL with its caption and engagement counts (views, likes, comments, shares, saves).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0004**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/video"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/video', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/video", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/video", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | TikTok video ID, the numeric run at the end of a video URL. Use it when a listing SKU handed you an id and no URL.  |
| `url` | string |  | Full TikTok video URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of…  |

## Details

Returns one TikTok video with its caption, author details, sound details and engagement counts. Send either the full video `url` or the numeric video `id`.

### Use cases

- Track the views, likes and shares of a single video over repeated checks.
- Pull the caption, author handle and sound name to log a video in a content database.
- Get the `videoUrl` or `sdVideoUrl` link for a video you want to review or archive.
- Check engagement on a video that a listing or partner handed you as a bare `id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@mrbeast/video/7654638524729216287?_r=1&u_code=elgjf3ff8cajhk&preview_pb=0&sharer_language=en&_d=elh6737j6kjl71&share_item_id=7654638524729216287&source=h5_m"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | TikTok video ID, the numeric run at the end of a video URL. Use it when a listing SKU handed you an id and no URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of t |
| `url` | string | No | Full TikTok video URL. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorFollowers": null,
    "authorHandle": "mrbeast",
    "authorImage": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/1e2348ca19d3940…",
    "authorName": "MrBeast",
    "authorUserId": "6614519312189947909",
    "authorVerified": null,
    "caption": "I raced Usain Bolt 😅",
    "comments": 48862,
    "createdUtc": 1782234434,
    "durationSeconds": 24,
    "hashtags": [],
    "id": "7654638524729216287"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `views` | Number of views on the video. |
| `likes / comments / shares / saves` | Engagement counts for the video. |
| `caption` | Text written by the creator for the video. |
| `authorHandle / authorName / authorUserId` | Handle, display name and numeric user ID of the creator. |
| `createdUtc` | Time the video was posted, as a Unix timestamp in seconds. |
| `durationSeconds` | Length of the video in seconds. |
| `videoUrl / sdVideoUrl` | Links to the video file and to a standard-definition version of it. |
| `soundTitle / soundAuthor / soundClipId` | Name, author and ID of the sound used in the video. |
| `authorFollowers / authorVerified` | Follower count and verified status of the author. Both can be `null` when the serving source does not return them. |
| `found` | `true` when the video was found. |

### Notes

- Pass either `url` or `id`. The `id` is the numeric run at the end of a video URL, such as `7654638524729216287`.
- Share parameters in the URL query string, such as `_r` and `share_item_id`, are accepted. The response `url` is the clean form without them.
- To get `authorFollowers` or `authorVerified` filled in, list them in `requireFields`. This can route the call to a dearer source.
- For more detail on a video, try [TikTok Video Details](/apis/tiktok/app-v3/one-video) or [TikTok Video Metrics](/apis/tiktok/analytics/video-metrics).

### Pricing

Billed at the actual cost of each call, about $0.0004 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/video.json`](../../../catalog/models/tiktok/video.json) · Store page: https://www.sandbase.ai/model/tiktok/video
