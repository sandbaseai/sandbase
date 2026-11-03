# Yahoo Images Search API: pricing, parameters and code examples

`yahoo/images` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yahoo Images results for a keyword: image URLs, thumbnails, sizes and source pages.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/images", "p": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/images', {'p': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/images", {
  "p": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/images", sandbase.Params{
	"p": "coffee",
})
```

Same call via the path form: `POST /v1/api/yahoo/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `p` | string | yes | p  |

## Details

Returns Yahoo Images search results for a keyword. Each result has the full image URL, a thumbnail, the pixel dimensions, the source page and a title. The only input is the search term in `p`.

### Use cases

- Collect image URLs and source pages for a keyword to review where pictures of a topic appear online.
- Filter results by `dimensions` to find large images for mockups or presentations.
- Build a keyword list from the related and suggested searches for image research.
- Show thumbnail previews of a search term in an internal tool without hosting the images.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"p": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `p` | string | Yes | p |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "images_results": [
    {
      "dimensions": "1200x800",
      "link": "https://images.search.yahoo.com/search/images;_ylt=A2RROKuTkelq1AIABYGJzbkF;_ylu…",
      "original": "https://neurosciencenews.com/files/2023/06/coffee-brain-caffeine-neuroscincces.j…",
      "position": 1,
      "source": "https://neurosciencenews.com/coffee-readiness-caffeine-23543/",
      "thumbnail": "https://tse2.mm.bing.net/th/id/OIP.zMFtlEEJqLUrX3QgDoG-qwHaE8?r=0&pid=Api&h=220&…",
      "title": "Beyond Caffeine: How the Coffee Experience Enhances Brain Readiness ..."
    }
  ],
  "related_searches": [
    {
      "link": "https://images.search.yahoo.com/search/images;_ylt=A2RROKuTkelq1AIAGYGJzbkF;_ylu…",
      "name": "coffee Drink Types",
      "thumbnail": "https://tse2.mm.bing.net/th?q=Coffee+Drink+Types&r=0&pid=Api&mkt=en-US&cc=US&set…"
    }
  ],
  "suggested_searches": [
    {
      "link": "https://images.search.yahoo.com/search/images;_ylt=A2RROKuTkelq1AIA9oCJzbkF;_ylu…",
      "name": "coffee Art",
      "thumbnail": "https://tse2.mm.bing.net/th?q=Coffee+Art&r=0&pid=Api&mkt=en-US&cc=US&setlang=en&…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `images_results[].original` | URL of the full-size image file. |
| `images_results[].thumbnail` | URL of a small preview version of the image. |
| `images_results[].dimensions` | Image size as a `widthxheight` string, for example `1200x800`. |
| `images_results[].source` | URL of the web page that hosts the image. |
| `images_results[].title` | Title of the result. Long titles may end with an ellipsis. |
| `images_results[].position` | Rank of the image in the results, starting at `1`. |
| `images_results[].link` | Yahoo Images link for this result. |
| `related_searches[].name / suggested_searches[].name` | Search phrase that Yahoo offers for the query. |
| `related_searches[].link / suggested_searches[].link` | Yahoo Images link that runs the related or suggested search. |
| `related_searches[].thumbnail / suggested_searches[].thumbnail` | Preview image URL for the related or suggested search. |

### Notes

- `dimensions` is a string, so split it on `x` to get width and height as numbers.
- Use `original` for the image file and `source` for the page it appears on. `link` points to the Yahoo results page.
- To search for video instead of images, call [Yahoo Videos Search](/apis/yahoo/videos).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo/images.json`](../../../catalog/models/yahoo/images.json) · Store page: https://www.sandbase.ai/model/yahoo/images
