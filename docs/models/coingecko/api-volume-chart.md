# CoinGecko Exchange Volume Chart by ID API: pricing, parameters and code examples

`coingecko/api-volume-chart` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

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

Returns a time series of trading volume for one exchange on CoinGecko. It needs an exchange `id` and a `days` value, and returns volume in BTC for each timestamp.

### Use cases

- Plot the recent trading volume of an exchange such as `binance` on a line chart.
- Compare the volume trend of two exchanges over the last 7 or 30 days.
- Detect volume spikes or drops on an exchange by checking changes between data points.
- Feed daily or weekly exchange volume into a report or dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/api-volume-chart" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "binance", "days": "1"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `days` | string | Yes | Data up to number of days ago. |
| `id` | string | Yes | Exchange ID or derivative exchange ID. *refers to [`/exchanges/list`](/reference/exchanges-list) or [`/derivatives/exchanges/list`](/reference/derivatives-exchanges-list). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  [
    1793604600000
  ]
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[][0]` | Timestamp of the data point. The value is a UNIX time in milliseconds, for example `1793604600000`. |
| `[][1]` | Trading volume of the exchange at that timestamp, returned as a string, for example `"50120.06192454506"`. The API description states the volume is in BTC. Parse it as a number before doing math. |

### Notes

- The response is a plain array of `[timestamp, volume]` pairs, not an object. Points are in time order.
- Get a valid `id` from [CoinGecko Exchanges List (ID Map)](/apis/coingecko/exchanges-list). Derivative exchange IDs also work.
- `days` must be one of `1`, `7`, `14`, `30`, `90`, `180` or `365`. Send it as a string.
- For exchange details such as name and country, call [CoinGecko Exchange Data by ID](/apis/coingecko/exchanges-by-id).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/api-volume-chart.json`](../../../catalog/models/coingecko/api-volume-chart.json) · Store page: https://www.sandbase.ai/model/coingecko/api-volume-chart
