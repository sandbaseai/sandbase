# Kalshi Get Market Price

`kalshi/markets-by-ticker` · api · Kalshi

Get Market Price from Kalshi. Returns the official Kalshi API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kalshi/markets-by-ticker", "ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kalshi/markets-by-ticker', {'ticker': 'KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kalshi/markets-by-ticker", {
  "ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kalshi/markets-by-ticker", sandbase.Params{
	"ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA",
})
```

Same call via the path form: `POST /v1/api/kalshi/markets-by-ticker` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | Market ticker  |

## Details

Get Market Price from Kalshi. Returns the official Kalshi API response unchanged.

The response is the official Kalshi API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kalshi/markets-by-ticker" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "KXMVECROSSCATEGORY-S202637DX42FCBU4IPV3N-ROZI3XFZA"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Market ticker |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/kalshi/markets-by-ticker.json`](../../../catalog/models/kalshi/markets-by-ticker.json) · Store page: https://www.sandbase.ai/model/kalshi/markets-by-ticker
