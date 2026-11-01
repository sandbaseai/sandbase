# CoinGecko Coin Tickers by ID

`coingecko/coins-tickers` · api · CoinGecko

Get the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-tickers", "id": "bitcoin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-tickers', {'id': 'bitcoin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-tickers", {
  "id": "bitcoin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-tickers", sandbase.Params{
	"id": "bitcoin",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-tickers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) default `"bitcoin"` |
| `page` | integer |  | Page through results  |
| `depth` | boolean |  | Include 2% orderbook depth, i.e. `cost_to_move_up_usd` and `cost_to_move_down_usd`. Default: false  |
| `order` | string |  | Sort the order of responses. Default: trust_score_desc one of: `trust_score_desc`, `trust_score_asc`, `volume_desc`, `volume_asc` |
| `exchange_ids` | string |  | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list)  |
| `dex_pair_format` | string |  | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` one of: `contract_address`, `symbol` |
| `include_exchange_logo` | boolean |  | Include exchange logo. Default: false  |

## Details

Get the coin tickers on both centralized exchange (CEX) and decentralized exchange (DEX) based on a particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-tickers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list) |
| `depth` | boolean | No | Include 2% orderbook depth, i.e. `cost_to_move_up_usd` and `cost_to_move_down_usd`. Default: false |
| `dex_pair_format` | string | No | Set to `symbol` to display DEX pair base and target as symbols. Default: `contract_address` |
| `exchange_ids` | string | No | Exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list) |
| `include_exchange_logo` | boolean | No | Include exchange logo. Default: false |
| `order` | string | No | Sort the order of responses. Default: trust_score_desc |
| `page` | integer | No | Page through results |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-tickers.json`](../../../catalog/models/coingecko/coins-tickers.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-tickers
