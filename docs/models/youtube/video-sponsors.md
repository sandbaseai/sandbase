# YouTube Video Sponsors API: pricing, parameters and code examples

`youtube/video-sponsors` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Detect suspected sponsors and paid promotions in a YouTube video by URL (sponsor names, websites, confidence).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-sponsors", "url": "https://www.youtube.com/watch?v=AVO0ifle-OU"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-sponsors', {'url': 'https://www.youtube.com/watch?v=AVO0ifle-OU'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-sponsors", {
  "url": "https://www.youtube.com/watch?v=AVO0ifle-OU"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-sponsors", sandbase.Params{
	"url": "https://www.youtube.com/watch?v=AVO0ifle-OU",
})
```

Same call via the path form: `POST /v1/api/youtube/video-sponsors` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | YouTube video or Short URL.  |
| `language` | string |  | 2-letter language code for transcript lookup (e.g. en, es, fr).  |

## Details

Returns whether a YouTube video or Short looks like a paid promotion, plus a list of suspected sponsors with their websites and a confidence level. It also returns basic video and channel details. It needs a video URL.

### Use cases

- Check whether a creator's video contains a paid promotion before you cite it in a report.
- Build a list of brands that sponsor videos in a niche by running many video URLs.
- Flag sponsored videos in an influencer vetting or ad tracking tool.
- Find the website of a sponsor named in a video so you can match it to a brand record.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-sponsors" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=AVO0ifle-OU"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | YouTube video or Short URL. |
| `language` | string | No | 2-letter language code for transcript lookup (e.g. en, es, fr). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorAvatarUrl": "https://yt3.ggpht.com/qmx-SPJT3bDScwd8KC4APZP82cpOoMN1b-kqdl5eASn8pub6jSBxWpq3OO…",
    "authorHandle": "letsKWOOWK",
    "authorId": "UC3vQEjRhwgH2HAOBKwLjxNA",
    "authorName": "KWOOWK",
    "authorUrl": "https://www.youtube.com/@letsKWOOWK",
    "detectionStatus": "found",
    "isPaidPromotion": true,
    "suspectedSponsors": [
      {
        "confidence": "medium",
        "name": "Betterhelp",
        "website": "betterhelp.com"
      }
    ],
    "title": "Why You Should Meal Prep Like A Restaurant",
    "url": "https://www.youtube.com/watch?v=AVO0ifle-OU",
    "videoId": "AVO0ifle-OU"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.isPaidPromotion` | `true` when the video is flagged as a paid promotion. |
| `data.detectionStatus` | Result of the sponsor check. The sample shows `found` when sponsors were detected. |
| `data.suspectedSponsors[].name` | Name of the suspected sponsor. |
| `data.suspectedSponsors[].website` | Website of the suspected sponsor, given as a domain. |
| `data.suspectedSponsors[].confidence` | Confidence level for that sponsor match. The sample shows `medium`. |
| `data.title` | Title of the video. |
| `data.videoId / data.url` | Video ID and full URL of the video that was checked. |
| `data.authorName / data.authorHandle` | Display name and handle of the channel that posted the video. |
| `data.authorId / data.authorUrl` | Channel ID and channel URL of the author. |
| `found` | `true` when the lookup returned a result for the video. |

### Notes

- Pass the full video or Short link in `url`. The optional `language` parameter takes a 2-letter code such as `en` and sets the transcript language used for the lookup.
- Channel IDs such as `UC3vQEjRhwgH2HAOBKwLjxNA` start with `UC`. Use `data.authorId` or the handle to look up the channel with [YouTube Channel](/apis/youtube/channel).
- To read the video itself, call [YouTube Video Details](/apis/youtube/video-detail) or [YouTube Video Transcript](/apis/youtube/video-transcript).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/video-sponsors.json`](../../../catalog/models/youtube/video-sponsors.json) · Store page: https://www.sandbase.ai/model/youtube/video-sponsors
