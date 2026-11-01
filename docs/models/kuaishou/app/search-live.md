# Kuaishou Livestream Search

`kuaishou/app/search-live` · api · Kuaishou

Searches Kuaishou livestreams using a specified search term. Returns matching active broadcast rooms with cursor pagination support.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-live", "keyword": "带货"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-live', {'keyword': '带货'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-live", {
  "keyword": "带货"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-live", sandbase.Params{
	"keyword": "带货",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Cursor, empty for first page default `""` |

## Details

Query active broadcast rooms on Kuaishou by providing a `keyword`. Supports cursor-based pagination through the `pcursor` parameter.

### Use cases

- Discover ongoing broadcast rooms related to specific topics.
- Monitor streaming activity for designated keywords.
- Track relevant broadcast sessions across paginated query results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-live" \
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

- Pass an empty string to `pcursor` to retrieve the first page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-live.json`](../../../../catalog/models/kuaishou/app/search-live.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-live
