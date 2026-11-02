# Bilibili User Dynamics API: pricing, parameters and code examples

`bilibili/web/user-dynamic` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves dynamic feed posts and timeline updates for a specified Bilibili user by UID, with optional offset-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-dynamic", "offset": "", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-dynamic', {'offset': '', 'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-dynamic", {
  "offset": "",
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-dynamic", sandbase.Params{
	"offset": "",
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-dynamic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |
| `offset` | string |  | offset default `""` |

## Details

Accesses dynamic timeline posts for a designated Bilibili account using `uid`. Supports navigating dynamic feed histories via the `offset` parameter.

### Use cases

- Monitor recent community posts from a specific content creator.
- Track timeline activity and status updates on Bilibili.
- Extract post history across paginated user feeds.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-dynamic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |
| `offset` | string | No | offset |

### Notes

- Specify the target account using `uid`.
- Pass `offset` to retrieve subsequent pages of dynamic posts.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-dynamic.json`](../../../../catalog/models/bilibili/web/user-dynamic.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-dynamic
