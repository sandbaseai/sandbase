# WeChat MP Account Profile API: pricing, parameters and code examples

`wechat-mp/v2/account-profile` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/account-profile", "username": "gh_363b924965e9"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/account-profile', {'username': 'gh_363b924965e9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/account-profile", {
  "username": "gh_363b924965e9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/account-profile", sandbase.Params{
	"username": "gh_363b924965e9",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/account-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw; False=simplified parsing.  |
| `username` | string | yes | Official account `gh_username` (`gh_…`). Sources: `content.user_name` from article detail, or `jumpInfo.userName` from WeChat Search V2 `fetch_search` (business_type=account) results. E.g. `gh_363b924965e9`  |

## Details

Returns the profile of an official WeChat account, plus its most recent published articles. It needs the account's `gh_` username in `username`.

### Use cases

- Check how many original articles an official account has published.
- Pull the latest article links and publish times for an account to track its posting activity.
- Read the account's IP location label for a profile record.
- Page through an account's message list with the returned `offset` cursor.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/account-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "gh_363b924965e9"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Official account `gh_username` (`gh_…`). Sources: `content.user_name` from article detail, or `jumpInfo.userName` from WeChat Search V2 `fetch_search` (business_type=account) results. E.g. `gh_363b924965e9` |
| `raw` | boolean | No | Optional, default True. True=raw; False=simplified parsing. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "accountInfo": {
    "banReason": "",
    "banType": 0,
    "pbRequestMsgInfo": null,
    "serviceType": 0,
    "userName": "gh_363b924965e9",
    "userRole": 0
  },
  "aiChatInfo": {
    "aiChatOpen": 2,
    "extInfo": "",
    "pbRequestMsgInfo": null,
    "pollInterval": 180,
    "reportExtInfo": "",
    "roomInfo": "",
    "stringBizuin": "MjM5MjAxNDM4MA=="
  },
  "aiIvrReplyInfo": {
    "aiReplyOpen": 0,
    "pbRequestMsgInfo": null,
    "wording": ""
  },
  "articleTab": {
    "msgList": {
      "featuredList": [],
      "featuredUpdateTime": 1793688509,
      "hideList": false,
      "msg": [
        {
          "appMsg": {
            "baseInfo": {
              "appMsgId": 2667043262,
              "bigPic": 1,
              "createTime": 1793687341,
              "hasExpanded": false,
              "pbRequestMsgInfo": null,
              "type": 9,
              "updateTime": 1793688161
            },
            "detailInfo": [
              {
                "appEditJumpUrl": "",
                "audioDuRation": 0,
                "audioId": 0,
                "audioPlayUrl": "",
                "authorDesc": "",
                "bizRecommendInfo": null,
                "canModifyByWxa": 0,
                "contentUrl": "http://mp.weixin.qq.com/s?__biz=MjM5MjAxNDM4MA==&mid=2667043262&idx=1&sn=efc2247…"
              }
            ],
            "pbRequestMsgInfo": null
          },
          "baseInfo": {
            "dateTime": 1793687341,
            "funcFlag": 0,
            "msgId": 2667043262,
            "msgType": 49,
            "pbRequestMsgInfo": null,
            "status": 0,
            "uniqueId": "0_2667043262",
            "virtualMsgType": 0
          },
          "featuredExposed": false,
          "image": null,
          "pbRequestMsgInfo": null,
          "text": null,
          "video": null,
          "voice": null
        }
      ],
      "pagingInfo": {
        "isEnd": 0,
        "offset": "WABgAGiBpOW+74vB9Go=",
        "pbRequestMsgInfo": null
      },
      "pbRequestMsgInfo": null,
      "poiInfo": null,
      "recommendSetting": null
    },
    "pbRequestMsgInfo": null,
    "show": true,
    "topicList": {
      "pbRequestMsgInfo": null,
      "title": "Top Topics",
      "topic": []
    }
  },
  "audioTab": {
    "msgList": {
      "featuredList": [],
      "featuredUpdateTime": 1793688509,
      "hideList": false,
      "msg": [],
      "pagingInfo": {
        "isEnd": 1,
        "offset": "WABgAGgAcAA=",
        "pbRequestMsgInfo": null
      },
      "pbRequestMsgInfo": null,
      "poiInfo": null,
      "recommendSetting": null
    },
    "pbRequestMsgInfo": null,
    "show": false,
    "topicList": {
      "pbRequestMsgInfo": null,
      "title": "Top Topics",
      "topic": []
    }
  },
  "baseInfo": {
    "bizRecommendUrl": "",
    "friendSubscribeCount": 0,
    "friendSubscribeStr": "",
    "isFans": 0,
    "isSubscribed": 0,
    "nickNameWhenSubscribe": "",
    "originalArticleCount": 1133,
    "originalContentStr": "1133 original articles",
    "pbRequestMsgInfo": null
  },
  "baseResponse": {
    "errMsg": {
      "pbRequestMsgInfo": null,
      "string": ""
    },
    "pbRequestMsgInfo": null,
    "ret": 0
  },
  "bindPoiInfo": null,
  "brandInfo": null,
  "debug_id": "b7b56c11",
  "debug_info": "gAAAAABq6ZEysXRPJLLgIxJIvLQd0bAzwA_WC34pPQO1EI1FDQy_kN3H5CloQ309xS0gUmx69615uZLF…",
  "finderVideoIsBizMode": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `accountInfo.userName` | The `gh_` username of the account, matching the value you sent. |
| `baseInfo.originalArticleCount / baseInfo.originalContentStr` | Number of original articles the account has published, as a number and as a display string such as `1133 original articles`. |
| `ipwording` | IP location label shown for the account, for example `北京`. |
| `msgList.msg[].appMsg.detailInfo[].contentUrl` | Link to an article published by the account. |
| `msgList.msg[].appMsg.baseInfo.appMsgId` | ID of the article message. It also appears in the article link as `mid`. |
| `msgList.msg[].appMsg.baseInfo.createTime / msgList.msg[].appMsg.baseInfo.updateTime` | Unix timestamps in seconds for when the article was created and last updated. |
| `msgList.msg[].baseInfo.uniqueId` | Unique ID of the message in the list, formatted like `0_2667043262`. |
| `msgList.pagingInfo.isEnd / msgList.pagingInfo.offset` | `isEnd` shows whether the list has ended (`1` means it has). `offset` is a cursor string for the next page of messages. |
| `articleTab.msgList.msg / audioTab.msgList.msg / pictextTab.msgList.msg` | The same message list split by tab: articles, audio and picture-text posts. |
| `baseResponse.ret` | Status code of the lookup. `0` appears in this response. |

### Notes

- Get `username` from `content.user_name` in [WeChat MP Article Detail](/apis/wechat-mp/v2/article-detail), or from `jumpInfo.userName` in WeChat Search V2 `fetch_search` results with `business_type=account`.
- `username` must match `gh_` followed by letters, digits or underscores, up to 64 characters.
- `raw` is optional and defaults to `true`. Set it to `false` for simplified parsing.
- For a dedicated article list, call [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.
- [WeChat MP Article Comments](/apis/wechat-mp/v2/article-comments): Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.

---
Machine-readable: [`catalog/models/wechat-mp/v2/account-profile.json`](../../../../catalog/models/wechat-mp/v2/account-profile.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/account-profile
