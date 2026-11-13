# Pexels Photo Search API: pricing, parameters and code examples

`pexels/search-photos` · data API · Pexels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0066 per call · **Modes:** sync

Search Pexels for free stock photos by keyword. Returns image URLs in several sizes, dimensions, alt text, the photographer's name and profile, and the photo's Pexels page.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0066**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pexels/search-photos", "query": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pexels/search-photos', {'query': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pexels/search-photos", {
  "query": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pexels/search-photos", sandbase.Params{
	"query": "coffee",
})
```

Same call via the path form: `POST /v1/api/pexels/search-photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of photos to return (1-20, default 20). You are billed per photo returned, so a lower limit costs less. range 1–20 |
| `query` | string | yes | Keyword or phrase to search Pexels photos for, e.g. "coffee" or "city skyline".  |
| `minWidth` | integer |  | Only return photos at least this many pixels wide. range 1– |
| `minHeight` | integer |  | Only return photos at least this many pixels tall. range 1– |
| `orientation` | string |  | Only return photos with this orientation. Omit for any orientation. one of: `landscape`, `portrait`, `square` |
| `peopleCount` | string |  | Only return photos showing this many people: "0" for none, "1" or "2". Omit for any number. one of: `0`, `1`, `2` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `tags`, and it is served only by a source that returns every one of…  |

## Details

Search Pexels for free stock photos by keyword. Returns image URLs in several sizes, dimensions, alt text, the photographer's name and profile, and the photo's Pexels page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "pexels/search-photos", "limit": 2, "query": "coffee"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword or phrase to search Pexels photos for, e.g. "coffee" or "city skyline". |
| `limit` | integer | No | Maximum number of photos to return (1-20, default 20). You are billed per photo returned, so a lower limit costs less. |
| `minHeight` | integer | No | Only return photos at least this many pixels tall. |
| `minWidth` | integer | No | Only return photos at least this many pixels wide. |
| `orientation` | string | No | Only return photos with this orientation. Omit for any orientation. One of: `landscape`, `portrait`, `square`. |
| `peopleCount` | string | No | Only return photos showing this many people: "0" for none, "1" or "2". Omit for any number. One of: `0`, `1`, `2`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `tags`, and it is served only by a source that returns every one of th |

### Pricing

Billed at the actual cost of each call: about $0.0033 per result returned, up to $0.0666 per request (about $0.0066 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/pexels/search-photos.json`](../../../catalog/models/pexels/search-photos.json) · Store page: https://www.sandbase.ai/model/pexels/search-photos
