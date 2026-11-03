# Bilibili Video Comments API: pricing, parameters and code examples

`bilibili/video-comment` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get comments for a Bilibili video identified by AID, with optional cursor pagination. Use it to review audience discussion, continue through comment pages, or support comment moderation and analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/video-comment", "aid": "80433022"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/video-comment', {'aid': '80433022'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/video-comment", {
  "aid": "80433022"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/video-comment", sandbase.Params{
	"aid": "80433022",
})
```

Same call via the path form: `POST /v1/api/bilibili/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aid` | string | yes | Bilibili Archive ID (AID).  |
| `cursor` | string |  | Pagination cursor.  |

## Details

Returns a page of comments for a Bilibili video. It needs the video's `aid` and accepts an optional `cursor` to fetch the next page.

### Use cases

- Read the newest comments on a video to see what viewers are saying right now.
- Page through all comments of a video to build a dataset for sentiment or topic analysis.
- Check comments for spam or unwanted content as part of a moderation workflow.
- Collect commenter IDs and locations to study who takes part in the discussion.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aid": "80433022"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aid` | string | Yes | Bilibili Archive ID (AID). |
| `cursor` | string | No | Pagination cursor. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "assist": 0,
    "blacklist": 0,
    "callbacks": {},
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
      "child_input_text": "新的风暴已经出现，你的妙评何时再现",
      "disable_jump_emote": false,
      "empty_page": null,
      "enable_charged": false,
      "enable_cm_biz_helper": false,
      "giveup_input_text": "不发没关系，请继续友善哦~",
      "input_disable": false
    },
    "cursor": {
      "all_count": 239733,
      "is_begin": true,
      "is_end": false,
      "mode": 2,
      "mode_text": "",
      "name": "最新评论",
      "next": 203073,
      "pagination_reply": {
        "next_offset": "CAESEDE4MzY3Mzk0MzQ1OTM4MjEaOAo2wdWey6QJ8c6+y6QJkOSpt7IJkKLKt7IJwInnt7IJgPGnurIJ…"
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
        "all_count": 239733,
        "assist": 0,
        "attr": 0,
        "content": {
          "jump_url": {},
          "max_line": 6,
          "members": [],
          "message": "测试一下，马上删。"
        },
        "count": 0,
        "ctime": 1793685983,
        "cursor": "CAESEDE4MzY3Mzk0MzQ1OTM4MjEaOAo2wdWey6QJ8c6+y6QJkOSpt7IJkKLKt7IJwInnt7IJgPGnurIJ…",
        "dialog": 0,
        "dialog_str": "0",
        "dynamic_id_str": "0",
        "fansgrade": 0
      }
    ],
    "top": {
      "admin": null,
      "upper": null,
      "vote": null
    },
    "top_replies": [],
    "upper": {
      "mid": 486906719
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.replies[].content.message` | Text of the comment. Emotes appear as text such as `[星星眼]`, and @mentions appear as `@name`. |
| `data.replies[].rpid / data.replies[].rpid_str` | ID of the comment, as a number and as a string. Use the string form to avoid number precision loss. |
| `data.replies[].ctime` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.replies[].like / data.replies[].rcount` | Number of likes on the comment, and the number of replies under it. |
| `data.replies[].mid_str` | ID of the user who wrote the comment, as a string. The same ID appears in `data.replies[].member.mid`. |
| `data.replies[].member.avatar` | URL of the commenter's avatar image. |
| `data.replies[].reply_control.location` | Location label shown with the comment, for example `IP属地：湖南`. |
| `data.replies[].content.members[]` | Profiles of users mentioned in the comment, with `mid`, `avatar` and `level_info.current_level`. |
| `data.cursor.all_count` | Total comment count reported for the video. |
| `data.cursor.is_end / data.cursor.next` | Flags whether this is the last page, and gives a paging value for the next one. |
| `data.cursor.pagination_reply.next_offset` | Offset string for the next page of comments. |

### Notes

- Pass `aid` as a string, for example `80433022`. If you only have a BV ID, convert it first with [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).
- For the next page, send the `cursor` parameter. The response shows `data.cursor.pagination_reply.next_offset` and a `cursor` string on each comment. Stop when `data.cursor.is_end` is `true`.
- Each comment has `oid` equal to the video `aid`, `parent` and `root` set to `0` for top-level comments, and `rcount` for the number of replies. To read replies to a comment, use [Bilibili Comment Replies](/apis/bilibili/web/comment-reply).
- `data.data.top_replies` is an empty list in this response, so pinned comments are not always present.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/video-comment.json`](../../../catalog/models/bilibili/video-comment.json) · Store page: https://www.sandbase.ai/model/bilibili/video-comment
