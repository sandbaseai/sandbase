# Weibo User Video Collection Detail API: pricing, parameters and code examples

`weibo/web-v2/user-video-collection-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves detailed information and video listings for a specified Weibo video collection. Supports sorting by default, hottest, or latest videos, alongside cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-video-collection-detail", "cid": "4883992307236954"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-video-collection-detail', {'cid': '4883992307236954'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-video-collection-detail", {
  "cid": "4883992307236954"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-video-collection-detail", sandbase.Params{
	"cid": "4883992307236954",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-video-collection-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cid` | string | yes | Collection ID (required, get from fetch_user_video_collection_list)  |
| `cursor` | string |  | Pagination cursor, pass empty for first request, use returned cursor for subsequent  |
| `tab_code` | integer |  | Sort type (0=default, 1=hottest, 2=latest)  |

## Details

Returns the videos in one Weibo video collection, plus a header with the collection's page segments and sort tabs. It needs the collection ID in `cid`. You can sort by default, hottest or latest and page with a cursor.

### Use cases

- Export every video post in a creator's themed collection, such as a celebrity edit series.
- Rank the videos in a collection by `attitudes_count`, `comments_count` and `reposts_count` to find the best performers.
- Collect cover images and durations to build a video gallery for a collection.
- Page through a long collection in hottest or latest order to track new uploads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-video-collection-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cid": "4883992307236954"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cid` | string | Yes | Collection ID (required, get from fetch_user_video_collection_list) |
| `cursor` | string | No | Pagination cursor, pass empty for first request, use returned cursor for subsequent |
| `tab_code` | integer | No | Sort type (0=default, 1=hottest, 2=latest) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "header": {
    "page_segment_size": 20,
    "page_segments": [
      {
        "action_log": {
          "act_code": 5599,
          "ext": "type:2|t_id:4883992307236954|t_name:%E5%89%AA%E8%BE%91|mid:null|oid:null"
        },
        "first_cursor": 4883992359471289,
        "first_cursorStr": "4883992359471289",
        "last_cursor": 4890466766557477,
        "last_cursorStr": "4890466766557477",
        "page_index": 0,
        "part_name": "1-20",
        "part_state": 1
      }
    ],
    "tabs": [
      {
        "code": 0,
        "name": "默认",
        "type": 0
      }
    ]
  },
  "list": [
    {
      "analysis_extra": "",
      "annotations": [
        []
      ],
      "attitudes_count": 121,
      "attitudes_status": 0,
      "can_edit": false,
      "cardid": "star_329",
      "comment_manage_info": {
        "approval_comment_type": 0,
        "comment_anon_type": 0,
        "comment_permission_type": -1,
        "comment_sort_type": 0
      },
      "comments_count": 1,
      "content_auth": 0,
      "created_at": "Mon Mar 27 19:53:01 +0800 2023",
      "favorited": false,
      "id": 4883992359471289
    }
  ],
  "next_cursor": 4890787378892026
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[]` | One video post in the collection. Each item is a Weibo post with its counts, time and video details. |
| `list[].mid / list[].idstr` | Post ID as a number-like string. `id` holds the same value as a number. |
| `list[].mblogid` | Short post ID. It is a different format from `mid`. |
| `list[].created_at` | Publish time as a text date, for example `Mon Mar 27 19:53:01 +0800 2023`. |
| `list[].attitudes_count / list[].comments_count / list[].reposts_count` | Counts of likes, comments and reposts on the post. |
| `list[].region_name` | Region label shown with the post, for example `发布于 辽宁`. |
| `list[].page_info.content2` | Short label shown on the video card. In this response it holds a person's name. |
| `list[].page_info.media_info.author_name` | Display name of the account that posted the video. |
| `list[].page_info.media_info.duration` | Video length. The values are small whole numbers, such as `16`. |
| `list[].page_info.media_info.big_pic_info.pic_big.url` | Cover image URL at the largest size. `pic_middle` and `pic_small` hold smaller versions with `width` and `height`. |
| `next_cursor` | Cursor value to send as `cursor` to get the next page of videos. |
| `header.tabs[]` | Sort options with `code` and `name`. The codes match the `tab_code` values 0, 1 and 2. |

### Notes

- Get `cid` from the [Weibo User Video Collection List](/apis/weibo/web-v2/user-video-collection-list) API.
- Leave `cursor` empty on the first call. Then pass `next_cursor` from the previous response.
- `header.page_segments[]` splits the collection into ranges such as `1-20` and `21-30`. Each range has `first_cursorStr` and `last_cursorStr`.
- Set `tab_code` to `0` for default, `1` for hottest or `2` for latest order.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-video-collection-detail.json`](../../../../catalog/models/weibo/web-v2/user-video-collection-detail.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-video-collection-detail
