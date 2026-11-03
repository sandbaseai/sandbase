# TikTok User Sec User ID Extractor API: pricing, parameters and code examples

`tiktok/web/all-sec-user-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs. Provide an array of user homepage links in the request body to retrieve their unique security IDs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/all-sec-user-id", "body": ["https://www.tiktok.com/@tiktok"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/all-sec-user-id', {'body': ['https://www.tiktok.com/@tiktok']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/all-sec-user-id", {
  "body": [
    "https://www.tiktok.com/@tiktok"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/all-sec-user-id", sandbase.Params{
	"body": []any{"https://www.tiktok.com/@tiktok"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/all-sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | User homepage link  |

## Details

This API takes an array of TikTok profile URLs and returns an array of `sec_user_id` strings. Send the URLs in the `body` field of the request.

### Use cases

- Convert a list of creator profile links into `sec_user_id` values before you query their profiles.
- Build a lookup table of `sec_user_id` values for a batch of TikTok accounts in one call.
- Prepare identifiers for follower, post or like lookups that need a `sec_user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.tiktok.com/@tiktok"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | User homepage link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[]` | The response is a plain array with no wrapper object. Each entry is a `sec_user_id` string. |
| `[0]` | The first entry in the array. In the example, the request has one URL, `https://www.tiktok.com/@tiktok`, and the array has one entry. |

### Notes

- Pass the profile links as a JSON array in `body`, for example `https://www.tiktok.com/@tiktok`.
- The response is a plain JSON array of strings. The example sends one URL and gets one ID back.
- For a single URL, use [TikTok Profile Sec User ID](/apis/tiktok/web/sec-user-id).
- To get the `unique_id` handle for many profiles, use [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.
- [TikTok Video ID from URL](/apis/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-sec-user-id.json`](../../../../catalog/models/tiktok/web/all-sec-user-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-sec-user-id
