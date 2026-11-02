# Y Combinator Person Detail API: pricing, parameters and code examples

`ycombinator/person-detail` · data API · Y Combinator · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get a detailed profile for a YC partner by slug. Returns full biography, achievement stats, associated companies, blog posts, press articles, tweets, and videos.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ycombinator/person-detail", "slug": "garry-tan"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ycombinator/person-detail', {'slug': 'garry-tan'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ycombinator/person-detail", {
  "slug": "garry-tan"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ycombinator/person-detail", sandbase.Params{
	"slug": "garry-tan",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ycombinator/person-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | YC partner slug (e.g. 'garry-tan', 'michael-seibel', 'jared-friedman'). Obtain from get_partners results.  |

## Details

Get a detailed profile for a YC partner by slug. Returns full biography, achievement stats, associated companies, blog posts, press articles, tweets, and videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/ycombinator/person-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "garry-tan"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | YC partner slug (e.g. 'garry-tan', 'michael-seibel', 'jared-friedman'). Obtain from get_partners results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ycombinator/person-detail.json`](../../../catalog/models/ycombinator/person-detail.json) · Store page: https://www.sandbase.ai/model/ycombinator/person-detail
