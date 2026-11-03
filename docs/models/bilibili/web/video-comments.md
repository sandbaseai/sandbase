# Bilibili Video Comments (Web) API: pricing, parameters and code examples

`bilibili/web/video-comments` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment threads and reply metadata for a specific Bilibili video. Query by video ID with optional page numbering.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-comments", "bv_id": "BV13eam6MEmV", "pn": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-comments', {'bv_id': 'BV13eam6MEmV', 'pn': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-comments", {
  "bv_id": "BV13eam6MEmV",
  "pn": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-comments", sandbase.Params{
	"bv_id": "BV13eam6MEmV",
	"pn": 1,
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number default `1` |
| `bv_id` | string | yes | Video id  |

## Details

Returns one page of top-level comments for a Bilibili video, with a few preview replies under each comment. It needs the video's BV ID in `bv_id` and takes an optional page number in `pn`.

### Use cases

- Pull the most liked comments on a video to see what viewers react to.
- Track how many replies a comment thread has gathered by reading `rcount` on each comment.
- Collect comment text from several pages of a video for sentiment or topic analysis.
- Find the user IDs of active commenters, then look up their profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1M1421t7hT"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "assist": 0,
    "blacklist": 0,
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
      "child_input_text": "天青色等烟雨，评论区在等你",
      "disable_jump_emote": false,
      "empty_page": null,
      "enable_charged": false,
      "enable_cm_biz_helper": false,
      "giveup_input_text": "不发没关系，请继续友善哦~",
      "input_disable": false
    },
    "folder": {
      "has_folded": false,
      "is_folded": false,
      "rule": ""
    },
    "mode": 3,
    "page": {
      "acount": 2258,
      "count": 2258,
      "num": 1,
      "size": 20
    },
    "replies": [
      {
        "action": 0,
        "assist": 0,
        "attr": 0,
        "content": {
          "jump_url": {},
          "max_line": 6,
          "members": [],
          "message": "惩治谣言，任重道远啊。现在造谣的成本还是有点低"
        },
        "count": 47,
        "ctime": 1723373621,
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
    "support_mode": [
      2
    ],
    "top": null,
    "upper": {
      "mid": 19286458,
      "top": null,
      "vote": null
    },
    "vote": 0
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.page.count / data.page.acount` | Total number of comments on the video. |
| `data.page.num / data.page.size` | Current page number and the number of comments per page. |
| `data.replies[].content.message` | Text of the top-level comment. |
| `data.replies[].like` | Number of likes on the comment. |
| `data.replies[].rcount / data.replies[].count` | Reply counts for the comment. `rcount` matches the number in `reply_control.sub_reply_entry_text` (for example "共34条回复"). |
| `data.replies[].ctime` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.replies[].rpid_str / data.replies[].mid_str` | ID of the comment and ID of the user who wrote it, as strings. |
| `data.replies[].oid_str` | ID of the video the comment belongs to. This is the numeric ID, not the BV ID. |
| `data.replies[].member.avatar` | URL of the commenter's avatar image. |
| `data.replies[].replies[].content.message` | Text of a preview reply under the comment. Only a few replies appear here, not the full thread. |

### Notes

- Take `bv_id` from a Bilibili video URL. It starts with `BV`, for example `BV1M1421t7hT`.
- Send `pn` to page through comments. It starts at 1, and the response shows the current page in `data.page.num` and the page size in `data.page.size`.
- To read all replies under one comment, call [Bilibili Comment Replies](/apis/bilibili/web/comment-reply). Use the comment's `rpid_str` and the video's `oid_str`.
- To get the numeric video ID from a BV ID, call [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-comments.json`](../../../../catalog/models/bilibili/web/video-comments.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-comments
