# SECForm4 Company Insider Trading API: pricing, parameters and code examples

`secform4/company-insider-trading` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns the full insider trading history for a specific company identified by its SEC CIK number. Includes all buy, sell, and option transactions filed in Form 4s for the company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/company-insider-trading", "cik": "320193"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/company-insider-trading', {'cik': '320193'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/company-insider-trading", {
  "cik": "320193"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/company-insider-trading", sandbase.Params{
	"cik": "320193",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/company-insider-trading` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cik` | string | yes | SEC CIK number of the company (e.g. '320193' for Apple Inc, '789019' for Microsoft)  |

## Details

Returns insider trading transactions from Form 4 filings for one company, identified by its SEC CIK number. Each row lists the insider, the trade size, the price, and a link to the filing. The only input is `cik`.

### Use cases

- Track which executives at a company sold or bought shares in recent weeks.
- Total the dollar value of insider sales for one company over a period.
- Open the original Form 4 filing for any transaction to check the details.
- Watch the holdings of a named officer after each reported trade.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/company-insider-trading" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cik": "320193"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cik` | string | Yes | SEC CIK number of the company (e.g. '320193' for Apple Inc, '789019' for Microsoft) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "average_price": "$343.36",
        "company": "Apple Inc.",
        "filing": "View",
        "filing_url": "https://www.secform4.com/filings/320193/0001140361-26-041201.htm",
        "insider_relationship": "Newstead Jennifer SVP, GC and Government Affairs",
        "insider_relationship_url": "https://www.secform4.com/insider-trading/1780525.htm",
        "reported_datetime": "2026-10-29 6:30 pm",
        "shares_owned": "32,396 (Direct)",
        "shares_traded": "2,399",
        "symbol": "AAPL",
        "symbol_url": "https://www.secform4.com/#S2",
        "total_amount": "$823,721"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].insider_relationship` | The insider's name followed by their role at the company, for example `SVP, GC and Government Affairs`. |
| `data.items[].insider_relationship_url` | Link to the page for this insider on the source site. |
| `data.items[].transaction_date` | The date of the trade followed by the transaction type, for example `2026-10-27 Sale`. |
| `data.items[].reported_datetime` | The date and time the transaction was reported. |
| `data.items[].shares_traded` | Number of shares in the transaction. |
| `data.items[].average_price` | Average price per share for the transaction, as a string with a `$` sign. |
| `data.items[].total_amount` | Total dollar value of the transaction, as a string with a `$` sign. |
| `data.items[].shares_owned` | Shares the insider holds after the trade, with the ownership type in brackets, for example `(Direct)`. |
| `data.items[].filing_url` | Link to the Form 4 filing for this transaction. |
| `data.items[].symbol / data.items[].company` | The ticker symbol and company name for the row. |

### Notes

- Find the `cik` for a company with [SECForm4 Search](/apis/secform4/search). Apple Inc is `320193` and Microsoft is `789019`.
- All values in each item are strings, including prices, amounts and share counts. Remove the `$` and commas before doing math.
- The trimmed response shows no pagination parameter. The request takes only `cik`.
- For market-wide lists, see [SECForm4 Insider Buys](/apis/secform4/insider-buys) and [SECForm4 Insider Sales](/apis/secform4/insider-sales).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/company-insider-trading.json`](../../../catalog/models/secform4/company-insider-trading.json) · Store page: https://www.sandbase.ai/model/secform4/company-insider-trading
