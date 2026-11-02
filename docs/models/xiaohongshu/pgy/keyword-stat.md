# Xiaohongshu PGY keyword overview API: pricing, parameters and code examples

`xiaohongshu/pgy/keyword-stat` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY keyword overview on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/keyword-stat", "search_word": "面膜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/keyword-stat', {'search_word': '面膜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/keyword-stat", {
  "search_word": "面膜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/keyword-stat", sandbase.Params{
	"search_word": "面膜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/keyword-stat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `search_word` | string | yes | Keyword  |

## Details

PGY keyword overview on Xiaohongshu. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/keyword-stat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "面膜"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Keyword |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/keyword-stat.json`](../../../../catalog/models/xiaohongshu/pgy/keyword-stat.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/keyword-stat
