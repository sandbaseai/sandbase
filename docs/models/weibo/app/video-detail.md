# Weibo Video Detail API: pricing, parameters and code examples

`weibo/app/video-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves detailed information for a single Weibo video, including playback URLs and metadata, based on a specified post identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/video-detail", "mid": "5242977759006596"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/video-detail', {'mid': '5242977759006596'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/video-detail", {
  "mid": "5242977759006596"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/video-detail", sandbase.Params{
	"mid": "5242977759006596",
})
```

Same call via the path form: `POST /v1/api/weibo/app/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mid` | string | yes | Video post ID or ID from link (required)  |

## Details

Retrieve detailed video metadata and playback URLs using a specific `mid`.

### Use cases

- Retrieve video playback URLs for Weibo posts.
- Access video metadata from Weibo TV or post links.
- Display video content details inside media dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mid": "5242977759006596"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mid` | string | Yes | Video post ID or ID from link (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status": {
    "video_info": {
      "menus": [
        {}
      ]
    }
  }
}
```

### Notes

- Accepts a video post ID or an ID extracted from a Weibo video URL in `mid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/video-detail.json`](../../../../catalog/models/weibo/app/video-detail.json) · Store page: https://www.sandbase.ai/model/weibo/app/video-detail
