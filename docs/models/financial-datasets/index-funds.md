# Financial Datasets ETF and Index Fund Holdings API: pricing, parameters and code examples

`financial-datasets/index-funds` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Holdings of an ETF or index fund by ticker, with fund name, asset class, net assets and each holding's weight.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/index-funds", "ticker": "SPY"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/index-funds', {'ticker': 'SPY'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/index-funds", {
  "ticker": "SPY"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/index-funds", sandbase.Params{
	"ticker": "SPY",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/index-funds` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ticker` | string | yes | ETF or index fund ticker, e.g. `SPY`.  |

## Details

Returns the holdings of an ETF or index fund, plus fund-level details such as name, asset class and total net assets. The only input is the fund `ticker`, for example `SPY`.

### Use cases

- Show the top holdings and weights of `SPY` in a portfolio dashboard.
- Check how much of a fund sits in a single stock such as `AAPL` or `NVDA`.
- Compare the make-up of two index funds by pulling both and matching holdings by `ticker`.
- Estimate the dollar exposure to a company through a fund using each holding's `market_value`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/index-funds" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "SPY"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | ETF or index fund ticker, e.g. `SPY`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "fund": {
    "as_of": "2026-10-30",
    "asset_class": "equity",
    "cik": "884394",
    "filing_date": "2026-10-30",
    "name": "State Street SPDR S&P 500 ETF",
    "offset": 0,
    "returned": 10,
    "source": "ssga",
    "total_holdings": 505,
    "total_net_assets": 796865210000.0
  },
  "holdings": [
    {
      "asset_class": "equity",
      "market_value": 61347943176.19,
      "name": "APPLE INC",
      "shares": 179157845.0,
      "ticker": "AAPL",
      "weight": 7.69866
    }
  ],
  "next_page_url": "https://api.financialdatasets.ai/index-funds?cursor=14PYl6nE1XOPv6nAM5DGqeHPMLv3…",
  "ticker": "SPY"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fund.name` | Full name of the fund. |
| `fund.asset_class` | Main asset class of the fund, for example `equity`. |
| `fund.total_net_assets` | Total net assets of the fund as a number. |
| `fund.as_of / fund.filing_date` | Dates tied to the holdings data. `as_of` is the date of the data and `filing_date` is the filing date. Both use `YYYY-MM-DD`. |
| `fund.total_holdings / fund.returned / fund.offset` | Total number of holdings in the fund, how many came back in this response, and the starting position of this page. |
| `holdings[].ticker / holdings[].name` | Ticker symbol and name of each holding. |
| `holdings[].weight` | Weight of the holding in the fund. `7.69866` for `AAPL` appears to be a percentage value. |
| `holdings[].market_value / holdings[].shares` | Value of the position and the number of shares held. |
| `holdings[].asset_class` | Asset class of the individual holding. |
| `next_page_url` | Full URL for the next page of holdings. It contains a `cursor` value. |

### Notes

- The response covers one page of holdings. In the sample, `fund.returned` is `10` out of `fund.total_holdings` of `505`.
- Use `next_page_url` to fetch the next page when there are more holdings than `fund.returned`.
- To look up a holding in more detail, call [Financial Datasets Get Company Facts](/apis/financial-datasets/company-facts) with its `ticker`.
- To get a holding's price, call [Financial Datasets Get Stock Price Snapshot](/apis/financial-datasets/prices-snapshot).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/index-funds.json`](../../../catalog/models/financial-datasets/index-funds.json) · Store page: https://www.sandbase.ai/model/financial-datasets/index-funds
