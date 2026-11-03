# SECForm4 Insider Buy Sell Ratios API: pricing, parameters and code examples

`secform4/insider-buy-sell-ratios` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns aggregate insider buy/sell ratio data with daily data points going back to 2003. Includes buy count, sell count, buy dollar volume, sell dollar volume per day, plus market index comparison data for S&P 500,.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/insider-buy-sell-ratios"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/insider-buy-sell-ratios', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/insider-buy-sell-ratios", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/insider-buy-sell-ratios", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/insider-buy-sell-ratios` with the body above minus `model`.

## Details

Returns daily aggregate insider trading data from SEC Form 4 filings, starting in July 2003. Each day has buy and sell counts, buy and sell dollar volumes, and closing-style values for the SP500, DOW and NASDAQ indexes. It needs no input.

### Use cases

- Chart the daily insider buy/sell balance over several years to spot periods of heavy insider selling.
- Compare insider buying activity against S&P 500, Dow or Nasdaq levels on the same dates.
- Build a market-wide insider sentiment indicator from buy and sell dollar volumes.
- Backtest whether spikes in insider buy counts line up with later index moves.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/insider-buy-sell-ratios" \
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
    "buySells": {
      "0": [
        85
      ],
      "1": [
        212
      ],
      "2": [
        "12147845"
      ],
      "3": [
        "541638370"
      ],
      "date": [
        "2003-07-01"
      ]
    },
    "marketIndex": {
      "0": [
        "982.32"
      ],
      "1": [
        "9040.95"
      ],
      "2": [
        "1640.13"
      ],
      "date": [
        "2003-07-01"
      ]
    },
    "marketIndexName": [
      "SP500"
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.buySells.date` | List of dates in `YYYY-MM-DD` format. Position `i` in this list matches position `i` in the other `buySells` lists. |
| `data.buySells.0 / data.buySells.1` | Daily counts of insider buys and sells. They follow the order in the API description: buy count first, sell count second. |
| `data.buySells.2 / data.buySells.3` | Daily dollar volumes for insider buys and sells, in the same order as the description. The values are numbers sent as strings. |
| `data.marketIndex.date` | List of dates for the market index values, in `YYYY-MM-DD` format. |
| `data.marketIndex.0` | Daily values for the first index in `marketIndexName`, which is `SP500`. Values are strings. |
| `data.marketIndex.1` | Daily values for the second index in `marketIndexName`, which is `DOW`. Values are strings. |
| `data.marketIndex.2` | Daily values for the third index in `marketIndexName`, which is `NASDAQ`. Values are strings. |
| `data.marketIndexName` | Names of the indexes, in the same order as the keys `0`, `1` and `2` under `data.marketIndex`. |

### Notes

- The call takes no parameters. Send an empty JSON object `{}`.
- The data comes as parallel lists, not as one object per day. Match values across lists by position, or by `date`.
- For the individual trades behind these totals, call [SECForm4 Insider Buys](/apis/secform4/insider-buys) or [SECForm4 Insider Sales](/apis/secform4/insider-sales).
- To look at one company instead of the whole market, use [SECForm4 Company Insider Trading](/apis/secform4/company-insider-trading).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/insider-buy-sell-ratios.json`](../../../catalog/models/secform4/insider-buy-sell-ratios.json) · Store page: https://www.sandbase.ai/model/secform4/insider-buy-sell-ratios
