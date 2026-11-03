# WeChat Channels Collection Videos API: pricing, parameters and code examples

`wechat-channels/v2/collection-videos` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns videos contained within a WeChat Channels collection using a collection ID. Provides video media URLs, decryption keys, and pagination cursors.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/collection-videos", "topic_id": "14616794565351966924"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/collection-videos', {'topic_id': '14616794565351966924'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/collection-videos", {
  "topic_id": "14616794565351966924"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/collection-videos", sandbase.Params{
	"topic_id": "14616794565351966924",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/collection-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `topic` |  |  | Collection name (optional, improves hit rate)  |
| `topic_id` | string | yes | Collection ID (numeric, from topic_id of fetch_user_collections)  |
| `username` |  |  | Optional, creator finder username (`v2_…@finder` format), improves hit rate.  |
| `topic_type` | integer |  | Optional, collection type, default 16 (align with the collection's `topic_type` from `fetch_user_collections`). range 0–1000 |
| `last_buffer` |  |  | Optional pagination cursor (base64), **leave empty for the first page**; when `down_continue` is truthy, pass the previous page's `last_buffer`.  |

## Details

Returns the videos in one WeChat Channels collection, plus a cursor for the next page. It needs a numeric collection ID in `topic_id`.

### Use cases

- List every video a creator has grouped into a single collection.
- Track comment, favorite and forward counts across the videos in a collection.
- Sort collection videos by publish time using the `createtime` value.
- Page through a long collection by passing the returned cursor back in each request.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/collection-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"topic_id": "14616794565351966924"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `topic_id` | string | Yes | Collection ID (numeric, from topic_id of fetch_user_collections) |
| `last_buffer` | string | No | Optional pagination cursor (base64), **leave empty for the first page**; when `down_continue` is truthy, pass the previous page's `last_buffer`. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download). |
| `topic` | string | No | Collection name (optional, improves hit rate) |
| `topic_type` | integer | No | Optional, collection type, default 16 (align with the collection's `topic_type` from `fetch_user_collections`). |
| `username` | string | No | Optional, creator finder username (`v2_…@finder` format), improves hit rate. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "baseResponse": {
    "errMsg": {
      "pbRequestMsgInfo": null,
      "string": ""
    },
    "pbRequestMsgInfo": null,
    "ret": 0
  },
  "collectionErrPage": null,
  "continueFlag": 0,
  "debug_id": "7082e094",
  "debug_info": "gAAAAABq6ZEhq3wc5WNY1_-oEZrVOrOwsxBBTqQKifALkxpFnno03zZ3KCcV8L21Uu7wz4j2Uo31-VK5…",
  "downContinueFlag": 1,
  "lastBuffer": "CJGS2OzH3MmHygEIppK4/5HC7ojKAQiPkvjt/qeTisoBCMmR2InmjbiLygEI0JGY677z3IzKAQjakdjL…",
  "last_buffer": "CJGS2OzH3MmHygEIppK4/5HC7ojKAQiPkvjt/qeTisoBCMmR2InmjbiLygEI0JGY677z3IzKAQjakdjL…",
  "object": [
    {
      "adFlag": 4,
      "adInfo": null,
      "attachmentList": {
        "attachments": [],
        "pbRequestMsgInfo": null
      },
      "blockCgiFlag": 0,
      "clientLocalBuffer": null,
      "commentClose": 0,
      "commentCount": 140,
      "commentList": [],
      "contact": {
        "additionalFlag": 9,
        "archievementInfo": null,
        "authInfo": {
          "appName": "gh_4ee148a6ecaa@app",
          "authGuarantor": null,
          "authIconType": 2,
          "authIconUrl": "http://dldir1.qq.com/weixin/checkresupdate/internet_news_media_auth_icon_38887ee…",
          "authProfession": "人民日报社",
          "authVerifyIdentity": 3,
          "customerType": 9,
          "detailLink": "pages/index/index.html?showdetail=true&username=v2_060000231003b20faec8c6e4811dc…"
        },
        "bindInfo": [
          {
            "bindType": 1,
            "bizInfo": {
              "info": [
                {
                  "authInfo": {
                    "authIconType": 2,
                    "authIconUrl": "http://dldir1.qq.com/weixin/checkresupdate/internet_news_media_auth_icon_38887ee…",
                    "pbRequestMsgInfo": null,
                    "verifyInfo": ""
                  },
                  "bizNickname": "人民日报",
                  "bizUin": 0,
                  "bizUsername": "gh_363b924965e9",
                  "friendFollowCount": 0,
                  "headImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/gww5x83NxjVLCJz1Xgu6PLzPKRdiaofFZTwdjSibW1mL8KA…",
                  "pbRequestMsgInfo": null,
                  "serviceTypeName": "公众号"
                }
              ],
              "miniapps": [],
              "pbRequestMsgInfo": null
            },
            "pbRequestMsgInfo": null,
            "profileBizInfo": null,
            "qqmusicInfo": null,
            "stickerInfo": null,
            "wecomInfo": null
          }
        ],
        "clubInfo": null,
        "coverEntranceFlag": 0,
        "coverImgUrl": "",
        "coverUrl": ""
      },
      "cookie": "",
      "createtime": 1735675201,
      "debugMessage": ""
    }
  ],
  "paidCollectionInfo": {
    "courseInfo": null,
    "dramaInfo": null,
    "pbRequestMsgInfo": null,
    "permissionFlag": 0,
    "type": 0
  },
  "pbRequestMsgInfo": null,
  "preloadInfo": {
    "globalInfo": {
      "allowToUseNewSpecMaxPercent": -1,
      "bufferingHealthLengthL0": 5,
      "bufferingHealthLengthL1": 10,
      "bufferingHealthLengthL2": 15,
      "canPreCreatedPlayer": false,
      "currentBufferLengthPart3": 0,
      "downloadWhenSpecChange": 0,
      "enableLivePhotoPreload": false,
      "enablePreloadTotalFeed": false,
      "ffmpegTcpRecvSocketBufferSize": 131072,
      "findPageEnableCellularPreload": false,
      "findPagePreloadSecond": 5
    },
    "megavideoInfo": [],
    "objectInfo": [
      {
        "enableFeedPreloadStrategy": true,
        "enhanceConfig": null,
        "feedId": 14559898883113486609,
        "interestFactor": 1,
        "isAutoIncrement": null,
        "lastInsertedRowID": null,
        "loadWithPlaying": [],
        "lutConfig": null,
        "maxBufferLength": 30,
        "minBufferLength": 25,
        "minCurrentFeedBufferLength": 5,
        "pbRequestMsgInfo": null
      }
    ],
    "pbRequestMsgInfo": null,
    "preloadStrategyId": 10985677411664704323
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `object[]` | The list of videos in this page of the collection. |
| `object[].id` | ID of the video. It is a large number, so keep it as a string or big integer. |
| `object[].createtime` | Publish time of the video. The value looks like a Unix timestamp in seconds, for example `1735675201`. |
| `object[].commentCount / object[].favCount / object[].forwardCount` | Counts of comments, favorites and forwards for the video. |
| `object[].contact.authInfo.authProfession` | Verified profession or organization shown for the creator, for example `人民日报社`. |
| `object[].contact.bindInfo[].bizInfo.info[].bizNickname` | Nickname of the official account linked to the creator's channel. |
| `object[].ipRegionInfo.regionText` | Region text shown for the video, for example `Beijing`. |
| `downContinueFlag` | Set to `1` when more pages exist. When it is truthy, request the next page. |
| `last_buffer / lastBuffer` | Base64 cursor for the next page. Both keys hold the same value. |
| `baseResponse.ret` | Status code of the call. `0` appeared in this response. |

### Notes

- Get `topic_id` and `topic_type` from [WeChat Channels User Collections](/apis/wechat-channels/v2/user-collections).
- For the first page, leave `last_buffer` empty. For the next page, pass the previous `last_buffer` while `downContinueFlag` is truthy.
- The default `raw` is true and returns the full raw structure shown here. Set `raw` to false for a simplified structure suited to media download.
- Use [WeChat Channels Video Detail](/apis/wechat-channels/v2/video-detail) to look up a single video from the collection.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Stream Detail](/apis/wechat-channels/v2/live-detail): Returns live-room details including anchor info, status, online count, and replay data using a live ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/collection-videos.json`](../../../../catalog/models/wechat-channels/v2/collection-videos.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/collection-videos
