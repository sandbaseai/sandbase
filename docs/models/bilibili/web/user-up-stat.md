# Bilibili Creator View and Like Statistics API: pricing, parameters and code examples

`bilibili/web/user-up-stat` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns total video view and like counts for a specified Bilibili creator account. Lookup requires the user unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-up-stat", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-up-stat', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-up-stat", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-up-stat", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-up-stat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Fetch cumulative statistics including total video views and likes for a Bilibili content creator by passing their `uid`.

### Use cases

- Analyze overall engagement metrics for a target creator.
- Monitor total audience reach and like growth across an account.
- Evaluate creator influence for partnership assessment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-up-stat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "178360345"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Notes

- Pass the creator account ID using the `uid` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-up-stat.json`](../../../../catalog/models/bilibili/web/user-up-stat.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-up-stat
