# Weibo User Profile Information API: pricing, parameters and code examples

`weibo/app/user-info` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns basic profile information for a Weibo user, including nickname, avatar, biography, follower counts, and channel metadata, using a user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-info", "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-info', {'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-info", {
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-info", sandbase.Params{
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Returns the profile page layout data for one Weibo user. It needs the numeric user ID in `uid`. The response holds the profile tabs (posts, videos, dynamic feed), a bottom toolbar with the user's follow state and avatar URLs, and a header block with profile info.

### Use cases

- Get the tab container IDs for a Weibo user so you can request their posts or videos feed.
- Read the post count shown on the all-posts filter title for a creator.
- Fetch the avatar image URLs for a Weibo user ID.
- Check whether the profile has messaging enabled and what follow state the toolbar shows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channelInfo": {
    "channelConfig": {
      "channelType": "userProfile",
      "selectInfo": {
        "flowId": "2328087648703289",
        "pageDataType": "flow",
        "pullRefreshTop": 1,
        "tabKey": "dynamic"
      },
      "style": {
        "backgroundColor": "#FFFFFF",
        "backgroundDarkColor": "#FFFFFF",
        "height": 44
      }
    },
    "channels": [
      {
        "apiPath": "/2/flowlist",
        "containerid": "2328087648703289",
        "dynaConfig": {
          "bizType": "profile",
          "enable": true
        },
        "flowId": "2328087648703289",
        "pageDataType": "flow",
        "params": {
          "profileTabType": "profile",
          "profile_check_ext": "2070301595320timestamp:1793691974|profileUid:7648703289",
          "profile_check_value": "timestamp:1793691974|profileUid:7648703289|token:b0056c25"
        },
        "theme": {
          "hidden": 0,
          "id": 18,
          "mustShow": 1,
          "tabKey": "dynamic"
        },
        "title": "动态",
        "titleInfo": {
          "style": {
            "font": "Normal",
            "fontSize": 15,
            "iconHeight": 24,
            "iconSkinKey": "channelIcon_1",
            "iconWidth": 24,
            "padding": [
              0
            ],
            "selectFont": "Bold",
            "selectFontSize": 15
          }
        }
      }
    ]
  },
  "config": "{}",
  "footer": {
    "data": {
      "toolbar_menus_new": {
        "items": [
          {
            "buttonMap": {
              "normal": {
                "actionlog": {
                  "act_code": 594,
                  "cardid": "230774_-_WEIBO_INDEX_PROFILE_CHAT",
                  "ext": "uid:2070301595320|ouid:7648703289|btn_name:留言|btn_type:zs_messege|toolbar_type:1…",
                  "fid": "2307747648703289",
                  "oid": "messagelist",
                  "uicode": "10000198"
                },
                "disable": "0",
                "param": {
                  "scheme": "sinaweibo://messagelist?uid=7648703289&nick=悲伤荷包蛋&verified_type=-1&send_from=use…",
                  "type": "vertical_arrange"
                },
                "style": {
                  "alignment": "1",
                  "image": {
                    "height": "28",
                    "pic": "https://d.sinaimg.cn/prd/100/1968/2025/06/23/sx_default.png",
                    "pic_dark": "https://d.sinaimg.cn/prd/100/1968/2025/06/23/sx_dark.png",
                    "skinKey": "messageNormalIcon",
                    "width": "28"
                  },
                  "name": {
                    "skinKey": "messageNormalText",
                    "text": "留言",
                    "textColor": "#636363",
                    "textColorDark": "#999999",
                    "textFontSize": "13"
                  },
                  "padding": [
                    "0"
                  ],
                  "space": "0",
                  "type": "normal",
                  "widthValue": 54
                }
              }
            },
            "handlerType": "default_handler",
            "identifier": "message",
            "notificationname": null,
            "status": "normal",
            "type": "toolbar_link"
          }
        ],
        "servicePopup": [],
        "style": {
          "backgroundUrl": "",
          "padding": [
            0
          ],
          "skinKey": "navigationBackground"
        }
      }
    },
    "type": "userProfile"
  },
  "header": {
    "config": {
      "type": "userProfile"
    },
    "data": {
      "action_more": {
        "actionlog": {
          "act_code": 4631,
          "cardid": "",
          "ext": "",
          "fid": "1076037648703289",
          "lfid": "232532",
          "luicode": "10000002",
          "oid": "",
          "uicode": "10000198"
        },
        "desc": "更多资料",
        "icon": "https://h5.sinaimg.cn/upload/1059/799/2022/02/28/info_more.png",
        "icon_dark": "https://h5.sinaimg.cn/upload/1059/799/2022/02/28/info_more_dark.png",
        "icon_height": 12,
        "icon_width": 6.5,
        "scheme": "sinaweibo://userdetailinfov2?uid=7648703289",
        "textcolor": "#939393"
      },
      "infoList": [
        {
          "actionlog": {
            "act_code": 4630,
            "cardid": "",
            "ext": "name:description",
            "fid": "1076037648703289",
            "lfid": "232532",
            "luicode": "10000002",
            "oid": "",
            "uicode": "10000198"
          },
          "desc": "恨比爱长久",
          "icon": "https://h5.sinaimg.cn/upload/1059/799/2020/05/19/description.png",
          "icon_dark": "https://h5.sinaimg.cn/upload/1059/799/2020/05/19/description-dark.png",
          "icon_video_style": "https://h5.sinaimg.cn/upload/1059/799/2021/04/16/video_description.png",
          "icon_video_style_dark": "https://h5.sinaimg.cn/upload/1059/799/2021/04/16/video_description_dark.png",
          "scheme": "",
          "textcolor": "#939393"
        }
      ],
      "isVideoCoverStyle": false,
      "style": {
        "avatar": {
          "avatarBorderSkinKey": "avatarBorderColor",
          "boder_color": "#ffffff",
          "boder_color_dark": "#00000000",
          "border_color_dark": "#1E1E1E",
          "border_width": 2,
          "inside_border_color": "#12000000",
          "inside_border_color_dark": "#1affffff",
          "inside_border_width": 1
        },
        "heightScale": 0.39,
        "nick": {
          "gender_top": 0,
          "grass_top": 0,
          "membershop_top": -2,
          "text_color": "#333333",
          "text_color_dark": "#D3D3D3",
          "verticalSpacing": 0
        },
        "nick_offset": 31,
        "nick_offset_ios": 31,
        "styleId": "headerDefalt",
        "userinfo_offset": 27
      },
      "tags": [
        {
          "actionlog": {
            "act_code": 4629,
            "cardid": "",
            "ext": "type:video_play",
            "fid": "1076037648703289",
            "lfid": "232532",
            "luicode": "10000002",
            "oid": "7648703289",
            "uicode": "10000198"
          },
          "backgroundSkinKey": "tagBackground_1",
          "bg_color": "#59FFDDCB",
          "bg_color_dark": "#FF181818",
          "bg_color_video_style": "#8C181818",
          "bg_color_video_style_dark": "#8C181818",
          "color": "#FFFF6200",
          "color_dark": "#FFEA8011"
        }
      ],
      "userDescribe": [
        {
          "actionlog": {
            "act_code": 4644
          },
          "scheme": "https://m.weibo.cn/c/attention/visit?showmenu=0&sign=7648703289&source=MQ==&role…",
          "text": [
            {
              "content": "362.4万",
              "style": {
                "bold": "1",
                "styleId": "defaultNumberContent",
                "textColor": "#333333",
                "textColorDark": "#D3D3D3",
                "textSize": 15
              },
              "type": "text"
            }
          ]
        }
      ],
      "userInfo": {
        "allow_all_act_msg": false,
        "allow_all_comment": false,
        "allow_msg": 1,
        "audio_ability": 2,
        "auth_career": null,
        "auth_career_name": null,
        "auth_realname": null,
        "auth_status": 2
      }
    }
  },
  "headerBack": {
    "config": {
      "fixed": 0,
      "type": "profileHeaderBack"
    },
    "default": {
      "channelBarStyle": {
        "backgroundColor": "#FFFFFF",
        "backgroundDarkColor": "#1E1E1E",
        "font": "Normal",
        "fontSize": 15,
        "padding": [
          0
        ],
        "selectFont": "Bold",
        "selectFontSize": 15,
        "selectTextColor": "#333333"
      },
      "data": {
        "backgroundDarkUrl": "",
        "backgroundSkinKey": "headBackground",
        "backgroundUrl": "",
        "coverImage": [
          {
            "cover": "https://wx1.sinaimg.cn/hworiginal/70ace9b7ly1ggzusnypoej20yi0yiaop.jpg",
            "cover_thumbnails": "https://wx1.sinaimg.cn/bmiddle/70ace9b7ly1ggzusnypoej20yi0yiaop.jpg",
            "pid": "70ace9b7ly1ggzusnypoej20yi0yiaop"
          }
        ],
        "coverImageSkinKey": "coverImage",
        "coverVideo": {
          "skinKey": "coverVideo"
        },
        "maskFillColor": [
          "#00FFFFFF"
        ],
        "maskFillColorDark": [
          "#001E1E1E"
        ]
      },
      "style": {
        "backgroundColor": "#EEEEEE",
        "backgroundColorDark": "#151515",
        "backgroundImageSize": [
          100
        ],
        "contentBottom": "ToChannelBarBottom",
        "contentInset": [
          0
        ],
        "contentModel": "scaleAspectTopFit",
        "height": 0,
        "heightScale": 0.39
      }
    }
  },
  "navigationBar": {
    "data": {
      "title_bar_menus": [
        {
          "actionlog": {
            "act_code": 3058,
            "ext": "type:profileSearch|isowner:0"
          },
          "bgColor": "#26000000",
          "permanent": 1,
          "pic": "https://h5.sinaimg.cn/upload/1014/739/2024/09/03/new_profile_sousuo2.png",
          "pic_highlight": "https://h5.sinaimg.cn/upload/1014/739/2024/09/03/new_profile_sousuo2_anxia.png",
          "pic_highlight_dark": "https://h5.sinaimg.cn/upload/1014/739/2024/09/03/new_profile_sousuo2_anxia_dark.…",
          "pic_pin": "https://h5.sinaimg.cn/upload/1014/739/2024/09/03/new_profile_sousuo2_shanghua.pn…",
          "scheme": "sinaweibo://userinfosearchall?disable_history=1&disable_hot=0&disable_search=0&d…"
        }
      ]
    },
    "type": "default"
  },
  "profileSkin": {
    "local": {
      "md5": "",
      "skinId": ""
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `channelInfo.channels[].title` | Name of each profile tab, such as `动态` (dynamic), `微博` (posts) and `视频` (videos). |
| `channelInfo.channels[].containerid / channelInfo.channels[].flowId` | Container ID of the tab's feed. The posts tab value starts with `107603` followed by the user ID. |
| `channelInfo.channels[].apiPath` | Path of the Weibo endpoint that serves the tab's feed, for example `/2/flowlist`. |
| `channelInfo.channels[].params.profileTabType` | Tab type key, such as `profile`, `weibo` or `water_fall`. |
| `channelInfo.channels[].serviceConfig.filter_group.filter_group[].title` | Label of a filter on the posts tab. The all-posts title includes a count, for example `全部微博(1136)`. |
| `footer.data.toolbar_menus_new.items[].identifier` | Name of each toolbar button: `message`, `recommend` and `follow`. |
| `footer.data.toolbar_menus_new.items[].userinfo.id` | Numeric ID of the profile user. It appears on the follow button item. |
| `footer.data.toolbar_menus_new.items[].userinfo.avatar_hd / footer.data.toolbar_menus_new.items[].userinfo.avatar_large` | Signed URLs of the user's avatar in high and large sizes. The URLs carry an `Expires` parameter. |
| `footer.data.toolbar_menus_new.items[].userinfo.following / footer.data.toolbar_menus_new.items[].userinfo.follow_me` | Booleans for whether the viewing account follows the user and whether the user follows that account. |

### Notes

- Pass `uid` as a string of digits, for example `7648703289`.
- The `profile_check_value` strings in `params` hold a `timestamp` and a `token`. Treat them as short-lived values tied to this response.
- For full profile details, call [Weibo User Profile Details (App)](/apis/weibo/app/user-info-detail).
- To read the user's posts, call [Weibo User Timeline](/apis/weibo/app/user-timeline) or [Weibo User Videos](/apis/weibo/app/user-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-info.json`](../../../../catalog/models/weibo/app/user-info.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-info
