# Douyin Single Video Data (Web) API: pricing, parameters and code examples

`douyin/web/one-video-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin video using its video identifier. The endpoint provides video properties such as bit rate and stream quality tiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video-v2", "aweme_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video-v2', {'aweme_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video-v2", {
  "aweme_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video-v2", sandbase.Params{
	"aweme_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Retrieve detailed metadata for a specific Douyin video by providing its `aweme_id`.

### Use cases

- Look up stream bit rates and video quality settings for a Douyin clip.
- Retrieve Douyin video details for content evaluation workflows.
- Inspect media specifications using a Douyin video identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "video": {
      "bit_rate": [
        {
          "bit_rate": 1603814,
          "gear_name": "normal_1080_0",
          "quality_type": 1
        }
      ]
    }
  }
}
```

### Notes

- Pass the target video identifier in `aweme_id`.
- If this web interface fails to return data, alternative options include `/fetch_one_video` or the app-based endpoints.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video-v2.json`](../../../../catalog/models/douyin/web/one-video-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video-v2
