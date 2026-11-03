# TikTok Video IDs from URLs (Batch) API: pricing, parameters and code examples

`tiktok/web/all-aweme-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves and extracts TikTok video IDs from a list of video URLs. Takes a list of video links to return corresponding item identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/all-aweme-id", "body": ["https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/all-aweme-id', {'body': ['https://www.tiktok.com/@owlcitymusic/video/7218694761253735723']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/all-aweme-id", {
  "body": [
    "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/all-aweme-id", sandbase.Params{
	"body": []any{"https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"},
})
```

Same call via the path form: `POST /v1/api/tiktok/web/all-aweme-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Video link  |

## Details

This API takes a list of TikTok video URLs and returns the video ID for each one. The response is a plain JSON array of ID strings. Send the links in the request `body` as an array.

### Use cases

- Turn a list of copied TikTok video links into video IDs before you call a video detail API.
- Clean a spreadsheet of TikTok post URLs into a column of IDs for joins and deduplication.
- Check which video an `@username/video/...` link points to without opening the page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"]}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Video link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  "7218694761253735723"
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[]` | The whole response is a list of video IDs. It has no wrapper object and no named fields. |
| `[0]` | The first video ID in the list. In the example, the single link returns `7218694761253735723`, which is the number after `/video/` in the URL. |
| `[] / [0]` | Each ID is a string of digits, not a JSON number. |

### Notes

- The response is a top-level array, not an object. It has no named fields.
- Video IDs come back as strings of digits. Keep them as strings in your code.
- To fetch details for a video once you have its ID, call [TikTok Video Detail](/apis/tiktok/web/post-detail).
- To resolve one link at a time, use [TikTok Video ID from URL](/apis/tiktok/web/aweme-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.
- [TikTok Video ID from URL](/apis/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-aweme-id.json`](../../../../catalog/models/tiktok/web/all-aweme-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-aweme-id
