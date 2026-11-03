# Bing Images Search API: pricing, parameters and code examples

`bing/images` · data API · Bing · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Bing Images results for a keyword: image URLs, thumbnails, titles, sizes and source pages.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bing/images", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bing/images', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bing/images", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bing/images", sandbase.Params{
	"q": "coffee",
})
```

Same call via the path form: `POST /v1/api/bing/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |

## Details

This API returns Bing Images results for a search keyword. Each result has the full image URL, a thumbnail, a title, the image size and the page it came from. It needs one input, the search term `q`.

### Use cases

- Collect image candidates for a topic such as `coffee` to review for a mood board or article.
- Find the source pages that host an image by reading `source` and `domain`.
- Build a list of related search terms for a keyword from `related_searches` and `suggested_searches`.
- Check which sites rank for an image query by comparing `domain` and `position` across results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bing/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | q |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "images_results": [
    {
      "description": "Beyond Caffeine: How the Coffee Experience Enhances Brain Readiness ...",
      "domain": "neurosciencenews.com",
      "link": "https://www.bing.com/images/search?view=detailV2&ccid=zMFtlEEJ&id=35451614604F69…",
      "original": "https://neurosciencenews.com/files/2023/06/coffee-brain-caffeine-neuroscincces.j…",
      "position": 1,
      "size": "1200×800",
      "source": "https://neurosciencenews.com/coffee-readiness-caffeine-23543/",
      "source_logo": "https://th.bing.com/th/id/ODF.G8TseB84io3WwAFhXBBUuA?w=12&h=12&c=7&rs=1&p=0&r=0&…",
      "thumbnail": "https://th.bing.com/th/id/OIP.zMFtlEEJqLUrX3QgDoG-qwHaE8?w=258&h=180&c=7&r=0&o=7…",
      "title": "Beyond Caffeine: How the Coffee Experience Enhances Brain Readi…"
    }
  ],
  "related_searches": [
    {
      "name": "Coffee Mugs"
    }
  ],
  "suggested_searches": [
    {
      "link": "https://www.bing.com/images/search?q=Coffee+Art&FORM=RESTAB",
      "name": "Coffee Art",
      "thumbnail": "https://th.bing.com/th?q=Coffee+Art&w=42&h=42&c=7&rs=1&p=0&r=0&o=7&pid=1.7&rm=3&…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `images_results[].original` | URL of the full-size image file. |
| `images_results[].thumbnail` | URL of a small preview image hosted by Bing. Some results do not include it. |
| `images_results[].title / images_results[].description` | Text shown for the image result. They are often the same, and long text may end with an ellipsis. |
| `images_results[].size` | Image dimensions as a string in the form `1200×800`. It reads width then height. |
| `images_results[].source / images_results[].domain` | `source` is the web page that contains the image. `domain` is the site name of that page. |
| `images_results[].position` | Rank of the image in the result list, starting at `1`. |
| `images_results[].link` | Link to the Bing image detail page for this result. |
| `images_results[].source_logo` | URL of a small logo image for the source site. |
| `related_searches[].name` | Text of a related search query. |
| `suggested_searches[].name / suggested_searches[].link / suggested_searches[].thumbnail` | A suggested search term, the Bing Images URL for that search, and a small preview image for it. |

### Notes

- The only input is `q`, the keyword to search for. Pass it as plain text.
- The result list is in `images_results`. The response shown has no pagination field.
- To search video results for the same keyword, call [Bing Videos Search](/apis/bing/videos).
- To get a written answer for a question instead of images, call [Bing Copilot Answer](/apis/bing/copilot).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bing/images.json`](../../../catalog/models/bing/images.json) · Store page: https://www.sandbase.ai/model/bing/images
