# DataForSEO Google Subdomains API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/google/subdomains/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0132 per call · **Modes:** sync

List the subdomains of a domain with their ranked keyword counts, position distribution and estimated organic traffic in Google.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0132**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/subdomains/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/subdomains/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/subdomains/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/subdomains/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/subdomains/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  |   |
| `target` | string |  |   |
| `language_code` | string |  |   |
| `location_code` | integer |  |   |

## Details

List the subdomains of a domain with their ranked keyword counts, position distribution and estimated organic traffic in Google.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/subdomains/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "openai.com", "location_code": 2840, "language_code": "en", "limit": 10}'
```

### Parameters

The body is passed through to DataForSEO. See the [official documentation](https://docs.dataforseo.com/v3/dataforseo_labs/google/subdomains/live/) for every field.

### Pricing

Billed at the actual cost of each call, about $0.0132 for the request above. The cost grows with the number of rows, targets or pages a call returns. One task per request; `limit` is capped at 100 and input lists (`keywords`, `targets`, `asins`, `app_ids` ...) accept at most 100 items. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/subdomains/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/subdomains/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/subdomains/live
