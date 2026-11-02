# YouTube Community Post Comments API: pricing, parameters and code examples

`youtube/web-v2/post-comments` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments from a YouTube community post with support for pagination, formatted output, and regional localization settings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/post-comments", "country_code": "US", "language_code": "zh-CN", "need_format": true, "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/post-comments', {'country_code': 'US', 'language_code': 'zh-CN', 'need_format': True, 'post_id': 'UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/post-comments", {
  "country_code": "US",
  "language_code": "zh-CN",
  "need_format": true,
  "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/post-comments", sandbase.Params{
	"country_code": "US",
	"language_code": "zh-CN",
	"need_format": true,
	"post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string |  | Post ID, required for first request  |
| `need_format` | boolean |  | Whether to format data, default `true` default `true` |
| `country_code` | string |  | Country code, default `"US"` default `"US"` |
| `language_code` | string |  | Language code, default `"zh-CN"` default `"zh-CN"` |
| `continuation_token` | string |  | Next page token  |

## Details

Look up community post comments on YouTube by specifying a `post_id`. Supports localized results and pagination using `continuation_token`.

### Use cases

- Retrieve audience feedback on channel community posts.
- Monitor user engagement and discussions across community updates.
- Extract comment threads for sentiment and topic analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | No | Post ID, required for first request |
| `need_format` | boolean | No | Whether to format data, default `true` |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |
| `continuation_token` | string | No | Next page token |

### Notes

- `post_id` is required for the first request.
- Pass `continuation_token` to retrieve subsequent pages of comments.
- Customize localization by setting `country_code` and `language_code`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/post-comments.json`](../../../../catalog/models/youtube/web-v2/post-comments.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/post-comments
