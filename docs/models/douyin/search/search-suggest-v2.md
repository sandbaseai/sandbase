# Douyin Search keyword suggestions V2 API: pricing, parameters and code examples

`douyin/search/search-suggest-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch search keyword suggestions V2 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/search-suggest-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/search-suggest-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/search-suggest-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/search-suggest-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/search-suggest-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | The keyword to be suggested default `"人工智能"` |
| `history_words` | string |  | Optional, the user's history search words (comma separated), affects the ranking of suggestions  |

## Details

Fetch search keyword suggestions V2 on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/search-suggest-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `history_words` | string | No | Optional, the user's history search words (comma separated), affects the ranking of suggestions |
| `keyword` | string | No | The keyword to be suggested |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/search/search-suggest-v2.json`](../../../../catalog/models/douyin/search/search-suggest-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/search-suggest-v2
