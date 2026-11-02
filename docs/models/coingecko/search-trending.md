# CoinGecko Trending Search List API: pricing, parameters and code examples

`coingecko/search-trending` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

This endpoint allows you query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/search-trending"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/search-trending', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/search-trending", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/search-trending", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/search-trending` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `show_max` | string |  | Show max number of results available for the given type. Available values: `coins`, `nfts`, `categories` e.g. `coins` or `coins,nfts,categories`  |

## Details

This endpoint allows you query trending search coins, NFTs and categories on CoinGecko in the last 24 hours

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/search-trending" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `show_max` | string | No | Show max number of results available for the given type. Available values: `coins`, `nfts`, `categories` e.g. `coins` or `coins,nfts,categories` |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/search-trending.json`](../../../catalog/models/coingecko/search-trending.json) · Store page: https://www.sandbase.ai/model/coingecko/search-trending
