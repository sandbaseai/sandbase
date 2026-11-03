# Pipixia Hot Search Words API: pricing, parameters and code examples

`pipixia/app/hot-search-words` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current list of trending search keywords from Pipixia. Helps track popular search topics and user query trends across the platform without requiring input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-words"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-words', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-words", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-words", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-words` with the body above minus `model`.

## Details

This endpoint returns current trending search queries from the Pipixia app without requiring any request parameters.

### Use cases

- Track current trending search queries on Pipixia.
- Analyze rising content topics and audience search interest.
- Power search suggestion interfaces with real-time platform trend data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-words" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Notes

- This endpoint does not require any request parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-words.json`](../../../../catalog/models/pipixia/app/hot-search-words.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-words
