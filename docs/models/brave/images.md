# Brave Image Search API: pricing, parameters and code examples

`brave/images` · data API · Brave · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Image Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/images", "q": "golden gate bridge"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/images', {'q': 'golden gate bridge'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/images", {
  "q": "golden gate bridge"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/images", sandbase.Params{
	"q": "golden gate bridge",
})
```

Same call via the path form: `POST /v1/api/brave/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query.  |
| `count` | integer |  | The number of search results returned in response. The maximum is 200. The actual number delivered may be less than requested. NOTE: Image search is not paginated and has no offset parameter. Raise count to get more… default `50`; range 1–200 |
| `country` | string |  | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries and ALL for worldwide. one of: `AR`, `AU`, `AT`, `BE`, `BR`, `CA`, `CL`, `DK`, `FI`, `FR`, `DE`, `GR` …; default `"US"` |
| `safesearch` | string |  | Filters search results for adult content. The following values are supported: off - No content filtering (except for illegal content). strict - Drops all adult content from search results. one of: `off`, `strict`; default `"strict"` |
| `spellcheck` | boolean |  | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. default `true` |
| `search_lang` | string |  | The search language preference. The 2 or more character language code for which the search results are provided. one of: `ar`, `eu`, `bn`, `bg`, `ca`, `zh-hans`, `zh-hant`, `hr`, `cs`, `da`, `nl`, `en` …; default `"en"` |

## Details

Returns image search results for a text query from Brave. Each result has the image URL, a thumbnail, the title, and the page that hosts the image. The only required input is `q`.

### Use cases

- Collect reference photos of a landmark, product, or topic for a mood board or article draft.
- Find the pages that host a given image by reading the `url` of each result.
- Build a gallery that shows thumbnails first and loads the full-size image on click.
- Compare which domains show up most often for a query using `source` or `meta_url.hostname`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "golden gate bridge"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | The user’s search query term. Query can not be empty. Maximum of 400 characters and 50 words in the query. |
| `count` | integer | No | The number of search results returned in response. The maximum is 200. The actual number delivered may be less than requested. NOTE: Image search is not paginated and has no offset parameter. Raise count to get more resu |
| `country` | string | No | The search query country, where the results come from. The country string is limited to 2 character country codes of supported countries and ALL for worldwide. |
| `safesearch` | string | No | Filters search results for adult content. The following values are supported: off - No content filtering (except for illegal content). strict - Drops all adult content from search results. |
| `search_lang` | string | No | The search language preference. The 2 or more character language code for which the search results are provided. |
| `spellcheck` | boolean | No | Whether to spell check provided query. If the spell checker is enabled, the modified query is always used for search. The modified query can be found in altered key from the query response model. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "might_be_offensive": false
  },
  "query": {
    "original": "golden gate bridge",
    "show_strict_warning": false,
    "spellcheck_off": false
  },
  "results": [
    {
      "confidence": "high",
      "meta_url": {
        "favicon": "https://imgs.search.brave.com/YSHe_5h9QnEav4cobHlGkLih-MR5YmLIBOWmywSPDz0/rs:fit…",
        "hostname": "oceanusadventure.com",
        "netloc": "oceanusadventure.com",
        "path": "› golden-gate-bridge-photo-spots",
        "scheme": "https"
      },
      "page_fetched": "2026-10-27T00:46:21Z",
      "properties": {
        "height": 683,
        "placeholder": "https://imgs.search.brave.com/jy6Pk7D1t1371CbAKbTqpirvz_d_6xaL9A_it0-MbX0/rs:fit…",
        "url": "https://oceanusadventure.com/wp-content/uploads/2025/02/DSC00616-min-1024x683.jp…",
        "width": 1024
      },
      "source": "oceanusadventure.com",
      "thumbnail": {
        "height": 333,
        "src": "https://imgs.search.brave.com/lSV2QLwhsI8RCUie7Uubj6f_jH7JYZ9eWA61tbjfrjs/rs:fit…",
        "width": 500
      },
      "title": "Photo of the Golden Gate Bridge half in Fog from Battery Spencer Viewpoint",
      "type": "image_result",
      "url": "https://oceanusadventure.com/golden-gate-bridge-photo-spots/"
    }
  ],
  "type": "images"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[].title` | Title text of the image result, taken from the page that hosts it. |
| `results[].url` | URL of the web page that contains the image. |
| `results[].properties.url` | Direct URL of the full-size image file. |
| `results[].properties.width / results[].properties.height` | Width and height of the full-size image. |
| `results[].thumbnail.src` | URL of a smaller preview of the image, served through a Brave image proxy. |
| `results[].thumbnail.width / results[].thumbnail.height` | Width and height of the thumbnail. |
| `results[].source` | Domain name of the site that hosts the image. |
| `results[].meta_url.hostname / results[].meta_url.favicon` | Hostname of the hosting page and the URL of its favicon. |
| `results[].confidence` | Confidence label for the result, such as `high`. |
| `results[].page_fetched` | ISO 8601 timestamp for when the hosting page was fetched. |
| `query.original` | The query string as you sent it. |

### Notes

- Image search has no pagination and no offset. Raise `count` (up to 200) to get more results. The response may contain fewer results than requested.
- Set `safesearch` to `off` to remove adult content filtering. The default is `strict`.
- Use `country` and `search_lang` to change the market and language of the results.
- For web pages instead of images, call [Brave Web Search](/apis/brave/web). For video results, call [Brave Video Search](/apis/brave/videos).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/brave/images.json`](../../../catalog/models/brave/images.json) · Store page: https://www.sandbase.ai/model/brave/images
