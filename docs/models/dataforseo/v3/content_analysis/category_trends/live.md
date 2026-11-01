# DataForSEO Content Analysis Category Trends

`dataforseo/v3/content_analysis/category_trends/live` · api · DataForSEO

Citation counts, sentiment and top domains over time for a content category.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024324**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/category_trends/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/category_trends/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/category_trends/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/category_trends/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/category_trends/live` with the body above minus `model`.

## Details

Citation counts, sentiment and top domains over time for a content category.

Request fields follow the official DataForSEO `/v3/content_analysis/category_trends/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/category_trends/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_code": 10994, "date_from": "2026-09-01", "date_group": "week"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `category_code` | Content category code, e.g. 10994. |
| `date_from` | Start date, "yyyy-mm-dd". |
| `date_to` | Optional end date. |
| `date_group` | "day", "week" or "month". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/content_analysis/category_trends/live/

### Pricing

Billed at the actual cost of each call, about $0.024324 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/category_trends/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/category_trends/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/category_trends/live
