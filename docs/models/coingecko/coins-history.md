# CoinGecko Coin Historical Data by ID

`coingecko/coins-history` · api · CoinGecko

Get the historical data (price, market cap, 24hrs volume, ...) at a given date for a coin based on a particular coin ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-history", "id": "bitcoin", "date": "30-12-2024"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-history', {'id': 'bitcoin', 'date': '30-12-2024'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-history", {
  "id": "bitcoin",
  "date": "30-12-2024"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-history", sandbase.Params{
	"id": "bitcoin",
	"date": "30-12-2024",
})
```

Same call via the path form: `POST /v1/api/coingecko/coins-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). default `"bitcoin"` |
| `date` | string | yes | The date of data snapshot. Format: `YYYY-MM-DD` default `"2025-12-30"` |
| `localization` | boolean |  | Include all the localized languages in response. Default: true  |

## Details

Get the historical data (price, market cap, 24hrs volume, ...) at a given date for a coin based on a particular coin ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "bitcoin", "date": "30-12-2024"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Coin ID. *refers to [`/coins/list`](/reference/coins-list). |
| `date` | string | Yes | The date of data snapshot. Format: `YYYY-MM-DD` |
| `localization` | boolean | No | Include all the localized languages in response. Default: true |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/coins-history.json`](../../../catalog/models/coingecko/coins-history.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-history
