# TikTok Web Hashed ID API: pricing, parameters and code examples

`tiktok/web/generate-hashed-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Calculates a hashed identifier for TikTok Web based on a provided email address. This endpoint takes an email input and returns the corresponding hashed ID value.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/generate-hashed-id", "email": "test@example.com"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/generate-hashed-id', {'email': 'test@example.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/generate-hashed-id", {
  "email": "test@example.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/generate-hashed-id", sandbase.Params{
	"email": "test@example.com",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/generate-hashed-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `email` | string | yes | Email address  |

## Details

Produces a hashed identifier for TikTok Web workflows using a target `email` address. Pass the required `email` parameter to obtain the hashed ID value.

### Use cases

- Look up hashed identifiers using user email addresses.
- Prepare hashed identity values for TikTok Web workflows.
- Convert email addresses into TikTok-compatible hashed IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/generate-hashed-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `email` | string | Yes | Email address |

### Notes

- `email` is a required string parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/generate-hashed-id.json`](../../../../catalog/models/tiktok/web/generate-hashed-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/generate-hashed-id
