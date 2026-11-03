# Xiaohongshu (RED) Video Note Detail API: pricing, parameters and code examples

`xiaohongshu/app-v2/video-note-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a video note on Xiaohongshu (RED) using an identifier or a share link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/video-note-detail", "note_id": "6a65b1e300000000110100ff"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/video-note-detail', {'note_id': '6a65b1e300000000110100ff'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/video-note-detail", {
  "note_id": "6a65b1e300000000110100ff"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/video-note-detail", sandbase.Params{
	"note_id": "6a65b1e300000000110100ff",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/video-note-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `note_id` | string |  | Note ID, e.g. "697c0eee000000000a03c308" default `""` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |

## Details

Returns metadata for a Xiaohongshu (RED) note. The response includes the note text, like, collect, comment and share counts, hashtags, and the poster's IP location. Pass a `note_id` or a `share_text` sharing link.

### Use cases

- Track `liked_count`, `collected_count` and `comments_count` for a specific note over time.
- Resolve a copied `xhslink.com` sharing link into a note ID and its description text.
- Collect the hashtags a note uses to study topic targeting.
- Check whether the author allows video downloads before building a save workflow.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/video-note-detail" \
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
      "api_upgrade": -1,
      "ats": [],
      "auto_slide_down": 0,
      "cny_red_envelope_note": false,
      "collected": false,
      "collected_count": 4265,
      "comment_prompt_config": {
        "forbidden_cmt_type": 0,
        "placeholder_long": "Share your thoughts...",
        "placeholder_short": "Say something"
      },
      "comments_count": 192,
      "content_trans_info": {
        "strategy": 9
      },
      "cooperate_binds": [],
      "countdown": 0,
      "cursor_score": ""
    }
  ],
  "debug_id": "b8839549",
  "debug_info": "gAAAAABq6ZFwNXXpY98vjWMdMcOQmI3mOvj3Z-kVpz7lLOndi5fAt5TadFbeaEcOiejRrPVQOZ8YBdaZ…",
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Note ID. Use it to look up comments or the note itself again. |
| `data[].desc` | Note title and body text. It can include inline hashtags such as `#巴斯克[话题]`. |
| `data[].liked_count / collected_count / comments_count` | Number of likes, collects and comments on the note. |
| `data[].interaction_info.share_count` | Number of times the note was shared. |
| `data[].interaction_info.nice_count` | Count of "nice" reactions on the note, separate from `liked_count`. |
| `data[].hash_tag[].name` | Name of a hashtag attached to the note. Each item also has an `id` and a `link` deeplink to the topic. |
| `data[].ip_location` | Location label shown for the note, such as `Guizhou` or `Singapore`. |
| `data[].images_list[]` | Cover or image entries with `fileid`, `height` and `index`. Some also have `origin_img` with the original `width` and `height`. |
| `data[].function_switch[]` | List of feature flags. Each has a `type` and an `enable` value. A `reason` appears when a feature is off, for example `video_download`. |
| `data[].native_voice_info.url` | Link to the audio file used by the note. `sound_id` identifies the sound and `use_count` shows how often it was used. |

### Notes

- `note_id` and `share_text` are both optional in the schema. Send at least one. The `note_id` is a 24-character hex string such as `697c0eee000000000a03c308`.
- `share_text` accepts app and web sharing links, for example `http://xhslink.com/o/8GqargIxrko`.
- `data` is a list. In this sample it holds the requested note first, followed by other notes with different `id` values. Match on `id` to find your note.
- To read the comments of a note, call [Xiaohongshu (RED) Note Comments](/apis/xiaohongshu/app-v2/note-comments).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/video-note-detail.json`](../../../../catalog/models/xiaohongshu/app-v2/video-note-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/video-note-detail
