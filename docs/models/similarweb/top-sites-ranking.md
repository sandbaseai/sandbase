# Similarweb Top Sites Ranking API: pricing, parameters and code examples

`similarweb/top-sites-ranking` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.075 per call · **Modes:** sync

Get the top-ranked websites worldwide or in a category, ordered by traffic rank.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.075 * Math.max(1.0, Math.min(20.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/top-sites-ranking", "category": "all", "limit": 3}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/top-sites-ranking', {'category': 'all', 'limit': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/top-sites-ranking", {
  "category": "all",
  "limit": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/top-sites-ranking", sandbase.Params{
	"category": "all",
	"limit": 3,
})
```

Same call via the path form: `POST /v1/api/similarweb/top-sites-ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer | yes | limit range 1–20 |
| `offset` | integer |  | offset range 0–100000 |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `category` | string | yes | category  |

## Details

Get the top-ranked websites worldwide or in a category, ordered by traffic rank.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/top-sites-ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "all", "country": "ww", "limit": 3}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | category |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `limit` | integer | Yes | limit |
| `offset` | integer | No | offset |

### Pricing

$0.075 per returned row (1 Similarweb credit), up to 20 rows; billed on rows returned. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/top-sites-ranking.json`](../../../catalog/models/similarweb/top-sites-ranking.json) · Store page: https://www.sandbase.ai/model/similarweb/top-sites-ranking
