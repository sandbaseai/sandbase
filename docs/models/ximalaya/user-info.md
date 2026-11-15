# Ximalaya User Info API: pricing, parameters and code examples

`ximalaya/user-info` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve public profile information for a user or anchor by numeric UID. Returns nickname, avatar, fan count, following count, track/album counts, personal signature, province/city, anchor grade, and live-stream status.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/user-info", "uid": "61885848"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/user-info', {'uid': '61885848'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/user-info", {
  "uid": "61885848"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/user-info", sandbase.Params{
	"uid": "61885848",
})
```

Same call via the path form: `POST /v1/api/ximalaya/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Numeric user ID (e.g. 10778196). Obtainable from album or track details (anchorUid or uid field).  |

## Details

Retrieve public profile information for a user or anchor by numeric UID. Returns nickname, avatar, fan count, following count, track/album counts, personal signature, province/city, anchor grade, and live-stream status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/user-info", "uid": "61885848"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Numeric user ID (e.g. 10778196). Obtainable from album or track details (anchorUid or uid field). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/user-info.json`](../../../catalog/models/ximalaya/user-info.json) · Store page: https://www.sandbase.ai/model/ximalaya/user-info
