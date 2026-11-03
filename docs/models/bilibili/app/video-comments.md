# Bilibili Video Comments (App) API: pricing, parameters and code examples

`bilibili/app/video-comments` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns user comments for a specified Bilibili video by AV or BV identifier. Supports sorting comments by popularity or post time, with cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/video-comments", "bv_id": "BV19uhb6mEWd", "next_offset": 3}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/video-comments', {'bv_id': 'BV19uhb6mEWd', 'next_offset': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/video-comments", {
  "bv_id": "BV19uhb6mEWd",
  "next_offset": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/video-comments", sandbase.Params{
	"bv_id": "BV19uhb6mEWd",
	"next_offset": 3,
})
```

Same call via the path form: `POST /v1/api/bilibili/app/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mode` | integer |  | Sort mode (3=hot, 2=time) default `3` |
| `av_id` | string |  | AV ID (choose one of av_id or bv_id)  |
| `bv_id` | string |  | BV ID (choose one of av_id or bv_id)  |
| `next_offset` | integer |  | Pagination cursor default `1` |

## Details

Returns a page of comments for one Bilibili video, including each comment's text, like count, author and a few nested replies. It needs a video ID, given as either `av_id` or `bv_id`.

### Use cases

- Pull the top comments of a video to study what viewers agree or argue about.
- Sort comments by post time with `mode` set to `2` to follow how a discussion develops.
- Collect comment authors' `mid` values to find active commenters on a video.
- Export comment text and like counts for sentiment analysis of a video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"av_id": "115568241811221", "bv_id": "BV18SCrBGE9E"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `av_id` | string | No | AV ID (choose one of av_id or bv_id) |
| `bv_id` | string | No | BV ID (choose one of av_id or bv_id) |
| `mode` | integer | No | Sort mode (3=hot, 2=time) |
| `next_offset` | integer | No | Pagination cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "assist": 0,
    "blacklist": 0,
    "callbacks": null,
    "config": {
      "read_only": false,
      "show_up_flag": true,
      "showtopic": 1
    },
    "control": {
      "answer_guide_android_url": "https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=6",
      "answer_guide_icon_url": "http://i0.hdslb.com/bfs/emote/96940d16602cacbbac796245b7bb99fa9b5c970c.png",
      "answer_guide_ios_url": "https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=12",
      "answer_guide_text": "需要升级成为lv2会员后才可以评论，先去答题转正吧！",
      "bg_text": "",
      "child_input_text": "只是一直在等你而已，才不是想被评论呢～",
      "disable_jump_emote": false,
      "empty_page": null,
      "enable_charged": true,
      "enable_cm_biz_helper": false,
      "giveup_input_text": "不发没关系，请继续友善哦~",
      "input_disable": false
    },
    "cursor": {
      "all_count": 1250,
      "is_begin": true,
      "is_end": false,
      "mode": 3,
      "mode_text": "",
      "name": "热门评论",
      "next": 2,
      "pagination_reply": {
        "next_offset": "CAEiAggC"
      },
      "prev": 0,
      "session_id": "",
      "support_mode": [
        2
      ]
    },
    "effects": {
      "preloading": ""
    },
    "note": 1,
    "replies": [
      {
        "action": 0,
        "assist": 0,
        "attr": 0,
        "content": {
          "jump_url": {},
          "max_line": 6,
          "members": [],
          "message": "猎鹰这个队的抽象之处在于老尼打的越菜其他人被踢的可能性反而越高。"
        },
        "count": 33,
        "ctime": 1763432703,
        "dialog": 0,
        "dialog_str": "0",
        "dynamic_id_str": "0",
        "fansgrade": 0,
        "folder": {
          "has_folded": false,
          "is_folded": false,
          "rule": ""
        },
        "invisible": false
      }
    ],
    "top": {
      "admin": null,
      "upper": null,
      "vote": null
    },
    "top_replies": null,
    "upper": {
      "mid": 203680252
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.replies[].content.message` | Text of the top-level comment. |
| `data.replies[].rpid_str` | ID of the comment, as a string. |
| `data.replies[].like` | Number of likes on the comment. |
| `data.replies[].rcount / data.replies[].count` | Reply counts for the comment. `rcount` matches the total shown in `reply_control.sub_reply_entry_text`, for example 26 replies. |
| `data.replies[].ctime` | Post time of the comment as a Unix timestamp in seconds. |
| `data.replies[].mid_str` | Bilibili user ID of the commenter, as a string. |
| `data.replies[].member.avatar` | URL of the commenter's avatar image. |
| `data.replies[].replies[]` | A short preview list of replies to the comment. Each item has its own `content.message`, `ctime` and `dialog_str`. |
| `data.replies[].content.pictures[].img_src` | URL of an image attached to the comment. It appears only on comments that have pictures. |
| `data.cursor.all_count` | Total comment count reported for the video. |
| `data.cursor.is_end` | Whether this page is the last one. |
| `data.cursor.pagination_reply.next_offset` | Cursor string for the next page. |

### Notes

- Send either `av_id` or `bv_id`. The BV ID looks like `BV18SCrBGE9E` and the AV ID is a number like `115568241811221`. The comments' `oid_str` matches the AV ID.
- Set `mode` to `3` for hot comments or `2` for time order. The response lists these values in `data.cursor.support_mode`.
- For more pages, check `data.cursor.is_end`. The response gives `data.cursor.next` (`2` on the first page) and `data.cursor.pagination_reply.next_offset` (a string cursor). Use these to set `next_offset` for the next call.
- To get details of the video itself, call [Bilibili App Single Video Details](/apis/bilibili/app/one-video). For a commenter's profile, call [Bilibili App User Info](/apis/bilibili/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili App Bangumi Tab](/apis/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/apis/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/apis/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/video-comments.json`](../../../../catalog/models/bilibili/app/video-comments.json) · Store page: https://www.sandbase.ai/model/bilibili/app/video-comments
