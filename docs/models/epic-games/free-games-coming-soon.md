# Epic Games Store Free Games Coming Soon API: pricing, parameters and code examples

`epic-games/free-games-coming-soon` · data API · Epic Games Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns only games labeled COMING SOON from the Epic Games Store free games section. Filters out currently free games. Subset of get_free_games.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/free-games-coming-soon"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('epic-games/free-games-coming-soon', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("epic-games/free-games-coming-soon", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "epic-games/free-games-coming-soon", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/epic-games/free-games-coming-soon` with the body above minus `model`.

## Details

Returns only games labeled COMING SOON from the Epic Games Store free games section. Filters out currently free games. Subset of get_free_games.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "epic-games/free-games-coming-soon"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/epic-games/free-games-coming-soon.json`](../../../catalog/models/epic-games/free-games-coming-soon.json) · Store page: https://www.sandbase.ai/model/epic-games/free-games-coming-soon
