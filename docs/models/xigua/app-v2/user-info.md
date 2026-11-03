# Xigua User Profile Details API: pricing, parameters and code examples

`xigua/app-v2/user-info` · data API · Xigua · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile and personal information for a specified Xigua account. Queries details using the target user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xigua/app-v2/user-info", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xigua/app-v2/user-info', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xigua/app-v2/user-info", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xigua/app-v2/user-info", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/xigua/app-v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User id  |

## Details

Retrieve detailed personal profile information for a Xigua user using their `user_id`.

### Use cases

- Display public profile information for a specific Xigua user.
- Verify Xigua account identifiers in analytics workflows.
- Track account metadata across creator platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xigua/app-v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "52712347586"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User id |

### Notes

- Requires a valid `user_id` parameter to look up profile records.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xigua Single Video Information](/apis/xigua/app-v2/one-video): Returns lightweight single video data and associated related video information from Xigua for a specific post by its unique item ID.
- [Xigua Video Play URL](/apis/xigua/app-v2/one-video-play-url): Returns the direct playback URL for a specific Xigua video using its unique item identifier.
- [Xigua Video Search](/apis/xigua/app-v2/search-video): Search Xigua Video (ByteDance long-form video) by keyword: titles, creators, duration, publish time and comment counts, with sort and duration filters.

---
Machine-readable: [`catalog/models/xigua/app-v2/user-info.json`](../../../../catalog/models/xigua/app-v2/user-info.json) · Store page: https://www.sandbase.ai/model/xigua/app-v2/user-info
