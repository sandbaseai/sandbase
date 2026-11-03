# Instagram Recommended Reels Feed API: pricing, parameters and code examples

`instagram/v3/recommended-reels` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns the Instagram Reels recommendation feed with media details and pagination support. Use optional pagination parameters to control page size and navigate subsequent results.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/recommended-reels"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/recommended-reels', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/recommended-reels", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/recommended-reels", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/instagram/v3/recommended-reels` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor`  |
| `first` | integer |  | Number of Reels to fetch per request (default 12, max 50) default `12`; range 1–50 |

## Details

Returns a page of Instagram Reels from the recommendation feed, with caption and media details for each Reel. It needs no input. You can set the page size with `first` and continue with an `after` cursor.

### Use cases

- Sample the Reels that Instagram recommends to collect captions and hashtags for trend research.
- Page through the feed to build a set of short video posts for content analysis.
- Check which hashtags and topics appear most often in recommended Reels.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/recommended-reels" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `after` | string | No | Pagination cursor, omit for first request, get from previous response `data.page_info.end_cursor` |
| `first` | integer | No | Number of Reels to fetch per request (default 12, max 50) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "175cd2383155a",
  "edges": [
    {
      "cursor": "",
      "node": {
        "__typename": "XDTClipsItemDict",
        "media": {
          "__typename": "XDTMediaDict",
          "ai_interactive_embodiment_attachment_style_info": null,
          "ai_label_info": null,
          "audience": null,
          "brs_severity": 70,
          "can_viewer_reshare": true,
          "caption": {
            "has_translation": null,
            "pk": "17886277431503571",
            "text": "Hoping to get more of these soon 🩵\n#northernlights #aurora #fairbanks #aurorabor…"
          },
          "carousel_media": null
        }
      }
    }
  ],
  "gating": null,
  "page_info": {
    "end_cursor": "Giae5PnbnMSEuG-wtPuzjbeFvm8mis2shbRoFAQ0AikIGAAaCBgNczoxYTFhMDU1OTM0NRQBGgYZDAA=",
    "has_next_page": true,
    "has_previous_page": false,
    "start_cursor": null
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `edges[].node.media` | The Reel item. It holds the media details for one recommended Reel. |
| `edges[].node.media.caption.text` | Caption text of the Reel, including hashtags. |
| `edges[].node.media.caption.pk` | ID of the caption. |
| `edges[].node.media.can_viewer_reshare` | Whether the viewer can reshare the Reel (`true` or `false`). |
| `edges[].node.media.carousel_media` | Carousel items. It is `null` for a single Reel. |
| `edges[].node.__typename` | Item type. Reels in this feed show `XDTClipsItemDict`. |
| `page_info.end_cursor` | Cursor for the last item on this page. Pass it as `after` to get the next page. |
| `page_info.has_next_page` | `true` when more Reels are available after this page. |

### Notes

- Omit `after` on the first request. For later pages, send the `page_info.end_cursor` value from the previous response as `after`.
- `first` sets the number of Reels per request. The default is 12 and the maximum is 50.
- In the response the pagination object is at `page_info`. The `edges[].cursor` values were empty in the sample, so use `page_info.end_cursor`.
- To get full details for a Reel you found, call [Instagram Post Details (V3)](/apis/instagram/v3/post-info).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/recommended-reels.json`](../../../../catalog/models/instagram/v3/recommended-reels.json) · Store page: https://www.sandbase.ai/model/instagram/v3/recommended-reels
