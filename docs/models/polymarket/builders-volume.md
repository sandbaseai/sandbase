# Polymarket Builders Volume API: pricing, parameters and code examples

`polymarket/builders-volume` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Daily, weekly or monthly volume of Polymarket builders over time.

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
| `limit` | integer |  | How many of the most recent buckets to return. Defaults to 30, capped at 90; a lower ceiling than the rest of the surface, because only ~308 daily buckets exist and the family maximum would return the whole series.… range 0–90 |
| `interval` | string |  | Bucket width: `day` \| `week` \| `month` \| `all`. Defaults to `day`. `timePeriod` and `time_period` are accepted aliases.  |

## Details

Daily, weekly or monthly volume of Polymarket builders over time.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/builders-volume" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `interval` | string | No | Bucket width: `day` / `week` / `month` / `all`. Defaults to `day`. `timePeriod` and `time_period` are accepted aliases. |
| `limit` | integer | No | How many of the most recent buckets to return. Defaults to 30, capped at 90; a lower ceiling than the rest of the surface, because only ~308 daily buckets exist and the family maximum would return the |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/builders-volume.json`](../../../catalog/models/polymarket/builders-volume.json) · Store page: https://www.sandbase.ai/model/polymarket/builders-volume
