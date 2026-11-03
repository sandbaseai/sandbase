# YouTube Trending Shorts API: pricing, parameters and code examples

`youtube/trending-shorts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List currently trending YouTube Shorts (title, channel, views, likes, duration).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/trending-shorts"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/trending-shorts', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/trending-shorts", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/trending-shorts", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/trending-shorts` with the body above minus `model`.

## Details

Returns a list of YouTube Shorts that are currently trending. It needs no input: send an empty JSON object `{}`. Each item has the title, channel, view, like and comment counts, duration, and links.

### Use cases

- Spot which Shorts are gaining views right now to find topics for your own content.
- Track the channels and categories that appear most often in the trending list.
- Build a dashboard or feed that shows trending Shorts with thumbnails and links.
- Collect channel IDs from trending Shorts and pass them to a channel lookup for deeper research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/trending-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "shorts": [
      {
        "authorHandle": "globalmindapparel",
        "authorId": "UC2pn4FHmt3Td-A2kkhcYAqg",
        "authorUrl": "https://www.youtube.com/@globalmindapparel",
        "category": "People & Blogs",
        "channelTitle": "Global Mind Apparel",
        "comments": 16000,
        "createdUtc": 1790109026,
        "duration": "00:02:24",
        "durationMs": 144000,
        "id": "jm-1NeOounQ",
        "image": "https://img.youtube.com/vi/jm-1NeOounQ/maxresdefault.jpg",
        "likes": 321806
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.shorts[].id` | The YouTube video ID of the Short. |
| `data.shorts[].title` | The title of the Short. |
| `data.shorts[].url` | Link to the Short on YouTube. |
| `data.shorts[].image` | Thumbnail image URL for the Short. |
| `data.shorts[].views / likes / comments` | Counts of views, likes and comments on the Short. |
| `data.shorts[].duration / durationMs` | Length of the Short as an `HH:MM:SS` string and in milliseconds. |
| `data.shorts[].channelTitle / authorHandle` | Display name and `@` handle of the channel that posted the Short. |
| `data.shorts[].authorId / authorUrl` | The channel ID (starts with `UC`) and the channel page URL. |
| `data.shorts[].category` | The YouTube category of the Short, for example `Entertainment`. |
| `data.shorts[].createdUtc` | Creation time of the Short as a Unix timestamp in seconds. |

### Notes

- The endpoint takes no parameters. Send `{}` as the body.
- Use `authorId` with [YouTube Channel](/apis/youtube/channel) or [YouTube Channel Shorts](/apis/youtube/channel-shorts) to look at the channel behind a Short.
- Pass `id` to [YouTube Video Details](/apis/youtube/video-detail) to get more data about a single Short.
- `duration` can be longer than one minute, so check `durationMs` if you need to filter by length.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/trending-shorts.json`](../../../catalog/models/youtube/trending-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/trending-shorts
