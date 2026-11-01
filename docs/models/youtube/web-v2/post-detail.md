# YouTube Community Post Details

`youtube/web-v2/post-detail` · api · YouTube

Returns detailed information for a YouTube community post, including post text, media attachments, and engagement metrics. Filter results by post ID, language, and country.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/post-detail", "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/post-detail', {'post_id': 'UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/post-detail", {
  "post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/post-detail", sandbase.Params{
	"post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | **Purpose**: Post ID  |
| `need_format` | boolean |  | Whether to format data, default `true` default `true` |
| `country_code` | string |  | Country code, default `"US"` default `"US"` |
| `language_code` | string |  | Language code, default `"zh-CN"` default `"zh-CN"` |

## Details

Retrieve detailed information for a specific YouTube community post using its `post_id`.

### Use cases

- Inspect community post text and attached image media.
- Monitor engagement metrics on specific YouTube community posts.
- Display localized community post content by setting country and language codes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "UgkxiCSRfD6g7SPlWGPDa3vbP7aIsytXRkvy"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Purpose: Post ID |
| `need_format` | boolean | No | Whether to format data, default `true` |
| `country_code` | string | No | Country code, default `"US"` |
| `language_code` | string | No | Language code, default `"zh-CN"` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "post": {
    "attachment": {
      "images": [
        {
          "url": "https://yt3.ggpht.com/wbxSQ9KLMZWcSCw2Q78wZ1YfvUb9zpWRs6QYRSHt4n277DENaKkLxd9WYZ…"
        }
      ]
    }
  }
}
```

### Notes

- `need_format` defaults to `true` to structure the response payload.
- `country_code` defaults to `"US"` and `language_code` defaults to `"zh-CN"`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/post-detail.json`](../../../../catalog/models/youtube/web-v2/post-detail.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/post-detail
