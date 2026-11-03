# Weibo Post Detail API: pricing, parameters and code examples

`weibo/web-v2/post-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the full data of a single Weibo post by its ID: text (including long posts), author, publish time, location and repost, comment and like counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/post-detail", "id": "5350731756601957", "is_get_long_text": "true"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/post-detail', {'id': '5350731756601957', 'is_get_long_text': 'true'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/post-detail", {
  "id": "5350731756601957",
  "is_get_long_text": "true"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/post-detail", sandbase.Params{
	"id": "5350731756601957",
	"is_get_long_text": "true",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Weibo post ID (required)  |
| `is_get_long_text` | string |  | Whether to get full text of long posts (default "true") default `"true"` |

## Details

Returns the data of a single Weibo post: publish time, region label, repost, comment and like counts, and attached images. It needs the Weibo post ID in `id`. Long posts can be expanded to full text with `is_get_long_text`.

### Use cases

- Track how reposts, comments and likes of one post change between calls.
- Archive a post with its images and publish time for news or brand monitoring.
- Check where a post was published from using the region label.
- Download the images of a post in several sizes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5350554563773695"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Weibo post ID (required) |
| `is_get_long_text` | string | No | Whether to get full text of long posts (default "true") |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "analysis_extra": "",
  "annotations": [
    {
      "photo_sub_type": "0"
    }
  ],
  "attitudes_count": 168,
  "attitudes_status": 0,
  "can_edit": false,
  "comment_manage_info": {
    "approval_comment_type": 0,
    "comment_anon_type": 0,
    "comment_permission_type": -1,
    "comment_sort_type": 0
  },
  "comments_count": 36,
  "content_auth": 0,
  "created_at": "Mon Oct 05 07:04:39 +0800 2026",
  "favorited": false,
  "id": 5350554563773695,
  "idstr": "5350554563773695"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / idstr / mid` | The post ID as a number and as strings. Use `idstr` or `mid` when you need the exact ID without number rounding. |
| `mblogid` | Short alphanumeric ID of the post, the kind used in Weibo post links. |
| `created_at` | Publish time as a text date with a `+0800` offset, for example `Mon Oct 05 07:04:39 +0800 2026`. |
| `reposts_count / comments_count / attitudes_count` | Number of reposts, comments and likes of the post. |
| `region_name` | Region label shown on the post, for example `发布于 美国`. |
| `isLongText` | `true` if the post is a long post. This sample post is `false`. |
| `pic_ids` | List of IDs of the images attached to the post. Each ID is a key in `pic_infos`. |
| `pic_infos.{pic_id}.large.url / pic_infos.{pic_id}.original.url` | Image URLs in different sizes. Other sizes are `thumbnail`, `bmiddle`, `largest` and `mw2000`, each with `width` and `height`. |
| `pic_num` | Number of images in the post. |
| `number_display_strategy.display_text` | Short display label for a large count, here `100万+`. |

### Notes

- Use the numeric `id` or `mid` from a post, or the post ID returned by a Weibo search API, as the `id` input.
- `is_get_long_text` is a string and defaults to `"true"`.
- The key under `pic_infos` is the image ID, so read `pic_ids` first and then look up each ID.
- To read replies, call [Weibo Post Comments](/apis/weibo/web-v2/post-comments) next.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.
- [Weibo AI Search Content Extension](/apis/weibo/web-v2/ai-related-search): Get content extensions related to keyword (related questions, blogger recommendations, reference posts).

---
Machine-readable: [`catalog/models/weibo/web-v2/post-detail.json`](../../../../catalog/models/weibo/web-v2/post-detail.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/post-detail
