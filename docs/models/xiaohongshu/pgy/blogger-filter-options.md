# Xiaohongshu PGY blogger filter options API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-filter-options` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get PGY blogger filter options on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-filter-options"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-filter-options', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-filter-options", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-filter-options", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-filter-options` with the body above minus `model`.

## Details

Get PGY blogger filter options on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-filter-options" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|


### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-filter-options.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-filter-options.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-filter-options
