# Xiaohongshu (RED) Topic Feed API: pricing, parameters and code examples

`xiaohongshu/app-v2/topic-feed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of notes listed under a specified topic page on Xiaohongshu (RED). Supports sorting options and cursor pagination using previous response indicators.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/topic-feed", "page_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/topic-feed', {'page_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/topic-feed", {
  "page_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/topic-feed", sandbase.Params{
	"page_id": "example",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/topic-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort type  |
| `source` | string |  | Source, default "normal"  |
| `page_id` | string | yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1"  |
| `session_id` | string |  | Session ID, keep consistent for pagination  |
| `cursor_score` | string |  | Pagination cursor score, pass last item's cursor_score from previous response  |
| `last_note_ct` | string |  | Last note create time from previous page  |
| `last_note_id` | string |  | Last note ID from previous page  |
| `first_load_time` | string |  | First load timestamp, keep consistent for pagination  |

## Details

Returns a page of notes posted under one Xiaohongshu (RED) topic. Each note includes its title, text, images, hashtags, author and engagement counts. The only required input is the topic `page_id`.

### Use cases

- Collect the newest notes under a campaign topic to see what creators are posting.
- Compare `like_count` and `collect_count` across notes in a niche topic to find the strongest posts.
- Build a list of authors who post under a topic by reading `user.user_id` and `user.nickname`.
- Find related topics that creators tag together by reading the `hash_tags` of each note.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/topic-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page_id": "5c1cc866febed9000184b7c1"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page_id` | string | Yes | Topic page ID (required), e.g. "5c1cc866febed9000184b7c1" |
| `cursor_score` | string | No | Pagination cursor score, pass last item's cursor_score from previous response |
| `first_load_time` | string | No | First load timestamp, keep consistent for pagination |
| `last_note_ct` | string | No | Last note create time from previous page |
| `last_note_id` | string | No | Last note ID from previous page |
| `session_id` | string | No | Session ID, keep consistent for pagination |
| `sort` | string | No | Sort type |
| `source` | string | No | Source, default "normal" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
    "items": [
      {
        "create_time": 1793691020000,
        "cursor_score": "2XknGYD5kwjgSQWY6z66-tZP76FbH-3lKerdWqinARk",
        "desc": "准备去东京的宝子们，这篇出发前赶紧码住！近东京塔，环球影城！不管gou物还是打卡，星.级酒店11-2🈷️差不多半jia就能拿下📉\n-\n🏨#东京康莱德酒店[话题]…",
        "hash_tags": [
          {
            "id": "5efab1bf0000000001007386",
            "link": "xhsdiscover://rn/sns-discover/topic/normal?id=5efab1bf450d6e0001d15a5e&topic_nam…",
            "name": "东京康莱德酒店",
            "type": "topic"
          }
        ],
        "id": "6ae98d8c000000000602e834",
        "images_list": [
          {
            "fileid": "notes_pre_post/1040g3k032725bhmnme5g5qjgcctks604ht4d9so",
            "height": 1920,
            "live_photo": {
              "media": {
                "stream": {
                  "av1": [],
                  "h264": [],
                  "h265": [
                    {
                      "audio_bitrate": 56002,
                      "audio_channels": 2,
                      "audio_codec": "aac",
                      "audio_duration": 34364,
                      "avg_bitrate": 2652909,
                      "backup_urls": [
                        "http://sns-bak-v11.xhscdn.com/stream/79/10/66/01eae98d8c1030c84f005001a1a0526791…"
                      ],
                      "default_stream": 1,
                      "duration": 34365
                    }
                  ],
                  "h266": []
                },
                "user_level": 0,
                "video": {
                  "biz_id": "282294720814311476",
                  "biz_name": 10,
                  "bound": [
                    {
                      "h": 1920,
                      "w": 1440,
                      "x": 0,
                      "y": 0
                    }
                  ],
                  "drm_type": 0,
                  "duration": 35,
                  "hdr_type": 0,
                  "height": 1920,
                  "opaque1": {
                    "amend": "15",
                    "amend_mobile": "60",
                    "domestic": "0",
                    "livephoto_flag": "1"
                  }
                },
                "video_id": "138179532737753288"
              }
            },
            "live_photo_file_id": "livephoto_pre_post/1040g3jg3272dqj8kme4g5qjgcctks60422oi3p8",
            "url": "https://sns-na-i11.xhscdn.com/notes_pre_post/1040g3k032725bhmnme5g5qjgcctks604ht…",
            "url_size_large": "https://sns-na-i11.xhscdn.com/notes_pre_post/1040g3k032725bhmnme5g5qjgcctks604ht…",
            "width": 1440
          }
        ],
        "interaction_info": {
          "collect_count": 4,
          "comment_count": 6,
          "like_count": 8,
          "liked": false,
          "share_count": 6
        },
        "note_time": {
          "create_time": 1793691020,
          "update_time": 1793691021
        },
        "share_info": {
          "content": "准备去东京的宝子们，这篇出发前赶紧码住！近东京塔，环球影城！不管gou物还是打卡，星.级酒店11-2🈷️差不多半jia就",
          "function_entries": [
            {
              "type": "generate_image"
            }
          ],
          "image": "https://sns-na-i11.xhscdn.com/notes_pre_post/1040g3k032725bhmnme5g5qjgcctks604ht…",
          "link": "https://www.xiaohongshu.com/discovery/item/6ae98d8c000000000602e834?app_platform…",
          "title": "别住贵了！东京酒店🏨11-2月集体下调"
        },
        "title": "别住贵了！东京酒店🏨11-2月集体下调52%😭",
        "topic_note_translate_info": {
          "translate_type": 2
        },
        "type": "normal"
      }
    ]
  },
  "debug_id": "63438a41",
  "debug_info": "gAAAAABq6ZFteeAY821utDooLpZuZF4b7YU4pwv_jC1VGnT_rsun4ez5vBGkO7sk24XwUmjAoGTxgogB…",
  "extra": {
    "force_message": "",
    "force_update": 0
  },
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | ID of the note. |
| `data.items[].title` | Title of the note. |
| `data.items[].desc` | Note text. Long text is cut and may contain topic tags written as `#name[话题]#`. |
| `data.items[].type` | Note type. The sample shows `normal`. |
| `data.items[].create_time` | Creation time of the note in milliseconds. |
| `data.items[].note_time.create_time / data.items[].note_time.update_time` | Creation and update times of the note in seconds. |
| `data.items[].interaction_info.like_count / collect_count / comment_count / share_count` | Counts of likes, collects, comments and shares on the note. |
| `data.items[].user.user_id / data.items[].user.nickname` | ID and display name of the author. |
| `data.items[].hash_tags[].name / data.items[].hash_tags[].id` | Name and ID of each topic tagged in the note. |
| `data.items[].cursor_score` | Cursor value for this note. Use it to request the next page. |
| `data.has_more` | `true` when more notes are available after this page. |

### Notes

- Pass `page_id` as the topic page ID, for example `5c1cc866febed9000184b7c1`. Get topic IDs from the `hash_tags[].id` field of a note or from [Xiaohongshu (RED) Topic Details](/apis/xiaohongshu/app-v2/topic-info).
- For the next page, send the `cursor_score` of the last item as `cursor_score`, plus its `id` as `last_note_id` and its creation time as `last_note_ct`. Keep `session_id` and `first_load_time` the same across pages.
- Check `data.has_more` before requesting another page.
- To read one note in full, pass its `id` to [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail) or [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/topic-feed.json`](../../../../catalog/models/xiaohongshu/app-v2/topic-feed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/topic-feed
