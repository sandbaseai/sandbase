# Instagram Post Details by URL (V2) API: pricing, parameters and code examples

`instagram/v1/post-by-url-v2` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns post details and media links for a specific Instagram post URL. Designed for faster responses when handling high-volume post lookups.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-url-v2", "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-url-v2', {'post_url': 'https://www.instagram.com/p/DPwhVB-jo9k/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-url-v2", {
  "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-url-v2", sandbase.Params{
	"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-url-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_url` | string | yes | Post URL  |

## Details

Look up media links and post items from an Instagram post using `post_url`. This endpoint provides accelerated response speeds for high-volume retrieval.

### Use cases

- Retrieve direct media download links from an Instagram post URL.
- Process bulk post media lookups at higher speeds.
- Inspect media types associated with a given Instagram post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-url-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_url` | string | Yes | Post URL |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "medias": [
      {
        "link": "https://scontent-cdg4-2.cdninstagram.com/v/t51.82787-15/562815025_18601398793054…",
        "type": "image"
      }
    ]
  }
}
```

### Notes

- `post_url` requires a standard Instagram post link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-url-v2.json`](../../../../catalog/models/instagram/v1/post-by-url-v2.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-url-v2
