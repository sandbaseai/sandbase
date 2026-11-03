# Xiaohongshu (RED) Image Note Details API: pricing, parameters and code examples

`xiaohongshu/app-v2/image-note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns detailed information for a Xiaohongshu image note. Queries accept a specific note identifier or a post sharing link from the app or web interface.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/image-note-detail", "note_id": "6ab0d3640000000035013990"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/image-note-detail', {'note_id': '6ab0d3640000000035013990'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/image-note-detail", {
  "note_id": "6ab0d3640000000035013990"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/image-note-detail", sandbase.Params{
	"note_id": "6ab0d3640000000035013990",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/image-note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string |  | Note ID, e.g. "697c0eee000000000a03c308" default `""` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |

## Details

Returns details for one Xiaohongshu (RED) image note, including engagement counts and author info. Send either a `note_id` or a `share_text` sharing link from the app or web.

### Use cases

- Read the save and comment counts of a single image note.
- Resolve a shared `xhslink.com` link to the note and its author.
- Identify the author of a note by name, ID and avatar.
- Check whether a note is saved or followed by the current account state shown in the response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/image-note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "697c0eee000000000a03c308", "share_text": "http://xhslink.com/o/8GqargIxrko"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `note_id` | string | No | Note ID, e.g. "697c0eee000000000a03c308" |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "comment_list": [],
      "model_type": "note",
      "note_list": [
        {
          "api_upgrade": -1,
          "ats": [],
          "biz_map": {},
          "collected": false,
          "collected_count": 4265,
          "comment_prompt_config": {
            "forbidden_cmt_type": 0,
            "placeholder_long": "Drop a comment...",
            "placeholder_short": "Say something"
          },
          "comments_count": 192,
          "content_trans_info": {
            "strategy": 9
          }
        }
      ],
      "track_id": "",
      "user": {
        "followed": false,
        "fstatus": "none",
        "group_id": "5d0b475af5a2636ef12b14c1",
        "id": "5efc6e660000000001006da1",
        "image": "https://sns-avatar-qc.rednotecdn.com/avatar/5f852121e2dbee0001dbb521.jpg?imageVi…",
        "level": {
          "image": ""
        },
        "name": "一条",
        "nickname": "一条"
      }
    }
  ],
  "debug_id": "737c3716",
  "debug_info": "gAAAAABq6ZFna0Zrnh34AKYVd8Awpg1s_azbSgNH1xYTM3B2A_rqbgPBWihik_80yhtEhYnpvZBpiNVi…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].note_list[].collected_count` | Number of times users saved the note. |
| `data[].note_list[].comments_count` | Number of comments on the note. |
| `data[].note_list[].collected` | Whether the note is saved by the viewing account. The sample value is `false`. |
| `data[].note_list[].comment_prompt_config.placeholder_long / data[].note_list[].comment_prompt_config.placeholder_short` | Text shown in the comment box of the app, in a long and a short form. |
| `data[].model_type` | Type of the returned item. The sample value is `note`. |
| `data[].user.id` | ID of the note author. |
| `data[].user.name / data[].user.nickname` | Display name of the author. |
| `data[].user.image` | URL of the author's avatar image. |
| `data[].user.followed / data[].user.fstatus` | Follow state between the viewing account and the author. The sample shows `false` and `none`. |
| `success / msg` | Whether the call worked, and a status message. |

### Notes

- Send `note_id` or `share_text`. The example request sends both, and either one identifies the note.
- The note ID in the example is a 24-character hex string, such as `697c0eee000000000a03c308`.
- The response data is a list. The note details sit in `data[].note_list[]`, and the author sits in `data[].user`.
- To read the comments of a note, call [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments). The `comment_list` field in this response was empty.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments): Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/image-note-detail.json`](../../../../catalog/models/xiaohongshu/app-v2/image-note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/image-note-detail
