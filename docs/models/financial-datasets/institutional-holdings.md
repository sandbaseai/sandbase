# Financial Datasets Institutional Holdings API: pricing, parameters and code examples

`financial-datasets/institutional-holdings` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

13F institutional holdings of a US stock by ticker: holder, shares, value and report period.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/institutional-holdings", "ticker": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/institutional-holdings', {'ticker': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/institutional-holdings", {
  "ticker": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/institutional-holdings", sandbase.Params{
	"ticker": "AAPL",
})
```

Same call via the path form: `POST /v1/api/financial-datasets/institutional-holdings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of holdings to return.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url.  |
| `ticker` | string | yes | Stock ticker, e.g. `AAPL`.  |

## Details

Returns 13F institutional holdings for a US stock. Each row shows one filer's position in the stock, with shares, value in USD and the report period. The only required input is a stock `ticker`, such as `AAPL`.

### Use cases

- List the largest institutional holders of a stock by `shares` or `value_usd`.
- Compare a filer's position across report periods to see whether it grew or shrank.
- Find late or amended 13F filings for a stock by checking `filing_date` and `form_type`.
- Check how a filer's stake splits by investment discretion and voting authority.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/institutional-holdings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "AAPL", "limit": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ticker` | string | Yes | Stock ticker, e.g. `AAPL`. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. |
| `limit` | integer | No | Maximum number of holdings to return. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "institutional_holdings": [
    {
      "accession_number": "0000102909-26-000031",
      "filer_cik": "0000102909",
      "filer_name": "VANGUARD GROUP INC",
      "filing_date": "2026-01-29",
      "form_type": "13F-HR",
      "name_of_issuer": "APPLE INC",
      "put_call": null,
      "report_period": "2025-12-31",
      "reported_price": 271.86,
      "shares": 1363322858,
      "subsidiaries": [
        {
          "investment_discretion": "SOLE",
          "other_managers": [],
          "row_num": 6673,
          "shares": 1279051701,
          "shares_principal_amount_type": "SH",
          "value_usd": 347722995434,
          "voting_authority_none": 1279051701,
          "voting_authority_shared": 0
        }
      ],
      "ticker": "AAPL"
    }
  ],
  "ticker": "AAPL"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `institutional_holdings[]` | One 13F position held by one filer in the requested stock. |
| `institutional_holdings[].filer_name / filer_cik` | Name and CIK of the institution that filed the 13F. |
| `institutional_holdings[].shares / value_usd` | Number of shares held and the reported value of the position in USD. |
| `institutional_holdings[].reported_price` | Share price used in the filing for this report period. |
| `institutional_holdings[].report_period / filing_date` | Quarter-end date the holding refers to, and the date the filing was made. |
| `institutional_holdings[].form_type` | SEC form type of the filing, such as `13F-HR` or the amended `13F-HR/A`. |
| `institutional_holdings[].accession_number` | SEC accession number that identifies the filing. |
| `institutional_holdings[].put_call` | Option type when the position is a put or call. It is `null` for plain shares. |
| `institutional_holdings[].subsidiaries[]` | Breakdown of the position into reported rows. It appears only on some holdings. |
| `institutional_holdings[].subsidiaries[].investment_discretion / voting_authority_none / voting_authority_shared` | Type of investment discretion for the row, and the shares with no voting authority or shared voting authority. |

### Notes

- Pass the stock symbol in `ticker`. Use `limit` to cap the number of holdings returned.
- For the next page, pass the cursor from the previous response's `next_page_url` as `cursor`.
- Rows can come from different `report_period` values, so check this field before you compare holders.
- To look up filings or insider activity for the same company, try [Financial Datasets Get Company SEC Filings](/apis/financial-datasets/filings) or [Financial Datasets Get Insider Trades](/apis/financial-datasets/insider-trades).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/institutional-holdings.json`](../../../catalog/models/financial-datasets/institutional-holdings.json) · Store page: https://www.sandbase.ai/model/financial-datasets/institutional-holdings
