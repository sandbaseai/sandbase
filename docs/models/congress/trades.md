# US Congress Stock Trades API: pricing, parameters and code examples

`congress/trades` · data API · US Congress · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00905 per call · **Modes:** sync

Get US Congress members' financial disclosures and stock trades (member, ticker, transaction type, amount range, and dates), filterable by member, ticker, or date range. Results come newest filing first (by reportedUtc, not tradedUtc), so a recent filing can list trades made years earlier.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00905**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "congress/trades"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('congress/trades', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("congress/trades", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "congress/trades", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/congress/trades` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. range 1–25 |
| `ticker` | string |  | Filter to transactions involving this stock ticker symbol (e.g. NVDA).  |
| `endDate` | string |  | Latest transaction date to include, inclusive, in YYYY-MM-DD format (e.g. 2026-06-01).  |
| `lastName` | string |  | Filter by the congressional member's last name, case-insensitive partial match (e.g. Pelosi).  |
| `firstName` | string |  | Filter by the congressional member's first name, case-insensitive partial match (e.g. Nancy).  |
| `startDate` | string |  | Earliest transaction date to include, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01).  |

## Details

Get US Congress members' financial disclosures and stock trades (member, ticker, transaction type, amount range, and dates), filterable by member, ticker, or date range. Results come newest filing first (by reportedUtc, not tradedUtc), so a recent filing can list trades made years earlier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "congress/trades", "limit": 5}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `endDate` | string | No | Latest transaction date to include, inclusive, in YYYY-MM-DD format (e.g. 2026-06-01). |
| `firstName` | string | No | Filter by the congressional member's first name, case-insensitive partial match (e.g. Nancy). |
| `lastName` | string | No | Filter by the congressional member's last name, case-insensitive partial match (e.g. Pelosi). |
| `limit` | integer | No | Maximum number of results to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. |
| `startDate` | string | No | Earliest transaction date to include, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01). |
| `ticker` | string | No | Filter to transactions involving this stock ticker symbol (e.g. NVDA). |

### Pricing

Billed at the actual cost of each call: about $0.00181 per result returned, up to $0.0462 per request (about $0.00905 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/congress/trades.json`](../../../catalog/models/congress/trades.json) · Store page: https://www.sandbase.ai/model/congress/trades
