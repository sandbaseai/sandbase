# Instagram User Highlights (V3) API: pricing, parameters and code examples

`instagram/v3/user-highlights` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns profile highlights for a specified Instagram account. Supports forward and backward cursor-based pagination to browse collections.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-highlights", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-highlights', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-highlights", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-highlights", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `last` | integer |  | Highlights per page for backward pagination, use with `before`  |
| `after` | string |  | Forward pagination cursor, from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Number of highlights per page (default 10, max 50) default `10`; range 1–50 |
| `before` | string |  | Backward pagination cursor, from previous response `data.page_info.start_cursor`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Returns the story highlights on a public Instagram profile. Each highlight has a title, a cover image, a creation time, and a count of the stories inside it. The only required input is `username`.

### Use cases

- Show an account's highlight reels, with titles and cover images, in a profile viewer.
- Track how many stories each highlight holds to see when a creator adds new material.
- Build a list of highlight IDs to feed into a tool that fetches the stories inside each highlight.
- Compare highlight titles across brand accounts to see which topics they feature.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `after` | string | No | Forward pagination cursor, from previous response `data.page_info.end_cursor` |
| `before` | string | No | Backward pagination cursor, from previous response `data.page_info.start_cursor` |
| `first` | integer | No | Number of highlights per page (default 10, max 50) |
| `last` | integer | No | Highlights per page for backward pagination, use with `before` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "355f3072ef4ec",
  "count": 7,
  "items": [
    {
      "cover_media": {
        "crop_rect": null,
        "cropped_image_version": {
          "height": 150,
          "scans_profile": "",
          "url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.71878-15/756700225_16539857623317…",
          "width": 150
        },
        "full_image_version": null,
        "media_id": null,
        "upload_id": null
      },
      "created_at": "2024-06-28T20:31:11Z",
      "id": "highlight:18223279177302854",
      "media_count": 52,
      "pk": "18223279177302854",
      "title": "close friends"
    }
  ],
  "tray": [
    {
      "cover_media": {
        "crop_rect": null,
        "cropped_image_version": {
          "height": 150,
          "scans_profile": "",
          "url": "https://scontent-xxc1-1.cdninstagram.com/v/t51.71878-15/756700225_16539857623317…",
          "width": 150
        },
        "full_image_version": null,
        "media_id": null,
        "upload_id": null
      },
      "created_at": "2024-06-28T20:31:11Z",
      "id": "highlight:18223279177302854",
      "media_count": 52,
      "pk": "18223279177302854",
      "title": "close friends"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Number of highlights in this response. |
| `items[]` | List of highlight collections for the account. Each entry is one highlight. |
| `items[].title` | Name of the highlight as shown under the profile. It can contain emoji. |
| `items[].id / items[].pk` | Identifier of the highlight. `id` is the `pk` value with a `highlight:` prefix. |
| `items[].media_count` | Number of stories stored in the highlight. |
| `items[].created_at` | Creation time of the highlight, in ISO 8601 UTC format. |
| `items[].cover_media.cropped_image_version.url` | URL of the cropped cover image for the highlight. |
| `items[].cover_media.cropped_image_version.width / items[].cover_media.cropped_image_version.height` | Pixel size of the cover image. Both are 150 in the sample. |
| `tray[]` | List of highlights with the same entries as `items[]` in this response. |

### Notes

- Pass the account name as `username`, for example `instagram`, without the `@` sign.
- Set `first` to change the page size (default 10, max 50). Use `after` for forward paging and `before` with `last` for backward paging.
- Use the `pk` value of a highlight with [Instagram Highlight Detail](/apis/instagram/highlight-detail) to read the stories inside it.
- The cover image URLs in the response are long and contain query parameters, so store the full string.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-highlights.json`](../../../../catalog/models/instagram/v3/user-highlights.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-highlights
