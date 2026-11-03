# Xiaohongshu (RED) Image Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-images` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns image notes and matching post metadata for a specified search keyword. Results include image URLs, engagement metrics, note identifiers, and author information.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-images", "keyword": "OpenAI", "page": 1, "search_id": "", "search_session_id": "", "source": "explore_feed", "word_request_id": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-images', {'keyword': 'OpenAI', 'page': 1, 'search_id': '', 'search_session_id': '', 'source': 'explore_feed', 'word_request_id': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-images", {
  "keyword": "OpenAI",
  "page": 1,
  "search_id": "",
  "search_session_id": "",
  "source": "explore_feed",
  "word_request_id": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-images", sandbase.Params{
	"keyword": "OpenAI",
	"page": 1,
	"search_id": "",
	"search_session_id": "",
	"source": "explore_feed",
	"word_request_id": "",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, start from 1 default `1` |
| `source` | string |  | Source, default "explore_feed" default `"explore_feed"` |
| `keyword` | string | yes | Search keyword  |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |
| `word_request_id` | string |  | Word request ID, pass value from first search response for pagination default `""` |
| `search_session_id` | string |  | Search session ID, pass value from first search response for pagination default `""` |

## Details

Returns image notes from Xiaohongshu (RED) that match a search keyword. Each result has image URLs, like, collect and comment counts, share link and author details. The only required input is `keyword`.

### Use cases

- Collect image notes about a brand or topic, such as `OpenAI`, with their cover image URLs.
- Compare `liked_count`, `collected_count` and `comments_count` across notes to spot posts that get the most engagement.
- Build a list of creators who post about a topic using `user_info.user_id` and `user_info.red_id`.
- Pull the share link of each note to open or store the original post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `page` | integer | No | Page number, start from 1 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `search_session_id` | string | No | Search session ID, pass value from first search response for pagination |
| `source` | string | No | Source, default "explore_feed" |
| `word_request_id` | string | No | Word request ID, pass value from first search response for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "filter_items": [
      {
        "filter_tags": [
          {
            "icon_tail_url": "",
            "icon_tail_url_night": "",
            "icon_url": "",
            "icon_url_night": "",
            "id": "综合",
            "name": "Top",
            "need_location_info": false,
            "origin_text": ""
          }
        ],
        "group_show_type": 1,
        "id": "filter_hot",
        "name": "热门词",
        "type": "single",
        "word_request_id": "9843f0d7-3991-46c6-a090-737d51134b49"
      }
    ],
    "items": [
      {
        "image_info": {
          "fileid": "spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8",
          "height": 1232,
          "need_load_original_image": true,
          "original": "https://sns-na-i27.xhscdn.com/spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8?…",
          "trace_id": "spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8",
          "url": "https://sns-na-i27.xhscdn.com/spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8?…",
          "url_size_large": "https://sns-na-i27.xhscdn.com/spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8?…",
          "width": 928
        },
        "note_info": {
          "collected": false,
          "collected_count": 136,
          "comments_count": 3,
          "cover_image_index": 0,
          "desc": "关键词[微笑R]\nlino cut of children following a trail of paw prints through a forest. …",
          "liked": false,
          "liked_count": 197,
          "model_type": "image_card"
        },
        "share_info": {
          "content": "关键词[微笑R] lino cut of children following a trail of paw print",
          "function_entries": [
            {
              "type": "generate_image"
            }
          ],
          "guide_audited": true,
          "image": "http://ci.xiaohongshu.com/spectrum/1040g0k030pksuqnjms005o5h6s4080o1km2vfn8?imag…",
          "link": "https://www.xiaohongshu.com/discovery/item/6517c4b2000000001e023667?app_platform…",
          "title": "Midjourney绘图 | 徒步穿越者"
        },
        "user_info": {
          "images": "https://sns-avatar-qc.xhscdn.com/avatar/64354610ec2be016c1cf5f6a.jpg?imageView2/…",
          "nickname": "快乐小欢",
          "red_id": "9549661040",
          "red_official_verified": false,
          "red_official_verify_type": 0,
          "show_red_official_verify_icon": false,
          "user_id": "60b137080000000001000301"
        }
      }
    ]
  },
  "debug_id": "93d2251f",
  "debug_info": "gAAAAABq6ZFrYKbq4HqNnLWHJ3QNkDMxoAXELty1PI8TT86wzgSoLiLgfoslJUw8IR5w3xJwt5IlyCxh…",
  "msg": "成功",
  "next_page": 2,
  "page": 1,
  "search_id": "072a2c2bb22b46fc",
  "search_session_id": "f0753ad5…",
  "success": true,
  "word_request_id": "2980fa4fd69148438758ba085698fd8d"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].note_info.desc` | Text body of the note, including hashtags. Long text may be cut. |
| `data.items[].note_info.liked_count / collected_count / comments_count` | Number of likes, collects and comments on the note. |
| `data.items[].note_info.model_type` | Type of the result card. The sample values are `image_card`. |
| `data.items[].image_info.url / url_size_large / original` | Image links at different sizes. `url` is a smaller preview, and `url_size_large` and `original` are larger versions. |
| `data.items[].image_info.width / height` | Image size in pixels. |
| `data.items[].share_info.title` | Title of the note. |
| `data.items[].share_info.link` | Share link to the note on xiaohongshu.com. The note ID is in the path after `/discovery/item/`. |
| `data.items[].user_info.nickname / red_id / user_id` | Display name, public RED ID and internal user ID of the author. |
| `data.items[].user_info.red_official_verified` | Whether the author has an official RED verification. |
| `data.filter_items[].filter_tags[].name` | Related filter tags for the search, such as `Top` and `Latest`. |

### Notes

- For the next page, send `page` set to the `next_page` value in the response.
- Copy `search_id`, `search_session_id` and `word_request_id` from the first response into later page requests.
- The note ID is not a separate field in this sample. Read it from `share_info.link`, then pass it to [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail) for the full note.
- To get comments for a note, call [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-images.json`](../../../../catalog/models/xiaohongshu/app-v2/search-images.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-images
