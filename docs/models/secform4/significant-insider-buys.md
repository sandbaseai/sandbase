# SECForm4 Significant Insider Buys API: pricing, parameters and code examples

`secform4/significant-insider-buys` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns insider purchase transactions filtered to significant buys only (larger dollar amounts). Same fields as get_insider_buys but limited to higher-value transactions.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/significant-insider-buys"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/significant-insider-buys', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/significant-insider-buys", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/significant-insider-buys", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/significant-insider-buys` with the body above minus `model`.

## Details

Returns a list of recent insider stock purchases reported on SEC Form 4, limited to larger dollar amounts. Each item names the company, the insider, the trade size and price, and links to the filing. The API takes no input.

### Use cases

- Spot directors and officers who put large amounts of their own money into a stock.
- Build a daily alert feed of high-value insider purchases by ticker `symbol`.
- Rank recent buys by `total_amount` to find the biggest conviction trades.
- Open the linked filing to check the original Form 4 for a flagged purchase.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/significant-insider-buys" \
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
        "average_price": "$3.0558",
        "company": "Angel Studios Inc.",
        "company_url": "https://www.secform4.com/insider-trading/1865200.htm",
        "filing": "View",
        "filing_url": "https://www.secform4.com/filings/1865200/0001865200-26-000038.htm",
        "insider_relationship": "Sarowitz Steven I Director",
        "insider_relationship_url": "https://www.secform4.com/insider-trading/1597870.htm",
        "reported_datetime": "2026-05-07 2:25 pm",
        "shares_owned": "326,840 (Direct)",
        "shares_traded": "321,544",
        "symbol": "ANGX",
        "symbol_url": "https://www.secform4.com/#S2"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].company / symbol` | Company name and stock ticker for the purchase, for example `Organon & Co.` and `OGN`. |
| `data.items[].insider_relationship` | Insider name followed by their role at the company, for example `Director` or `SVP and Corporate Controller`. |
| `data.items[].transaction_date` | Trade date followed by the transaction type. In this response the type is `Purchase`. |
| `data.items[].reported_datetime` | Date and time the filing was reported, as text like `2026-05-07 2:25 pm`. |
| `data.items[].shares_traded` | Number of shares bought in the transaction, as a formatted string. |
| `data.items[].average_price` | Average price paid per share, as a string with a `$` sign. |
| `data.items[].total_amount` | Total dollar value of the purchase, as a string with a `$` sign. |
| `data.items[].shares_owned` | Shares the insider holds after the trade, with the ownership type in parentheses such as `(Direct)`. |
| `data.items[].filing_url` | Link to the Form 4 filing page for this transaction. |
| `data.items[].company_url / insider_relationship_url` | Links to the SECForm4 pages for the company and for the insider. |

### Notes

- The request has no parameters, so send an empty JSON object `{}`.
- Numbers and dates come back as formatted strings, such as `$982,574` and `321,544`. Strip the `$` sign and commas before you do math.
- The `symbol_url` value is the same generic link in every item, so use `company_url` to reach a company page.
- To see purchases of all sizes, call [SECForm4 Insider Buys](/apis/secform4/insider-buys). For the sell side, use [SECForm4 Insider Sales](/apis/secform4/insider-sales).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/significant-insider-buys.json`](../../../catalog/models/secform4/significant-insider-buys.json) · Store page: https://www.sandbase.ai/model/secform4/significant-insider-buys
