# TikTok Profile Sec User ID API: pricing, parameters and code examples

`tiktok/web/sec-user-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the internal TikTok sec_user_id string for a specified user homepage URL. This identifier serves as a key parameter for downstream TikTok web endpoints.

## Pricing

- **$0.001 per call** (USD)
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

Returns the `sec_user_id` string for a TikTok user. You send the full profile homepage link in `url`, for example `https://www.tiktok.com/@tiktok`.

### Use cases

- Convert a profile link into the `sec_user_id` that other TikTok web endpoints ask for.
- Store a stable user key for each creator you track by profile link.
- Prepare the input for profile, post list, or follower list calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@tiktok"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | User homepage link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
```

### Response fields

| Field | Meaning |
|---|---|
| `$` | The whole body is one JSON string. It is the `sec_user_id` of the profile in `url`. There is no wrapper object and there are no other keys. |
| `$[0:8]` | The first 8 characters of the string. In the example they are `MS4wLjAB`. |
| `$[8:]` | The rest of the string after the first 8 characters. Keep the full value together and pass it unchanged to other endpoints. |

### Notes

- The body is a bare string, not an object. Read it directly instead of looking for a field name.
- Send a full homepage link in the form `https://www.tiktok.com/@username`.
- To resolve many profile links in one call, use [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id).
- To get the user ID from a profile link instead, use [TikTok User ID from Profile Link](/apis/tiktok/web/user-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/sec-user-id.json`](../../../../catalog/models/tiktok/web/sec-user-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/sec-user-id
