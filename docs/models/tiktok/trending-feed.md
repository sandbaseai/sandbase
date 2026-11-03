# TikTok Trending Feed API: pricing, parameters and code examples

`tiktok/trending-feed` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Sample TikTok's For You feed as served to a viewer in one country (caption, views, likes, comments, author). Returns a rotating sample, not a ranked chart.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/trending-feed", "region": "US"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/trending-feed', {'region': 'US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/trending-feed", {
  "region": "US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/trending-feed", sandbase.Params{
	"region": "US",
})
```

Same call via the path form: `POST /v1/api/tiktok/trending-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `trim` | string |  | Set to true to return a simplified response.  |
| `region` | string | yes | 2-letter country code for the proxy location (e.g. "US").  |

## Details

Returns a sample of videos from TikTok's For You feed as served to a viewer in one country. Each video includes the caption, author, view, like, comment, save and share counts, sound details and links. The only required input is a 2-letter `region` code.

### Use cases

- Spot what kind of content TikTok is showing to viewers in a given country right now.
- Collect sample captions and hashtags to study content styles in a market.
- Track the engagement counts of videos that appear in a country's feed.
- Find authors and sounds that show up in the feed, then look them up in more detail.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/trending-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"region": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | Yes | 2-letter country code for the proxy location (e.g. "US"). |
| `trim` | string | No | Set to true to return a simplified response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "videos": [
      {
        "author": "sampletok.store",
        "authorImage": "https://p16-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/53a084b13e8c4b8d037…",
        "authorName": "SampleTok",
        "authorUserId": "7565970382990869526",
        "caption": "#sampletok 💋 Free e.l.f. Glow Reviver Melting Lip Balm alert! 😍✨ Melt-in moistur…",
        "comments": 1551,
        "createdUtc": 1788564307,
        "durationSeconds": 5,
        "hashtags": [
          "sampletok"
        ],
        "id": "7681825159417810208",
        "image": "https://p16-common-sign.tiktokcdn-us.com/tos-useast2a-p-0037-euttp/o0kf4AYbpmTNr…",
        "likes": 59833
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videos[].id` | Video ID as a string of digits. Use it to look up the video in other APIs. |
| `data.videos[].url` | Link to the video page on TikTok. |
| `data.videos[].caption` | Text posted with the video. Long captions can include hashtags inline. |
| `data.videos[].hashtags` | List of hashtag names from the caption, without the `#` sign. |
| `data.videos[].views / likes / comments / saves / shares` | Engagement counts for the video. |
| `data.videos[].author / authorName / authorUserId` | The account handle, its display name and its numeric user ID. |
| `data.videos[].createdUtc` | Time the video was posted, as a Unix timestamp in seconds. |
| `data.videos[].durationSeconds` | Length of the video in seconds. |
| `data.videos[].region` | 2-letter country code attached to the video. It can differ from the requested `region`. |
| `data.videos[].soundTitle / soundAuthor / soundClipId` | Name, author and ID of the sound used in the video. |
| `data.videos[].image / videoUrl / authorImage` | Links to the cover image, the video file and the author's avatar. |

### Notes

- `region` is required. Use a 2-letter country code such as `US`.
- The result is a rotating sample, so repeated calls can return different videos. It is not a ranked chart.
- Set `trim` to `true` to get a simplified response.
- To get more detail on a video from this feed, pass its `id` to [TikTok Video Details](/apis/tiktok/app-v3/one-video). To see trending tags, use [TikTok Trending Hashtags](/apis/tiktok/ads/trends-hashtag-list).

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/trending-feed.json`](../../../catalog/models/tiktok/trending-feed.json) · Store page: https://www.sandbase.ai/model/tiktok/trending-feed
