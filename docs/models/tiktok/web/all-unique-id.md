# TikTok Profile Unique IDs API: pricing, parameters and code examples

`tiktok/web/all-unique-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers. Accepts a list of profile URLs in the request payload.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/all-unique-id", "body": ["https://www.tiktok.com/@tiktok"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/all-unique-id', {'body': ['https://www.tiktok.com/@tiktok']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/all-unique-id", {
  "body": [
    "https://www.tiktok.com/@tiktok"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/all-unique-id", sandbase.Params{
	"body": []any{"https://www.tiktok.com/@tiktok"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/all-unique-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | User homepage link  |

## Details

Takes a list of TikTok profile URLs and returns the matching unique IDs (the handles) as a JSON array of strings. The request needs one field, `body`, which holds the profile links.

### Use cases

- Turn a list of `https://www.tiktok.com/@name` links into plain handles for a spreadsheet or database.
- Normalize a batch of creator links before you look up each profile.
- Check which handle sits behind each profile URL in an influencer list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-unique-id" \
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
  "tiktok"
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[]` | One TikTok unique ID, which is the handle shown after the `@` in the profile URL. For `https://www.tiktok.com/@tiktok` the value is `tiktok`. |
| `[0]` | The first item in the array. In the sample request, the single link in `body` returned `tiktok` at this position. |

### Notes

- The response is a bare JSON array of strings. It has no wrapper object and no named keys.
- Send the profile links as an array of strings in `body`, for example `["https://www.tiktok.com/@tiktok"]`.
- To get the `sec_user_id` for each profile link in one call, use [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id).
- To resolve a single profile link to a user ID, use [TikTok User ID from Profile Link](/apis/tiktok/web/user-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Video ID from URL](/apis/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-unique-id.json`](../../../../catalog/models/tiktok/web/all-unique-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-unique-id
