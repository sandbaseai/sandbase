# Instagram Post Details by ID API: pricing, parameters and code examples

`instagram/v1/post-by-id` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a single Instagram post using its unique post identifier. Use this endpoint to look up post metadata and display resources.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/post-by-id", "post_id": "3742637871112032100"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/post-by-id', {'post_id': '3742637871112032100'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/post-by-id", {
  "post_id": "3742637871112032100"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/post-by-id", sandbase.Params{
	"post_id": "3742637871112032100",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/post-by-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | Post ID  |

## Details

Retrieve detailed post information and display resources for a specific Instagram post by providing its `post_id`.

### Use cases

- Look up media display resources and details for a specific post.
- Inspect post information when building Instagram content views.
- Verify post availability and retrieve associated metadata by post ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/post-by-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "3742637871112032100"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "display_resources": [
    {}
  ]
}
```

### Notes

- Pass the target post identifier in `post_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/post-by-id.json`](../../../../catalog/models/instagram/v1/post-by-id.json) · Store page: https://www.sandbase.ai/model/instagram/v1/post-by-id
