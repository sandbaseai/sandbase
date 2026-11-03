# Xiaohongshu PGY blogger note cases v2 (cross-platform) API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-notes-v2` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Get PGY blogger note cases v2 (cross-platform) on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-notes-v2", "user_id": "5c668b3e0000000012021605"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-notes-v2', {'user_id': '5c668b3e0000000012021605'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-notes-v2", {
  "user_id": "5c668b3e0000000012021605"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-notes-v2", sandbase.Params{
	"user_id": "5c668b3e0000000012021605",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-notes-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `note_type` | integer |  | Note type one of: `0`, `1`, `2`; default `0` |
| `page_size` | integer |  | Page size, 1-8 (fixed at 8 on PGY web) default `8` |
| `order_type` | integer |  | Sort one of: `1`, `2`, `3`; default `1` |
| `page_number` | integer |  | Page number, from 1 default `1` |

## Details

Returns a paged list of note cases for one blogger on Xiaohongshu's PGY (Pugongying) creator platform. Each item has note metrics, a cover image URL and a short blogger summary. The only required input is the blogger's `user_id`.

### Use cases

- Review a blogger's past notes with impressions and engagement before you pick them for a campaign.
- Separate sponsored notes from organic ones using `noteInfo.isAdNote` and `noteInfo.cooperNote`.
- Compare engagement against impressions across a blogger's notes to spot the posts that did best.
- Pull the blogger's content tags and follower count next to each note to build a creator shortlist.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-notes-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5c668b3e0000000012021605", "page_number": 1, "page_size": 8, "note_type": 0, "order_type": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `note_type` | integer | No | Note type |
| `order_type` | integer | No | Sort |
| `page_number` | integer | No | Page number, from 1 |
| `page_size` | integer | No | Page size, 1-8 (fixed at 8 on PGY web) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "highlightWords": [
      "白菜"
    ],
    "noteList": [
      {
        "brandInfo": null,
        "noteInfo": {
          "content": null,
          "cooperNote": 0,
          "engageNum": 154,
          "favNum": 58,
          "imageUrl": "http://ci.xiaohongshu.com/1040g2sg32701l0ef70705n36hcv4k5g5ti3p138?imageView2/2/…",
          "impNum": 2249,
          "isAdNote": 0,
          "noteId": "6ae5be8f000000000e036b30"
        },
        "userInfo": {
          "advertiserId": null,
          "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31hpod1vijs705n36hcv4k5g5f8fn40g…",
          "clickMidNum": 1050,
          "contentTags": [
            {
              "taxonomy1Tag": "美食",
              "taxonomy2Tags": [
                "美食探店"
              ]
            }
          ],
          "cooperType": 1,
          "currentLevel": 2,
          "fansNum": 10177,
          "featureTags": [
            "探店"
          ]
        }
      }
    ],
    "total": 43,
    "trackId": null
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.noteList[].noteInfo.noteId` | ID of the note. Use it to look up the note in other note APIs. |
| `data.noteList[].noteInfo.impNum` | Impression count for the note. |
| `data.noteList[].noteInfo.engageNum / data.noteList[].noteInfo.favNum` | Engagement count and favorite count for the note. |
| `data.noteList[].noteInfo.isAdNote / data.noteList[].noteInfo.cooperNote` | Flags that mark whether the note is an ad or a cooperation note. The sample shows `0` for both. |
| `data.noteList[].noteInfo.imageUrl` | URL of the note's cover image. |
| `data.noteList[].userInfo.fansNum` | Follower count of the blogger. |
| `data.noteList[].userInfo.currentLevel / data.noteList[].userInfo.cooperType` | Blogger level value and cooperation type code, as returned by PGY. |
| `data.noteList[].userInfo.contentTags[].taxonomy1Tag` | Top-level content category of the blogger. The matching `taxonomy2Tags` list holds the sub-categories. |
| `data.noteList[].userInfo.featureTags` | Short style tags that describe the blogger. |
| `data.total` | Total number of note cases for this blogger across all pages. |

### Notes

- Get `user_id` from a blogger search such as [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list).
- Page with `page_number` (starts at 1) and `page_size` (1 to 8). Compare `data.total` with the number of items you have fetched to know when to stop.
- `note_type` accepts `0`, `1` or `2`, and `order_type` accepts `1`, `2` or `3`. The defaults are `0` and `1`.
- For the blogger's full note list, see [Xiaohongshu (RED) PGY Blogger Notes](/apis/xiaohongshu/pgy/blogger-notes).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-notes-v2.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-notes-v2.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-notes-v2
