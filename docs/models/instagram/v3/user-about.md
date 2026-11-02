# Instagram User About Details API: pricing, parameters and code examples

`instagram/v3/user-about` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns About This Account details for an Instagram profile using a target username. Output includes metadata such as account join date, location, and former usernames.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-about", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-about', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-about", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-about", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-about` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username (required)  |

## Details

Retrieve About This Account metadata for an Instagram profile by providing the `username` parameter.

### Use cases

- Verify profile authenticity by checking account join dates and country locations.
- Track former username history for brand protection and due diligence.
- Audit influencer account changes and credibility metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-about" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |

### Notes

- `username` is a required string parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-about.json`](../../../../catalog/models/instagram/v3/user-about.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-about
