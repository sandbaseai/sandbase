# YouTube Video Information (V2) API: pricing, parameters and code examples

`youtube/web-v2/video-info-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comprehensive details for a YouTube video identified by its ID or direct URL, with an option to retrieve a cleaned payload format.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-info-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-info-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-info-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-info-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-info-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID, e.g. `"dQw4w9WgXcQ"`  |
| `video_url` | string |  | Full video URL (ignored if video_id provided)  |
| `need_format` | boolean |  | Whether to return cleaned payload. Default `True` default `true` |

## Details

Fetch detailed information for a specific YouTube video by providing either `video_id` or `video_url`.

### Use cases

- Retrieve video metadata such as title and description for display in media applications.
- Inspect video properties using direct YouTube video links.
- Extract cleaned video payloads for ingestion into reporting dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-info-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | No | Video ID, e.g. |
| `video_url` | string | No | Full video URL (ignored if video_id provided) |
| `need_format` | boolean | No | Whether to return cleaned payload. |

### Notes

- If `video_id` is provided, `video_url` is ignored.
- Set `need_format` to true to receive a cleaned data structure.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-info-v2.json`](../../../../catalog/models/youtube/web-v2/video-info-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-info-v2
