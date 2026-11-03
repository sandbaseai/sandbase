# Xiaohongshu User Notes API: pricing, parameters and code examples

`xiaohongshu/user-note-list` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a user's published public Xiaohongshu (RedNote) notes by user ID or supported profile URL, with lastCursor pagination. This endpoint does not create, upload or publish notes.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/user-note-list", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/user-note-list', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/user-note-list", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/user-note-list", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/user-note-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | A Xiaohongshu user ID or a profile URL containing /user/profile/.  |
| `lastCursor` | string |  | Omit on the first request. For the next page, pass the last note's cursor value from the previous response.  |

## Details

Returns a page of public notes published by one Xiaohongshu (RedNote) user. Each note includes its title, text, images or video details, engagement counts and author summary. The input is a user ID or a profile URL containing `/user/profile/`.

### Use cases

- Track what a brand or creator account posts and how each note performs.
- Build a content archive of an account's titles, text and image URLs.
- Compare `likes`, `collected_count` and `comments_count` across a creator's notes.
- Find which notes an account pins to the top of its profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/user-note-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | A Xiaohongshu user ID or a profile URL containing /user/profile/. |
| `lastCursor` | string | No | Omit on the first request. For the next page, pass the last note's cursor value from the previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
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
      "collected_count": 678,
      "comments_count": 817,
      "create_time": 1792745872,
      "cursor": "6adb2190000000002403bf87",
      "desc": "🎁各位小红薯粉丝们！本周福利来袭，100元喜茶礼品卡等你来拿！\n\t\n潇湘晨报小红书为感谢各位一路以来的厚爱和支持（疯狂比心），宝子们的奶茶我们来安排！本周专属粉…",
      "display_title": "粉丝福利：送100元喜茶礼品卡",
      "guide_context": "{\"show_goods_c2c\":false}",
      "has_music": false,
      "id": "6adb2190000000002403bf87",
      "images_list": [
        {
          "fileid": "spectrum/1040g0k0326lm1uo04c005p5oj0ol6up1hfehkuo",
          "height": 2400,
          "original": "",
          "trace_id": "spectrum/1040g0k0326lm1uo04c005p5oj0ol6up1hfehkuo",
          "url": "https://sns-i11-ae.rednotecdn.com/spectrum/1040g0k0326lm1uo04c005p5oj0ol6up1hfeh…",
          "url_size_large": "https://sns-i11-ae.rednotecdn.com/spectrum/1040g0k0326lm1uo04c005p5oj0ol6up1hfeh…",
          "width": 1440
        }
      ]
    }
  ],
  "tags": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `has_more` | `true` when more notes are available after this page. |
| `notes[].id / notes[].cursor` | The note ID and the cursor for that note. In the sample the two values are identical. Pass the last note's `cursor` as `lastCursor` to get the next page. |
| `notes[].title / notes[].display_title / notes[].desc` | The note headline and the note body text. `desc` can contain line breaks and emoji. |
| `notes[].type` | The note format. The sample shows `normal` for image notes and `video` for a video note. |
| `notes[].likes / notes[].collected_count / notes[].comments_count / notes[].share_count` | Engagement counts for the note. `view_count` is also present but shows `0` in the sample. |
| `notes[].create_time / notes[].last_update_time / notes[].time_desc` | `create_time` and `last_update_time` look like Unix timestamps in seconds, and `last_update_time` is `0` when the note was not updated. `time_desc` is a short display string such as `10-23` or `1分钟前`. |
| `notes[].sticky` | `true` when the note is pinned on the profile. |
| `notes[].images_list[].url_size_large / notes[].images_list[].width / notes[].images_list[].height` | The large image URL and its dimensions for each image in the note. |
| `notes[].video_info_v2.media.stream.h264[] / notes[].video_info_v2.capa.duration` | For video notes, the list of H.264 stream variants with bitrate and `backup_urls`, plus the video `duration`. H.265 variants appear under `h265`. |
| `notes[].user.userid / notes[].user.nickname` | The ID and display name of the note's author. |

### Notes

- Pass the `userId` from a profile URL path after `/user/profile/`, or send the full profile URL.
- For the first page, omit `lastCursor`. For the next page, send the `cursor` of the last note in `notes[]`, and keep going while `has_more` is `true`.
- Pinned notes (`sticky` is `true`) appear first in the sample, ahead of the other notes.
- To read a single note in full, call [Xiaohongshu Note Details](/apis/xiaohongshu/note-detail). To read its comments, call [Xiaohongshu Note Comments](/apis/xiaohongshu/note-comment).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/user-note-list.json`](../../../catalog/models/xiaohongshu/user-note-list.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/user-note-list
