# Youku User Profile API: pricing, parameters and code examples

`youku/user-detail` · data API · Youku · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a Youku user profile identified by UID. Use it to look up a known account for creator research, profile review, or related video discovery.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youku/user-detail", "uid": "UMTM2MTEzNzk5Ng=="}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youku/user-detail', {'uid': 'UMTM2MTEzNzk5Ng=='})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youku/user-detail", {
  "uid": "UMTM2MTEzNzk5Ng=="
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youku/user-detail", sandbase.Params{
	"uid": "UMTM2MTEzNzk5Ng==",
})
```

Same call via the path form: `POST /v1/api/youku/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | The unique identifier for the user.  |

## Details

Returns a Youku user profile page as a list of components, including the header, tabs, and a feed of the user's videos. It needs one input, the user's `uid`.

### Use cases

- Look up a known Youku creator and read the avatar and header data on their profile.
- List the albums and short videos a creator has published, with titles and cover images.
- Check which tabs a profile offers, such as short videos and dynamic posts.
- Collect video titles from a creator before fetching each one with a video details call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youku/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "UMTM2MTEzNzk5Ng=="}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | The unique identifier for the user. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "componentList": [
    {
      "componentId": "h5-profile-header",
      "componentName": "页头",
      "dataNode": [
        {
          "data": {
            "allowPgcFollowRec": false,
            "atmospherex": {
              "icon": "https://gw.alicdn.com/imgextra/i4/O1CN01tx3Yvy1NwsEpQMYY1_!!6000000001635-2-tps-…"
            },
            "avatar": "https://image.9xsecndns.cn/image/uicon/550f0355577e9aa79d5ceaec54f82be2a745ff5d0…",
            "birthday": 0,
            "buttonColor": "#FFFFFF",
            "circle": {
              "action": {
                "callback": null,
                "contentType": null,
                "contentValue": null,
                "extra": null,
                "report": {
                  "arg1": null,
                  "index": 0,
                  "pageName": "page_miniapp",
                  "reportDataOpt": null,
                  "scmAB": "20140689.rcmd",
                  "scmC": "20752",
                  "scmD": "url_YW_ZPD_FOLLOW_CIRCLE",
                  "spmAB": "a2h0j.personalchannel"
                },
                "reportConfig": null,
                "reportDisabled": false,
                "type": "JUMP_TO_URL"
              },
              "title": "10",
              "titlex": 0
            },
            "customBg": false,
            "customChangeBgTitle": "点击定制我的个性背景~"
          },
          "id": "null",
          "logInfo": {},
          "moduleType": "",
          "type": null
        }
      ],
      "id": "69384_0",
      "logInfo": {},
      "moduleList": [
        {
          "dataNode": [],
          "moduleType": ""
        }
      ],
      "state": "header",
      "type": "YW_ZPD_HEADER"
    }
  ],
  "pageData": {
    "avatar": "https://image.9xsecndns.cn/image/uicon/550f0355577e9aa79d5ceaec54f82be2a745ff5d0…",
    "more": false,
    "navState": "video",
    "nextSession": "{\"subIndex\":13,\"trackInfo\":{},\"spmA\":\"a2h0j\",\"level\":1,\"spmC\":\"drawer2\",\"spmB\":\"…",
    "nickName": "娱乐圈打工日常",
    "pageNo": "1",
    "shareInfo": {
      "describe": "快来看TA的精彩视频吧",
      "img": "https://image.9xsecndns.cn/image/uicon/550f0355577e9aa79d5ceaec54f82be2a745ff5d0…",
      "link": "https://m.youku.com/profile?uid=UMTM2MTEzNzk5Ng==",
      "title": "娱乐圈打工日常的优酷主页"
    },
    "showDCloumTitle": true,
    "spmA": "a2h0j",
    "spmAB": "a2h0j.personalchannel",
    "spmB": "personalchannel"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `componentList[].componentId` | Name of each profile section, such as `h5-profile-header`, `h5-profile-nav`, and `h5-profile-video`. |
| `componentList[].componentName` | Display label of the section. Values seen include the tab names `短视频` (short videos) and `动态` (dynamic posts). |
| `componentList[].dataNode[].data.avatar` | URL of the user's avatar image. It appears in the header component. |
| `componentList[].dataNode[].data.circle.title` | Count shown for the user's circle in the header, returned as a string such as `10`. |
| `componentList[].dataNode[].state` | Tab key for each entry in the nav component, such as `video` or `dynamic`. |
| `componentList[].dataNode[].title / componentList[].dataNode[].subTitle` | Title of a video or album in the feed, and its short status text such as `更新至4集` (updated to episode 4). |
| `componentList[].dataNode[].imgUrl` | Cover image URL for the feed item. |
| `componentList[].dataNode[].data.comments.count` | Comment count on a short video item in the feed. |
| `componentList[].dataNode[].logInfo.trackInfo` | JSON string with tracking details. It contains values such as `albumid` for album items and `pgcpgcid` for the account. |

### Notes

- The response keeps the platform's original structure. Find sections by `componentId` instead of by position in `componentList`.
- Feed items appear both in `dataNode` and again inside `moduleList[].dataNode` of the same component.
- Short video items carry an ID in `logInfo.spmD`-style report fields such as `scmD`, for example `video_XNjU3Njg2MzE3Mg==`. Use the part after `video_` as a video ID in [Youku Video Details](/apis/youku/video-detail).
- To find videos by keyword instead of by account, use [Youku Video Search](/apis/youku/search-video).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youku/user-detail.json`](../../../catalog/models/youku/user-detail.json) · Store page: https://www.sandbase.ai/model/youku/user-detail
