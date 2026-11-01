# Instagram Post Details (V2)

`instagram/v2/post-info` · api · Instagram

Returns detailed information for an Instagram post, including available media streams and video versions, using a post shortcode or full URL.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/post-info", "code_or_url": "DRhvwVLAHAG"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/post-info', {'code_or_url': 'DRhvwVLAHAG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/post-info", {
  "code_or_url": "DRhvwVLAHAG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/post-info", sandbase.Params{
	"code_or_url": "DRhvwVLAHAG",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/post-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code_or_url` | string | yes | Post shortcode or full URL  |

## Details

Retrieve detailed Instagram post data by providing the target post shortcode or full link in `code_or_url`.

### Use cases

- Extract media asset URLs for a specific Instagram post.
- Inspect post metadata using a post shortcode or direct URL.
- Verify video versions and source links for Instagram content.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/post-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code_or_url": "DRhvwVLAHAG"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code_or_url` | string | Yes | Post shortcode or full URL |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "video_versions": [
      {
        "id": "1961917128003357v",
        "type": 101,
        "url": "https://scontent-arn2-1.cdninstagram.com/o1/v/t2/f2/m86/AQM5-tU7kYwNnMkDKY2gOnuG…"
      }
    ]
  }
}
```

### Notes

- Accepts either a post shortcode or a complete URL in `code_or_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/post-info.json`](../../../../catalog/models/instagram/v2/post-info.json) · Store page: https://www.sandbase.ai/model/instagram/v2/post-info
