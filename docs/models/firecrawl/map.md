# Firecrawl URL Discovery API: pricing, parameters and code examples

`firecrawl/map` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0075 per call (free daily quota) · **Modes:** sync

Discovers and returns URLs found across a target website. Provide an HTTPS target address and define the maximum link count to map site pages.

## Pricing

- **$0.0075 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/map", "url": "https://docs.firecrawl.dev", "limit": 10}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/map', {'url': 'https://docs.firecrawl.dev', 'limit': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/map", {
  "url": "https://docs.firecrawl.dev",
  "limit": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/map", sandbase.Params{
	"url": "https://docs.firecrawl.dev",
	"limit": 10,
})
```

Same call via the path form: `POST /v1/api/firecrawl/map` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The HTTPS URL to map.  |
| `limit` | integer | yes | Maximum number of links to discover. range 1–100000 |

## Details

Map website architecture and discover internal links using `url` and `limit`.

### Use cases

- Discover reachable pages across an entire domain.
- Map site link structures for search and content indexers.
- Extract lists of internal website endpoints prior to scraping.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/map" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://docs.firecrawl.dev", "limit": 10}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The HTTPS URL to map. |
| `limit` | integer | Yes | Maximum number of links to discover. |

### Notes

- Requires a valid HTTPS address for `url`.
- Set `limit` to specify the maximum number of links to discover.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/map.json`](../../../catalog/models/firecrawl/map.json) · Store page: https://www.sandbase.ai/model/firecrawl/map
