# Bing Videos Search API: pricing, parameters and code examples

`bing/videos` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Bing Videos results for a keyword: titles, thumbnails, durations, views and source sites.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/videos", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/videos', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/videos", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/videos", sandbase.Params{
	"q": "coffee",
})
```

Same call via the path form: `POST /v1/api/bing/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |

## Details

Returns Bing video search results for a keyword. It gives a list of regular videos and a list of short videos, each with title, channel, source platform, view count and a link. The only input is the search keyword in `q`.

### Use cases

- Find which TikTok and other channels publish the most viewed videos for a keyword.
- Track how popular a topic is by comparing `extracted_views` across the top results.
- Collect video titles, thumbnails and links to build a content feed for a topic.
- Find short-form video ideas by reading the `shorts_results` list for a niche keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | q |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "shorts_results": [
    {
      "channel": "yourcoffeedude",
      "date": "1 week ago",
      "duration": "1:34",
      "extracted_views": 157100,
      "link": "https://www.bing.com/videos/search?q=coffee&view=detail&mid=BD8FFCFD1A1E73F81D41…",
      "position": 1,
      "source": "TikTok",
      "title": "3 Fancy Iced Coffee Recipes: Snickers, Brown Sugar & Maple Butter",
      "views": "157.1K views"
    }
  ],
  "video_results": [
    {
      "channel": "yourcoffeedude",
      "date": "1 week ago",
      "extracted_views": 157100,
      "length": "1:34",
      "link": "https://www.tiktok.com/@yourcoffeedude/video/7699133225892973856",
      "position": 1,
      "source": "TikTok",
      "thumbnail": "https://tse1.mm.bing.net/th/id/OVP.tfYqTMGP_vXgr_qNA9amhQEkII?w=354&h=199&c=7&rs…",
      "title": "3 Fancy Iced Coffee Recipes: Snickers, Brown Sugar & Maple Butter",
      "views": "157.1K views"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_results[].title` | Title of the video. |
| `video_results[].link` | Direct URL of the video on its source platform. |
| `video_results[].channel` | Name or handle of the channel that posted the video. |
| `video_results[].source` | Platform where the video is hosted, for example `TikTok`. |
| `video_results[].views / video_results[].extracted_views` | View count as display text (for example `157.1K views`) and as a plain number (for example `157100`). |
| `video_results[].length` | Video duration as text, for example `1:34`. |
| `video_results[].thumbnail` | URL of a thumbnail image for the video. |
| `video_results[].date` | Relative posting time as text, for example `1 week ago`. |
| `video_results[].position` | Rank of the video in the list, starting at 1. |
| `shorts_results[].link` | Bing video detail page URL for the short video, not the source platform URL. |
| `shorts_results[].duration` | Duration of the short video as text. |

### Notes

- Pass the search keyword in `q`. It is the only parameter and it is required.
- `shorts_results` and `video_results` can list the same videos. Use `video_results[].link` for the direct source URL.
- `date` is relative text such as `1 week ago`, not a timestamp.
- To search images for the same keyword, call [Bing Images Search](/apis/bing/images).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/videos.json`](../../../catalog/models/bing/videos.json) · Store page: https://www.sandbase.ai/model/bing/videos
