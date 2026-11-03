# Xiaohongshu PGY content square leaderboards API: pricing, parameters and code examples

`xiaohongshu/pgy/content-square` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY content square leaderboards on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/content-square", "biz_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/content-square', {'biz_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/content-square", {
  "biz_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/content-square", sandbase.Params{
	"biz_type": 1,
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/content-square` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `fans` | object |  | Creator fans range, board 4 only  |
| `price` | object |  | Creator price, board 4 only  |
| `theme` | string |  | 4/5/7/Theme  |
| `biz_type` | integer | yes | Leaderboard one of: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |
| `category` | string |  | Board 1 only  |
| `industry` | string |  | 3/4/5/6/7/Industry, values differ per board  |
| `order_by` | string |  | Sort field, empty=board default  |
| `page_num` | integer |  | Page; each board has only 100 items default `1` |
| `note_type` | integer |  | Content type one of: `1`, `2` |
| `page_size` | integer |  | Page size, 1-34 default `34` |
| `placement` | integer |  | 3/5/7/Traffic placement one of: `1`, `2`, `3` |
| `date_range` | integer |  | 7/14/Date window in days one of: `3`, `7`, `14`, `30`; default `7` |
| `author_type` | integer |  | Board 4 only one of: `1`, `2` |
| `search_word` | string |  | Keyword, comma-separated for batch  |
| `content_type` | integer |  | Content source one of: `1`, `2`, `3`, `5`, `6`, `11`, `-1` |
| `sub_biz_type` | integer |  | Board 8 only one of: `1`, `2`, `3` |
| `marketing_target` | integer |  | Board 3 only one of: `3`, `8` |

## Details

Returns one page of a PGY content square leaderboard on Xiaohongshu. Each item is a note with its engagement counts, images and author. You choose the leaderboard with `biz_type` (1 to 8) and can narrow it with filters such as `date_range`, `category` and `industry`.

### Use cases

- Pull the top notes of a leaderboard to see which content is performing best this week.
- Compare `likeNum`, `favNum` and `cmtNum` across ranked notes to spot formats that draw saves and comments.
- Build a list of high-ranking authors with their follower counts to shortlist creators for outreach.
- Track how a board changes by calling it with `date_range` set to 3, 7, 14 or 30.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/content-square" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"biz_type": 1, "page_num": 1, "page_size": 20, "date_range": 7}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `biz_type` | integer | Yes | Leaderboard |
| `author_type` | integer | No | Board 4 only |
| `category` | string | No | Board 1 only |
| `content_type` | integer | No | Content source |
| `date_range` | integer | No | 7/14/Date window in days |
| `fans` | object | No | Creator fans range, board 4 only |
| `industry` | string | No | 3/4/5/6/7/Industry, values differ per board |
| `marketing_target` | integer | No | Board 3 only |
| `note_type` | integer | No | Content type |
| `order_by` | string | No | Sort field, empty=board default |
| `page_num` | integer | No | Page; each board has only 100 items |
| `page_size` | integer | No | Page size, 1-34 |
| `placement` | integer | No | 3/5/7/Traffic placement |
| `price` | object | No | Creator price, board 4 only |
| `search_word` | string | No | Keyword, comma-separated for batch |
| `sub_biz_type` | integer | No | Board 8 only |
| `theme` | string | No | 4/5/7/Theme |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
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
      "pageSize": 20,
      "total": 100,
      "totalPage": 0
    },
    "total": 100
  },
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.noteList[].noteInfo.noteId` | ID of the note. Use it to look up the note in other APIs. |
| `data.noteList[].noteInfo.likeNum / favNum / cmtNum` | Counts of likes, favorites and comments on the note. |
| `data.noteList[].noteInfo.isAdNote` | Flag for ad notes. The sample items show `0`. |
| `data.noteList[].noteInfo.noteImages[].imageUrl` | URL of an image in the note. |
| `data.noteList[].noteInfo.noteImages[].imageWidth / imageHeight` | Width and height of that image. |
| `data.noteList[].userInfo.userId` | ID of the author who posted the note. |
| `data.noteList[].userInfo.nickName` | Display name of the author. |
| `data.noteList[].userInfo.fansNum` | Follower count of the author. |
| `data.pageInfoDto.pageNum / pageSize` | Page number and page size of this response. |
| `data.total` | Total number of items on the board. The sample shows `100`. |

### Notes

- Set `page_num` and `page_size` to page through results. Each board holds only 100 items, and `page_size` accepts 1 to 34.
- Some filters apply to certain boards only: `category` to board 1, `author_type`, `price` and `fans` to board 4, `sub_biz_type` to board 8, `marketing_target` to board 3.
- Pass the `userId` to [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail) to get creator details.
- Pass the `noteId` to [Xiaohongshu (RED) PGY Note Detail](/apis/xiaohongshu/pgy/note-detail) to get details for one note.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/content-square.json`](../../../../catalog/models/xiaohongshu/pgy/content-square.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/content-square
