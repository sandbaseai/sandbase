# CoinGecko Exchange Data by ID

`coingecko/exchanges-by-id` · api · CoinGecko

Get exchange's data (name, year established, country, ...), exchange volume in BTC and top 100 tickers based on exchange's ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges-by-id", "id": "binance"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges-by-id', {'id': 'binance'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges-by-id", {
  "id": "binance"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges-by-id", sandbase.Params{
	"id": "binance",
})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). default `"binance"` |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |

## Details

Get exchange's data (name, year established, country, ...), exchange volume in BTC and top 100 tickers based on exchange's ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/exchanges-by-id.json`](../../../catalog/models/coingecko/exchanges-by-id.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-by-id
