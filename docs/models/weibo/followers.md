# Weibo User Followers

`weibo/followers` · api · Weibo

Get a page of accounts followed by a Weibo user identified by UID. Use it to examine the account's outgoing follow network or continue through its following list.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/followers", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/followers', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/followers", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/followers", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `page` | integer |  | Page number, starting with 1. default `1` |

## Details

Get a page of accounts followed by a Weibo user identified by UID. Use it to examine the account's outgoing follow network or continue through its following list.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |
| `page` | integer | No | Page number, starting with 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/weibo/followers.json`](../../../catalog/models/weibo/followers.json) · Store page: https://www.sandbase.ai/model/weibo/followers
