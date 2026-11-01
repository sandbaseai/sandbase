# Xiaohongshu User Profile

`xiaohongshu/user` · api · Xiaohongshu

Get a Xiaohongshu (RedNote) user profile from a user ID or supported profile URL. Use it to support creator discovery, account research, and reviewing a known profile before related content analysis.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/user", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/user', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/user", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/user", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | A Xiaohongshu user ID or a profile URL containing /user/profile/.  |

## Details

Get a Xiaohongshu (RedNote) user profile from a user ID or supported profile URL. Use it to support creator discovery, account research, and reviewing a known profile before related content analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | A Xiaohongshu user ID or a profile URL containing /user/profile/. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/user.json`](../../../catalog/models/xiaohongshu/user.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/user
