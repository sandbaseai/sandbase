# Facebook Page Photos API: pricing, parameters and code examples

`facebook/photos` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch recent photos posted by any public Facebook page or profile (image URLs, captions, and dimensions) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/photos", "url": "https://www.facebook.com/Spurs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/photos', {'url': 'https://www.facebook.com/Spurs'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/photos", {
  "url": "https://www.facebook.com/Spurs"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/photos", sandbase.Params{
	"url": "https://www.facebook.com/Spurs",
})
```

Same call via the path form: `POST /v1/api/facebook/photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of the public Facebook page or profile to fetch photos from (e.g. https://www.facebook.com/Spurs).  |
| `cursor` | string |  | Pagination cursor from a previous response to fetch the next page.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imageWidth`, and it is served only by a source that returns every…  |

## Details

Returns recent photos posted by a public Facebook page or profile. Each photo includes an image URL, a thumbnail, a caption, and pixel dimensions. The only required input is the page or profile `url`.

### Use cases

- Build a visual archive of a sports team's or brand's Facebook photo posts.
- Collect image URLs and captions from a page to review its visual content.
- Check the size of photos on a page to see which image formats it posts.
- Page through a profile's photo history by passing the returned cursor into the next call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.facebook.com/Spurs"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of the public Facebook page or profile to fetch photos from (e.g. https://www.facebook.com/Spurs). |
| `cursor` | string | No | Pagination cursor from a previous response to fetch the next page. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imageWidth`, and it is served only by a source that returns every one |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_Pj9HdDCCE7wOBzMCeA_dDA",
    "nextPageId": "YXBwX2NvbGxlY3Rpb246cGZiaWQwN25Vc3R3MVFhWG80bTRKMkxqQU5NWXJ6VVZRM29FQUFvaExjN3NQ…",
    "photos": [
      {
        "caption": "May be an image of basketball and text",
        "id": "YXBwX2l0ZW06MTAwMDQ0NjM0NDUwMjA4OjIzMDUyNzI3MzI6NTo6MTY2NDkxMDI5MTY3MzQzNw==",
        "imageHeight": 1350,
        "imageUrl": "https://scontent-sjc6-1.xx.fbcdn.net/v/t51.82787-15/883176128_18645685630004556_…",
        "imageWidth": 1080,
        "photoId": "1664910291673437",
        "thumbnail": "https://scontent-sjc6-1.xx.fbcdn.net/v/t51.82787-15/883176128_18645685630004556_…",
        "url": "https://www.facebook.com/photo.php?fbid=1664910291673437&set=pb.100044634450208.…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.photos[].photoId` | Facebook ID of the photo. It also appears as the `fbid` value in the photo `url`. |
| `data.photos[].id` | Encoded item ID for the photo in the page's photo list. |
| `data.photos[].imageUrl` | Link to the full-size image file. |
| `data.photos[].thumbnail` | Link to a smaller, square-cropped version of the image. |
| `data.photos[].url` | Link to the photo's page on Facebook. |
| `data.photos[].caption` | Text description of the photo. In this response it reads like an automatic image description, such as `May be an image of basketball and text`. |
| `data.photos[].imageWidth / data.photos[].imageHeight` | Width and height of the image. Values such as `1080` and `1350` look like pixels, but the response does not state the unit. |
| `data.nextCursor` | Cursor to pass as `cursor` to fetch the next page of photos. |
| `data.nextPageId` | Encoded ID for the next page of results. Only some sources return it. |
| `found` | `true` when the page or profile was found. |

### Notes

- Pass a public page or profile address in `url`, for example `https://www.facebook.com/Spurs`.
- To get the next page, send the same `url` with `cursor` set to the `data.nextCursor` value from the previous response.
- Use `requireFields` with `imageHeight`, `imageWidth`, or `nextPageId` if your request needs those fields. This can change which source serves the call and its price.
- To find a page first, try [Facebook Page Search](/apis/facebook/search-pages). To read posts from the same page, use [Facebook Get Profile Posts](/apis/facebook/profile-posts).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/facebook/photos.json`](../../../catalog/models/facebook/photos.json) · Store page: https://www.sandbase.ai/model/facebook/photos
