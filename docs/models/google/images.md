# Google Images API: pricing, parameters and code examples

`google/images` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Run a Google Images search and get structured results: image URLs, dimensions, titles, and source pages.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/images", "query": "golden retriever"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/images', {'query': 'golden retriever'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/images", {
  "query": "golden retriever"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/images", sandbase.Params{
	"query": "golden retriever",
})
```

Same call via the path form: `POST /v1/api/google/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code for result localization (e.g. us, gb, de). default `"us"` |
| `hl` | string |  | Two-letter interface and results language code (e.g. en, es, de). default `"en"` |
| `limit` | integer |  | Maximum number of images to return (1-100, default 20). Requests for 10 results or fewer are billed at a lower rate than larger requests. default `20`; range 1–100 |
| `query` | string | yes | Image search query (e.g. golden gate bridge at sunset).  |
| `location` | string |  | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl.  |
| `timeframe` | string |  | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). one of: `1h`, `1d`, `7d`, `1y`, `all` |
| `autocorrect` | boolean |  | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction.  |

## Details

This API runs a Google Images search and returns a list of matching images. Each result has the full image URL, a thumbnail, the page it came from, a title, and pixel dimensions. It needs one input, a search `query`.

### Use cases

- Collect image candidates for a topic such as a dog breed to review for an editorial article.
- Find the source pages that host an image so you can check where it was published.
- Build a mood board or dataset by pulling many image URLs and sizes for one search term.
- Compare image results across countries by changing `gl`, `hl`, or `location`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"gl": "us", "hl": "en", "limit": 5, "query": "golden retriever"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Image search query (e.g. golden gate bridge at sunset). |
| `autocorrect` | boolean | No | Toggle Google spelling autocorrect (default true). Set false to search the exact query without correction. |
| `gl` | string | No | Two-letter country code for result localization (e.g. us, gb, de). |
| `hl` | string | No | Two-letter interface and results language code (e.g. en, es, de). |
| `limit` | integer | No | Maximum number of images to return (1-100, default 20). Requests for 10 results or fewer are billed at a lower rate than larger requests. |
| `location` | string | No | Fine-grained location for result localization, given as a canonical Google location string (e.g. 'New York, United States', 'London, United Kingdom'). More specific than the country-level gl. |
| `timeframe` | string | No | Restrict results to a recent time window: 1h, 1d, 7d, 1y, or all. Default all (no time restriction). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "height": 1707,
        "position": 1,
        "source": "blog.ollie.com",
        "sourceUrl": "https://blog.ollie.com/breed-deets-golden-retriever/",
        "thumbnailUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe1mLcW_M8xRI0J5UcnG6soPw9…",
        "title": "Golden Retriever: Pros, Cons & Diet Guide | Ollie",
        "url": "https://blog.ollie.com/wp-content/uploads/250506_Livingroom_SHOT-10_0173_FR-scal…",
        "width": 2560
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the search returned results. A search with no results returns `false`. |
| `data.items[]` | One image result. Results appear in the order Google ranked them. |
| `data.items[].position` | Rank of the image in the results, starting at 1. |
| `data.items[].url` | Direct URL of the full-size image. Long URLs may be cut off in some cases, so check that a URL loads before you rely on it. |
| `data.items[].thumbnailUrl` | URL of a small preview version of the image. |
| `data.items[].width / data.items[].height` | Image dimensions. Both values look like pixel counts. |
| `data.items[].title` | Title shown for the image, usually the title of the page that hosts it. |
| `data.items[].source` | Domain name of the site that hosts the image. |
| `data.items[].sourceUrl` | URL of the web page where the image appears. |

### Notes

- Use `limit` to set how many images come back. It accepts 1 to 100 and defaults to 20.
- Use `timeframe` with `1h`, `1d`, `7d`, `1y`, or `all` to limit results to recent images.
- Set `autocorrect` to `false` to search the exact query without spelling correction.
- To search by an image instead of text, try [Google Lens](/apis/google/lens). For video results, use [Google Videos](/apis/google/videos).

### Pricing

Billed at the actual cost of each call, about $0.00085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/images.json`](../../../catalog/models/google/images.json) · Store page: https://www.sandbase.ai/model/google/images
