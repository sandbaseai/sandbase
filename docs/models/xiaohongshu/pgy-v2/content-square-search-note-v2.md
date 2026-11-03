# Xiaohongshu Pugongying Content Square Notes API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/content-square-search-note-v2` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Search Xiaohongshu Pugongying Content Square notes by keyword or browse all notes, with business-category, ranking, time-window, and page controls. Use it to discover high-performing campaign content.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/content-square-search-note-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/content-square-search-note-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/content-square-search-note-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/content-square-search-note-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/content-square-search-note-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `nd` | string |  | Time range in days. one of: `DAY_3`, `DAY_7`, `DAY_14`, `DAY_30`; default `"DAY_7"` |
| `bizType` | string |  | Business category. one of: `XIAOHONGSHU_HOT`, `PRODUCT_SEEDING`, `ECOMMERCE_PROMOTION`, `PUGONGYING_COOPERATION`, `LEAD_COLLECTION`, `ECOMMERCE_HOT`, `SEEDING_DIRECT`, `APP_PROMOTION`; default `"XIAOHONGSHU_HOT"` |
| `orderBy` | string |  | Ranking metric. one of: `premium_imp_num`, `premium_good_read_rate`, `premium_read_num`, `premium_engage_num`, `premium_engage_rate`, `premium_like_num`, `premium_fav_num`, `premium_cmt_num`; default `"premium_imp_num"` |
| `pageNum` | integer |  | Page number for results. default `1` |
| `searchWord` | string |  | Keyword for note search. Empty string searches all notes.  |

## Details

This API returns a page of notes from the Xiaohongshu Pugongying Content Square. Each result has note engagement counts, note images, and the author's profile summary. All inputs are optional. Send `searchWord` to filter by keyword, or leave it empty to browse all notes.

### Use cases

- Find the most liked or saved notes for a keyword to study what content works in a product category.
- Rank notes by a metric such as `premium_engage_num` over the last 7 or 30 days to spot campaign content that is gaining traction.
- Collect author `userId` values from top notes to build a list of creators to review.
- Compare note formats by checking image count and image size across top-ranked notes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/content-square-search-note-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bizType` | string | No | Business category. |
| `nd` | string | No | Time range in days. |
| `orderBy` | string | No | Ranking metric. |
| `pageNum` | integer | No | Page number for results. |
| `searchWord` | string | No | Keyword for note search. Empty string searches all notes. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "noteList": [
    {
      "noteInfo": {
        "bindType": 4,
        "bizType": 0,
        "cmtNum": 489,
        "favNum": 3285,
        "isAdNote": 0,
        "likeNum": 56359,
        "noteId": "6ae00b99000000001200a9f9",
        "noteImages": [
          {
            "imageHeight": 2400,
            "imageUrl": "http://ci.xiaohongshu.com/spectrum/1040g34o326qfkfqpl8105p5oj0ol6up1kacjbf8?imag…",
            "imageWidth": 1440
          }
        ]
      },
      "userInfo": {
        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31qobul3rgm005p5oj0ol6up1tu11gg8…",
        "currentLevel": 0,
        "fansNum": 567283,
        "nickName": "潇湘晨报",
        "userId": "64b898310000000014037b21",
        "userType": 1
      }
    }
  ],
  "pageInfoDto": {
    "pageNum": 1,
    "pageSize": 10,
    "total": 100,
    "totalPage": 0
  },
  "total": 100
}
```

### Response fields

| Field | Meaning |
|---|---|
| `noteList[].noteInfo.noteId` | ID of the note. Pass it to a note detail API for more data. |
| `noteList[].noteInfo.likeNum / favNum / cmtNum` | Like, favorite and comment counts for the note. |
| `noteList[].noteInfo.noteImages[].imageUrl` | URL of one image in the note. |
| `noteList[].noteInfo.noteImages[].imageWidth / imageHeight` | Width and height of that image. |
| `noteList[].noteInfo.isAdNote` | Ad flag for the note. The sample values are `0`. |
| `noteList[].userInfo.userId` | ID of the note's author. |
| `noteList[].userInfo.nickName` | Display name of the author. |
| `noteList[].userInfo.fansNum` | Follower count of the author. |
| `pageInfoDto.pageNum / pageSize` | Current page number and the number of notes per page. |
| `total` | Total number of matching notes reported for the query. |

### Notes

- Use `pageNum` to move through results. The sample response shows `pageSize` of `10`.
- `pageInfoDto.totalPage` returned `0` in the sample even though `total` was `100`, so rely on `total` and `pageSize` to work out the page count.
- Take `noteList[].noteInfo.noteId` to [Xiaohongshu Pugongying Note Details](/apis/xiaohongshu/pgy-v2/note-id-detail) for a single note.
- Take `noteList[].userInfo.userId` to [Xiaohongshu Pugongying Creator Profile](/apis/xiaohongshu/pgy-v2/blogger-user-id) to look at the author.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/content-square-search-note-v2.json`](../../../../catalog/models/xiaohongshu/pgy-v2/content-square-search-note-v2.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/content-square-search-note-v2
