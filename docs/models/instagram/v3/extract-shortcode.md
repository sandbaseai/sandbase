# Instagram Shortcode Extractor

`instagram/v3/extract-shortcode` · api · Instagram

Extracts and returns the unique shortcode identifier from an Instagram post, reel, or TV URL. Requires the full target post URL as input.

## Pricing

- **$0.003 per call** (USD)
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

This endpoint resolves the unique shortcode identifier from an Instagram link provided in `url`. It accepts links from standard posts, reels, and TV items.

### Use cases

- Parse a shortcode identifier from an Instagram reel or post link.
- Prepare Instagram post identifiers for downstream media lookups.
- Normalize diverse Instagram content URLs into standardized post keys.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/extract-shortcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/p/DUajw4YkorV/"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full Instagram post URL |

### Notes

- Provide a full Instagram post link in the `url` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/extract-shortcode.json`](../../../../catalog/models/instagram/v3/extract-shortcode.json) · Store page: https://www.sandbase.ai/model/instagram/v3/extract-shortcode
