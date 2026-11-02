# DataForSEO App Store App Competitors API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/apple/app_competitors/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

Find App Store apps that compete with an iOS app for the same search keywords, with intersecting keyword counts and positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/apple/app_competitors/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/apple/app_competitors/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/apple/app_competitors/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/apple/app_competitors/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/apple/app_competitors/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `app_id` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

Find App Store apps that compete with an iOS app for the same search keywords, with intersecting keyword counts and positions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/apple/app_competitors/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "6448311069", "location_code": 2840, "language_code": "en", "limit": 10}'
```

### Parameters

The body is passed through to DataForSEO. See the [official documentation](https://docs.dataforseo.com/v3/dataforseo_labs/apple/app_competitors/live/) for every field.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. The cost grows with the number of rows, targets or pages a call returns. One task per request; `limit` is capped at 100 and input lists (`keywords`, `targets`, `asins`, `app_ids` ...) accept at most 100 items. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/apple/app_competitors/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/apple/app_competitors/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/apple/app_competitors/live
