# Douyin Video search V4 API: pricing, parameters and code examples

`douyin/search/video-search-v4` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch video search V4 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/video-search-v4"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/video-search-v4', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/video-search-v4", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/video-search-v4", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/video-search-v4` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor, 0 for the first request, then the cursor from the last response default `0` |
| `keyword` | string |  | Video title or keyword default `"猫咪"` |

## Details

Returns a page of Douyin video search results for a keyword. Each result includes the video ID, caption, author, engagement counts, cover image and play URLs. The request needs a `keyword` and an optional `cursor`.

### Use cases

- Find popular Douyin videos about a topic by sorting results on `DiggCount` and `ShareCount`.
- Build a list of creators who post about a niche, using author nickname and follower count.
- Collect video IDs and captions for a keyword to track which hashtags appear in them.
- Pull cover images and play URLs to preview matching videos in a research tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/video-search-v4" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫咪", "cursor": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor, 0 for the first request, then the cursor from the last response |
| `keyword` | string | No | Video title or keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": 12,
    "hasMore": true,
    "itemList": [
      {
        "AwemeInfo": {
          "Author": {
            "AvatarMedium": {
              "Uri": "720x720/aweme-avatar/tos-cn-avt-0015_dce2e69766f648747e4a8a37d0384ee6",
              "UrlList": [
                "https://p26.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_dce2e69766f…"
              ]
            },
            "AvatarThumb": {},
            "FollowerCount": 19256,
            "LabelList": [],
            "Nickname": "一碗肉肉",
            "SecUid": "MS4wLjABAAAAI02THT4NuvuEm03thf3AiaNbcC5HjVq66fNCQi-IC2Q",
            "ShortId": "",
            "Signature": ""
          },
          "AwemeId": "7678569006274124793",
          "CreateTime": "1787806164000",
          "Desc": "咪就这样萌萌哒看着你 ⠀⢠⠋⠙⠲⠔⠒⠒⠒⠒⠒⠦⠒⠉⢳⠀⠀\n⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⡇⠀\n⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⁺ ⊹\n ⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀…",
          "IsPhoto": false,
          "Statistics": {
            "AwemeId": "",
            "CommentCount": 33,
            "DiggCount": 5640,
            "ShareCount": 3969
          },
          "Video": {
            "Cover": {
              "Uri": "tos-cn-i-0813c000-ce/oc87oFDW9AEJ1IASJPEEKHCAwAnwdeAMjqf37C",
              "UrlList": [
                "https://p3-sign.douyinpic.com/tos-cn-i-0813c000-ce/oc87oFDW9AEJ1IASJPEEKHCAwAnwd…"
              ]
            },
            "CreateTime": "1787806164",
            "ImageURL": {},
            "IsPhoto": false,
            "ItemID": "7678569006274124793",
            "ItemOptions": {},
            "PlayAddr": {
              "Height": 1024,
              "Uri": "v1e00fgi0000da7s1dvog65h4b22ova0",
              "UrlKey": "",
              "UrlList": [
                "https://v26-cold.douyinvod.com/9e488854a656f5efd2cc34ae0462de1e/6ae99c38/video/t…"
              ],
              "Width": 576
            },
            "Statistics": {}
          }
        },
        "HasLocalAnchor": false,
        "IsAd": false,
        "ItemSource": {
          "ItemGeneraion": 0,
          "SourceType": 1
        },
        "PlayletType": 1
      }
    ]
  },
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.cursor` | Pagination value to send as `cursor` in the next request. |
| `data.hasMore` | `true` when more results are available for this keyword. |
| `data.itemList[].AwemeInfo.AwemeId` | ID of the video. The same value appears in `Video.ItemID`. |
| `data.itemList[].AwemeInfo.Desc` | Caption of the video, including its hashtags. |
| `data.itemList[].AwemeInfo.CreateTime` | Creation time of the video as a Unix timestamp in milliseconds, sent as a string. |
| `data.itemList[].AwemeInfo.Statistics.DiggCount / CommentCount / ShareCount` | Counts of likes, comments and shares for the video. |
| `data.itemList[].AwemeInfo.Author.Nickname / FollowerCount` | Display name of the author and the number of followers they have. |
| `data.itemList[].AwemeInfo.Author.SecUid` | Secure user ID of the author. Use it to look up the author in user APIs. |
| `data.itemList[].AwemeInfo.Video.PlayAddr.UrlList` | Candidate URLs for the video file. `Width` and `Height` give its pixel size. |
| `data.itemList[].AwemeInfo.Video.Cover.UrlList` | Candidate URLs for the cover image of the video. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, send the `data.cursor` value from the last response, and stop when `data.hasMore` is `false`.
- The cover URLs contain an `x-expires` parameter and are signed, so save the images soon if you need them.
- Use `AwemeId` with [Douyin Single Video Details](/apis/douyin/app-v3/one-video) to get the full details of one video.
- Other versions of this search are available, such as [Douyin Video search V3](/apis/douyin/search/video-search-v3).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/search/video-search-v4.json`](../../../../catalog/models/douyin/search/video-search-v4.json) · Store page: https://www.sandbase.ai/model/douyin/search/video-search-v4
