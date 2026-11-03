# Instagram Highlight Detail API: pricing, parameters and code examples

`instagram/highlight-detail` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Fetch the details and media items of a single Instagram story highlight by id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/highlight-detail", "id": "18201653992314974"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/highlight-detail', {'id': '18201653992314974'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/highlight-detail", {
  "id": "18201653992314974"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/highlight-detail", sandbase.Params{
	"id": "18201653992314974",
})
```

Same call via the path form: `POST /v1/api/instagram/highlight-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | The id of the highlight to retrieve details for.  |

## Details

This API returns the details of one Instagram story highlight: its title, owner handle, cover image, and the media items inside it. It needs the highlight `id` as input.

### Use cases

- Archive the photos and videos of a brand's highlight such as a campaign or event reel.
- Check how many stories a highlight holds and when each one was posted.
- Pull the video and image URLs of a highlight to review its content.
- Track when an account adds or renames a highlight by comparing `title` and `mediaCount` over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/highlight-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "18201653992314974"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | The id of the highlight to retrieve details for. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://scontent-sea5-1.cdninstagram.com/v/t51.2885-19/29090066_159271188110124_…",
    "coverUrl": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/718648521_12119525676283…",
    "createdUtc": 1780937715,
    "id": "18201653992314974",
    "items": [
      {
        "code": "DZTBP2mCTYj",
        "createdUtc": 1780862187,
        "durationSeconds": 45.8,
        "hasAudio": true,
        "height": 1920,
        "id": "3914477988573951523",
        "image": "https://scontent-sea5-1.cdninstagram.com/v/t51.71878-15/720146318_86724670251437…",
        "mediaType": 2,
        "paidPartnership": false,
        "productType": "story",
        "videoUrl": "https://scontent-sea5-1.cdninstagram.com/o1/v/t2/f2/m78/AQMNdjoi8emz-9Ae21X6Ohss…",
        "width": 1080
      }
    ],
    "mediaCount": 20,
    "ownerHandle": "nasa",
    "title": "Artemis III"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the highlight exists. A lookup that finds nothing returns `false`. |
| `data.id / data.title` | The highlight id and the title shown on the profile. |
| `data.ownerHandle` | Instagram username of the account that owns the highlight. |
| `data.createdUtc` | Time the highlight was created, as a Unix timestamp in seconds (UTC). |
| `data.mediaCount` | Total number of media items in the highlight. The `items` list in the response can hold fewer entries than this number. |
| `data.coverUrl / data.avatarUrl` | Image URL of the highlight cover and of the owner's profile picture. |
| `data.items[].id / data.items[].code` | The id and the short code of each story item. |
| `data.items[].mediaType` | Numeric media type. In this response `1` marks an image item and `2` marks a video item. |
| `data.items[].image / data.items[].videoUrl` | Image URL of the item. Video items also include a `videoUrl`. |
| `data.items[].durationSeconds / data.items[].hasAudio` | Length of a video item in seconds and whether it has an audio track. Both appear only on video items. |
| `data.items[].width / data.items[].height` | Pixel size of the item as given in the response. |

### Notes

- Each item has its own `createdUtc` Unix timestamp in seconds, which is the time that story was posted.
- `data.items[].productType` is `story` for the items in this highlight.
- To find highlight ids for an account, call [Instagram User Highlights](/apis/instagram/user-highlights).
- To list an account's current stories instead, use [Instagram Stories (full)](/apis/instagram/stories-full).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/highlight-detail.json`](../../../catalog/models/instagram/highlight-detail.json) · Store page: https://www.sandbase.ai/model/instagram/highlight-detail
