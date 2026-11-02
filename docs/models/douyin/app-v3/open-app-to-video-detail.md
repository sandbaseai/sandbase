# Douyin Video Detail App Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-video-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a Douyin share URL for a given video ID. The resulting link opens the Douyin mobile application directly to the specified video detail screen.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-video-detail", "aweme_id": "7197598285882789120"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-video-detail', {'aweme_id': '7197598285882789120'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-video-detail", {
  "aweme_id": "7197598285882789120"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-video-detail", sandbase.Params{
	"aweme_id": "7197598285882789120",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Generate a direct Douyin application jump link by supplying `aweme_id`.

### Use cases

- Direct mobile users straight to a specific Douyin clip inside the app.
- Produce short share links for external marketing campaigns.
- Facilitate seamless deep linking from web pages to Douyin video details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7197598285882789120"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_id": "7197598285882789120",
  "short_url": "https://v.douyin.com/Zk1puu-EI8A/",
  "status": "success"
}
```

### Notes

- Requires a valid `aweme_id` representing the target video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-video-detail.json`](../../../../catalog/models/douyin/app-v3/open-app-to-video-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-video-detail
