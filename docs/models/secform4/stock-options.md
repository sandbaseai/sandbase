# SECForm4 Stock Options API: pricing, parameters and code examples

`secform4/stock-options` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns recent stock option transactions including exercises, awards, grants, conversions, and tax withholdings from SEC Form 4 filings.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/stock-options"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/stock-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/stock-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/stock-options", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/stock-options` with the body above minus `model`.

## Details

Returns a list of recent stock option transactions reported on SEC Form 4 filings. Each row shows the company, the insider, the transaction type, share counts, and a link to the filing. The API takes no input.

### Use cases

- Track option awards and exercises by executives and directors at public companies.
- Spot tax withholding events tied to equity vesting for a specific insider.
- Build a feed of new Form 4 option filings and link each row to the source document.
- Compare conversion prices across companies to see the strike levels of recent option activity.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/stock-options" \
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
    "items": [
      {
        "company": "Citi Trends Inc",
        "company_url": "https://www.secform4.com/insider-trading/1318484.htm",
        "conversion_price": "$46.82",
        "exercisable_expiration": "N/A N/A",
        "filing": "View",
        "filing_url": "https://www.secform4.com/filings/1318484/0001104659-26-057071.htm",
        "insider_relationship": "Plutino Heather L EVP and CFO",
        "insider_relationship_url": "https://www.secform4.com/insider-trading/1935258.htm",
        "reported_datetime": "2026-05-07 3:58 pm",
        "shares_owned": "21,036 (Direct)",
        "shares_traded": "1,252",
        "symnbol": "CTRN"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].company` | Name of the company that issued the options. |
| `data.items[].symnbol` | Ticker symbol of the company. The key name is spelled `symnbol` in the response. |
| `data.items[].insider_relationship` | Insider name followed by their role at the company, for example `EVP and CFO` or `Director`. |
| `data.items[].transaction_date` | Date of the transaction followed by the transaction type, for example `2026-05-05 Tax Withholding` or `2026-05-05 Option Award`. |
| `data.items[].shares_traded` | Number of shares involved in the transaction. |
| `data.items[].shares_owned` | Shares the insider holds after the transaction, with the ownership type in parentheses, for example `(Direct)`. |
| `data.items[].conversion_price` | Price per share tied to the option, shown as a dollar string. Awards can show `$0`. |
| `data.items[].exercisable_expiration` | Exercisable and expiration dates for the option. It shows `N/A N/A` when none are given. |
| `data.items[].reported_datetime` | Date and time the filing was reported, in the format `YYYY-MM-DD h:mm am/pm`. |
| `data.items[].filing_url / company_url / insider_relationship_url` | Links to the Form 4 filing, the company page, and the insider page on the SEC Form 4 site. |

### Notes

- The request body is empty. The response gives no pagination parameters.
- Numeric values such as `shares_traded` and `conversion_price` come back as strings with commas or a `$` sign, so parse them before doing math.
- For all insider trades at one company, call [SECForm4 Company Insider Trading](/apis/secform4/company-insider-trading).
- For open market purchases and sales instead of option activity, see [SECForm4 Insider Buys](/apis/secform4/insider-buys) and [SECForm4 Insider Sales](/apis/secform4/insider-sales).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/stock-options.json`](../../../catalog/models/secform4/stock-options.json) · Store page: https://www.sandbase.ai/model/secform4/stock-options
