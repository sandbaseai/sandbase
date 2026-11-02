# DataForSEO Labs Domain Metrics by Categories API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.132 per call · **Modes:** sync

Top domains in product or service categories with organic traffic and keyword metrics on two dates.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live` with the body above minus `model`.

## Details

Top domains in product or service categories with organic traffic and keyword metrics on two dates.

Request fields follow the official DataForSEO `/v3/dataforseo_labs/google/domain_metrics_by_categories/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_codes": [10994], "location_code": 2840, "language_code": "en", "first_date": "2026-01-01", "second_date": "2026-06-01", "limit": 10}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `category_codes` | Array of category codes. |
| `first_date` | First comparison date, "yyyy-mm-dd". |
| `second_date` | Second comparison date, "yyyy-mm-dd". |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |
| `limit` | Maximum number of domains to return. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/dataforseo_labs/google/domain_metrics_by_categories/live/

### Pricing

Billed at the actual cost of each call, about $0.132 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/domain_metrics_by_categories/live
