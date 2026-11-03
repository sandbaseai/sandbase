# TikTok Video ID from URL API: pricing, parameters and code examples

`tiktok/web/aweme-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts and returns the unique single video ID from a provided TikTok video link. Enables quick identification of video assets for downstream lookups.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/aweme-id", "url": "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/aweme-id', {'url': 'https://www.tiktok.com/@owlcitymusic/video/7218694761253735723'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/aweme-id", {
  "url": "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/aweme-id", sandbase.Params{
	"url": "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/aweme-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Video link  |

## Details

Extract the video ID (`aweme_id`) from a TikTok video link such as `https://www.tiktok.com/@user/video/<aweme_id>`. Most TikTok video, comment and download APIs take this ID.

### Use cases

- Normalize shared TikTok links before calling video detail or comment APIs.
- Deduplicate videos collected as links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Video link |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"7218694761253735723"
```

### Response fields

| Field | Meaning |
|---|---|
| `(body)` | The `aweme_id` as a string, e.g. `"7218694761253735723"`. |

### Notes

- Keep the ID as a string; it exceeds JavaScript's safe integer range.
- The same ID works with the TikTok app (`app-v3`) and web endpoints.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/aweme-id.json`](../../../../catalog/models/tiktok/web/aweme-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/aweme-id
