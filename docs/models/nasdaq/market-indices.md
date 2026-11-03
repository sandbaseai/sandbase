# Nasdaq Market Indices API: pricing, parameters and code examples

`nasdaq/market-indices` · data API · Nasdaq · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Current values for the NASDAQ Composite index (COMP) including last price, net change, percentage change, volume, and daily high/low.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "nasdaq/market-indices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('nasdaq/market-indices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("nasdaq/market-indices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "nasdaq/market-indices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/nasdaq/market-indices` with the body above minus `model`.

## Details

Returns the current quote for the NASDAQ Composite index (`COMP`), including last price, net change, percentage change, volume, and the day's high and low. The API takes no input.

### Use cases

- Show the current NASDAQ Composite level and daily move on a market dashboard.
- Check whether the index is up or down today with `deltaIndicator` before running other market queries.
- Log the index value and volume at set times to build your own intraday history.
- Compare the day's `high` and `low` against `previousClose` to see how wide the trading range is.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/nasdaq/market-indices" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "data": [
      {
        "chartCloseTime": 1793635259000,
        "chartOpenTime": 1793611800000,
        "companyName": "NASDAQ Composite Index",
        "datetime": "2026-11-02T17:16:01",
        "deltaIndicator": "down",
        "high": 25799.46,
        "indexCharts": null,
        "lastSalePrice": "25,164.32",
        "low": 25145.95,
        "netChange": "-272.68",
        "percentageChange": "-1.07%",
        "previousClose": "25,437"
      }
    ],
    "message": null,
    "status": {
      "bCodeMessage": null,
      "developerMessage": null,
      "rCode": 200
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[].symbol / data.data[].companyName` | Ticker symbol of the index (`COMP`) and its full name. |
| `data.data[].lastSalePrice` | Latest index value, as a string with thousands separators. |
| `data.data[].netChange / data.data[].percentageChange` | Change from the previous close, as a signed number and as a percent string. Both are strings. |
| `data.data[].deltaIndicator` | Direction of the move, for example `down`. |
| `data.data[].high / data.data[].low` | Highest and lowest index values for the day. These are numbers. |
| `data.data[].previousClose` | Index value at the previous close, as a string. |
| `data.data[].volume` | Trading volume as a string with thousands separators. |
| `data.data[].datetime / data.data[].timeStamp` | Time of the quote as an ISO-style datetime, and the same date in a short text form. |
| `data.data[].chartOpenTime / data.data[].chartCloseTime` | Start and end of the chart window as 13-digit Unix timestamps, which look like milliseconds. |

### Notes

- Send an empty JSON object `{}` as the body. There are no parameters.
- Price, change, previous close, and volume are formatted strings with commas. Remove the commas and the `%` sign before you do math on them.
- `indexCharts` is `null` in this response, and `data.data[]` is a list that holds one item for `COMP`.
- For more detail on an index, call [Nasdaq Index Detail](/apis/nasdaq/index-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/nasdaq/market-indices.json`](../../../catalog/models/nasdaq/market-indices.json) · Store page: https://www.sandbase.ai/model/nasdaq/market-indices
