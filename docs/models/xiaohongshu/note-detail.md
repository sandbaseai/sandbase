# Xiaohongshu Note Details API: pricing, parameters and code examples

`xiaohongshu/note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu (RedNote) details for a note identified by a note ID or supported explore URL. Use it to perform direct note lookup and content review from stored identifiers or shared explore links.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/note-detail", "noteId": "6ae00b99000000001200a9f9"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/note-detail', {'noteId': '6ae00b99000000001200a9f9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/note-detail", {
  "noteId": "6ae00b99000000001200a9f9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/note-detail", sandbase.Params{
	"noteId": "6ae00b99000000001200a9f9",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `noteId` | string | yes | A Xiaohongshu note ID or an explore URL containing /explore/.  |

## Details

Returns the details of one Xiaohongshu (RedNote) note: its text, hashtags, images, engagement counts, and author. It needs a note ID or an explore URL containing `/explore/` in the `noteId` parameter.

### Use cases

- Pull the text, hashtags, and images of a saved note ID to review its content.
- Track `liked_count`, `collected_count`, and `comments_count` for a note over repeated calls.
- Identify the author of a shared explore link and read the author's `red_id` and nickname.
- Check which topics and accounts a note tags through `hash_tag` and `ats`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/note-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6ae00b99000000001200a9f9"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | A Xiaohongshu note ID or an explore URL containing /explore/. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "comment_list": [],
    "model_type": "note",
    "note_list": [
      {
        "api_upgrade": -1,
        "ats": [
          {
            "followed": false,
            "id": "622f299f00000000100098c8",
            "level": {
              "image": ""
            },
            "name": "热点薯",
            "nickname": "热点薯",
            "red_official_verified": false,
            "red_official_verify_type": 0,
            "show_red_official_verify_icon": false
          }
        ],
        "biz_map": {},
        "co_produce_link": "xhsdiscover://post_new_note?source=%7B%22type%22%3A%22together_post%22%2C%22extr…",
        "collected": false,
        "collected_count": 3209,
        "comment_prompt_config": {
          "forbidden_cmt_type": 0,
          "placeholder_long": "有话要说，快来评论",
          "placeholder_short": "说点什么..."
        },
        "comments_count": 511,
        "content_trans_info": {
          "strategy": 10
        },
        "cooperate_binds": [],
        "countdown": 0,
        "desc": "10月27日，东鹏饮料集团发布关于终止与基利安·姆巴佩合作的声明：我司坚决反对、零容忍伤害民族感情的行为。即日起终止与基利安·姆巴佩全部合作。（财联社）#新闻[…"
      }
    ],
    "track_id": "",
    "user": {
      "followed": false,
      "fstatus": "none",
      "id": "64b898310000000014037b21",
      "image": "https://sns-avatar-qc-ae.rednotecdn.com/avatar/1040g2jo31qobul3rgm005p5oj0ol6up1…",
      "level": {
        "image": ""
      },
      "live": {
        "has_draw": false,
        "has_goods": false,
        "has_red_packet": false,
        "live_link": "xhsdiscover://live_audience?room_id=570525084055212707&note_id=6ae00b99000000001…",
        "live_status": 2,
        "room_id": "570525084055212707",
        "start_time": 1793690366000,
        "user_id": "64b898310000000014037b21"
      },
      "name": "潇湘晨报",
      "nickname": "潇湘晨报",
      "red_id": "63048342102",
      "red_official_verified": false,
      "red_official_verify_type": 0,
      "show_red_official_verify_icon": false
    }
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `note_list[].id` | ID of the note. It matches the `noteId` you sent. |
| `note_list[].desc` | Full note text, including the hashtags and @mentions written in it. |
| `note_list[].liked_count / collected_count / comments_count` | Number of likes, collects, and comments on the note. |
| `note_list[].hash_tag[].name` | Name of each hashtag topic on the note. `id` holds the topic ID. |
| `note_list[].ats[].nickname` | Nickname of each account mentioned in the note. `id` holds that account's user ID. |
| `note_list[].images_list[]` | One row per image. `fileid` identifies the image, `width` and `height` give its size, and `origin_img` holds the original size. |
| `note_list[].ip_location` | Location label shown for the note, such as a province name. |
| `note_list[].mini_program_info.webpage_url` | Web link to the note on xiaohongshu.com. |
| `user.nickname / user.red_id` | Display name and public RED ID of the note's author. |
| `user.id` | User ID of the author. `user.userid` holds the same value. |

### Notes

- The response is a JSON array. The note data sits in `note_list[]`, and the author sits in `user`.
- `comment_list` is empty in this response. Call [Xiaohongshu Note Comments](/apis/xiaohongshu/note-comment) to read the comments on a note.
- For notes that contain images or video, you can also try [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail) or [Xiaohongshu (RED) Video Note Detail](/apis/xiaohongshu/app-v2/video-note-detail).
- Use `user.id` with [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes) to list the author's other notes.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/note-detail.json`](../../../catalog/models/xiaohongshu/note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/note-detail
