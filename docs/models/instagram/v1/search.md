# Instagram Keyword Search API: pricing, parameters and code examples

`instagram/v1/search` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Instagram users, hashtags, or places matching a search keyword. Filter results by specific target types using an optional filter parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/search", "query": "openai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/search', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/search", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/search", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |
| `select` | string |  | Filter type (optional)  |

## Details

Search across Instagram profiles, hashtags, and locations by passing a search term into `query`. Narrow the search category by supplying `select`.

### Use cases

- Locate Instagram profiles by keyword or brand name.
- Discover hashtags related to specific topics or campaigns.
- Find place entities and locations across Instagram.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "openai"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |
| `select` | string | No | Filter type (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "user": {
        "full_name": "OpenAI",
        "id": "45374573700",
        "profile_pic_url": "https://scontent-cdg4-1.cdninstagram.com/v/t51.82787-19/788716177_18115256264517…",
        "username": "<user>"
      }
    }
  ]
}
```

### Notes

- Specify `query` with the target keyword to perform the search.
- Use `select` to filter search results by target type, such as hashtags.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Cities by Country](/model/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/model/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/model/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/search.json`](../../../../catalog/models/instagram/v1/search.json) · Store page: https://www.sandbase.ai/model/instagram/v1/search
