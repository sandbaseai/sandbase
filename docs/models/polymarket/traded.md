# Polymarket User Stats API: pricing, parameters and code examples

`polymarket/traded` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

A wallet's profile stats: total trades, biggest win, profile views and join date.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/traded", "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/traded', {'user': '0xfe787d2da716d60e8acff57fb87eb13cd4d10319'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/traded", {
  "user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/traded", sandbase.Params{
	"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319",
})
```

Same call via the path form: `POST /v1/api/polymarket/traded` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user` | string | yes | The wallet whose profile stats to return. Required; `0x` followed by 40 hexadecimal characters.  |

## Details

A wallet's profile stats: total trades, biggest win, profile views and join date.

Served from the Polymarket Data API v2. The result is returned in `outputs[0].data`: rows are under `data`, and paginated routes add `pagination.next_cursor` (pass it back as `cursor`).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/traded" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user": "0xfe787d2da716d60e8acff57fb87eb13cd4d10319"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user` | string | Yes | The wallet whose profile stats to return. Required; `0x` followed by 40 hexadecimal characters. |

### Reference

- Official docs: https://docs.polymarket.com/api-reference/data-api/overview

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/traded.json`](../../../catalog/models/polymarket/traded.json) · Store page: https://www.sandbase.ai/model/polymarket/traded
