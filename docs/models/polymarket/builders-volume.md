# Polymarket Get daily builder volume time-series API: pricing, parameters and code examples

`polymarket/builders-volume` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Get daily builder volume time-series from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/builders-volume"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/builders-volume', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/builders-volume", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/builders-volume", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/builders-volume` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `timePeriod` | string |  | The time period to fetch records for. DAY is not offered because its response (about 18 MB) exceeds the 10 MB response limit. one of: `WEEK`, `MONTH`, `ALL`; default `"WEEK"` |

## Details

Get daily builder volume time-series from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/builders-volume" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"timePeriod": "MONTH"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `timePeriod` | string | No | WEEK (default), MONTH or ALL. DAY is not offered because its response (about 18 MB) exceeds the 10 MB response limit. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/builders-volume.json`](../../../catalog/models/polymarket/builders-volume.json) · Store page: https://www.sandbase.ai/model/polymarket/builders-volume
