# Polymarket Get current active rewards configurations API: pricing, parameters and code examples

`polymarket/rewards-markets-current` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns the current active rewards configurations for markets.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets-current"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets-current', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets-current", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets-current", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets-current` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sponsored` | boolean |  | If true, returns sponsored reward configurations instead of standard ones default `false` |
| `next_cursor` | string |  | Pagination cursor from previous response  |

## Details

Returns the current active rewards configurations for markets.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets-current" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `next_cursor` | string | No | Pagination cursor from previous response |
| `sponsored` | boolean | No | If true, returns sponsored reward configurations instead of standard ones |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets-current.json`](../../../catalog/models/polymarket/rewards-markets-current.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets-current
