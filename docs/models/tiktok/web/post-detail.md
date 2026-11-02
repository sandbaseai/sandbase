# TikTok Video Detail API: pricing, parameters and code examples

`tiktok/web/post-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed data for a single TikTok video using its item ID. Supports filtering by region code to view localized post content.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-detail", "itemId": "7218694761253735723"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-detail', {'itemId': '7218694761253735723'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-detail", {
  "itemId": "7218694761253735723"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-detail", sandbase.Params{
	"itemId": "7218694761253735723",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Video id  |
| `region` | string |  | Region code, optional; affects content region, e.g. US/GB/JP/ID, default US.  |

## Details

Returns details for an individual video post by providing its `itemId`. An optional `region` parameter adjusts the geographic content scope.

### Use cases

- Inspect metrics and metadata for a specific TikTok post.
- Retrieve localized video data based on selected country codes.
- Track performance details for individual video items.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "<itemId>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Video id |
| `region` | string | No | Region code, optional; affects content region, e.g. |

### Notes

- Specify `itemId` to target a specific video post.
- The `region` parameter accepts country codes such as US, GB, JP, or ID and defaults to US.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/post-detail.json`](../../../../catalog/models/tiktok/web/post-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-detail
