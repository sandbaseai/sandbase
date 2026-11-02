# Bilibili Hot Searches API: pricing, parameters and code examples

`bilibili/web/hot-search` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current trending search keywords along with their heat scores from Bilibili. Results are restricted according to the specified count limit.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/hot-search", "limit": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/hot-search', {'limit': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/hot-search", {
  "limit": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/hot-search", sandbase.Params{
	"limit": 10,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | Return number  |

## Details

Look up real-time trending search topics and heat scores on Bilibili. Specify the desired quantity of items using the `limit` parameter.

### Use cases

- Monitor trending topics and viral search terms across Bilibili.
- Analyze audience interest levels using trending heat scores.
- Supply search suggestion widgets with top community queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | Yes | Return number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "trending": {
      "list": [
        {
          "heat_score": 4248008,
          "keyword": "当你意识到来不及写国庆作业时"
        }
      ]
    }
  }
}
```

### Notes

- Use `limit` to control the number of trending search keywords returned.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/hot-search.json`](../../../../catalog/models/bilibili/web/hot-search.json) · Store page: https://www.sandbase.ai/model/bilibili/web/hot-search
