# TikTok Profile Sec User ID API: pricing, parameters and code examples

`tiktok/web/sec-user-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the internal TikTok sec_user_id string for a specified user homepage URL. This identifier serves as a key parameter for downstream TikTok web endpoints.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/sec-user-id", "url": "https://www.tiktok.com/@tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/sec-user-id', {'url': 'https://www.tiktok.com/@tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/sec-user-id", {
  "url": "https://www.tiktok.com/@tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/sec-user-id", sandbase.Params{
	"url": "https://www.tiktok.com/@tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | User homepage link  |

## Details

Extract the internal `sec_user_id` from a TikTok profile by providing the homepage link through `url`.

### Use cases

- Resolve a public profile link into a TikTok sec_user_id string.
- Obtain the required user identifier for subsequent API calls.
- Automate profile data gathering workflows from standard web links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@tiktok"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | User homepage link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
```

### Notes

- The `url` parameter expects a full TikTok user homepage link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/sec-user-id.json`](../../../../catalog/models/tiktok/web/sec-user-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/sec-user-id
