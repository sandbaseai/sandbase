# Douyin Douplus User Posts API: pricing, parameters and code examples

`douyin/douplus/user-posts` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a concise list of homepage video posts for a specified Douyin user. Supports cursor-based pagination and custom result counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/user-posts", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/user-posts', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/user-posts", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/user-posts", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Page size, default 10  |
| `cursor` |  |  | Pagination cursor (string), "0" for first page, then pass the cursor from the previous response  |
| `sec_uid` | string | yes | User sec_uid (required)  |

## Details

Returns a page of homepage video posts for one Douyin user, including description, publish time, engagement counts, cover and play URLs. It needs the user's `sec_uid`. You can set the page size with `count` and page forward with `cursor`.

### Use cases

- Pull the latest videos from a Douyin creator's profile to check what they posted.
- Track `Statistics` counts such as likes and shares across a creator's posts for a performance report.
- Find posts that carry a `DouplusUserPostTag` label to see which videos the DOU+ tool flags.
- Collect play URLs and cover images for a creator's videos to build a content archive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid (required) |
| `count` | string | No | Page size, default 10 |
| `cursor` | string | No | Pagination cursor (string), "0" for first page, then pass the cursor from the previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": "1790585915000",
    "hasMore": true,
    "itemInfoList": [
      {
        "AwemeInfo": {
          "Author": {
            "AvatarMedium": {
              "Uri": "720x720/aweme-avatar/tos-cn-avt-0015_9186d2f6f96963551bd89aaa2c745843",
              "UrlList": [
                "https://p26.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_9186d2f6f96…"
              ]
            },
            "AvatarThumb": {},
            "FollowerCount": 0,
            "LabelList": [],
            "Nickname": "栗子味",
            "SecUid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
            "ShortId": "",
            "Signature": ""
          },
          "AwemeId": "7701639863695617457",
          "CreateTime": "1793177767000",
          "Desc": "伊人妆 秋眉晃 宛在水中央",
          "IsPhoto": false,
          "Statistics": {
            "AwemeId": "",
            "CommentCount": 32,
            "DiggCount": 2283,
            "ShareCount": 41
          },
          "Video": {
            "Cover": {
              "Height": 0,
              "Uri": "tos-cn-p-0015c000-ce/ocjh9b0CqIecA6EjuC4FGfiEQTDDraAoHwfTKk",
              "UrlKey": "",
              "UrlList": [
                "http://p6-douplus-sign.byteimg.com/tos-cn-p-0015c000-ce/ocjh9b0CqIecA6EjuC4FGfiE…"
              ],
              "Width": 0
            },
            "CreateTime": "1793177767",
            "ImageURL": {},
            "IsPhoto": false,
            "ItemID": "7701639863695617457",
            "ItemOptions": {},
            "PlayAddr": {
              "Height": 576,
              "Uri": "v1e00fgi0000dbgrh1vog65hqsh78ht0",
              "UrlKey": "",
              "UrlList": [
                "https://v13-cold.douyinvod.com/d6e2d6ff40f7293164b039c01c0d8daa/6ae99c0c/video/t…"
              ],
              "Width": 1024
            },
            "Statistics": {
              "CommentCnt": "0",
              "FinishPlayRate": 0,
              "IndexCnt": "0",
              "LikeCnt": "0",
              "LikeRate": 0,
              "NewFansCnt": "0",
              "NewFansRate": 0,
              "NewLikeCnt": "0"
            }
          }
        },
        "CanMountEnterpriseShopCartType": 2,
        "DouplusUserPostTag": "爆款预定",
        "IsAd": false,
        "IsItemPromotional": false,
        "IsOver90Days": false,
        "ItemSource": {
          "ItemGeneraion": 0,
          "SourceType": 1
        },
        "PlayletType": 0
      }
    ]
  },
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.itemInfoList[].AwemeInfo.AwemeId` | ID of the video post, as a string. |
| `data.itemInfoList[].AwemeInfo.Desc` | Caption text of the video. |
| `data.itemInfoList[].AwemeInfo.CreateTime` | Publish time of the post as a string. The value looks like a Unix timestamp in milliseconds. |
| `data.itemInfoList[].AwemeInfo.Statistics.DiggCount / CommentCount / ShareCount` | Like, comment and share counts for the post. |
| `data.itemInfoList[].AwemeInfo.Author.Nickname / SecUid` | Display name and `sec_uid` of the post author. |
| `data.itemInfoList[].AwemeInfo.Video.PlayAddr.UrlList` | List of video file URLs. `Width` and `Height` in the same object give the video size. |
| `data.itemInfoList[].AwemeInfo.Video.Cover.UrlList` | List of cover image URLs for the video. |
| `data.itemInfoList[].DouplusUserPostTag` | Tag text attached to a post, such as `爆款预定`. It appears only on some posts. |
| `data.itemInfoList[].IsAd / IsItemPromotional / IsOver90Days` | Boolean flags for whether the post is an ad, is promotional, or is over 90 days old. |
| `data.cursor / data.hasMore` | `cursor` is the value to send for the next page. `hasMore` tells you whether more posts remain. |

### Notes

- Send `cursor` as `"0"` for the first page. For later pages, pass the `data.cursor` value from the previous response.
- Keep paging while `data.hasMore` is `true`.
- `count` sets the page size and defaults to 10.
- Cover and play URLs are signed links, and some include an `x-expires` value, so download them soon after the call.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/apis/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/user-posts.json`](../../../../catalog/models/douyin/douplus/user-posts.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/user-posts
