# CoinGecko Exchange Tickers by ID

`coingecko/exchanges-tickers` · api · CoinGecko

Exchange Tickers by ID from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/exchanges-tickers", "id": "binance"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/exchanges-tickers', {'id': 'binance'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/exchanges-tickers", {
  "id": "binance"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/exchanges-tickers", sandbase.Params{
	"id": "binance",
})
```

Same call via the path form: `POST /v1/api/coingecko/exchanges-tickers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). default `"binance"` |
| `page` | number |  | Page through results.  |
| `depth` | boolean |  | Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false  |
| `order` | string |  | Sort the order of responses. Default: `trust_score_desc` one of: `market_cap_asc`, `market_cap_desc`, `trust_score_desc`, `trust_score_asc`, `volume_desc`, `volume_asc`, `base_target` |
| `coin_ids` | string |  | Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list).  |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |
| `include_exchange_logo` | boolean |  | Include exchange logo. Default: false  |

## Details

Exchange Tickers by ID from CoinGecko. Returns the official CoinGecko API response unchanged.

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/exchanges-tickers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list). |
| `coin_ids` | string | No | Filter tickers by coin IDs, comma-separated if querying more than 1 coin. *refers to [`/coins/list`](/reference/coins-list). |
| `depth` | boolean | No | Include 2% orderbook depth (cost_to_move_up_usd and cost_to_move_down_usd). Default: false |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |
| `include_exchange_logo` | boolean | No | Include exchange logo. Default: false |
| `order` | string | No | Sort the order of responses. Default: `trust_score_desc` |
| `page` | number | No | Page through results. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/exchanges-tickers.json`](../../../catalog/models/coingecko/exchanges-tickers.json) · Store page: https://www.sandbase.ai/model/coingecko/exchanges-tickers
