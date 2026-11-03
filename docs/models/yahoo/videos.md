# Yahoo Videos Search API: pricing, parameters and code examples

`yahoo/videos` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yahoo Videos results for a keyword: titles, thumbnails, durations and source sites.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/videos", "p": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/videos', {'p': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/videos", {
  "p": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/videos", sandbase.Params{
	"p": "coffee",
})
```

Same call via the path form: `POST /v1/api/yahoo/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `p` | string | yes | p  |

## Details

This API returns Yahoo video search results for a keyword. Each result has a title, duration, view count, thumbnail and the site that hosts the video. It needs one input, the search query `p`.

### Use cases

- Find the most viewed videos for a keyword to see what content ranks for a topic.
- Collect original video URLs from sites like YouTube for a content research list.
- Track related search terms to expand a keyword list for video content.
- Compare video titles and durations across queries to plan new video formats.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"p": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `p` | string | Yes | p |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "related_searches": [
    {
      "link": "https://video.search.yahoo.com/search/video;_ylt=A2RRXHqUkelq8gIAlhP7w8QF;_ylu=Y…",
      "position": 1,
      "thumbnail": "https://tse1.mm.bing.net/th?q=Best+Coffee&pid=Api&mkt=en-US&cc=US&setlang=en&adl…",
      "title": "Best coffee"
    }
  ],
  "videos_results": [
    {
      "duration": "05:35",
      "extracted_views": 3300000,
      "link": "https://video.search.yahoo.com/search/video;_ylt=A2RRXHqUkelq8gIApRP7w8QF;_ylu=Y…",
      "original": "https://www.youtube.com/watch?v=xQ156y4TtJs",
      "position": 1,
      "source": "youtube.com",
      "thumbnail": "https://up.yimg.com/ib/th/id/OVP.3w2J3ife7H_kW-PbU9Q-lAHgFo?pid=Api&h=360&w=480&…",
      "title": "How humanity got hooked on coffee - Jonathan Morris",
      "views": "3.3M views"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos_results[].title` | Title of the video. |
| `videos_results[].original` | URL of the video on the site that hosts it, such as a YouTube watch page. |
| `videos_results[].source` | Domain that hosts the video, for example `youtube.com`. |
| `videos_results[].duration` | Video length as a text string, for example `05:35`. |
| `videos_results[].views` | View count as shown in the result, for example `3.3M views`. |
| `videos_results[].extracted_views` | View count as a plain number, for example `3300000`. Use it for sorting and filtering. |
| `videos_results[].link / videos_results[].thumbnail` | `link` opens the result on Yahoo video search. `thumbnail` is the preview image URL. |
| `videos_results[].position` | Rank of the video in the results, starting at 1. |
| `related_searches[].title` | Suggested related search query. |
| `related_searches[].link / related_searches[].thumbnail` | `link` opens the related search on Yahoo video search. `thumbnail` is a preview image for it. |

### Notes

- Pass the search keyword in `p`. It is the only parameter and it is required.
- Use `extracted_views` when you need numbers. The `views` field is a display string such as `1.8K views`.
- To search for pictures instead of videos, use [Yahoo Images Search](/apis/yahoo/images).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo/videos.json`](../../../catalog/models/yahoo/videos.json) · Store page: https://www.sandbase.ai/model/yahoo/videos
