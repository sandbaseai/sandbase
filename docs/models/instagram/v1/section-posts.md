# Instagram Explore Section Posts API: pricing, parameters and code examples

`instagram/v1/section-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts listed under a specific Instagram explore section. Supports pagination controls and page size configuration by section ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/section-posts", "section_id": "10156104410190727"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/section-posts', {'section_id': '10156104410190727'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/section-posts", {
  "section_id": "10156104410190727"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/section-posts", sandbase.Params{
	"section_id": "10156104410190727",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/section-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Count per page, default 20 range 1–50 |
| `max_id` | string |  | Pagination cursor, omit for first request  |
| `section_id` | string | yes | Section ID (from fetch_explore_sections API)  |

## Details

Retrieve a feed of posts from a designated explore section using `section_id`. Paginate through results using `max_id` and adjust batch size with `count`.

### Use cases

- Retrieve posts featured in specific Instagram explore categories.
- Track trending content feeds organized by explore sections.
- Collect post streams for topic-based social media monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/section-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"section_id": "10156104410190727"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `section_id` | string | Yes | Section ID (from fetch_explore_sections API) |
| `count` | integer | No | Count per page, default 20 |
| `max_id` | string | No | Pagination cursor, omit for first request |

### Notes

- Requires `section_id`, obtained from the explore sections endpoint.
- Use `max_id` as a pagination cursor, omitting it on the first request.
- `count` defines the number of posts per page and defaults to 20.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/section-posts.json`](../../../../catalog/models/instagram/v1/section-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/section-posts
