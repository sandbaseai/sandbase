# Epic Games Store Free Games API: pricing, parameters and code examples

`epic-games/free-games` · data API · Epic Games Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns all currently free and upcoming free games from the Epic Games Store free games promotion page. Each game includes its status (FREE NOW or COMING SOON) and the promotional date range. The list refreshes weekly.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/free-games"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('epic-games/free-games', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("epic-games/free-games", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "epic-games/free-games", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/epic-games/free-games` with the body above minus `model`.

## Details

Returns all currently free and upcoming free games from the Epic Games Store free games promotion page. Each game includes its status (FREE NOW or COMING SOON) and the promotional date range. The list refreshes weekly.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "epic-games/free-games"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/epic-games/free-games.json`](../../../catalog/models/epic-games/free-games.json) · Store page: https://www.sandbase.ai/model/epic-games/free-games
