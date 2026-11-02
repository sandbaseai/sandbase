# Tencent Huxuan Official Account Creator Search API: pricing, parameters and code examples

`tencent-huxuan/mp-publisher-search` · data API · Tencent Huxuan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Search or browses QQ Huxuan Official Account creators by optional nickname or account keyword with page-number pagination. Use it to discover and shortlist publishers for Tencent Huxuan campaign planning.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/mp-publisher-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent-huxuan/mp-publisher-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent-huxuan/mp-publisher-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent-huxuan/mp-publisher-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tencent-huxuan/mp-publisher-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number. The first page is 1. default `1` |
| `keyword` | string |  | Creator nickname or account keyword. Leave empty to browse the default marketplace list.  |

## Details

Search or browses QQ Huxuan Official Account creators by optional nickname or account keyword with page-number pagination. Use it to discover and shortlist publishers for Tencent Huxuan campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tencent-huxuan/mp-publisher-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Creator nickname or account keyword. Leave empty to browse the default marketplace list. |
| `page` | integer | No | Page number. The first page is 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tencent-huxuan/mp-publisher-search.json`](../../../catalog/models/tencent-huxuan/mp-publisher-search.json) · Store page: https://www.sandbase.ai/model/tencent-huxuan/mp-publisher-search
