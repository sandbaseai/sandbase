# WeChat Channels Stream Detail API: pricing, parameters and code examples

`wechat-channels/v2/live-detail` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns live-room details including anchor info, status, online count, and replay data using a live ID. Allows switching between raw and parsed output formats.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/v2/live-detail", "live_id": "2078950291205875194"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/v2/live-detail', {'live_id': '2078950291205875194'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/v2/live-detail", {
  "live_id": "2078950291205875194"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/v2/live-detail", sandbase.Params{
	"live_id": "2078950291205875194",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/v2/live-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified parsed structure.  |
| `scene` | integer |  | Optional, entry scene, default 5. range 0–1000 |
| `live_id` | string | yes | Live ID (numeric). Source: replay items of `fetch_live_history`, live entry, or live share. E.g. `2078950291205875194`.  |
| `finder_username` |  |  | Optional, anchor finder username (`v2_…@finder` format), improves hit rate. E.g. `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu).  |

## Details

Returns details for one WeChat Channels live room: the anchor's profile and bound accounts, the live status, and timing and engagement counters for the session. It needs a numeric `live_id`. The default response is the raw payload, and `raw` set to `false` returns a simplified structure.

### Use cases

- Check whether a live room has ended by reading `liveStatus` and `liveInfo.endTime`.
- Pull the anchor's nickname, avatar, signature and verification details for a given live session.
- Find the public account linked to a live anchor through the bound account entries.
- Measure how long a finished stream ran using `liveInfo.liveElapsedTime`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/v2/live-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"live_id": "2078950291205875194"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `live_id` | string | Yes | Live ID (numeric). Source: replay items of `fetch_live_history`, live entry, or live share. E.g. `2078950291205875194`. |
| `finder_username` | string | No | Optional, anchor finder username (`v2_…@finder` format), improves hit rate. E.g. `v2_060000231003b20faec8cae1811ac4d5c702ea32b0771737aa785454f7f8177114cc4d248d66@finder` (Huxiu). |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified parsed structure. |
| `scene` | integer | No | Optional, entry scene, default 5. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "abnormalClosePage": null,
  "anchorContact": {
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
      "detailLink": "pages/index/index.html?showdetail=true&username=v2_060000231003b20faec8cae1811ac…",
      "pbRequestMsgInfo": null,
      "realName": "",
      "unauthProfession": "",
      "verifyStatus": 0
    },
    "bindInfo": [
      {
        "bindType": 4,
        "bizInfo": null,
        "pbRequestMsgInfo": null,
        "profileBizInfo": {
          "info": [
            {
              "authInfo": null,
              "bizNickname": "虎嗅APP",
              "bizUin": 0,
              "bizUsername": "wxid_7620846208112",
              "friendFollowCount": 0,
              "headImgUrl": "https://wx.qlogo.cn/mmhead/ver_1/ZiaKbNU8WkY5x0OJj4Hj3f0oiaznQz6LLxUsZeXIJRcLukO…",
              "pbRequestMsgInfo": null,
              "serviceTypeName": "公众号"
            }
          ],
          "miniapps": [],
          "pbRequestMsgInfo": null
        },
        "qqmusicInfo": null,
        "stickerInfo": null,
        "wecomInfo": null
      }
    ],
    "clubInfo": null,
    "coverEntranceFlag": 0,
    "coverImgUrl": "http://mmsns.qpic.cn/mmsns/B2EfAOZfS1gDQfFF87q9ZrpjCaxbyB46BMsxicdXsvkqtgxWtibAp…",
    "coverUrl": "",
    "extFlag": 2490372,
    "extInfo": {
      "birthDay": 0,
      "birthMonth": 0,
      "birthYear": 0,
      "city": "",
      "country": "CN",
      "pbRequestMsgInfo": null,
      "province": "",
      "sex": 0
    },
    "fansCount": 0,
    "feedCount": 0
  },
  "anchorInfo": {
    "anchorLiveStatus": 2,
    "pbRequestMsgInfo": null
  },
  "anchorNewLiveJumpInfo": null,
  "anchorQuestEntrance": null,
  "audienceEndPageControl": 0,
  "audienceFollowInfo": null,
  "audienceMicStats": null,
  "authCollectJumpInfo": null,
  "autoGenReplayOption": null,
  "autoPlayControlFlag": 0,
  "backupFeedsOnImpression": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `liveInfo.liveId` | Numeric ID of the live room. It matches the `live_id` you sent. |
| `liveInfo.endTime` | End time of the live session. The value looks like a Unix timestamp in seconds. |
| `liveInfo.liveElapsedTime` | Elapsed time of the session, as a number. In this response it is `6368`. |
| `liveInfo.likeCnt / liveInfo.forwardCnt / liveInfo.heatValue` | Like count, forward count and heat value for the live room. All are `0` in this response. |
| `anchorContact.nickname` | Display name of the anchor account. |
| `anchorContact.signature` | Profile signature text of the anchor. |
| `anchorContact.headUrl` | Avatar image URL of the anchor. |
| `anchorContact.authInfo.authProfession` | Verified organization name shown on the anchor's account. |
| `anchorContact.bindInfo[].profileBizInfo.info[].bizNickname / anchorContact.bindInfo[].profileBizInfo.info[].bizUsername` | Name and username of an official account linked to the anchor. `serviceTypeName` gives the account type. |
| `anchorContact.liveStatus / anchorInfo.anchorLiveStatus` | Numeric live status code for the anchor. Both are `2` in this response, and the response does not explain the code. |

### Notes

- Get `live_id` from the replay items of [WeChat Channels Stream Replay History](/apis/wechat-channels/v2/live-history), or from a live entry or live share.
- Pass `finder_username` in the `v2_…@finder` format to improve the hit rate. [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username) converts a Channel ID into this value.
- `liveId` is a number in the response, while `live_id` is a string in the request.
- Most fields in the raw response are `null`, `0` or empty strings for this ended session.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat Channels ID to Username](/apis/wechat-channels/v2/channel-id-to-username): Convert a public WeChat Channels Channel ID (sph… short ID) into the finder username (v2_…@finder) required by the other WeChat Channels APIs.
- [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info): Get the public "More info" panel of a WeChat Channels account: Channel ID, IP and profile location, and verification details such as entity type, service categ…
- [WeChat Channels Collection Videos](/apis/wechat-channels/v2/collection-videos): Returns videos contained within a WeChat Channels collection using a collection ID.

---
Machine-readable: [`catalog/models/wechat-channels/v2/live-detail.json`](../../../../catalog/models/wechat-channels/v2/live-detail.json) · Store page: https://www.sandbase.ai/model/wechat-channels/v2/live-detail
