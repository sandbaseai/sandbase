# Unsplash Photo Search API: pricing, parameters and code examples

`unsplash/search-photos` · data API · Unsplash · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0033 per call · **Modes:** sync

Search Unsplash for free stock photos by keyword. Returns image URLs in several sizes, dimensions, alt text, the photographer's name and profile, and the photo's Unsplash page.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0033**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "unsplash/search-photos", "query": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('unsplash/search-photos', {'query': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("unsplash/search-photos", {
  "query": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "unsplash/search-photos", sandbase.Params{
	"query": "coffee",
})
```

Same call via the path form: `POST /v1/api/unsplash/search-photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `color` | string |  | Only return photos with this dominant color tone. Omit for any color. one of: `black_and_white`, `black`, `white`, `yellow`, `orange`, `red`, `purple`, `magenta`, `green`, `teal`, `blue` |
| `limit` | integer |  | Maximum number of photos to return (1-20, default 20). You are billed per photo returned, so a lower limit costs less. range 1–20 |
| `query` | string | yes | Keyword or phrase to search Unsplash photos for, e.g. "coffee" or "minimal workspace".  |
| `sortBy` | string |  | Order results by best match (relevant, the default) or newest first (recent). one of: `relevant`, `recent`; default `"relevant"` |
| `orientation` | string |  | Only return photos with this orientation. Omit for any orientation. one of: `landscape`, `portrait`, `square` |

## Details

Search Unsplash for free stock photos by keyword. Returns image URLs in several sizes, dimensions, alt text, the photographer's name and profile, and the photo's Unsplash page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "unsplash/search-photos", "limit": 2, "query": "coffee"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword or phrase to search Unsplash photos for, e.g. "coffee" or "minimal workspace". |
| `color` | string | No | Only return photos with this dominant color tone. Omit for any color. One of: `black_and_white`, `black`, `white`, `yellow`, `orange`, `red`, `purple`, `magenta`, `green`, `teal`, `blue`. |
| `limit` | integer | No | Maximum number of photos to return (1-20, default 20). You are billed per photo returned, so a lower limit costs less. |
| `orientation` | string | No | Only return photos with this orientation. Omit for any orientation. One of: `landscape`, `portrait`, `square`. |
| `sortBy` | string | No | Order results by best match (relevant, the default) or newest first (recent). One of: `relevant`, `recent`. |

### Pricing

Billed at the actual cost of each call: about $0.00165 per result returned, up to $0.0336 per request (about $0.0033 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/unsplash/search-photos.json`](../../../catalog/models/unsplash/search-photos.json) · Store page: https://www.sandbase.ai/model/unsplash/search-photos
