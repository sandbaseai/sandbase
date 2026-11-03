# Kuaishou Video Comments (App) API: pricing, parameters and code examples

`kuaishou/app/video-comment` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment records for a specified Kuaishou video, including author metadata and like counts. Supports pagination using a cursor.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/video-comment", "photo_id": "5193494945927590140"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/video-comment', {'photo_id': '5193494945927590140'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/video-comment", {
  "photo_id": "5193494945927590140"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/video-comment", sandbase.Params{
	"photo_id": "5193494945927590140",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pcursor` | string |  | 评论游标/Comment cursor  |
| `photo_id` | string | yes | 作品ID/Photo ID  |

## Details

Returns top-level comments for a Kuaishou video, plus a preview of replies under each comment. It needs the video's `photo_id`. Each comment includes author details, a like count and a timestamp.

### Use cases

- Collect the most-liked comments on a Kuaishou video to study audience reaction.
- Group commenters by `authorArea` to see which regions engage with a video.
- Track new comments on a video by comparing `timestamp` values across pages.
- Find comments with many replies and fetch the full reply thread for them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "5193494945927590140"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes |  |
| `pcursor` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "commentCount": 3053,
  "host-name": "public-bjx-c34-kce-node3496.idchb1az1.hb1.kwaidc.com",
  "pcursor": "V2#0b7e6e34-41ee-4c9f-b34d-c96048e72443#dph#30#938768612848_32",
  "result": 1,
  "rootComments": [
    {
      "attachments": [
        {
          "content": {
            "photoInfo": {
              "photoId": "149640945284",
              "photoSource": "COLLECTION_TAB",
              "photoType": 1,
              "serverExpTag": "",
              "userName": "及时止损"
            },
            "smallUrl": [
              {
                "cdn": "p66-plat.wsukwai.com",
                "url": "https://p66-plat.wsukwai.com/upic/2024/11/26/20/BMjAyNDExMjYyMDM5MTVfNTA0OTk1Njd…"
              }
            ]
          },
          "id": "149640945284",
          "layout": {
            "height": 0,
            "thumbHeight": 640,
            "thumbWidth": 360,
            "width": 0
          },
          "previewURL": "kwai://work/149640945284?disableSidebar=true&pageType=1&utm_source=feedCommentDe…",
          "type": "PHOTO"
        }
      ],
      "authorArea": "山东",
      "authorVerified": false,
      "author_id": 23458411,
      "author_liked": false,
      "author_name": "宝宝心里变态",
      "cashTags": {},
      "commentAuthorTags": [],
      "commentBottomTags": [],
      "comment_id": 938889241499,
      "content": "",
      "displaySubCommentCount": true
    }
  ],
  "subCommentsMap": {
    "938846333271": {
      "pcursor": "V1-1006-1-eyJwaG90b0lkIjoxNTI1Mjk4MzQyMTYsImNvbW1lbnRJZCI6OTM4ODQ2NDI1MDk3fQ==",
      "subComments": [
        {
          "authorArea": "广西",
          "authorVerified": false,
          "author_id": 514350277,
          "author_liked": false,
          "author_name": "ℳ̶̶̶̶♡̶҉释怀ℳᥫ",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "938889241499": {
      "pcursor": "V1-1006-1-eyJwaG90b0lkIjoxNTI1Mjk4MzQyMTYsImNvbW1lbnRJZCI6OTQ2NDM1NjE1NTY3fQ==",
      "subComments": [
        {
          "authorArea": "山西",
          "authorVerified": false,
          "author_id": 2037328243,
          "author_liked": false,
          "author_name": "略略略略略略",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "938911268848": {
      "pcursor": "V1-1006-1-eyJwaG90b0lkIjoxNTI1Mjk4MzQyMTYsImNvbW1lbnRJZCI6OTM4OTQxNjMzMDQ5fQ==",
      "subComments": [
        {
          "authorArea": "贵州",
          "authorVerified": false,
          "author_id": 2023087307,
          "author_liked": false,
          "author_name": "欲念风^",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "939054445981": {
      "pcursor": "no_more",
      "subComments": [
        {
          "authorArea": "浙江",
          "authorVerified": false,
          "author_id": 1089010476,
          "author_liked": false,
          "author_name": "黑无常！",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "939071729265": {
      "pcursor": "no_more",
      "subComments": [
        {
          "authorArea": "重庆",
          "authorVerified": false,
          "author_id": 268579944,
          "author_liked": false,
          "author_name": "重炮",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "940946335966": {
      "pcursor": "V1-1006-1-eyJwaG90b0lkIjoxNTI1Mjk4MzQyMTYsImNvbW1lbnRJZCI6OTQxODcwNDIyNzA4fQ==",
      "subComments": [
        {
          "authorArea": "山东",
          "authorVerified": false,
          "author_id": 2673361092,
          "author_liked": false,
          "author_name": "至高神",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "947100605905": {
      "pcursor": "no_more",
      "subComments": [
        {
          "authorArea": "广西",
          "authorVerified": false,
          "author_id": 759752785,
          "author_liked": false,
          "author_name": "持续攻速暴击",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "947331566664": {
      "pcursor": "no_more",
      "subComments": [
        {
          "authorArea": "浙江",
          "authorVerified": false,
          "author_id": 4576919076,
          "author_liked": false,
          "author_name": "快手用户1737179161502",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    },
    "964868751848": {
      "pcursor": "V1-1006-1-eyJwaG90b0lkIjoxNTI1Mjk4MzQyMTYsImNvbW1lbnRJZCI6OTc1MDQyODc5Njc2fQ==",
      "subComments": [
        {
          "authorArea": "安徽",
          "authorVerified": false,
          "author_id": 4433943584,
          "author_liked": false,
          "author_name": "看淡一切。",
          "cashTags": {},
          "commentAuthorTags": [],
          "commentBottomTags": []
        }
      ]
    }
  },
  "transparentPayload": "{\"kwaiShopItemCmtInjectCnt\":0,\"kwaiShopItemCmtInjectCursor\":0}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `commentCount` | Total number of comments on the video. |
| `pcursor` | Cursor for the next page of top-level comments. Send it back as the `pcursor` request parameter. |
| `rootComments[].comment_id` | ID of the top-level comment. It also appears as a key in `subCommentsMap`. |
| `rootComments[].content` | Text of the comment. It can be an empty string when the comment only has an attachment. |
| `rootComments[].likedCount / rootComments[].subCommentCount` | Number of likes on the comment and number of replies to it. |
| `rootComments[].author_id / rootComments[].author_name / rootComments[].authorArea` | ID, display name and region of the user who wrote the comment. |
| `rootComments[].time / rootComments[].timestamp` | Comment time as a text date and as a numeric timestamp. The numeric value looks like milliseconds since the Unix epoch. |
| `rootComments[].hot` | Whether the comment is flagged as hot. |
| `rootComments[].attachments[].type` | Type of media attached to the comment, such as `PHOTO`. The linked work is under `content.photoInfo`. |
| `subCommentsMap.<comment_id>.subComments[]` | Preview of replies for that top-level comment. Each entry has the same author fields as a root comment. |
| `subCommentsMap.<comment_id>.pcursor` | Cursor for more replies to that comment. The value `no_more` means there are no further replies. |

### Notes

- `photo_id` is the numeric ID of the video, for example `5193494945927590140`. Pass it as a string.
- For the next page of comments, send the returned `pcursor` together with the same `photo_id`.
- To read all replies under a comment, use [Kuaishou Video Sub Comments (App)](/apis/kuaishou/app/video-sub-comments) with the reply cursor.
- To look up the video itself, use [Kuaishou Video Details (V1)](/apis/kuaishou/app/one-video).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/video-comment.json`](../../../../catalog/models/kuaishou/app/video-comment.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/video-comment
