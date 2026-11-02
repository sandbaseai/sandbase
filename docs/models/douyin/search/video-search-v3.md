# Douyin Video search V3 API: pricing, parameters and code examples

`douyin/search/video-search-v3` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch video search V3 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v3"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v3', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v3", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/video-search-v3", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string |  | Search keyword default `"美食"` |
| `date_type` | integer |  | Publish date filter: 0=any, 3=last 3 days, 7=last 7 days, 30=last 30 days default `0` |
| `label_type` | integer |  | Video type filter: 0=any, 1=low-follower hit, 2=high completion rate, 3=high follower growth, 4=high like rate default `0` |
| `duration_type` | integer |  | Duration filter: 0=any, 1=0-15s, 6=15-60s, 7=60-120s, 8=120-180s, 9=over 180s default `0` |

## Details

Fetch video search V3 on Douyin. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "美食", "date_type": 0, "label_type": 0, "duration_type": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_type` | integer | No | Publish date filter: 0=any, 3=last 3 days, 7=last 7 days, 30=last 30 days |
| `duration_type` | integer | No | Duration filter: 0=any, 1=0-15s, 6=15-60s, 7=60-120s, 8=120-180s, 9=over 180s |
| `label_type` | integer | No | Video type filter: 0=any, 1=low-follower hit, 2=high completion rate, 3=high follower growth, 4=high like rate |
| `query` | string | No | Search keyword |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v3.json`](../../../../catalog/models/douyin/search/video-search-v3.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v3
