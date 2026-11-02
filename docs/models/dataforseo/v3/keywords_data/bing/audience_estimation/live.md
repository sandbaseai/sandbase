# DataForSEO Bing Audience Estimation API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/bing/audience_estimation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Estimate Microsoft Ads audience size for targeting criteria. Bing Ads audience estimate for a location plus optional age, gender, industry, and job_function targeting, bid, and daily budget.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/audience_estimation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/audience_estimation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/audience_estimation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/audience_estimation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/audience_estimation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `age` | array |  | Audience age groups.  |
| `bid` | integer |  | Bid in USD.  |
| `daily_budget` | integer |  | Daily budget in USD.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Estimate Microsoft Ads audience size for targeting criteria.

Request fields follow the official DataForSEO `/v3/keywords_data/bing/audience_estimation/live` task schema (one task per call; send `{"tasks": [...]}` for several). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/audience_estimation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_code": 2840, "language_code": "en", "age": ["twenty_five_to_thirty_four"], "bid": 1, "daily_budget": 100}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |
| `age` | Audience age groups. |
| `bid` | Bid in USD. |
| `daily_budget` | Daily budget in USD. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/keywords_data/bing/audience_estimation/live/

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/audience_estimation/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/audience_estimation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/audience_estimation/live
