# YouTube Video Comment List API: pricing, parameters and code examples

`youtube/video-comment` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get first-level comments for a YouTube video with sorting, locale options, and cursor pagination. Use it to review audience discussion or continue through additional comment pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-comment", "videoId": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-comment', {'videoId': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-comment", {
  "videoId": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-comment", sandbase.Params{
	"videoId": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `sortBy` | string |  | Sort order for the comment list. one of: `top`, `newest`; default `"newest"` |
| `videoId` | string | yes | The unique identifier for a YouTube video.  |
| `countryCode` | string |  | Region code for response data. default `"US"` |
| `languageCode` | string |  | Language preference for response data. default `"zh-CN"` |

## Details

Get first-level comments for a YouTube video with sorting, locale options, and cursor pagination. Use it to review audience discussion or continue through additional comment pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |
| `languageCode` | string | No | Language preference for response data. |
| `countryCode` | string | No | Region code for response data. |
| `sortBy` | string | No | Sort order for the comment list. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youtube/video-comment.json`](../../../catalog/models/youtube/video-comment.json) · Store page: https://www.sandbase.ai/model/youtube/video-comment
