# Douyin High-Quality Video Play URLs API: pricing, parameters and code examples

`douyin/web/multi-video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 per call · **Modes:** sync

Returns direct high-quality playback URLs for multiple Douyin videos using comma-separated video IDs and an optional region code.

## Pricing

- **$0.25 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/multi-video-high-quality-play-url"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/multi-video-high-quality-play-url', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/multi-video-high-quality-play-url", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/multi-video-high-quality-play-url", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/multi-video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` |  |  | Optional ISO country code (for example, CN, US, or HK). Pass CN for users in mainland China to get China-region CDN URLs for faster downloads.  |
| `aweme_ids` | string |  | Video id list, separated by commas, for example: "123,456,789", up to 50.  |

## Details

Retrieve high-quality video playback URLs in bulk by passing comma-separated video IDs via `aweme_ids`. An optional `region` parameter adjusts the returned CDN links for specific geographic locations.

### Use cases

- Collect clean video source files for offline media archiving.
- Retrieve high-resolution Douyin video streams for video editing pipelines.
- Extract original video links in batches to supply training datasets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/multi-video-high-quality-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `region` | string | No | Optional ISO country code (for example, CN, US, or HK). |
| `aweme_ids` | string | No | Video id list, separated by commas, for example: "123,456,789", up to 50. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "videos": [
    {
      "content_type": "video/quicktime",
      "original_video_url": "https://v26-colds.douyinvod.com/910b338418b78405b24b3c9b02ad6db1/6ac4fa01/video/…",
      "video_id": "7512756548356492544"
    }
  ]
}
```

### Notes

- Accepts up to 50 video IDs separated by commas in `aweme_ids`.
- Set `region` to an ISO country code like CN, US, or HK to route to regional CDN URLs.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/multi-video-high-quality-play-url.json`](../../../../catalog/models/douyin/web/multi-video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/multi-video-high-quality-play-url
