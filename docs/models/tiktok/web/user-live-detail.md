# TikTok User Stream Detail API: pricing, parameters and code examples

`tiktok/web/user-live-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns current broadcast information for a TikTok user based on their unique handle. Provides stream quality options and room playback data.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-live-detail", "uniqueId": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-live-detail', {'uniqueId': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-live-detail", {
  "uniqueId": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-live-detail", sandbase.Params{
	"uniqueId": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-live-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uniqueId` | string | yes | User uniqueId  |

## Details

Retrieve broadcast and stream room details for a TikTok account by passing the user handle in `uniqueId`.

### Use cases

- Check whether a specific TikTok creator is broadcasting.
- Retrieve stream playback configurations and video qualities.
- Monitor broadcast activity for target user handles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-live-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uniqueId": "tiktok"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uniqueId` | string | Yes | User uniqueId |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "liveRoom": {
      "hevcStreamData": {
        "pull_data": {
          "options": {
            "qualities": [
              {
                "name": "Original"
              }
            ]
          }
        }
      }
    }
  }
}
```

### Notes

- Requires the TikTok user handle via `uniqueId`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-live-detail.json`](../../../../catalog/models/tiktok/web/user-live-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-live-detail
