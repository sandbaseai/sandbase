# TikTok User ID from Profile Link API: pricing, parameters and code examples

`tiktok/web/user-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Resolves a TikTok profile URL to extract and return the corresponding user ID. Input the profile homepage link to retrieve account identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-id", "url": "https://static.sandbase.ai/examples/e0e8276f-b86b-4299-81d4-e769cc020a8b/input/c01fe486-11a3-4caf-bf06-2347828e1b40.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-id', {'url': 'https://static.sandbase.ai/examples/e0e8276f-b86b-4299-81d4-e769cc020a8b/input/c01fe486-11a3-4caf-bf06-2347828e1b40.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-id", {
  "url": "https://static.sandbase.ai/examples/e0e8276f-b86b-4299-81d4-e769cc020a8b/input/c01fe486-11a3-4caf-bf06-2347828e1b40.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-id", sandbase.Params{
	"url": "https://static.sandbase.ai/examples/e0e8276f-b86b-4299-81d4-e769cc020a8b/input/c01fe486-11a3-4caf-bf06-2347828e1b40.bin",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | User homepage link  |

## Details

Look up a TikTok user identifier from a profile link provided in `url`.

### Use cases

- Resolve account identifiers from TikTok profile links.
- Map creator profile URLs to user IDs for downstream data retrieval.
- Extract user IDs to integrate TikTok accounts into internal databases.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@tiktok"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | User homepage link |

### Notes

- Requires a TikTok profile homepage link passed to `url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-id.json`](../../../../catalog/models/tiktok/web/user-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-id
