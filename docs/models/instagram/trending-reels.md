# Instagram Trending Reels API: pricing, parameters and code examples

`instagram/trending-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

List currently trending Instagram reels. Instagram does not return play counts on this feed.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/trending-reels"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/trending-reels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/trending-reels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/trending-reels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/trending-reels` with the body above minus `model`.

## Details

This API returns a list of Instagram reels that are currently trending. It needs no input. Each reel includes its creator, caption, like and comment counts, and media links.

### Use cases

- Spot which topics and creators are getting attention on Instagram Reels right now.
- Collect trending captions, hashtags and mentions to feed a content idea list.
- Pull `videoUrl` and `image` links to build a gallery or review queue of trending clips.
- Track which verified accounts appear on the trending feed over repeated calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/trending-reels" \
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
    "reels": [
      {
        "avatarUrl": "https://scontent-ord5-1.cdninstagram.com/v/t51.82787-19/670420059_18588202909062…",
        "caption": "SHEEEEESH @stephencurry30",
        "comments": 5668,
        "createdUtc": 1793419180,
        "handle": "warriors",
        "hasAudio": true,
        "hashtags": [],
        "height": 1080,
        "id": "4019813681585443721",
        "image": "https://scontent-ord5-2.cdninstagram.com/v/t51.71878-15/882860826_36810059887168…",
        "likes": 628329,
        "mentions": [
          "@stephencurry30"
        ]
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.reels[]` | One trending reel. The list holds every reel on the feed. |
| `data.reels[].id / data.reels[].shortcode` | Identifiers for the reel. `shortcode` is the code that appears in the reel `url`. |
| `data.reels[].url` | Public Instagram link to the reel. |
| `data.reels[].caption` | Caption text of the reel. Some reels have no `caption` key. |
| `data.reels[].likes / data.reels[].comments` | Number of likes and comments on the reel. The feed gives no play count. |
| `data.reels[].createdUtc` | Time the reel was posted, as a Unix timestamp in seconds. |
| `data.reels[].handle / data.reels[].userId` | Username and numeric ID of the account that posted the reel. |
| `data.reels[].verified / data.reels[].private` | Whether the posting account is verified, and whether it is private. |
| `data.reels[].hashtags / data.reels[].mentions` | Hashtags and @mentions found in the caption, as lists of strings. Both can be empty. |
| `data.reels[].videoUrl / data.reels[].image / data.reels[].avatarUrl` | Links to the video file, the cover image and the poster's avatar. Use `width`, `height` and `hasAudio` to describe the video. |

### Notes

- This API takes no parameters. Send an empty JSON object `{}`.
- Pass a reel `url` or `shortcode` to [Instagram Post Details](/apis/instagram/post-detail) for more data on one reel.
- Use [Instagram Reel Transcript](/apis/instagram/reel-transcript) to get the spoken text of a reel.
- Use `handle` with [Instagram Profile](/apis/instagram/profile) to look up the creator.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/trending-reels.json`](../../../catalog/models/instagram/trending-reels.json) · Store page: https://www.sandbase.ai/model/instagram/trending-reels
