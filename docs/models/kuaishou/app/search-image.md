# Kuaishou Image Post Search API: pricing, parameters and code examples

`kuaishou/app/search-image` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Searches Kuaishou image posts matching a specified search term. Returns feed details including captions, engagement metrics, and pagination tokens.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-image", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-image', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-image", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-image", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Search for Kuaishou image feeds by passing a query string in `keyword`. Supports cursor-based pagination through the `pcursor` parameter.

### Use cases

- Find relevant image content on Kuaishou based on specific keywords.
- Track user engagement statistics such as comment and collection counts for image feeds.
- Page through discovery search results using cursor tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | — |
| `pcursor` | string | No | Cursor, empty for first page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "feeds": [
    {
      "atmosphereType": 0,
      "itemType": 5,
      "rank": 0,
      "feed": {
        "caption": "下一家万亿美元公司，会是谁？  anthropic、OpenAI、字节跳动、宇树科技...12家最值得关注的科技独角兽(2026年8月最新版)赶紧收藏!  #IPO #Anthr…",
        "captionToComment": "下一家万亿美元公司，会是谁？  anthropic、OpenAI、字节跳动、宇树科技...12家最值得关注的科技独角兽(2026年8月最新版)赶紧收藏!  #IPO #Anthr…",
        "clearScreenSameAuthorCount": 709,
        "collect_count": 17,
        "comment_count": 5,
        "disableCommentDislike": false
      }
    }
  ]
}
```

### Notes

- Leave `pcursor` empty to retrieve the first page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-image.json`](../../../../catalog/models/kuaishou/app/search-image.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-image
