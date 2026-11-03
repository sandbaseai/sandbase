# Xiaohongshu (RED) User Posted Notes API: pricing, parameters and code examples

`xiaohongshu/app-v2/user-posted-notes` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves a list of notes posted by a specific Xiaohongshu user with cursor pagination. Query by providing a user identifier or a shared post link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/user-posted-notes", "user_id": "6673f0820000000007005d06"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/user-posted-notes', {'user_id': '6673f0820000000007005d06'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/user-posted-notes", {
  "user_id": "6673f0820000000007005d06"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/user-posted-notes", sandbase.Params{
	"user_id": "6673f0820000000007005d06",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/user-posted-notes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page  |
| `user_id` | string |  | User ID, e.g. "61b46d790000000010008153"  |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link)  |

## Details

Returns a page of notes posted by one Xiaohongshu (RED) user. Each note includes its title, text, engagement counts, images or video streams, and author details. Pass either `user_id` or a shared profile link in `share_text`.

### Use cases

- Build a posting history for a creator, including note type, publish date and engagement counts.
- Compare `likes`, `collected_count` and `comments_count` across a creator's notes to see which posts did best.
- Download cover images and video stream URLs for notes from a given account.
- Spot pinned notes with `sticky` and separate them from recent posts when tracking a profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/user-posted-notes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "61b46d790000000010008153", "share_text": "http://xhslink.com/o/8GqargIxrko"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |
| `user_id` | string | No | User ID, e.g. "61b46d790000000010008153" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
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
        "collected_count": 1186,
        "comments_count": 887,
        "create_time": 1756598549,
        "cursor": "68b39115000000001c037dad",
        "desc": "作为职业运动员，我们一直都知道“退休”就在不远处。过去的15年职业生涯，我明确的知道有一天我会需要离开，但现在真的到了要和篮球说再见的时候，这仍然是我这辈子做过…",
        "display_title": "是时候说再见了❤️",
        "guide_context": "{\"show_goods_c2c\":false}",
        "has_music": false,
        "id": "68b39115000000001c037dad",
        "images_list": [
          {
            "fileid": "1040g00831lr18klv50005odkdlsk10ajcajkq5g",
            "height": 1440,
            "original": "",
            "trace_id": "1040g00831lr18klv50005odkdlsk10ajcajkq5g",
            "url": "https://sns-i11.rednotecdn.com/1040g00831lr18klv50005odkdlsk10ajcajkq5g?imageVie…",
            "url_size_large": "https://sns-i11.rednotecdn.com/1040g00831lr18klv50005odkdlsk10ajcajkq5g?imageVie…",
            "width": 1080
          }
        ]
      }
    ],
    "tags": []
  },
  "debug_id": "edd83f15",
  "debug_info": "gAAAAABq6ZFvM1UIsoIPWDCov4Adm9KgR0lO1JwORkWqFOeuccNww-8jdEuh7VG-dcmYT3c6pgfdR_no…",
  "msg": "success",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.notes[].id` | ID of the note. It matches the `cursor` value on the same note. |
| `data.notes[].title / data.notes[].display_title` | Title of the note as shown to readers. |
| `data.notes[].desc` | Body text of the note, including hashtags. |
| `data.notes[].type` | Note format. The response shows `video` and `normal` (image note). |
| `data.notes[].likes / data.notes[].collected_count / data.notes[].comments_count / data.notes[].share_count` | Engagement counts for the note: likes, collects, comments and shares. |
| `data.notes[].create_time` | Publish time of the note as a Unix timestamp in seconds. |
| `data.notes[].time_desc` | Display text for the publish time. It can be a date such as `2025-08-30` or a relative value such as `2d ago`. |
| `data.notes[].sticky` | `true` when the note is pinned to the top of the profile. |
| `data.notes[].images_list[].url_size_large` | Link to the large version of an image in the note. `width` and `height` give its size. |
| `data.notes[].video_info_v2.media.stream` | Video streams by codec (`h264`, `h265`). Each entry has `avg_bitrate`, `duration` and `backup_urls`. Only video notes have this field. |
| `data.notes[].user.nickname / data.notes[].user.userid` | Display name and ID of the note author. |
| `data.has_more` | `true` when more notes are available on a later page. |

### Notes

- Send `user_id` or `share_text`. Leave `cursor` empty on the first request.
- To get the next page, pass the `cursor` of the last note in `data.notes` while `data.has_more` is `true`.
- Use the note `id` with [Xiaohongshu (RED) Video Note Detail](/apis/xiaohongshu/app-v2/video-note-detail) or [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail) to get the full note.
- Call [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments) to read the comments on a note.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/user-posted-notes.json`](../../../../catalog/models/xiaohongshu/app-v2/user-posted-notes.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/user-posted-notes
