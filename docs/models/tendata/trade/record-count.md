# Customs Trade Record Count API: pricing, parameters and code examples

`tendata/trade/record-count` · data API · Tendata · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Count the customs records that match a trade query before paying for rows, to check that filters are narrow enough.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0 |

Formula: `0`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tendata/trade/record-count", "catalog": "imports", "endDate": "2025-12-31", "startDate": "2025-01-01"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tendata/trade/record-count', {'catalog': 'imports', 'endDate': '2025-12-31', 'startDate': '2025-01-01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tendata/trade/record-count", {
  "catalog": "imports",
  "endDate": "2025-12-31",
  "startDate": "2025-01-01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tendata/trade/record-count", sandbase.Params{
	"catalog": "imports",
	"endDate": "2025-12-31",
	"startDate": "2025-01-01",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/tendata/trade/record-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `hsCode` | string |  | Customs HS code, 4+ digits (e.g. '630492'). A 2-digit chapter code works only combined with productDesc or a company name.  |
| `weight` | array |  | Weight range in kilograms, as [min, max].  |
| `catalog` | string | yes | Data-source side: customs import records or export records. one of: `imports`, `exports` |
| `endDate` | string | yes | Query window end, YYYY-MM-DD.  |
| `exporter` | string |  | Exporter company name (min 2 chars). Drop company suffixes and special characters for better matching.  |
| `importer` | string |  | Importer company name (min 2 chars). Drop company suffixes and special characters for better matching.  |
| `quantity` | array |  | Quantity range, as [min, max].  |
| `sumOfUSD` | array |  | Total USD value range, as [min, max].  |
| `startDate` | string | yes | Query window start, YYYY-MM-DD. The window may span at most three years.  |
| `searchMode` | string |  | Set to FUZZY_SINGLE for single-keyword fuzzy matching; omit for the default smart search.  |
| `productDesc` | string |  | Product description keywords; separate multiple keywords with semicolons (e.g. 'electronics; home appliance').  |
| `quantityUnit` | string |  | Quantity unit filter (e.g. 'PCS', 'PKG').  |
| `portOfArrival` | string |  | Arrival port name.  |
| `transportType` | string |  | Transport mode (e.g. sea, air, road).  |
| `containProducer` | boolean |  | Include producer companies (available on Russia/Kazakhstan sources).  |
| `portOfDeparture` | string |  | Departure port name.  |
| `filterBlankFields` | array |  | Drop records whose named party is blank (e.g. ["importer"]).  |
| `optimizationModel` | boolean |  | Prefer the vendor's optimized data sources.  |
| `weightUnitPriceUSD` | array |  | USD unit price per kilogram range, as [min, max].  |
| `countryOfOriginCode` | string |  | Origin country ISO3 code(s), semicolon-separated (e.g. 'CHN;USA').  |
| `filterLogisticFields` | array |  | Drop records whose named party is a logistics company (e.g. ["exporter"]). Buyers have reported forwarders still being returned, so screen party names yourself.  |
| `quantityUnitPriceUSD` | array |  | USD unit price per quantity range, as [min, max].  |
| `countryOfDestinationCode` | string |  | Destination country ISO3 code(s), semicolon-separated (e.g. 'USA;CHN').  |

## Details

Count the customs records that match a trade query before paying for rows, to check that filters are narrow enough.

---
Machine-readable: [`catalog/models/tendata/trade/record-count.json`](../../../../catalog/models/tendata/trade/record-count.json) · Store page: https://www.sandbase.ai/model/tendata/trade/record-count
