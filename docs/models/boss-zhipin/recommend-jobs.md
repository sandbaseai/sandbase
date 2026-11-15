# BOSS Zhipin Recommend Jobs API: pricing, parameters and code examples

`boss-zhipin/recommend-jobs` · data API · BOSS Zhipin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve recommended and trending job listings from the BOSS直聘 homepage.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "boss-zhipin/recommend-jobs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('boss-zhipin/recommend-jobs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("boss-zhipin/recommend-jobs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "boss-zhipin/recommend-jobs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/boss-zhipin/recommend-jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `city` | string |  | City code for filtering jobs. Supported values: 100010000 (all cities), 101010100 (Beijing), 101020100 (Shanghai), 101280100 (Guangzhou), 101280600 (Shenzhen), 101210100 (Hangzhou), 101270100 (Chengdu), 101190100…  |

## Details

Retrieve recommended and trending job listings from the BOSS直聘 homepage.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "boss-zhipin/recommend-jobs", "city": "100010000"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city` | string | No | City code for filtering jobs. Supported values: 100010000 (all cities), 101010100 (Beijing), 101020100 (Shanghai), 101280100 (Guangzhou), 101280600 (Shenzhen), 101210100 (Hangzhou), 101270100 (Chengdu), 101190100 (Nanjin |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/boss-zhipin/recommend-jobs.json`](../../../catalog/models/boss-zhipin/recommend-jobs.json) · Store page: https://www.sandbase.ai/model/boss-zhipin/recommend-jobs
