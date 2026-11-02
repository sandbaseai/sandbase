# TikTok Video IDs from URLs (Batch) API: pricing, parameters and code examples

`tiktok/web/all-aweme-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Resolves and extracts TikTok video IDs from a list of video URLs. Takes a list of video links to return corresponding item identifiers.

## Pricing

- **$0.0015 per call** (USD)
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

Extract video identifiers from TikTok video links by supplying an array of URLs in the request `body`.

### Use cases

- Convert web video links into unique TikTok video IDs.
- Prepare video IDs in bulk for downstream data retrieval pipelines.
- Parse item identifiers from standard TikTok post URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/all-aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": ["https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Video link |

### Notes

- Accepts an array of TikTok video links in the request `body`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.
- [TikTok Video ID from URL](/model/tiktok/web/aweme-id): Extracts and returns the unique single video ID from a provided TikTok video link.

---
Machine-readable: [`catalog/models/tiktok/web/all-aweme-id.json`](../../../../catalog/models/tiktok/web/all-aweme-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/all-aweme-id
