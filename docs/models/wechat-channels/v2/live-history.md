# WeChat Channels Stream Replay History API: pricing, parameters and code examples

`wechat-channels/v2/live-history` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a creator's broadcast replay list, including media download URLs and decryption keys. Supports cursor pagination via a finder username.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/live-history", "username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/live-history', {'username': 'v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/live-history", {
  "username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/live-history", sandbase.Params{
	"username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/live-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download).  |
| `flag` | integer |  | Optional fetch flag, default 12. range 0–1000 |
| `username` | string | yes | WeChat Channels finder username (`v2_…@finder` format). Example (an account with live replays): `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu).  |
| `last_buffer` |  |  | Optional pagination cursor (base64), **leave empty for the first page**; when `continue_flag` is truthy, pass the previous page's `last_buffer`.  |

## Details

Returns a list of past broadcast replays for a WeChat Channels account. The only required input is the account's finder `username` in `v2_…@finder` format. Each item carries engagement counts, a creation time, and the account's profile and verification details.

### Use cases

- Build an archive index of a creator's past live streams by collecting each replay's `id` and `createtime`.
- Compare `forwardCount` and `favCount` across replays to see which broadcasts drew the most sharing and saving.
- Check a company account's verification name and linked official account before you add it to a monitoring list.
- Page through a channel's full replay history with `last_buffer` and store each page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/live-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | WeChat Channels finder username (`v2_…@finder` format). Example (an account with live replays): `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu). |
| `flag` | integer | No | Optional fetch flag, default 12. |
| `last_buffer` | string | No | Optional pagination cursor (base64), **leave empty for the first page**; when `continue_flag` is truthy, pass the previous page's `last_buffer`. |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure (recommended for media download). |

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
  "continueFlag": 1,
  "debug_id": "cf556551",
  "debug_info": "gAAAAABq6ZEltSt0UZhsH6puzPVzjr-Oh_FM5KWdUjb0PBKdJDogNVxSv4W9pcBDvEp3j-Iu6lskJ0le…",
  "lastBuffer": "CNK99OOI74OiwQEQASDavtietcSus9ABIKm1nOvlm+qx0AEg7bqU7Nv6kvjPASDdsvC9r7+L3c8BII6w…",
  "last_buffer": "CNK99OOI74OiwQEQASDavtietcSus9ABIKm1nOvlm+qx0AEg7bqU7Nv6kvjPASDdsvC9r7+L3c8BII6w…",
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
      "commentCount": 0,
      "commentList": [],
      "contact": {
        "additionalFlag": 201,
        "archievementInfo": null,
        "authInfo": {
          "appName": "gh_4ee148a6ecaa@app",
          "authGuarantor": null,
          "authIconType": 2,
          "authIconUrl": "https://dldir1v6.qq.com/weixin/checkresupdate/icons_filled_channels_authenticati…",
          "authProfession": "北京虎嗅信息科技股份有限公司",
          "authVerifyIdentity": 3,
          "customerType": 1,
          "detailLink": "pages/index/index.html?showdetail=true&username=v2_060000231003b20faec8cae1811ac…"
        },
        "bindInfo": [
          {
            "bindType": 2,
            "bizInfo": null,
            "pbRequestMsgInfo": null,
            "profileBizInfo": null,
            "qqmusicInfo": null,
            "stickerInfo": null,
            "wecomInfo": {
              "contactId": "",
              "contactWording": "",
              "kfUrl": "https://channels.weixin.qq.com/shop/mchkf/wxc33765a11668893d",
              "pbRequestMsgInfo": null
            }
          }
        ],
        "clubInfo": null,
        "coverEntranceFlag": 0,
        "coverImgUrl": "http://mmsns.qpic.cn/mmsns/B2EfAOZfS1gDQfFF87q9ZrpjCaxbyB46BMsxicdXsvkqtgxWtibAp…",
        "coverUrl": ""
      },
      "cookie": "",
      "createtime": 1790153344,
      "debugMessage": ""
    }
  ],
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
    "megavideoInfo": [
      {
        "feedId": 15016894668406660954,
        "interestFactor": 1,
        "pbRequestMsgInfo": null
      }
    ],
    "objectInfo": [
      {
        "enableFeedPreloadStrategy": true,
        "enhanceConfig": null,
        "feedId": 15016894668406660954,
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
    "preloadStrategyId": 10594020206984739840
  },
  "totalCount": 48
}
```

### Response fields

| Field | Meaning |
|---|---|
| `object[]` | One entry per replay in the current page. |
| `object[].id / object[].displayid` | Numeric ID of the replay. In this response both fields hold the same value. |
| `object[].createtime` | Creation time of the replay as a Unix timestamp in seconds. |
| `object[].favCount / object[].forwardCount / object[].commentCount` | Number of saves, forwards and comments on the replay. |
| `object[].ipRegionInfo.regionText` | Region text shown for the replay, for example `Beijing`. |
| `object[].contact.authInfo.authProfession` | Verified entity name of the account that owns the replay. |
| `object[].contact.bindInfo[].bizInfo.info[].bizNickname` | Nickname of the official account linked to the channel. |
| `object[].contact.coverImgUrl` | URL of the account's cover image. |
| `continueFlag` | Shows whether more pages exist. `1` means you can request the next page. |
| `lastBuffer / last_buffer` | Base64 cursor for the next page. Both keys hold the same value. |

### Notes

- Leave `last_buffer` empty on the first call. While `continueFlag` is `1`, send the returned `last_buffer` in the next request.
- If you only have a public Channel ID, convert it first with [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username).
- Set `raw` to `false` for the simplified parsed structure, which the parameter description recommends for media download.
- For details on a single stream, try [WeChat Channels Stream Detail](/apis/wechat-channels/v2/live-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/live-history.json`](../../../../catalog/models/wechat-channels/v2/live-history.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/live-history
