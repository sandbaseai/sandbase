# Yellow Pages Category List API: pricing, parameters and code examples

`yellowpages/category-list` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

List business categories from the YellowPages categories page, organized by service group (e.g., Home Services, Medical Services, Auto Services). Each group contains named sub-categories with their browse paths.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/category-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/category-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/category-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/category-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/yellowpages/category-list` with the body above minus `model`.

## Details

List business categories from the YellowPages categories page, organized by service group (e.g., Home Services, Medical Services, Auto Services). Each group contains named sub-categories with their browse paths.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/category-list"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/category-list.json`](../../../catalog/models/yellowpages/category-list.json) · Store page: https://www.sandbase.ai/model/yellowpages/category-list
