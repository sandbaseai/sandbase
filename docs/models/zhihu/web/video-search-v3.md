# Zhihu Video Search (V3) API: pricing, parameters and code examples

`zhihu/web/video-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns Zhihu video search results matching a specified keyword. Supports pagination using offset and limit parameters, and accepts a search hash ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/video-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/video-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/video-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/video-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/video-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of videos per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Search for Zhihu videos by providing a query in `keyword`. Control result paging through `offset` and `limit`.

### Use cases

- Search Zhihu videos related to specific topics or keywords.
- Retrieve video metadata such as play counts, comments, and durations.
- Paginate through video search results for content monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/video-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of videos per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": "1634622855538356224",
      "type": "zvideo",
      "highlight": {
        "description": "起底OpenAI：从人类救世主到“微软的附庸”",
        "title": "OpenAI到底是一家怎样的公司？"
      },
      "object": {
        "comment_count": 0,
        "cover_url": "https://pic1.zhimg.com/v2-96167a53ed8bb7c4a3842263b1deee69.jpg?source=4e949a73",
        "description": "起底OpenAI：从人类救世主到“微软的附庸”",
        "duration": 913.641,
        "favorites_count": 8,
        "play_count": 9562
      }
    }
  ]
}
```

### Notes

- Use `limit` to set the number of videos returned per page.
- Use `offset` for result pagination.
- Pass `search_hash_id` when tracking search sessions.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/video-search-v3.json`](../../../../catalog/models/zhihu/web/video-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/video-search-v3
