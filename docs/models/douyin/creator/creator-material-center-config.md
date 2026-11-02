# Douyin Material Center Configuration API: pricing, parameters and code examples

`douyin/creator/creator-material-center-config` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns configuration details and settings for the Douyin material center. Provides system parameters and feature availability for account asset workflows.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-config"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-config', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-config", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-config", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-config` with the body above minus `model`.

## Details

Access Douyin material center configuration settings without passing query parameters.

### Use cases

- Inspect available material center features and options.
- Verify system configurations for Douyin digital assets.
- Load material center settings into management dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-config" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-config.json`](../../../../catalog/models/douyin/creator/creator-material-center-config.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-config
