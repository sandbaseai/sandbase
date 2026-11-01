# CoinGecko Coin Data by Token Address

`coingecko/coins-contract` · api · CoinGecko

Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform and a.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-contract", "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-contract', {'contract_address': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 'id': 'ethereum'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-contract", {
  "contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
  "id": "ethereum"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-contract", sandbase.Params{
	"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
	"id": "ethereum",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-contract` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). default `"ethereum"` |
| `contract_address` | string | yes | The contract address of token. default `"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"` |

## Details

Get all the metadata (image, websites, socials, description, contract address, etc.) and market data (price, ATH, exchange tickers, etc.) of a coin from the CoinGecko coin page based on an asset platform and a.

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-contract" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contract_address": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48", "id": "ethereum"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `contract_address` | string | Yes | The contract address of token. |
| `id` | string | Yes | Asset platform ID. *refers to [`/asset_platforms`](/reference/asset-platforms-list). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-contract.json`](../../../catalog/models/coingecko/coins-contract.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-contract
