# Bilibili Comment Replies API: pricing, parameters and code examples

`bilibili/web/comment-reply` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns replies to a specific comment on a Bilibili video by video ID and comment ID. Supports pagination to browse threaded discussion replies.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/comment-reply", "bv_id": "BV1dFad6aEz9", "rpid": "237108091664"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/comment-reply', {'bv_id': 'BV1dFad6aEz9', 'rpid': '237108091664'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/comment-reply", {
  "bv_id": "BV1dFad6aEz9",
  "rpid": "237108091664"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/comment-reply", sandbase.Params{
	"bv_id": "BV1dFad6aEz9",
	"rpid": "237108091664",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/comment-reply` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number  |
| `rpid` | string | yes | Reply id  |
| `bv_id` | string | yes | Video id  |

## Details

List the replies under one Bilibili comment (a comment thread), with each reply's text, author, likes and time. You need the video's BV ID and the root comment's `rpid`.

### Use cases

- Read full discussion threads, not only top-level comments.
- Collect replies for sentiment or community analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/comment-reply" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1dFad6aEz9", "rpid": "237108091664"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |
| `rpid` | string | Yes | Reply id |
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "config": {
      "read_only": false,
      "show_up_flag": false,
      "showtopic": 0
    },
    "control": {
      "answer_guide_android_url": "https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=6",
      "answer_guide_icon_url": "http://i0.hdslb.com/bfs/emote/96940d16602cacbbac796245b7bb99fa9b5c970c.png",
      "answer_guide_ios_url": "https://www.bilibili.com/h5/newbie/entry?navhide=1&re_src=12",
      "answer_guide_text": "需要升级成为lv2会员后才可以评论，先去答题转正吧！",
      "bg_text": "",
      "child_input_text": "下面我简单喵两句",
      "disable_jump_emote": false,
      "empty_page": null,
      "enable_charged": false,
      "enable_cm_biz_helper": false,
      "giveup_input_text": "不发没关系，请继续友善哦~",
      "input_disable": false
    },
    "page": {
      "count": 34,
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
          "message": "那是相当低，很多都是法不责众，真的恶心！"
        },
        "count": 0,
        "ctime": 1723373731,
        "dialog": 237107560304,
        "dialog_str": "237107560304",
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
    "root": {
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
    },
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
| `data.page` | `count` total replies, `num` page number, `size` replies per page (20). |
| `data.replies[]` | Replies: `rpid`, `content.message` (text), `like`, `ctime` (Unix seconds), `member` (author name, level, avatar) and `dialog` (the reply it answers). |
| `data.root` | The root comment itself. |

### Notes

- Get `rpid` values from the comments returned by [Bilibili Video Comments](/apis/bilibili/app/video-comments).
- Page through replies with `pn` (1, 2, ...) until `replies` is empty.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/comment-reply.json`](../../../../catalog/models/bilibili/web/comment-reply.json) · Store page: https://www.sandbase.ai/model/bilibili/web/comment-reply
