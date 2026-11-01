# Instagram Shortcode to Media ID (V3)

`instagram/v3/shortcode-to-media-id` · api · Instagram

Converts an Instagram post shortcode into its corresponding numeric media ID. Requires a post shortcode string to return the unique platform identifier.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/shortcode-to-media-id", "shortcode": "DUajw4YkorV"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/shortcode-to-media-id', {'shortcode': 'DUajw4YkorV'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/shortcode-to-media-id", {
  "shortcode": "DUajw4YkorV"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/shortcode-to-media-id", sandbase.Params{
	"shortcode": "DUajw4YkorV",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/shortcode-to-media-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shortcode` | string | yes | Post shortcode  |

## Details

Look up the numeric media ID for any Instagram post by providing its URL `shortcode`.

### Use cases

- Resolve Instagram post URLs into numeric identifiers for downstream API calls.
- Translate public post shortcodes to media IDs for tracking engagement metrics.
- Map user-submitted links to system IDs in content monitoring pipelines.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/shortcode-to-media-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shortcode": "DUajw4YkorV"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shortcode` | string | Yes | Post shortcode |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "media_id": "3826528124109228757"
}
```

### Notes

- Pass the post identifier extracted from the Instagram URL into `shortcode`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/shortcode-to-media-id.json`](../../../../catalog/models/instagram/v3/shortcode-to-media-id.json) · Store page: https://www.sandbase.ai/model/instagram/v3/shortcode-to-media-id
