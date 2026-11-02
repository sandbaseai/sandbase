# Tavily Site Map API: pricing, parameters and code examples

`tavily/map` · data API · Tavily · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call · **Modes:** sync

Discovers the URL structure of a target website without extracting full page content. Accepts a starting URL, maximum traversal depth, and URL discovery limits.

## Pricing

- **$0.012 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tavily/map", "limit": 10, "url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tavily/map', {'limit': 10, 'url': 'https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tavily/map", {
  "limit": 10,
  "url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tavily/map", sandbase.Params{
	"limit": 10,
	"url": "https://static.sandbase.ai/examples/b1ca8e2d-8fe7-4358-99d8-4dac64d43e91/input/73ac2081-9c93-4d56-a0c0-0d23d590e501.com",
})
```

Same call via the path form: `POST /v1/api/tavily/map` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The starting URL to map.  |
| `limit` | integer |  | Maximum number of URLs to discover. range 1–1000 |
| `max_depth` | integer |  | Maximum traversal depth from the starting URL. range 1–5 |

## Details

Maps website URL structures starting from a target `url`. Controls discovery bounds using optional `limit` and `max_depth` parameters.

### Use cases

- Map domain architectures before targeted content extraction.
- Discover all accessible subpages across a specific website.
- Audit site navigation depth and internal link structures.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/map" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The starting URL to map. |
| `limit` | integer | No | Maximum number of URLs to discover. |
| `max_depth` | integer | No | Maximum traversal depth from the starting URL. |

### Notes

- Configure `limit` to restrict the maximum number of discovered URLs.
- Use `max_depth` to define how many levels deep traversal continues from `url`.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tavily/map.json`](../../../catalog/models/tavily/map.json) · Store page: https://www.sandbase.ai/model/tavily/map
