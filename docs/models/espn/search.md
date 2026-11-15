# ESPN Search API: pricing, parameters and code examples

`espn/search` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Search for athletes and teams across all sports. Returns matching results with IDs for use in other endpoints. When type filter is specified, only results of that type are returned.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/search", "query": "LeBron"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/search', {'query': 'LeBron'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/search", {
  "query": "LeBron"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/search", sandbase.Params{
	"query": "LeBron",
})
```

Same call via the path form: `POST /v1/api/espn/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Filter results by type. Accepted values: 'player', 'team'. When omitted, searches both players and teams.  |
| `limit` | integer |  | Maximum results to return. default `25` |
| `query` | string | yes | Search query (player name, team name, etc.)  |

## Details

Search for athletes and teams across all sports. Returns matching results with IDs for use in other endpoints. When type filter is specified, only results of that type are returned.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/search", "type": "player", "limit": 5, "query": "LeBron"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query (player name, team name, etc.) |
| `limit` | integer | No | Maximum results to return. |
| `type` | string | No | Filter results by type. Accepted values: 'player', 'team'. When omitted, searches both players and teams. |

### Pricing

Flat $0.06 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/search.json`](../../../catalog/models/espn/search.json) · Store page: https://www.sandbase.ai/model/espn/search
