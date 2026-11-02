# TikTok Video ID from URL API: pricing, parameters and code examples

`tiktok/web/aweme-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Extracts and returns the unique single video ID from a provided TikTok video link. Enables quick identification of video assets for downstream lookups.

## Pricing

- **$0.0015 per call** (USD)
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

Extract the unique video ID from a TikTok web URL by providing the target link in `url`.

### Use cases

- Parse video IDs from shared TikTok links.
- Resolve canonical video identifiers for downstream data queries.
- Validate and clean TikTok video URLs before ingestion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/aweme-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@owlcitymusic/video/7218694761253735723"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Video link |

### Notes

- Accepts a complete TikTok video link via the `url` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/aweme-id.json`](../../../../catalog/models/tiktok/web/aweme-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/aweme-id
