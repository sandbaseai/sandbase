# Bilibili User Collection Folders

`bilibili/web/collect-folders` · api · Bilibili

Returns the collection folders owned by a specific Bilibili user. Supply the user identifier via `uid` to inspect their public collection folders.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/collect-folders", "uid": "178360345"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/collect-folders', {'uid': '178360345'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/collect-folders", {
  "uid": "178360345"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/collect-folders", sandbase.Params{
	"uid": "178360345",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/collect-folders` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

This endpoint retrieves the collection folders for a specified user account. Pass the target user ID using the `uid` parameter.

### Use cases

- Inspect public collection folder lists for a specific Bilibili user.
- Organize and display saved video collections from a target account.
- Monitor changes in a creator's collection folder structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/collect-folders" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1437582453"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Notes

- Requires the target user ID in the `uid` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili Comprehensive Popular Videos](/model/bilibili/web/com-popular): Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

---
Machine-readable: [`catalog/models/bilibili/web/collect-folders.json`](../../../../catalog/models/bilibili/web/collect-folders.json) · Store page: https://www.sandbase.ai/model/bilibili/web/collect-folders
