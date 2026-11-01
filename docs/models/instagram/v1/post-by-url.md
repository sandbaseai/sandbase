# Instagram Post Details by URL

`instagram/v1/post-by-url` · api · Instagram

Returns details and display resources for a single Instagram post. Queries the platform using a target post link.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-url", "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-url', {'post_url': 'https://www.instagram.com/p/DPwhVB-jo9k/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-url", {
  "post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-url", sandbase.Params{
	"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_url` | string | yes | Post URL  |

## Details

Returns Instagram post information based on the link provided in `post_url`.

### Use cases

- Retrieve display resources and media data for a specific Instagram link.
- Inspect single post information for content archiving.
- Extract post metadata directly using public Instagram URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_url": "https://www.instagram.com/p/DPwhVB-jo9k/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_url` | string | Yes | Post URL |

### Notes

- Requires a full Instagram post link passed to `post_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-url.json`](../../../../catalog/models/instagram/v1/post-by-url.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-url
