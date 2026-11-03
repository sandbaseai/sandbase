# SECForm4 Search API: pricing, parameters and code examples

`secform4/search` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Searches for insider trading activity by company ticker symbol, CIK number, or company name. Returns all matching transaction records for the company including buys, sells, and option exercises.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/search", "query": "Tesla"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/search', {'query': 'Tesla'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/search", {
  "query": "Tesla"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/search", sandbase.Params{
	"query": "Tesla",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query - company ticker symbol (e.g. 'AAPL'), CIK number (e.g. '320193'), or company name (e.g. 'Apple')  |

## Details

Returns insider trading records from SEC Form 4 filings for a company. You pass one `query` value: a ticker symbol, a CIK number, or a company name.

### Use cases

- Check whether Tesla executives have been selling shares in recent months.
- Build an alert that watches new insider filings for a ticker.
- Pull the filing link for a specific insider transaction to read the original document.
- Compare trade size and price across several transactions by the same officer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Tesla"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query - company ticker symbol (e.g. 'AAPL'), CIK number (e.g. '320193'), or company name (e.g. 'Apple') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "query": "Tesla",
    "results": [
      {
        "average_price": "$360.13",
        "company": "Tesla Inc.",
        "filing": "View",
        "filing_url": "https://www.secform4.com/filings/1318605/0001104659-26-106432.htm",
        "insider_relationship": "Taneja Vaibhav Chief Financial Officer",
        "insider_relationship_url": "https://www.secform4.com/insider-trading/1771340.htm",
        "reported_datetime": "2026-09-09 7:00 pm",
        "shares_owned": "189,277 (Indirect Direct)",
        "shares_traded": "2,606",
        "symbol": "TSLA",
        "symbol_url": "https://www.secform4.com/#S2",
        "total_amount": "$938,419"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.query` | The search text that was sent in the request. |
| `data.results[].company / data.results[].symbol` | Company name and stock ticker for the transaction, such as `Tesla Inc.` and `TSLA`. |
| `data.results[].insider_relationship` | Name of the insider followed by their role at the company, for example a Chief Financial Officer. |
| `data.results[].insider_relationship_url` | Link to the page for that insider. |
| `data.results[].transaction_date` | Date of the trade followed by the transaction type, such as `Sale`. |
| `data.results[].reported_datetime` | Date and time the transaction was reported. |
| `data.results[].shares_traded` | Number of shares in the transaction, returned as a string. |
| `data.results[].average_price` | Average price per share for the transaction, returned as a string with a `$` sign. |
| `data.results[].total_amount` | Total dollar value of the transaction, returned as a string with a `$` sign. |
| `data.results[].shares_owned` | Shares held by the insider after the transaction, with an ownership label in parentheses. |
| `data.results[].filing_url` | Link to the filing document for the transaction. |

### Notes

- All numeric values, such as `shares_traded`, `average_price` and `total_amount`, are strings with commas and `$` signs. Strip them before doing math.
- The `transaction_date` field combines the date and the transaction type in one string, for example `2026-09-08 Sale`.
- The `filing_url` path contains the company CIK, for example `1318605`, followed by the filing accession number.
- For a narrower view of one company, try [SECForm4 Company Insider Trading](/apis/secform4/company-insider-trading). For sales only, use [SECForm4 Insider Sales](/apis/secform4/insider-sales).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/secform4/search.json`](../../../catalog/models/secform4/search.json) · Store page: https://www.sandbase.ai/model/secform4/search
