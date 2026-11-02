# Kuaishou Music Search API: pricing, parameters and code examples

`kuaishou/app/search-music` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou music tracks by song name or artist keyword. Returns matched audio results with support for cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-music", "keyword": "周杰伦"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-music', {'keyword': '周杰伦'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-music", {
  "keyword": "周杰伦"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-music", sandbase.Params{
	"keyword": "周杰伦",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-music` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Query Kuaishou music tracks by specifying a search term in `keyword`. Supports cursor pagination across search results using `pcursor`.

### Use cases

- Search for specific songs or artists on Kuaishou
- Discover background audio tracks matching query terms
- Paginate through music catalog search results

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-music" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | — |
| `pcursor` | string | No | Cursor, empty for first page |

### Notes

- Leave `pcursor` empty to retrieve the first page of results, or supply the cursor string for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-music.json`](../../../../catalog/models/kuaishou/app/search-music.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-music
