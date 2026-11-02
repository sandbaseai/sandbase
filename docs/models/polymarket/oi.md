# Polymarket Open Interest API: pricing, parameters and code examples

`polymarket/oi` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Open interest in USDC for one or more markets by condition ID.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/oi", "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/oi', {'condition': '0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/oi", {
  "condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/oi", sandbase.Params{
	"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b",
})
```

Same call via the path form: `POST /v1/api/polymarket/oi` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `condition` | string | yes | Condition id(s), comma-separated (at most 20 distinct values). `condition` is the unified key across v2 (same as the feeds); `condition_id` / `conditionId` are accepted aliases. Omit for global open interest.  |

## Details

Open interest in USDC for one or more markets by condition ID.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/oi" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition": "0xc5eae79d1ffe716572353962eb926b1e3964c500a4880a7a94f58408218ee76b"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition` | string | Yes | Condition id(s), comma-separated (at most 20 distinct values). `condition` is the unified key across v2 (same as the feeds); `condition_id` / `conditionId` are accepted aliases. Omit for global open i |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/oi.json`](../../../catalog/models/polymarket/oi.json) · Store page: https://www.sandbase.ai/model/polymarket/oi
