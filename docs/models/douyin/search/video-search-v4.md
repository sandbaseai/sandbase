# Douyin Video search V4 API: pricing, parameters and code examples

`douyin/search/video-search-v4` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch video search V4 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v4', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v4", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/video-search-v4", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v4` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor, 0 for the first request, then the cursor from the last response default `0` |
| `keyword` | string |  | Video title or keyword default `"猫咪"` |

## Details

Fetch video search V4 on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v4" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪", "cursor": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor, 0 for the first request, then the cursor from the last response |
| `keyword` | string | No | Video title or keyword |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v4.json`](../../../../catalog/models/douyin/search/video-search-v4.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v4
