# Epic Games Store Game Details API: pricing, parameters and code examples

`epic-games/game-details` · data API · Epic Games Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetches full details for a specific game on the Epic Games Store by its URL slug. Returns description, pricing, genres, features, ratings, media gallery, and publisher info. Requires multiple GraphQL round-trips internally (mapping lookup, offer fetch, ratings).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/game-details", "game_slug": "fortnite"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('epic-games/game-details', {'game_slug': 'fortnite'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("epic-games/game-details", {
  "game_slug": "fortnite"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "epic-games/game-details", sandbase.Params{
	"game_slug": "fortnite",
})
```

Same call via the path form: `POST /v1/api/epic-games/game-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `game_slug` | string | yes | Product URL slug from the Epic Games Store product page URL (e.g. 'fortnite', 'ghostrunner-2'). Obtainable from the product_url field of other endpoints by extracting the last path segment after /p/.  |

## Details

Fetches full details for a specific game on the Epic Games Store by its URL slug. Returns description, pricing, genres, features, ratings, media gallery, and publisher info. Requires multiple GraphQL round-trips internally (mapping lookup, offer fetch, ratings).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "epic-games/game-details", "game_slug": "fortnite"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `game_slug` | string | Yes | Product URL slug from the Epic Games Store product page URL (e.g. 'fortnite', 'ghostrunner-2'). Obtainable from the product_url field of other endpoints by extracting the last path segment after /p/. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/epic-games/game-details.json`](../../../catalog/models/epic-games/game-details.json) · Store page: https://www.sandbase.ai/model/epic-games/game-details
