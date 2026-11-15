# Ximalaya Categories API: pricing, parameters and code examples

`ximalaya/categories` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve all top-level content categories on Ximalaya. Each category has a pinyin name usable as a key in get_category_albums. Returns the full category tree in one call (no pagination).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/ximalaya/categories` with the body above minus `model`.

## Details

Retrieve all top-level content categories on Ximalaya. Each category has a pinyin name usable as a key in get_category_albums. Returns the full category tree in one call (no pagination).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/categories"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/categories.json`](../../../catalog/models/ximalaya/categories.json) · Store page: https://www.sandbase.ai/model/ximalaya/categories
