# Hacker News Search API: pricing, parameters and code examples

`hacker-news/search` · data API · Hacker News · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Search Hacker News by keyword - matching stories with title, link, author, points, and comment count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/search", "query": "ai"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/search', {'query': 'ai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/search", {
  "query": "ai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/search", sandbase.Params{
	"query": "ai",
})
```

Same call via the path form: `POST /v1/api/hacker-news/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tags` | string |  | Optional result filter, e.g. "story" or "comment".  |
| `query` | string | yes | Search keyword, e.g. "ai".  |

## Details

Returns Hacker News items that match a keyword. Each result has the title, link, author, points, comment count, and creation time. The only required input is `query`.

### Use cases

- Track how often a topic such as AI reaches Hacker News and how many points those posts earn.
- Find the most discussed Hacker News posts about a product or company name.
- Collect source URLs shared on Hacker News for a keyword to build a reading list.
- Filter results with `tags` to look only at stories or only at comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ai"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword, e.g. "ai". |
| `tags` | string | No | Optional result filter, e.g. "story" or "comment". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "results": [
      {
        "author": "usefulposter",
        "comments": 1668,
        "createdUtc": 1773257369,
        "id": "47340079",
        "permalink": "https://news.ycombinator.com/item?id=47340079",
        "points": 4229,
        "title": "Don't post generated/AI-edited comments. HN is for conversation between humans",
        "url": "https://news.ycombinator.com/newsguidelines.html#generated"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.results[].title` | Title of the Hacker News post. |
| `data.results[].url` | Link the post points to. This is the external page or guideline the author shared. |
| `data.results[].permalink` | Link to the item's discussion page on Hacker News. |
| `data.results[].id` | Hacker News item ID, returned as a string. |
| `data.results[].author` | Hacker News username of the person who posted the item. |
| `data.results[].points` | Score of the post. |
| `data.results[].comments` | Number of comments on the post. |
| `data.results[].createdUtc` | Creation time as a Unix timestamp in seconds. |
| `found` | `true` when the search returned results. |

### Notes

- Set `tags` to a value such as `story` or `comment` to filter the result type.
- Use the `id` value from a result as the input for [Hacker News Story](/apis/hacker-news/story) to get one post, or [Hacker News Story Comments](/apis/hacker-news/story-comments) to read its discussion.
- Pass an author name from `author` to [Hacker News Profile](/apis/hacker-news/profile) to look up that user.

### Pricing

Billed at the actual cost of each call, about $0.0015 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hacker-news/search.json`](../../../catalog/models/hacker-news/search.json) · Store page: https://www.sandbase.ai/model/hacker-news/search
