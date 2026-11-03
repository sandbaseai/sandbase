# Weibo Post Detail (App) API: pricing, parameters and code examples

`weibo/app/status-detail` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed post information from the Weibo app based on a specified post identifier. Use this endpoint to inspect post metadata and actions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-detail", "status_id": "5016922058656962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-detail', {'status_id': '5016922058656962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-detail", {
  "status_id": "5016922058656962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-detail", sandbase.Params{
	"status_id": "5016922058656962",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status_id` | string | yes | Post ID (required)  |

## Details

Returns the details of one Weibo post from the Weibo app. It needs the post ID in `status_id`. The response holds the post's counts, creation time, IDs, and the tabs the app uses to load reposts, comments and likes.

### Use cases

- Read the like, comment and favorite counts of a single Weibo post.
- Get the creation time and the `mblogid` of a post to build a link or match records.
- Check whether a post allows comments or reposting before you plan an action.
- Find the paging paths for a post's reposts, comments and likes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5016922058656962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "selectInfo": {
        "flowId": "comment",
        "pageDataType": "flow"
      }
    },
    "channels": [
      {
        "actionLog": {
          "act_code": 6688,
          "ext": "",
          "fid": "232532",
          "lfid": "",
          "luicode": "",
          "uicode": "10000002"
        },
        "apiPath": "statuses/container_detail_forward",
        "flowId": "repost",
        "pageDataType": "flow",
        "params": {
          "is_container": "1",
          "max_id_type": 0
        },
        "style": {
          "flowType": "flow",
          "padding": [
            0.0
          ]
        },
        "title": "转发",
        "titleInfo": {
          "icon": "",
          "iconDark": "",
          "style": {
            "backgroundDarkIcon": "",
            "backgroundIcon": "",
            "font": "",
            "fontSize": 16,
            "iconHeight": 24,
            "iconWidth": 24,
            "padding": [
              0.0
            ],
            "selectBackgroundDarkIcon": ""
          },
          "subTitle": ""
        }
      }
    ]
  },
  "config": "{}",
  "detailInfo": {
    "extend": {
      "ab_switcher": 33947716,
      "ad_marked": false,
      "ai_search_config": {
        "ai_preload_time": 1000
      },
      "alchemy_params": {
        "status_header_enable": true,
        "ug_red_envelope": true
      },
      "allow_comment": false,
      "annotations": [
        {
          "photo_sub_type": "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        }
      ],
      "attitudes_count": 87629,
      "attitudes_status": 0,
      "author_type": 1,
      "bullet_screens_shield": 0,
      "can_reprint": false,
      "comment_data": {
        "actionlog": {
          "act": "actlog",
          "act_code": "3860",
          "ext": "rid:0_0_0_5226270566909505518_0_0_0|type:comment_guide",
          "fid": "232532",
          "uicode": "10000001"
        },
        "desc": "有话要说，快来评论",
        "icon": "",
        "show_follow_screen_ratio": "0.5",
        "show_log": {
          "act": "actlog",
          "act_code": "3859",
          "ext": "rid:0_0_0_5226270566909505518_0_0_0|type:comment_guide",
          "fid": "232532",
          "uicode": "10000001"
        },
        "type": 0
      }
    },
    "status": {
      "ad_marked": false,
      "annotations": [
        {
          "photo_sub_type": "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
        }
      ],
      "appid": 2731378,
      "attitudes_animation": 1,
      "attitudes_count": 87629,
      "attitudes_status": 0,
      "author_type": 1,
      "bmiddle_pic": "https://wx1.sinaimg.cn/bmiddle/008lDb85gy1ho6nv2h43qj30u0140n42.jpg",
      "bottom_bar_dyna": {
        "cell_item": {
          "category": "dynamic",
          "itemExt": {
            "bizType": "common"
          },
          "type": "detailBottomBarDefaultButtonStyle"
        }
      },
      "can_edit": false,
      "can_reprint": false,
      "comment_guide_ext": "guide_type:-1|source:1"
    }
  },
  "loadedInfo": "{}",
  "pageFooter": {
    "type": "detail_default"
  },
  "pageHeader": "{}",
  "pageRefresh": "{}",
  "pageTabBar": "{}",
  "pageTitle": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `detailInfo.status.id / detailInfo.status.idstr / detailInfo.status.mid` | Post ID as a number and as a string. The string form is safer for large values. |
| `detailInfo.status.mblogid` | Short post code (for example `O76dDAk4q`). It is a second identifier for the same post. |
| `detailInfo.status.created_at` | Time the post was created, as text with a `+0800` offset. |
| `detailInfo.status.attitudes_count / detailInfo.status.comments_count / detailInfo.status.favorites_count` | Counts of likes, comments and favorites for the post. |
| `detailInfo.status.isLongText` | Shows `true` when the post is a long text post. |
| `detailInfo.status.bmiddle_pic` | URL of a medium-size picture attached to the post. |
| `detailInfo.extend.followers_count / detailInfo.extend.followers_count_str` | Follower count of the post author, as a number and as a short display text such as `362.4万`. |
| `detailInfo.extend.allow_comment / detailInfo.extend.can_reprint` | Flags that show whether commenting and reposting are allowed on the post. |
| `detailInfo.extend.multi_attitude[]` | Counts of reactions by reaction `type`. |
| `channelInfo.channels[].apiPath` | App path used to load each tab: reposts, comments or likes. `flowId` names the tab and `title` is its label. |

### Notes

- `status_id` is the numeric post ID. The same value comes back as `detailInfo.status.idstr`.
- To read the comments, likes or reposts of the post, call [Weibo Post Comments (App)](/apis/weibo/app/status-comments), [Weibo Post Likes](/apis/weibo/app/status-likes) or [Weibo Post Reposts](/apis/weibo/app/status-reposts).
- Many fields are app display settings, such as `actionlog`, `style` and `scheme`. Most users can ignore them.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-detail.json`](../../../../catalog/models/weibo/app/status-detail.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-detail
