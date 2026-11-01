# DataForSEO Keyword Trend Explore

`dataforseo/v3/keywords_data/dataforseo_trends/explore/live` · api · DataForSEO

Get keyword search trend series from an independent trends dataset. DataForSEO Trends explore for up to 5 keywords.

## Pricing

- **$0.0012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/dataforseo_trends/explore/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/dataforseo_trends/explore/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/dataforseo_trends/explore/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/dataforseo_trends/explore/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/dataforseo_trends/explore/live` with the body above minus `model`.

## Details

Get keyword search trend series from an independent trends dataset.

Request fields follow the official DataForSEO `/v3/keywords_data/dataforseo_trends/explore/live` task schema (one task per call; send `{"tasks": [...]}` for several). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/dataforseo_trends/explore/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keywords` | List of keywords (up to 100 per call). |
| `location_code` | Location code, e.g. 2840 for the United States. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/keywords_data/dataforseo_trends/explore/live/

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/explore/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/dataforseo_trends/explore/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/dataforseo_trends/explore/live
