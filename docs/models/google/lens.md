# Google Lens API: pricing, parameters and code examples

`google/lens` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Reverse image search: find web pages and visual matches for an image URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/lens", "url": "https://i.imgur.com/HBrB8p0.png"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/lens', {'url': 'https://i.imgur.com/HBrB8p0.png'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/lens", {
  "url": "https://i.imgur.com/HBrB8p0.png"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/lens", sandbase.Params{
	"url": "https://i.imgur.com/HBrB8p0.png",
})
```

Same call via the path form: `POST /v1/api/google/lens` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public URL of the image to search with.  |

## Details

The Google Lens API runs a reverse image search on a public image URL. It returns a list of web pages and visual matches, each with a title, source site, link and image. The only input is the `url` of the image.

### Use cases

- Find the original page or other sites that host a given image.
- Check where a profile photo or product photo appears online.
- Collect pages that mention or show the same subject as an image, such as a person, object or meme.
- Build a list of source sites (for example Reddit or Facebook) that share a picture.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/lens" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://i.imgur.com/HBrB8p0.png"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Public URL of the image to search with. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "results": [
      {
        "image": "https://preview.redd.it/arnold-schwarzenegger-and-danny-devito-v0-mnja7ruli9dh1.…",
        "link": "https://www.reddit.com/r/CelebrityLookalikes/comments/1uwlrps/arnold_schwarzeneg…",
        "source": "Reddit",
        "thumbnailUrl": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQd3AyHbyvFtdWZ50GZr6_g7e9I…",
        "title": "Arnold Schwarzenegger und Danny DeVito : r/CelebrityLookalikes"
      }
    ],
    "url": "https://i.imgur.com/HBrB8p0.png"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the search returned matches. The request still succeeds when nothing is found, and `found` is `false` in that case. |
| `data.url` | The image URL that was searched, echoed back from the request. |
| `data.results[].title` | Title of the matching web page or post. |
| `data.results[].link` | URL of the web page that contains the matching image. |
| `data.results[].source` | Name of the site that hosts the match, such as `Reddit` or `Facebook`. |
| `data.results[].image` | URL of the matching image on the source site. Some values are cut or point to a resized preview. |
| `data.results[].thumbnailUrl` | URL of a small thumbnail of the match. |

### Notes

- The `url` must point to a public image. Pages that need a login will not work.
- The request takes only `url`. It has no pagination parameters.
- To search by keyword instead of by image, use [Google Images](/apis/google/images).

### Pricing

Billed at the actual cost of each call, about $0.00085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/lens.json`](../../../catalog/models/google/lens.json) · Store page: https://www.sandbase.ai/model/google/lens
