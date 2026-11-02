# Instagram Shortcode to Media ID (V2) API: pricing, parameters and code examples

`instagram/v2/shortcode-to-media-id` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Converts an Instagram post shortcode into its numeric media ID. Provide the shortcode extracted from a post URL to receive the corresponding media identifier.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/shortcode-to-media-id", "shortcode": "DRhvwVLAHAG"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/shortcode-to-media-id', {'shortcode': 'DRhvwVLAHAG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/shortcode-to-media-id", {
  "shortcode": "DRhvwVLAHAG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/shortcode-to-media-id", sandbase.Params{
	"shortcode": "DRhvwVLAHAG",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/shortcode-to-media-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shortcode` | string | yes | Post shortcode  |

## Details

Look up the numeric media ID for an Instagram post by supplying its URL `shortcode`.

### Use cases

- Resolve Instagram post URLs to internal media IDs for downstream API calls.
- Convert user-submitted post links into numeric IDs for tracking content.
- Standardize post identifiers across Instagram data processing pipelines.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/shortcode-to-media-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shortcode": "DRhvwVLAHAG"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shortcode` | string | Yes | Post shortcode |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "media_id": "3774507992167247878",
  "status": true
}
```

### Notes

- The `shortcode` is the unique identifier string found in a post URL path.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Replies (V2)](/model/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/model/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/model/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/shortcode-to-media-id.json`](../../../../catalog/models/instagram/v2/shortcode-to-media-id.json) · Store page: https://www.sandbase.ai/model/instagram/v2/shortcode-to-media-id
