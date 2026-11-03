# Xiaohongshu Hot Search API: pricing, parameters and code examples

`xiaohongshu/hot-search` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Search Xiaohongshu (RedNote) hot-content entries with optional keyword, content-category path, pagination, ranking metric, and time-range controls.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/hot-search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/hot-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/hot-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/hot-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `nd` | string |  | Time range in days. one of: `DAY_3`, `DAY_7`, `DAY_14`, `DAY_30`; default `"DAY_7"` |
| `orderBy` | string |  | Sort metric for the result set. one of: `premium_imp_num`, `premium_good_read_rate`, `premium_read_num`, `premium_engage_num`, `premium_engage_rate`, `premium_like_num`, `premium_fav_num`, `premium_cmt_num`; default `"premium_imp_num"` |
| `pageNum` | integer |  | Page number for pagination. default `1` |
| `searchWord` | string |  | Search keyword.  |
| `noteContentCategory` | string |  | Content category filter. Pass one complete Pugongying category path joined with # separators. You may pass a parent path or append one listed child with another #. Only one path is accepted. Available values: Content…  |

## Details

Returns a ranked list of hot Xiaohongshu (RedNote) notes with engagement counts, cover images and author details. All inputs are optional. You can filter by keyword, content or industry category, time window and ranking metric.

### Use cases

- Find the top notes in a category such as beauty or pets over the last 3 to 30 days.
- Rank notes by likes, favorites, comments or impressions to spot what drives engagement in a niche.
- Collect authors of fast-rising notes and their follower counts to build a creator shortlist.
- Check which notes carry ad labels by reading `isAdNote` across a keyword's results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `nd` | string | No | Time range in days. |
| `noteContentCategory` | string | No | Content category filter. Pass one complete Pugongying category path joined with # separators. You may pass a parent path or append one listed child with another #. Only one path is accepted. Available values: Content cat |
| `orderBy` | string | No | Sort metric for the result set. |
| `pageNum` | integer | No | Page number for pagination. |
| `searchWord` | string | No | Search keyword. |

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
        "fansNum": 567281,
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
| `noteList[].noteInfo.noteId` | ID of the note. Use it to look up the full note or its comments. |
| `noteList[].noteInfo.likeNum / favNum / cmtNum` | Like, favorite and comment counts for the note. |
| `noteList[].noteInfo.isAdNote` | Ad flag for the note. The sample values are `0`. |
| `noteList[].noteInfo.noteImages[].imageUrl` | URL of an image in the note. |
| `noteList[].noteInfo.noteImages[].imageWidth / imageHeight` | Pixel size of that image. |
| `noteList[].userInfo.userId` | ID of the author. |
| `noteList[].userInfo.nickName` | Display name of the author. |
| `noteList[].userInfo.fansNum` | Follower count of the author. |
| `pageInfoDto.pageNum / pageSize` | Current page number and the number of entries per page. |
| `total` | Total number of matching entries. The same value appears in `pageInfoDto.total`. |

### Notes

- Send `pageNum` to move through pages. The sample shows `pageSize` of `10` and `total` of `100`.
- `pageInfoDto.totalPage` returned `0` in the sample, so work out the page count from `total` and `pageSize`.
- Pass `noteContentCategory` as one `#`-joined path, such as `内容类目#美妆#整体妆容`. Only one path is accepted.
- Take `noteId` to [Xiaohongshu Note Details](/apis/xiaohongshu/note-detail) or [Xiaohongshu Note Comments](/apis/xiaohongshu/note-comment) for more data on a note.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/hot-search.json`](../../../catalog/models/xiaohongshu/hot-search.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/hot-search
