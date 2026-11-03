# Instagram Shortcode Extractor API: pricing, parameters and code examples

`instagram/v3/extract-shortcode` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL. Requires the full target post URL as input.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/extract-shortcode", "url": "https://www.instagram.com/p/DUajw4YkorV/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/extract-shortcode', {'url': 'https://www.instagram.com/p/DUajw4YkorV/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/extract-shortcode", {
  "url": "https://www.instagram.com/p/DUajw4YkorV/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/extract-shortcode", sandbase.Params{
	"url": "https://www.instagram.com/p/DUajw4YkorV/",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/extract-shortcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full Instagram post URL  |

## Details

Extract the shortcode from an Instagram post, reel or TV link. Instagram links take the forms `instagram.com/p/<shortcode>/`, `instagram.com/reel/<shortcode>/` and `instagram.com/tv/<shortcode>/`, often with tracking query strings such as `?igsh=`.

### Use cases

- Normalize links pasted by users before calling post APIs.
- Deduplicate the same post shared with different tracking parameters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/extract-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/DUajw4YkorV/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Instagram post URL |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "shortcode": "DUajw4YkorV",
  "url": "https://www.instagram.com/p/DUajw4YkorV/"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shortcode` | The 11-character post shortcode. |
| `url` | The link you sent. |

### Notes

- The shortcode is the media ID in base 64; convert it with [Shortcode to Media ID](/apis/instagram/v1/shortcode-to-media-id).
- This only parses the link; it does not check that the post exists.

### Pricing

$0.002 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/extract-shortcode.json`](../../../../catalog/models/instagram/v3/extract-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v3/extract-shortcode
