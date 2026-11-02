# DataForSEO Clickstream Bulk Search Volume API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01224 per call · **Modes:** sync

Clickstream-based monthly search volume for up to 1,000 keywords in one request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01224**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keywords` | array |  | Array of keywords (up to 1,000).  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Clickstream-based monthly search volume for up to 1,000 keywords in one request.

Request fields follow the official DataForSEO `/v3/keywords_data/clickstream_data/bulk_search_volume/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["coffee", "tea"], "location_code": 2840}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `keywords` | Array of keywords (up to 1,000). |
| `location_code` | Location code, e.g. 2840 for the United States. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/keywords_data/clickstream_data/bulk_search_volume/live/

### Pricing

Billed at the actual cost of each call, about $0.01224 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/clickstream_data/bulk_search_volume/live
