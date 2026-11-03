# Kuaishou User Broadcast Replay API: pricing, parameters and code examples

`kuaishou/web/user-live-replay` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns recorded stream replay data for a specified Kuaishou user. The endpoint accepts a user identifier and an optional cursor parameter for paginating through past streams.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/user-live-replay", "user_id": "3795214411"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/user-live-replay', {'user_id': '3795214411'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/user-live-replay", {
  "user_id": "3795214411"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/user-live-replay", sandbase.Params{
	"user_id": "3795214411",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/user-live-replay` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 作品游标/Post cursor  |
| `user_id` | string | yes | 用户 ID (eid)/User ID (eid)  |

## Details

Retrieve recorded broadcast replays for a Kuaishou account using `user_id`. Supports pagination across past recordings via `pcursor`.

### Use cases

- Review recorded stream sessions from a specific broadcaster.
- Extract past broadcast replays for archive storage.
- Track historical streaming activity across user profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/user-live-replay" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3795214411"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | — |
| `pcursor` | string | No | — |

### Notes

- Pass `user_id` to identify the target account.
- Use `pcursor` to navigate across paginated pages of replay records.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/user-live-replay.json`](../../../../catalog/models/kuaishou/web/user-live-replay.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/user-live-replay
