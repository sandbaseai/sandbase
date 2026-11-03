# YouTube Channel Live Streams API: pricing, parameters and code examples

`youtube/channel-lives` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List a YouTube channel's live and past-live streams by handle or channel ID with cursor pagination (title, views, length, publish time).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/channel-lives"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/channel-lives', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/channel-lives", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/channel-lives", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/channel-lives` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `handle` | string |  | YouTube channel handle.  |
| `channelId` | string |  | YouTube channel ID.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `lengthText`, and it is served only by a source that returns every…  |

## Details

Returns a list of a YouTube channel's live and past-live streams, with title, view count, length, and a relative publish time. Pass a channel `handle` such as `@IShowSpeed` or a `channelId`.

### Use cases

- Track how often a creator streams and how long each stream runs.
- Rank a channel's past live streams by view count to find its biggest broadcasts.
- Collect stream titles and thumbnails for a channel archive or dashboard.
- Feed stream video IDs into a video details or transcript lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/channel-lives" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "@IShowSpeed"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channelId` | string | No | YouTube channel ID. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `handle` | string | No | YouTube channel handle. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `lengthText`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "lives": [
      {
        "id": "IkhjzYsvCmw",
        "image": "https://i.ytimg.com/vi/IkhjzYsvCmw/hq720.jpg",
        "lengthText": "2:00:20",
        "publishedTime": "Streamed 2d ago",
        "title": "HALLOWEEN SPIDER-MAN SPEED-VERSE IRL STREAM 🎃🕷",
        "url": "https://www.youtube.com/watch?v=IkhjzYsvCmw",
        "views": 3700000
      }
    ],
    "nextCursor": "cur_iqioDVdrk2HZB14YevFECQ"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.lives[].id` | YouTube video ID of the live stream. |
| `data.lives[].title` | Title of the stream. |
| `data.lives[].url` | Full watch URL for the stream. |
| `data.lives[].image` | Thumbnail image URL. |
| `data.lives[].views` | View count as a number. |
| `data.lives[].lengthText` | Stream length as text, for example `2:00:20`. |
| `data.lives[].publishedTime` | Relative publish label such as `Streamed 2d ago`. It is not an exact timestamp. |
| `data.nextCursor` | Token for the next page of streams. Send it as `cursor` in the next request. |
| `found` | `true` when the channel lookup returned a result. |

### Notes

- Send either `handle` (with the leading `@`) or `channelId`.
- For the next page, pass `data.nextCursor` as `cursor` in the same request.
- Set `requireFields` to `["lengthText"]` only if you need `lengthText` on every stream. This can change which source serves the call and its price.
- To get more detail on a stream, pass its `id` to [YouTube Video Details](/apis/youtube/video-detail) or [YouTube Video Transcript](/apis/youtube/video-transcript).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/channel-lives.json`](../../../catalog/models/youtube/channel-lives.json) · Store page: https://www.sandbase.ai/model/youtube/channel-lives
