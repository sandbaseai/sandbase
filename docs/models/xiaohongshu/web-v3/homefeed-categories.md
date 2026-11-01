# Xiaohongshu (RED) Homepage Categories

`xiaohongshu/web-v3/homefeed-categories` · api · Xiaohongshu

Returns a list of available homefeed category channels on Xiaohongshu (RED). Use this endpoint to inspect valid category identifiers for content discovery.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/homefeed-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/homefeed-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/homefeed-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/homefeed-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/homefeed-categories` with the body above minus `model`.

## Details

Call this endpoint to retrieve the full list of homefeed category channels available on Xiaohongshu (RED). The request requires no query parameters.

### Use cases

- Populate channel navigation menus in client applications.
- Discover valid category identifiers for homefeed content exploration.
- Track changes to top-level content channels across the platform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/homefeed-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/model/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Web Note Details](/model/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.
- [Xiaohongshu (RED) Search Suggestions](/model/xiaohongshu/web-v3/search-suggest): Returns search query suggestions and autocomplete terms from Xiaohongshu (RED).

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/homefeed-categories.json`](../../../../catalog/models/xiaohongshu/web-v3/homefeed-categories.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/homefeed-categories
