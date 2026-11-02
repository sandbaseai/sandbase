# Douyin Search Field Options API: pricing, parameters and code examples

`douyin/xingtu-v2/search-field-options` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Search Field Options on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/search-field-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/search-field-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/search-field-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/search-field-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/search-field-options` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `task_category` | integer |  | Task category, 1=Douyin video, 6=Douyin live, 11=Toutiao article default `1` |
| `platform_source` | integer |  | Platform source, 1=Douyin, 2=Toutiao default `1` |

## Details

Get Search Field Options on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/search-field-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform_source": 1, "task_category": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `platform_source` | integer | No | Platform source, 1=Douyin, 2=Toutiao |
| `task_category` | integer | No | Task category, 1=Douyin video, 6=Douyin live, 11=Toutiao article |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/search-field-options.json`](../../../../catalog/models/douyin/xingtu-v2/search-field-options.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/search-field-options
