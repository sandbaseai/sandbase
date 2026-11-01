# TikTok Photos

`tiktok/photos` · api · TikTok

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

Get every image in a TikTok photo-mode (slideshow) post by URL, in order, with pixel dimensions and both the clean and watermarked variant of each. Videos carry no images - use tiktok.video_download for those.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/photos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@foodbyfranchi/video/7479916555602513174"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full TikTok photo-mode post URL. TikTok serves slideshow posts under the same /video/<id> path as videos, so the normal share link works. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `authorFollowers`, and it is served only by a source that returns ever |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/photos.json`](../../../catalog/models/tiktok/photos.json) · Store page: https://www.sandbase.ai/model/tiktok/photos
