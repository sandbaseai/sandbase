# Yandex Images Search API: pricing, parameters and code examples

`yandex/images` · data API · Yandex · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yandex Images results for a keyword: image URLs, thumbnails, sizes and source pages.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yandex/images", "text": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yandex/images', {'text': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yandex/images", {
  "text": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yandex/images", sandbase.Params{
	"text": "coffee",
})
```

Same call via the path form: `POST /v1/api/yandex/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `text` | string | yes | text  |

## Details

This API returns Yandex Images results for a keyword. Each result has the full image URL, a thumbnail, the image size and the page it came from. It needs one input, `text`, the search query.

### Use cases

- Collect image URLs and source pages for a keyword to build a reference set for a design or content project.
- Check which sites rank for a keyword in image search by reading the `source` domain of each result.
- Filter results by `size.width` and `size.height` to find images that are large enough for print or banners.
- Trace where an image appears online by following `link` back to the page that hosts it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yandex/images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `text` | string | Yes | text |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "images_results": [
    {
      "link": "https://www.ixbt.com/live/offtopic/espresso-flet-uayt-latte-makiato-kak-razobrat…",
      "original": "https://img.ixbt.site/live/images/original/32/75/48/2024/10/16/13debe3369.jpg",
      "position": 1,
      "size": {
        "bytes": 52497,
        "height": 501,
        "width": 877
      },
      "snippet": "Эспрессо",
      "source": "ixbt.com",
      "thumbnail": "https://avatars.mds.yandex.net/i?id=3792c6e26c505c0c57105cad26b374d0e32045bf-154…",
      "title": "Эспрессо, флэт уайт, латте макиато. Как разобраться в видах кофе? / Оффтопик / i"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `images_results[]` | List of image results for the query, in the order returned. |
| `images_results[].position` | Rank of the result in the list, starting at `1`. |
| `images_results[].original` | URL of the full-size image file. |
| `images_results[].thumbnail` | URL of a smaller preview image hosted on a Yandex domain. |
| `images_results[].link` | URL of the web page that contains the image. |
| `images_results[].source` | Domain name of the site that hosts the page, for example `en.wikipedia.org`. |
| `images_results[].title` | Title of the source page. Long titles may be cut off. |
| `images_results[].snippet` | Short text shown with the image, such as a caption or page description. |
| `images_results[].size.width / images_results[].size.height` | Width and height of the original image. |
| `images_results[].size.bytes` | File size of the original image, as given by the `bytes` key. |

### Notes

- `text` is the only parameter and it is required. Pass the search phrase as a plain string, for example `coffee`.
- Results are not in English only. Titles and snippets keep the language of the source page.
- To search video results for the same keyword, use [Yandex Videos Search](/apis/yandex/videos).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yandex/images.json`](../../../catalog/models/yandex/images.json) · Store page: https://www.sandbase.ai/model/yandex/images
