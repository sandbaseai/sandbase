# Xiaohongshu (RED) Homepage Feed API: pricing, parameters and code examples

`xiaohongshu/web-v3/homefeed` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves recommended notes from the Xiaohongshu homepage feed. Supports filtering by category channel, restricting results to image notes, and paginating via cursor score.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/homefeed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/homefeed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/homefeed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/homefeed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/homefeed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Number of results, max 40 default `20`; range –40 |
| `category` | string |  | Category channel ID default `"homefeed_recommend"` |
| `cursor_score` | string |  | Pagination cursor default `""` |
| `need_filter_image` | boolean |  | Image notes only default `false` |

## Details

Returns a page of recommended notes from the Xiaohongshu homepage feed. All input parameters are optional, so an empty request returns the default `homefeed_recommend` channel with 20 notes.

### Use cases

- Sample what the homepage recommends to study which topics and formats get surfaced.
- Collect note IDs and `xsec_token` values to fetch full note details afterward.
- Compare `liked_count` across video and image notes to see which format draws more likes in the feed.
- Pull image-only notes with `need_filter_image` for building a visual inspiration set.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/homefeed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Category channel ID |
| `cursor_score` | string | No | Pagination cursor |
| `need_filter_image` | boolean | No | Image notes only |
| `num` | integer | No | Number of results, max 40 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor_score": "seo_homefeed_20261031_19",
    "items": [
      {
        "id": "6ad817e6000000002403ce45",
        "ignore": false,
        "model_type": "note",
        "note_card": {
          "cover": {
            "file_id": "",
            "height": 1920,
            "info_list": [
              {
                "image_scene": "WB_PRV",
                "url": "http://sns-web-i10.rednotecdn.com/202611031547/b242cb6396e334c65c2b748fe75b9e09/…"
              }
            ],
            "url": "",
            "url_default": "http://sns-web-i10.rednotecdn.com/202611031547/af943230633f8f3511e8268ad03a65de/…",
            "url_pre": "http://sns-web-i10.rednotecdn.com/202611031547/b242cb6396e334c65c2b748fe75b9e09/…",
            "width": 960
          },
          "display_title": "怒扒pv20遍还原未央城妙妙猫",
          "interact_info": {
            "liked": false,
            "liked_count": "4442"
          },
          "type": "video",
          "user": {
            "avatar": "https://sns-avatar-qc.rednotecdn.com/avatar/1040g2jo322g7jfr27u604a0vmckkdhvqd4u…",
            "nick_name": "纳兰凤鸣",
            "nickname": "纳兰凤鸣",
            "user_id": "5a636946e8ac2b756187c7fa",
            "xsec_token": "ABODvCtL…"
          },
          "video": {
            "capa": {
              "duration": 22
            }
          }
        },
        "xsec_token": "ABflsL_F…"
      }
    ]
  },
  "msg": "成功",
  "ok": true,
  "status": 200,
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | ID of the note. Use it with the note detail APIs. |
| `data.items[].xsec_token` | Security token for the note. Pass it along with the note ID when requesting note details. |
| `data.items[].note_card.display_title` | Title shown on the note card. |
| `data.items[].note_card.type` | Note format. The response shows `video` and `normal` as values. |
| `data.items[].note_card.interact_info.liked_count` | Number of likes on the note, returned as a string. |
| `data.items[].note_card.cover.url_default / data.items[].note_card.cover.url_pre` | Cover image URLs. `url_default` is the standard version and `url_pre` is the preview version. |
| `data.items[].note_card.cover.width / data.items[].note_card.cover.height` | Cover image dimensions. |
| `data.items[].note_card.user.user_id` | ID of the note author. |
| `data.items[].note_card.user.nickname / data.items[].note_card.user.avatar` | Display name and avatar URL of the author. |
| `data.items[].note_card.video.capa.duration` | Length of the video. Only present on video notes. |
| `data.cursor_score` | Cursor value to send as `cursor_score` to request the next page. |

### Notes

- Send `data.cursor_score` from the response as `cursor_score` in the next request to page forward. `num` accepts up to 40.
- Call [Xiaohongshu (RED) Homepage Categories](/apis/xiaohongshu/web-v3/homefeed-categories) to find valid `category` channel IDs.
- Pass an item's `id` and `xsec_token` to [Xiaohongshu (RED) Web Note Details](/apis/xiaohongshu/web-v3/note-detail) to get the full note.
- Each author has their own `xsec_token` under `note_card.user`, separate from the note-level `xsec_token`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Homepage Categories](/apis/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Web Note Details](/apis/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.
- [Xiaohongshu (RED) Search Suggestions](/apis/xiaohongshu/web-v3/search-suggest): Returns search query suggestions and autocomplete terms from Xiaohongshu (RED).

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/homefeed.json`](../../../../catalog/models/xiaohongshu/web-v3/homefeed.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/homefeed
