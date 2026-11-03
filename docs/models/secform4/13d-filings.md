# SECForm4 13D Filings API: pricing, parameters and code examples

`secform4/13d-filings` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns recent Schedule 13D filings showing significant ownership positions (>5%) in public companies. 13D filers are activist investors who intend to influence the company.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/13d-filings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/13d-filings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/13d-filings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/13d-filings", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/13d-filings` with the body above minus `model`.

## Details

Returns a list of recent Schedule 13D filings, which report ownership stakes above 5% in public companies. Each row names the company, the filer, the share count, the change from the previous report, and links to the filing. The API takes no input.

### Use cases

- Track new activist positions as they are filed, such as a `New Position` entry for a fund.
- Spot filers who are selling down a stake by checking negative values in `shares_vs_prev_report`.
- Build a daily feed of 13D activity that links back to the source filing for each row.
- Compare 13D activity with passive holders by pairing this list with 13G filings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/13d-filings" \
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
        "company_symbol": "BLACKBERRY LTD BB",
        "company_symbol_url": "https://www.secform4.com/13dg-history/1070235.html",
        "filed_by_symbol": "FAIRFAX FINANCIAL HOLDINGS LIMITED",
        "filed_by_symbol_url": "https://www.secform4.com/13dg-history/915191.html",
        "reported_datetime": "2026-05-06 4:19 pm Sale",
        "shares_owned_owned": "26,264,199 4.500%",
        "shares_vs_prev_report": "-9,556,692 (-26.68%)",
        "transaction_date": "2026-05-04",
        "type": "13D",
        "view": "Filing History",
        "view_url": "https://www.secform4.com/13dg/915191/0000947871-26-000499.html"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].company_symbol` | Company name followed by its ticker, for example `BLACKBERRY LTD BB`. |
| `data.items[].filed_by_symbol` | Name of the investor or fund that filed the 13D. |
| `data.items[].reported_datetime` | Date and time of the report, followed by a label for the action such as `Sale`, `Purchase` or `Unchanged`. |
| `data.items[].shares_owned_owned` | Number of shares the filer owns, followed by the percentage of the company that stake represents. |
| `data.items[].shares_vs_prev_report` | Change in shares since the filer's previous report, with the percent change or a label such as `New Position` or `Unchanged`. |
| `data.items[].transaction_date` | Date of the transaction that triggered the filing, in `YYYY-MM-DD` format. |
| `data.items[].type` | Filing type. All rows in this response are `13D`. |
| `data.items[].company_symbol_url / data.items[].filed_by_symbol_url` | Links to the filing history page for the company or the filer. |
| `data.items[].view_url` | Link to the individual filing. |

### Notes

- The request body is an empty object `{}`. There are no pagination or filter parameters.
- `reported_datetime` and `transaction_date` can differ, so use `transaction_date` for when the trade happened.
- For passive stakes above 5%, call [SECForm4 13G Filings](/apis/secform4/13g-filings).
- For insider trades at a single company, call [SECForm4 Company Insider Trading](/apis/secform4/company-insider-trading).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/13d-filings.json`](../../../catalog/models/secform4/13d-filings.json) · Store page: https://www.sandbase.ai/model/secform4/13d-filings
