# Xiaohongshu (RED) User Favorited Notes API: pricing, parameters and code examples

`xiaohongshu/app-v2/user-faved-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a paginated list of notes favorited by a specified Xiaohongshu (RED) user. Supports querying by user ID or profile share link, with cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-faved-notes", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-faved-notes', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-faved-notes", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-faved-notes", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-faved-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass last note_id from previous page for next page  |
| `user_id` | string |  | User ID, e.g. "5a8cf39111be10466d285d6b"  |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link)  |

## Details

Returns a page of notes that a Xiaohongshu (RED) user has favorited. Each note includes its title, text, images, engagement counts, author, and video details when the note is a video. Pass either `user_id` or a profile share link in `share_text`.

### Use cases

- Study which topics and creators a specific user saves most often.
- Collect the IDs and `xsec_token` values of favorited notes, then fetch full details for each one.
- Compare `likes` and `collected_count` across a user's favorites to see which kinds of posts draw saves.
- Page through a public favorites list to build a reading history of one account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-faved-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5a8cf39111be10466d285d6b", "share_text": "https://xhslink.com/a/EZ4M9TwMA6c3"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass last note_id from previous page for next page |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |
| `user_id` | string | No | User ID, e.g. "5a8cf39111be10466d285d6b" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": "6adc6b9e0000000025023fcf",
    "fallback": false,
    "has_more": true,
    "need_clean": true,
    "notes": [
      {
        "advanced_widgets_groups": {
          "groups": [
            {
              "fetch_types": [
                "guos_test"
              ],
              "mode": 1
            }
          ]
        },
        "ats": [],
        "collected_count": 43,
        "comments_count": 123,
        "create_time": 1793533275,
        "cursor_score": "6ae7255b000000001e014133",
        "desc": "🍚\n姐姐提议的居家万圣小聚\n5分钟搞定老农民妆造\n懒人友好🧑‍🤝‍🧑哈哈哈哈\n\t\n#万圣节拍照[话题]#",
        "display_title": "当你的万圣节任务是cos一些出其不意的",
        "id": "6ae7255b000000001e014133",
        "images_list": [
          {
            "fileid": "notes_pre_post/1040g3k83271dhedgma205o562cn0962uf1ik58g",
            "height": 1799,
            "index": 0,
            "latitude": 0,
            "longitude": 0,
            "original": "https://sns-i11.rednotecdn.com/notes_pre_post/1040g3k83271dhedgma205o562cn0962uf…",
            "trace_id": "notes_pre_post/1040g3k83271dhedgma205o562cn0962uf1ik58g",
            "url": "https://sns-i11.rednotecdn.com/notes_pre_post/1040g3k83271dhedgma205o562cn0962uf…"
          }
        ],
        "infavs": false,
        "inlikes": false
      }
    ]
  },
  "debug_id": "8b6df836",
  "debug_info": "gAAAAABq6ZFueMYwiAkZGc-YgvqgWFhh3Gwhnh28JadPeh-jnMCPe9lc5zapDVdpcg1o66eAT5nt0XvR…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.notes[]` | The list of favorited notes on this page. |
| `data.notes[].id` | The note ID. It matches `cursor_score` in these samples. |
| `data.notes[].title / data.notes[].display_title` | The note title as shown to readers. |
| `data.notes[].desc` | The note body text, including hashtags written as `#tag[话题]#`. |
| `data.notes[].type` | The note format. Values seen are `normal` for image notes and `video` for video notes. |
| `data.notes[].likes / data.notes[].collected_count / data.notes[].comments_count / data.notes[].share_count` | Counts of likes, saves, comments, and shares for the note. |
| `data.notes[].create_time / data.notes[].last_update_time` | Unix timestamps in seconds for when the note was created and last edited. `last_update_time` is `0` when the note was never updated. |
| `data.notes[].user.user_id / data.notes[].user.nickname` | The ID and display name of the author who posted the note, not the user whose favorites you requested. |
| `data.notes[].images_list[].url / data.notes[].images_list[].original` | Image links for the note. `url` is a smaller version and `original` is the large version. |
| `data.notes[].xsec_token` | A token attached to the note. Keep it with the note `id` for later note lookups. |
| `data.notes[].video_info_v2.capa.duration` | Video length for video notes. Only video notes include `video_info_v2`. |
| `data.has_more / data.cursor` | Whether another page exists, and the cursor value returned for paging. |

### Notes

- Leave `cursor` empty on the first call. For the next page, pass the `cursor` value from the previous response, or the last note `id` as the parameter description says.
- Keep calling while `data.has_more` is `true`.
- Send either `user_id` or `share_text`. The `user_id` is a 24-character hex string such as `5a8cf39111be10466d285d6b`.
- To get more detail on one note, call [Xiaohongshu (RED) Video Note Detail](/apis/xiaohongshu/app-v2/video-note-detail) or [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail). For the user's own posts, use [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-faved-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/user-faved-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-faved-notes
