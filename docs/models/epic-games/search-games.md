# Epic Games Store Search Games API: pricing, parameters and code examples

`epic-games/search-games` · data API · Epic Games Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Searches for games by keyword in the Epic Games Store catalog. Returns up to 20 matching results sorted by relevancy.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/search-games", "query": "fortnite"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('epic-games/search-games', {'query': 'fortnite'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("epic-games/search-games", {
  "query": "fortnite"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "epic-games/search-games", sandbase.Params{
	"query": "fortnite",
})
```

Same call via the path form: `POST /v1/api/epic-games/search-games` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (e.g. 'fortnite', 'action', 'racing').  |

## Details

Searches for games by keyword in the Epic Games Store catalog. Returns up to 20 matching results sorted by relevancy.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "epic-games/search-games", "query": "fortnite"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (e.g. 'fortnite', 'action', 'racing'). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/epic-games/search-games.json`](../../../catalog/models/epic-games/search-games.json) · Store page: https://www.sandbase.ai/model/epic-games/search-games
