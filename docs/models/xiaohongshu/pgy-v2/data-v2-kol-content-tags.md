# Xiaohongshu PGY Creator Content Tags API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v2-kol-content-tags` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Content category tags of a Xiaohongshu (RedNote) Pugongying creator by user ID, showing which subjects the creator publishes about.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v2-kol-content-tags", "userId": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v2-kol-content-tags', {'userId': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v2-kol-content-tags", {
  "userId": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v2-kol-content-tags", sandbase.Params{
	"userId": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v2-kol-content-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |

## Details

Content category tags of a Xiaohongshu (RedNote) Pugongying creator by user ID, showing which subjects the creator publishes about.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v2-kol-content-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5c668b3e0000000012021605"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v2-kol-content-tags.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v2-kol-content-tags.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v2-kol-content-tags
