# CoinGecko Exchange Volume Chart by ID

`coingecko/api-volume-chart` · api · CoinGecko

Get the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange's ID

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/api-volume-chart", "id": "binance", "days": "1"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/api-volume-chart', {'id': 'binance', 'days': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/api-volume-chart", {
  "id": "binance",
  "days": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/api-volume-chart", sandbase.Params{
	"id": "binance",
	"days": "1",
})
```

Same call via the path form: `POST /v1/api/coingecko/api-volume-chart` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Exchange ID or derivative exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list) or [`/derivatives/exchanges/list`](/reference/derivatives-exchanges-list). default `"binance"` |
| `days` | string | yes | Data up to number of days ago. one of: `1`, `7`, `14`, `30`, `90`, `180`, `365`; default `"1"` |

## Details

Get the historical volume chart data with time in UNIX and trading volume data in BTC based on exchange's ID

The response is the official CoinGecko API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/api-volume-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance", "days": "1"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Exchange ID or derivative exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list) or [`/derivatives/exchanges/list`](/reference/derivatives-excha |
| `days` | string | Yes | Data up to number of days ago. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/coingecko/api-volume-chart.json`](../../../catalog/models/coingecko/api-volume-chart.json) · Store page: https://www.sandbase.ai/model/coingecko/api-volume-chart
