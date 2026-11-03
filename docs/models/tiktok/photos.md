# TikTok Photos API: pricing, parameters and code examples

`tiktok/photos` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get every image in a TikTok photo-mode (slideshow) post by URL, in order, with pixel dimensions and both the clean and watermarked variant of each. Videos carry no images - use tiktok.video_download for those.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/photos", "url": "https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/photos', {'url': 'https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/photos", {
  "url": "https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/photos", sandbase.Params{
	"url": "https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174",
})
```

Same call via the path form: `POST /v1/api/tiktok/photos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full TikTok photo-mode post URL. TikTok serves slideshow posts under the same /video/<id> path as videos, so the normal share link works.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorFollowers`, and it is served only by a source that returns…  |

## Details

This API returns the images of a TikTok photo-mode (slideshow) post. It needs the full post `url`. Each image comes with its pixel size, a clean link and a watermarked link, alongside post stats, author details and sound details.

### Use cases

- Download every slide of a recipe or travel slideshow in its original order.
- Archive a post's clean images together with its caption and hashtags.
- Compare engagement across slideshow posts using `views`, `likes`, `saves` and `shares`.
- Check image sizes before you place the slides in a layout or a moodboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full TikTok photo-mode post URL. TikTok serves slideshow posts under the same /video/<id> path as videos, so the normal share link works. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorFollowers`, and it is served only by a source that returns ever |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorFollowers": null,
    "authorHandle": "foodbyfranchi",
    "authorImage": "https://p19-common-sign.tiktokcdn-us.com/tos-maliva-avt-0068/1b81784e343ee84feee…",
    "authorName": "Emily Franchi",
    "authorUserId": "6743592683137287173",
    "caption": "#food #cooking #dinner #dinnerideas #dinnerinspo #dinnerwithme #cookwithme #dish…",
    "comments": 272,
    "createdUtc": 1741553789,
    "hashtags": [
      "food"
    ],
    "id": "7479916555602513174",
    "images": [
      {
        "height": 1919,
        "image": "https://p16-common-sign.tiktokcdn-us.com/tos-no1a-i-photomode-no/470310afedf94b2…",
        "watermarkedImage": "https://p16-common-sign.tiktokcdn-us.com/tos-no1a-i-photomode-no/470310afedf94b2…",
        "width": 1080
      }
    ],
    "likes": 315259
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.images[]` | The slides of the post, in posting order. Each item holds one image. |
| `data.images[].image` | Link to the clean version of the slide, without a watermark. |
| `data.images[].watermarkedImage` | Link to the same slide with the TikTok watermark and author handle added. |
| `data.images[].width / data.images[].height` | Pixel size of the slide. |
| `data.caption` | Caption text of the post. Long captions may be cut in the sample, so do not rely on its length. |
| `data.hashtags[]` | Hashtags from the caption, without the `#` sign. |
| `data.views / data.likes / data.comments / data.saves / data.shares` | Engagement counts for the post. |
| `data.authorHandle / data.authorName / data.authorUserId` | The author's handle, display name and numeric user ID. |
| `data.createdUtc` | Post creation time as a Unix timestamp in seconds (UTC). |
| `data.soundTitle / data.soundAuthor / data.soundClipId` | Title, author and ID of the sound used on the post. |

### Notes

- Use the normal share link of the post. TikTok serves slideshows under the same `/video/<id>` path as videos, and the response `url` shows the `/photo/<id>` form.
- `authorFollowers` is `null` in this response. Pass `requireFields: ["authorFollowers"]` to ask for a source that returns it. This can change the price.
- If no post is found, the call still succeeds and returns `found: false`.
- Videos have no images. Use the video download API for those posts.

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/photos.json`](../../../catalog/models/tiktok/photos.json) · Store page: https://www.sandbase.ai/model/tiktok/photos
