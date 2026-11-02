# DataForSEO Google Play Bulk App Metrics API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01212 per call · **Modes:** sync

Get ranking metrics for up to 100 Google Play apps at once: keyword counts, position distribution and estimated search visibility.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_ids` | array |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Get ranking metrics for up to 100 Google Play apps at once: keyword counts, position distribution and estimated search visibility.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_ids": ["com.openai.chatgpt"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. See the [official documentation](https://docs.dataforseo.com/v3/dataforseo_labs/google/bulk_app_metrics/live/) for every field.

### Pricing

Billed at the actual cost of each call, about $0.01212 for the request above. The cost grows with the number of rows, targets or pages a call returns. One task per request; `limit` is capped at 100 and input lists (`keywords`, `targets`, `asins`, `app_ids` ...) accept at most 100 items. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/bulk_app_metrics/live
