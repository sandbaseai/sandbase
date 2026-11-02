# DataForSEO Labs Historical Bulk Traffic Estimation API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1224 per call · **Modes:** sync

Monthly estimated organic and paid traffic history for up to 1,000 domains.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `targets` | array |  | Array of domains (up to 1,000).  |
| `date_from` | string |  | Optional start date, "yyyy-mm-dd".  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Monthly estimated organic and paid traffic history for up to 1,000 domains.

Request fields follow the official DataForSEO `/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `targets` | Array of domains (up to 1,000). |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |
| `date_from` | Optional start date, "yyyy-mm-dd". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live/

### Pricing

Billed at the actual cost of each call, about $0.1224 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live
