# TikTok User Sec User ID Extractor

`tiktok/web/all-sec-user-id` · api · TikTok

Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs. Provide an array of user homepage links in the request body to retrieve their unique security IDs.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve sec_user_id values in bulk by providing an array of TikTok user profile URLs in the `body` parameter.

### Use cases

- Resolving profile homepage URLs into internal sec_user_id identifiers.
- Preparing user identifier lists for downstream TikTok profile and video queries.
- Batch processing creator profile links to collect account security IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.tiktok.com/@tiktok"]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | User homepage link |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
[
  "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
]
```

### Notes

- Pass an array of user homepage URLs in `body`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.
- [TikTok Video ID from URL](/model/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-sec-user-id.json`](../../../../catalog/models/tiktok/web/all-sec-user-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-sec-user-id
