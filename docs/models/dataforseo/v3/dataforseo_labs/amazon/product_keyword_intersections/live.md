# DataForSEO Amazon Product Keyword Intersections API: pricing, parameters and code examples

`dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.012 per call · **Modes:** sync

List keywords several ASINs rank for together, with positions.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asins` | object |  | Amazon ASINs, keyed "1", "2", ...  |
| `limit` | integer |  | Maximum number of results (up to 100).  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

List keywords several ASINs rank for together, with positions.

Request fields follow the official DataForSEO `/v3/dataforseo_labs/amazon/product_keyword_intersections/live` task schema (one task per call; send `{"tasks": [...]}` for several). `limit` is capped at 100. The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asins": {"1": "B0CP9YB3Q4", "2": "B0D1XD1ZV3"}, "limit": 5, "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `asins` | Amazon ASINs, keyed "1", "2", ... |
| `limit` | Maximum number of results (up to 100). |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Billed at the actual cost of each call, about $0.012 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/amazon/product_keyword_intersections/live
