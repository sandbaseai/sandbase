# Weibo User following API: pricing, parameters and code examples

`weibo/app/user-following` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user following on Weibo. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-following", "uid": "1856404484"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-following', {'uid': '1856404484'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-following", {
  "uid": "1856404484"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-following", sandbase.Params{
	"uid": "1856404484",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Uid  |
| `since_id` | string |  | since_id  |
| `sort_type` | integer |  | Sort Type default `2` |

## Details

Get user following on Weibo. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1856404484", "sort_type": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes |  |
| `since_id` | string | No |  |
| `sort_type` | integer | No |  |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/weibo/app/user-following.json`](../../../../catalog/models/weibo/app/user-following.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-following
