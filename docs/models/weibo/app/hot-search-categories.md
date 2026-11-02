# Weibo Hot Search Categories API: pricing, parameters and code examples

`weibo/app/hot-search-categories` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns all available hot search categories from Weibo. Enables browsing trending topics segmented by specific Weibo category classifications.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/hot-search-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/hot-search-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/hot-search-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/hot-search-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/weibo/app/hot-search-categories` with the body above minus `model`.

## Details

Retrieves the full list of Weibo hot search categories without requiring query parameters. Use this endpoint to look up available category classifications for trending content.

### Use cases

- Discover available category options for segmenting hot search feeds.
- Populate category filter dropdowns in social analytics dashboards.
- Map hot search content across specific Weibo topic classifications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/hot-search-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/hot-search-categories.json`](../../../../catalog/models/weibo/app/hot-search-categories.json) · Store page: https://www.sandbase.ai/model/weibo/app/hot-search-categories
