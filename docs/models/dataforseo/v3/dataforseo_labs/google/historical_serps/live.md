# DataForSEO Labs Historical SERPs

`dataforseo/v3/dataforseo_labs/google/historical_serps/live` · api · DataForSEO

Past Google search results for a keyword within a date range.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/historical_serps/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/historical_serps/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/historical_serps/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/historical_serps/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/historical_serps/live` with the body above minus `model`.

## Details

Past Google search results for a keyword within a date range.

Request fields follow the official DataForSEO `/v3/dataforseo_labs/google/historical_serps/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/historical_serps/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coffee", "location_code": 2840, "language_code": "en", "date_from": "2026-06-01"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `keyword` | Keyword. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |
| `date_from` | Optional start date, "yyyy-mm-dd". |
| `date_to` | Optional end date. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/dataforseo_labs/google/historical_serps/live/

### Pricing

Billed at the actual cost of each call, about $0.00024 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/historical_serps/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/historical_serps/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/historical_serps/live
