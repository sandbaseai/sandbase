# Financial Datasets Get SEC Filing Items API: pricing, parameters and code examples

`financial-datasets/filings-items` · data API · Financial Datasets · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get SEC Filing Items from Financial Datasets. Returns the official Financial Datasets API response unchanged.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "financial-datasets/filings-items", "filing_type": "10-K", "ticker": "AAPL", "year": 2024}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('financial-datasets/filings-items', {'filing_type': '10-K', 'ticker': 'AAPL', 'year': 2024})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("financial-datasets/filings-items", {
  "filing_type": "10-K",
  "ticker": "AAPL",
  "year": 2024
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "financial-datasets/filings-items", sandbase.Params{
	"filing_type": "10-K",
	"ticker": "AAPL",
	"year": 2024,
})
```

Same call via the path form: `POST /v1/api/financial-datasets/filings-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item` | string |  | The item to get. one of: `Item-1`, `Item-1A`, `Item-1B`, `Item-2`, `Item-3`, `Item-4`, `Item-5`, `Item-6`, `Item-7`, `Item-7A`, `Item-8`, `Item-9` … |
| `year` | integer | yes | The year of the filing.  |
| `ticker` | string | yes | The ticker symbol.  |
| `quarter` | integer |  | The quarter of the filing if 10-Q.  |
| `filing_type` | string | yes | The type of filing. one of: `10-K`, `10-Q`, `8-K` |
| `accession_number` | string |  | The accession number of the filing if 8-K.  |
| `include_exhibits` | boolean |  | Whether to include the raw text from linked exhibits. Only applicable for 8-K filings. When true, exhibit objects will include the 'text' field containing the full exhibit content. default `false` |

## Details

Returns the text of sections (items) from a company's SEC filing, such as Item 1 Business or Item 1A Risk Factors. It needs a `ticker`, a `filing_type` (`10-K`, `10-Q` or `8-K`) and a `year`.

### Use cases

- Pull the Risk Factors section of a 10-K to compare risk language year over year.
- Feed the Business section of an annual report into a summarizer or search index.
- Read specific 8-K items to track events such as executive changes for a ticker.
- Collect filing text for a given company to build a dataset for text analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/financial-datasets/filings-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filing_type": "10-K", "ticker": "AAPL", "year": 2024}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `filing_type` | string | Yes | The type of filing. |
| `ticker` | string | Yes | The ticker symbol. |
| `year` | integer | Yes | The year of the filing. |
| `accession_number` | string | No | The accession number of the filing if 8-K. |
| `include_exhibits` | boolean | No | Whether to include the raw text from linked exhibits. Only applicable for 8-K filings. When true, exhibit objects will include the 'text' field containing the full exhibit content. |
| `item` | string | No | The item to get. |
| `quarter` | integer | No | The quarter of the filing if 10-Q. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "accession_number": "0000320193-24-000123",
  "cik": "0000320193",
  "filing_type": "10-K",
  "filing_url": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.…",
  "items": [
    {
      "number": "Item 1",
      "text": "Item 1. Business  Company Background  The Company designs, manufactures and mark…",
      "title": "Business"
    }
  ],
  "resource": "filing_items",
  "ticker": "AAPL",
  "year": 2024
}
```

### Response fields

| Field | Meaning |
|---|---|
| `accession_number` | The SEC accession number that identifies the filing. |
| `cik` | The company's SEC Central Index Key, as a zero-padded string. |
| `filing_type` | The form type of the filing, such as `10-K`. |
| `filing_url` | Link to the original filing document on sec.gov. |
| `items[].number` | The item label in the filing, such as `Item 1A`. |
| `items[].title` | The section name for the item, such as `Risk Factors`. |
| `items[].text` | The text of the item. Some items may contain table of contents text instead of the section body, so check the content before using it. |
| `ticker / year` | The ticker and filing year that the response matches. |

### Notes

- `filing_type`, `ticker` and `year` are required. Use `quarter` for `10-Q` filings and `accession_number` for `8-K` filings.
- Set `item` to a value such as `Item-1A` to request a single section. Set `include_exhibits` to `true` for `8-K` filings to add exhibit text.
- To find filings and their accession numbers first, call [Financial Datasets Get Company SEC Filings](/apis/financial-datasets/filings).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/financial-datasets/filings-items.json`](../../../catalog/models/financial-datasets/filings-items.json) · Store page: https://www.sandbase.ai/model/financial-datasets/filings-items
