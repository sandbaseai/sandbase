# Douyin Multi-Video High Quality Play URLs API: pricing, parameters and code examples

`douyin/app-v3/multi-video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 per call · **Modes:** sync

Returns highest-quality direct video playback URLs for multiple Douyin videos based on comma-separated video IDs, with optional CDN region targeting.

## Pricing

- **$0.25 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/multi-video-high-quality-play-url"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/multi-video-high-quality-play-url', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/multi-video-high-quality-play-url", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/multi-video-high-quality-play-url", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/multi-video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` |  |  | Optional ISO country code (for example, CN, US, or HK). Pass CN for users in mainland China to get China-region CDN URLs for faster downloads.  |
| `aweme_ids` | string |  | Video id list, separated by commas, for example: "123,456,789", up to 50.  |

## Details

Fetch direct high-quality video playback URLs in batches by supplying comma-separated video IDs via `aweme_ids`. You can also specify `region` to route to regional CDNs for faster access.

### Use cases

- Batch downloading high-definition Douyin videos without watermarks.
- Archiving original-quality media files for offline video asset storage.
- Collecting video files for video editing pipelines and dataset preparation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video-high-quality-play-url" \
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
      "content_type": "video/mp4",
      "original_video_url": "https://v9-colds.douyinvod.com/492702c4e428390a26b1578fe5e5b5ac/6ac4fa06/video/t…",
      "video_id": "7512756548356492544"
    }
  ]
}
```

### Notes

- Pass up to 50 comma-separated video IDs in `aweme_ids`.
- Provide an ISO country code such as CN, US, or HK in `region` to select regional CDN links.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video-high-quality-play-url.json`](../../../../catalog/models/douyin/app-v3/multi-video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video-high-quality-play-url
