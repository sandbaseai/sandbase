# Financial Datasets Get Insider Trades API: pricing, parameters and code examples

`financial-datasets/insider-trades` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get insider trades like buys and sells for a ticker by a company insider.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/insider-trades"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/insider-trades', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/insider-trades", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/insider-trades", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/financial-datasets/insider-trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string |  | Filter by insider name (e.g., 'Jen Hsun Huang'). Use the /insider-trades/names endpoint to get available names for a ticker.  |
| `limit` | string |  | The maximum number of transactions to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema):…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or…  |
| `ticker` | string |  | The ticker symbol of the company.  |
| `form_type` | string |  | Filter by SEC form type: 4 for trades, 5 for annual statements (or their amendments 4/A, 5/A). one of: `4`, `4/A`, `5`, `5/A` |
| `filing_date` | string |  | Filter by exact filing date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gt` | string |  | Filter by filing date greater than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lt` | string |  | Filter by filing date less than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_gte` | string |  | Filter by filing date greater than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `filing_date_lte` | string |  | Filter by filing date less than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`.  |
| `transaction_type` | string |  | Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use the /insider-trades/transaction-types endpoint to get available types.  |

## Details

Returns SEC insider trade records for a company, such as open market sales and purchases by officers and directors. Each record shows the insider, the transaction size and price, and share holdings before and after. The main input is a `ticker` such as `AAPL`.

### Use cases

- Track when executives at a company sell or buy shares and at what price.
- Build an alert that flags new insider sales filed after a given date with `filing_date_gte`.
- Compare an insider's holdings before and after each trade to see how much of their position they sold.
- Filter by `transaction_type` to separate open market sales from gifts when screening for insider sentiment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/insider-trades" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": "2", "ticker": "AAPL"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a previous response's next_page_url. When provided, all other query parameters are ignored: the cursor carries the original request's filters. Treat it as opaque; do not construct or modify  |
| `filing_date` | string | No | Filter by exact filing date in YYYY-MM-DD format. Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gt` | string | No | Filter by filing date greater than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_gte` | string | No | Filter by filing date greater than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lt` | string | No | Filter by filing date less than this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `filing_date_lte` | string | No | Filter by filing date less than or equal to this date (YYYY-MM-DD). Provider reference (supplier schema): `{"format":"date","type":"string"}`. |
| `form_type` | string | No | Filter by SEC form type: 4 for trades, 5 for annual statements (or their amendments 4/A, 5/A). |
| `limit` | string | No | The maximum number of transactions to return (default: 10). This is the total across all pages, not a page size: each page holds up to 10 records, linked by `next_page_url`. Provider reference (supplier schema): `{"defau |
| `name` | string | No | Filter by insider name (e.g., 'Jen Hsun Huang'). Use the /insider-trades/names endpoint to get available names for a ticker. |
| `ticker` | string | No | The ticker symbol of the company. |
| `transaction_type` | string | No | Filter by transaction type (e.g., 'Open market sale', 'Gift'). Use the /insider-trades/transaction-types endpoint to get available types. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "insider_trades": [
    {
      "filing_date": "2026-10-29",
      "form_type": "4",
      "is_board_director": false,
      "issuer": "Apple Inc.",
      "name": "Newstead Jennifer",
      "report_period": "2026-10-27",
      "security_title": "Common Stock",
      "shares_owned_after_transaction": 32396.0,
      "shares_owned_before_transaction": 34795.0,
      "ticker": "AAPL",
      "title": "SVP, GC and Government Affairs",
      "transaction_code": "S"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `insider_trades[]` | List of insider transactions, one object per transaction. |
| `insider_trades[].name / insider_trades[].title` | Name of the insider and their role at the company. `is_board_director` shows whether they sit on the board. |
| `insider_trades[].issuer / insider_trades[].ticker` | Company name and ticker symbol of the company whose shares were traded. |
| `insider_trades[].transaction_date / insider_trades[].filing_date` | Date of the trade and date the form was filed, both in `YYYY-MM-DD` format. `report_period` is the period date reported on the filing. |
| `insider_trades[].transaction_type / insider_trades[].transaction_code` | Text label of the transaction, such as `Open market sale`, and its short code, such as `S`. |
| `insider_trades[].transaction_shares` | Number of shares in the transaction. |
| `insider_trades[].transaction_price_per_share / insider_trades[].transaction_value` | Price per share and the total value of the transaction. In the sample, the value equals shares times price. |
| `insider_trades[].shares_owned_before_transaction / insider_trades[].shares_owned_after_transaction` | Number of shares the insider held before and after the transaction. |
| `insider_trades[].form_type / insider_trades[].security_title` | SEC form type the trade was reported on, such as `4`, and the type of security traded, such as `Common Stock`. |

### Notes

- Use `limit` to set the total number of records. Each page holds up to 10 records, and `next_page_url` links to the next page.
- Pass the `cursor` from `next_page_url` to get the next page. When you send `cursor`, all other parameters are ignored.
- Get valid `name` values from the `/insider-trades/names` endpoint and valid `transaction_type` values from the `/insider-trades/transaction-types` endpoint.
- To see the filings behind a trade, call [Financial Datasets Get Company SEC Filings](/apis/financial-datasets/filings).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/insider-trades.json`](../../../catalog/models/financial-datasets/insider-trades.json) · Store page: https://www.sandbase.ai/model/financial-datasets/insider-trades
