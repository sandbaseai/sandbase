# YouTube Shorts Search API: pricing, parameters and code examples

`youtube/search-shorts` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search YouTube Shorts by keyword and get matching Shorts (title, views, URL) with cursor pagination as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search-shorts", "query": "cats"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search-shorts', {'query': 'cats'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search-shorts", {
  "query": "cats"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search-shorts", sandbase.Params{
	"query": "cats",
})
```

Same call via the path form: `POST /v1/api/youtube/search-shorts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The keyword to search Shorts for.  |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `sortBy` | string |  | Sort order: "relevance" (default) or "popular" (most-viewed). one of: `relevance`, `popular`; default `"relevance"` |
| `uploadDate` | string |  | Filter by upload recency. Omit for any time. one of: `today`, `this_week`, `this_month`, `this_year` |

## Details

Returns YouTube Shorts that match a keyword. Each result has an ID, title, URL and view count. You only need a `query`, and you can sort, filter by upload date and page through results.

### Use cases

- Find the most-viewed Shorts for a topic by setting `sortBy` to `popular`.
- Track new Shorts about a brand or keyword by setting `uploadDate` to `today` or `this_week`.
- Build a list of Short URLs and IDs to pass to a video details lookup.
- Compare view counts across Shorts that cover the same topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "cats"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The keyword to search Shorts for. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `sortBy` | string | No | Sort order: "relevance" (default) or "popular" (most-viewed). |
| `uploadDate` | string | No | Filter by upload recency. Omit for any time. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_fPTLy4Ok3x74uh2aBTeYXQ",
    "shorts": [
      {
        "contentType": "short",
        "id": "M93h41hyPsM",
        "title": "Ranking Funny Cat Moment",
        "url": "https://www.youtube.com/watch?v=M93h41hyPsM",
        "views": 17000000,
        "viewsAvailable": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.shorts[]` | List of Shorts that match the query. |
| `data.shorts[].id` | YouTube video ID of the Short. |
| `data.shorts[].title` | Title of the Short. It can include hashtags and emoji. |
| `data.shorts[].url` | Watch URL for the Short, in the form `https://www.youtube.com/watch?v=<id>`. |
| `data.shorts[].views` | View count as a number. |
| `data.shorts[].viewsAvailable` | `true` when a view count was found for the Short. Check it before you use `views`. |
| `data.shorts[].contentType` | Type of the result. The value is `short` for these results. |
| `data.nextCursor` | Token for the next page of results. Send it as `cursor` in the next request. |
| `found` | `true` when the search returned results. |

### Notes

- For the next page, repeat the same request and add `cursor` with the value of `data.nextCursor`.
- Use the `id` value with [YouTube Video Details](/apis/youtube/video-detail) to get more data about a single Short.
- To list the Shorts of one channel instead of searching by keyword, use [YouTube Channel Shorts](/apis/youtube/channel-shorts).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/search-shorts.json`](../../../catalog/models/youtube/search-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/search-shorts
