# Web3.career Web3 Companies API: pricing, parameters and code examples

`web3-career/web3-companies` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch a paginated list of Web3 companies hiring on the platform. Each company includes its name and profile page URL.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/web3-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/web3-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/web3-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/web3-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/web3-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |

## Details

Returns a page of Web3 companies that are hiring on Web3.career. Each company has a name and a profile page URL. The only input is an optional `page` number.

### Use cases

- Build a list of crypto employers to target for outreach or recruiting research.
- Track which companies appear on the first pages of the Web3.career company directory.
- Collect company profile URLs to feed a scraper or a CRM import.
- Match company names against your own watchlist of exchanges and protocols.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/web3-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "companies": [
      {
        "name": "Binance",
        "url": "https://web3.career/web3-companies/binance"
      }
    ],
    "page": "1"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.companies[]` | List of companies on the requested page. |
| `data.companies[].name` | Company name as shown on Web3.career, for example `Binance`. |
| `data.companies[].url` | Link to the company profile page on Web3.career. The last part of the path looks like a slug, for example `crypto-com`. |
| `data.page` | Page number of this result, returned as a string such as `"1"`. |
| `status` | Result status of the call. `success` means the data was returned. |

### Notes

- Send `page` to move through the list. The request without `page` returned page `1`.
- To see open roles for a company, call [Web3.career Company Jobs](/apis/web3-career/company-jobs).
- To browse all open roles instead of companies, use [Web3.career Job Listings](/apis/web3-career/job-listings).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/web3-companies.json`](../../../catalog/models/web3-career/web3-companies.json) · Store page: https://www.sandbase.ai/model/web3-career/web3-companies
