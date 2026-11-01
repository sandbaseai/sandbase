# DataForSEO App Store Bulk App Metrics

`dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live` · api · DataForSEO

Get ranking metrics for up to 100 App Store apps at once: keyword counts, position distribution and estimated search visibility.

## Pricing

- **$0.024 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live` with the body above minus `model`.

## Details

Get ranking metrics for up to 100 App Store apps at once: keyword counts, position distribution and estimated search visibility.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_ids": ["6448311069"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The body is passed through to DataForSEO. See the [official documentation](https://docs.dataforseo.com/v3/dataforseo_labs/apple/bulk_app_metrics/live/) for every field.

### Pricing

Flat price per call. One task per request; `limit` is capped at 100 and input lists (`keywords`, `targets`, `asins`, `app_ids` ...) accept at most 100 items. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/apple/bulk_app_metrics/live
