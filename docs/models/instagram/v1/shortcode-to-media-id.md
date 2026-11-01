# Instagram Shortcode to Media ID

`instagram/v1/shortcode-to-media-id` · api · Instagram

Convert an Instagram post shortcode (from instagram.com/p/<shortcode>/) into the numeric media ID required by the Instagram post, comments and likes APIs.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/shortcode-to-media-id", "shortcode": "DYurEPdgKQ4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/shortcode-to-media-id', {'shortcode': 'DYurEPdgKQ4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/shortcode-to-media-id", {
  "shortcode": "DYurEPdgKQ4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/shortcode-to-media-id", sandbase.Params{
	"shortcode": "DYurEPdgKQ4",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/shortcode-to-media-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `shortcode` | string | yes | Post shortcode  |

## Details

Pass the shortcode from an Instagram post or reel URL and get its numeric media ID.

### Use cases

- Resolve post links into media IDs.
- First step before fetching comments or likers.
- Deduplicate posts across sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/shortcode-to-media-id" \
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

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get cities by country](/model/instagram/v1/cities): Get cities/regions list of specified country.
- [Get posts by hashtag](/model/instagram/v1/hashtag-posts): Get posts under specific hashtag.
- [Get location info](/model/instagram/v1/location-info): Get detailed information of specified location.

---
Machine-readable: [`catalog/models/instagram/v1/shortcode-to-media-id.json`](../../../../catalog/models/instagram/v1/shortcode-to-media-id.json) · Store page: https://www.sandbase.ai/model/instagram/v1/shortcode-to-media-id
