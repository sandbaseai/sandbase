# Kuaishou Video Search (V2) API: pricing, parameters and code examples

`kuaishou/app/search-video-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou videos matching a designated keyword query. Returns matching video results with support for cursor-based pagination across multiple pages.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-video-v2", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-video-v2', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-video-v2", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-video-v2", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Pagination cursor, empty for first page, pass pcursor from previous response default `""` |

## Details

Search Kuaishou videos by providing a query term in `keyword`. Page through additional result sets by supplying the `pcursor` value from previous responses.

### Use cases

- Find Kuaishou videos matching specific topic or product keywords.
- Track video content trends for brand names and industry terms.
- Retrieve continuous pages of video search results for external analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | — |
| `pcursor` | string | No | Pagination cursor, empty for first page, pass pcursor from previous response |

### Notes

- Leave `pcursor` empty for the first page, and pass the token from the previous response to retrieve the next page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-video-v2.json`](../../../../catalog/models/kuaishou/app/search-video-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-video-v2
