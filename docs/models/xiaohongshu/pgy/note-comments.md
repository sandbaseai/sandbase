# Xiaohongshu PGY note featured comments API: pricing, parameters and code examples

`xiaohongshu/pgy/note-comments` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get PGY note featured comments on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/note-comments", "note_id": "6a20edfa0000000021020951"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/note-comments', {'note_id': '6a20edfa0000000021020951'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/note-comments", {
  "note_id": "6a20edfa0000000021020951"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/note-comments", sandbase.Params{
	"note_id": "6a20edfa0000000021020951",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/note-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string | yes | Note ID  |

## Details

Returns the featured comments on a Xiaohongshu note as listed in the PGY platform. Each item holds a top-level comment, its replies, and the profiles of users who took part. The only input is `note_id`.

### Use cases

- Read the featured comments on a sponsored note to check how the audience reacts to a creator's post.
- Collect reply threads under a note to review the tone of the conversation before a brand partnership.
- Export commenter nicknames and avatars to see which accounts engage with a note.
- Save comment text and timestamps for a note to compare discussion across several campaign posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/note-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "6a20edfa0000000021020951"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | Yes | Note ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "comment": {
        "atUsers": null,
        "content": "哈哈哈哈是很抽象了",
        "createTime": "2026-06-04 16:45",
        "enabled": true,
        "id": 426189652624445299,
        "idStr": "426189652624445299",
        "likeCount": 0,
        "noteId": 282074133146503505
      },
      "createTime": 1780562724000,
      "l1L2Comments": [
        {
          "atUsers": null,
          "content": "[大笑R]",
          "createTime": "2026-06-04 16:58",
          "enabled": true,
          "id": 426189665996270140,
          "idStr": "426189665996270140",
          "likeCount": 0,
          "noteId": 282074133146503505
        }
      ],
      "updateTime": 1780563520000,
      "userMap": {
        "154079314044039259": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hgr2d32k20048r6a7ed9c2rtq5ln80…",
          "userId": "5823dcd46a6a6932625eb05b",
          "userNickName": "猫尾纱"
        },
        "206148394384023427": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31el0tfrrle6g5n32rtd4dns3332hv88…",
          "userId": "5c62df5a000000001102df83",
          "userNickName": "杭州哈哈哈"
        },
        "206152431183730181": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hpod1vijs705n36hcv4k5g5f8fn40g…",
          "userId": "5c668b3e0000000012021605",
          "userNickName": "一颗白菜"
        },
        "207686035407138026": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/61d9594d0000000010006cea.jpg?imageView2/…",
          "userId": "61d9594d0000000010006cea",
          "userNickName": "韩国小怡子"
        },
        "207796091125561765": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31sqch5lc5c0g5ohte6ik1ud5dgbbq9g…",
          "userId": "623d71a5000000001000f9a5",
          "userNickName": "小Yang又困la💤"
        },
        "208971837144499622": {
          "gender": "FEMALE",
          "imageUrl": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31eus34uima005pjaotcgu1d6agk6jhg…",
          "userId": "666ac75900000000030305a6",
          "userNickName": "一个大贤贤"
        }
      }
    }
  ],
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].comment.content` | Text of the top-level featured comment. Emoji codes such as `[大笑R]` appear inline as text. |
| `data[].comment.createTime` | Time the comment was posted, as a formatted string like `2026-06-04 16:45`. |
| `data[].comment.id / data[].comment.idStr` | Comment ID as a number and as a string. Use `idStr` to avoid precision loss in some JSON parsers. |
| `data[].comment.likeCount` | Number of likes on the top-level comment. |
| `data[].comment.noteId` | Internal numeric ID of the note the comment belongs to. |
| `data[].l1L2Comments[]` | Replies attached to the featured comment. Each reply has `content`, `createTime`, `id`, `idStr`, `likeCount` and `noteId`. |
| `data[].createTime / data[].updateTime` | Millisecond timestamps for the featured comment entry and its last update. |
| `data[].userMap` | Object of user profiles keyed by an internal numeric key. Each profile has `userId`, `userNickName`, `gender` and `imageUrl` (avatar). |

### Notes

- `note_id` is the 24-character note ID, for example `6a20edfa0000000021020951`. This differs from the numeric `comment.noteId` in the response.
- The `userMap` object is repeated in every item and contains the same users. Comments do not name their author directly in the visible fields, so match users by reading `userMap` for the whole item.
- For the note's own metrics, call [Xiaohongshu (RED) PGY Note Detail](/apis/xiaohongshu/pgy/note-detail).
- To read all public comments on a note, use [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/note-comments.json`](../../../../catalog/models/xiaohongshu/pgy/note-comments.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/note-comments
