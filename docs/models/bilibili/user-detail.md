# Bilibili User Profile API: pricing, parameters and code examples

`bilibili/user-detail` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a Bilibili user profile identified by UID. Use it to look up a known account for creator research, profile review, or subsequent retrieval of that user's videos.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/user-detail", "uid": "546195"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/user-detail', {'uid': '546195'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/user-detail", {
  "uid": "546195"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/user-detail", sandbase.Params{
	"uid": "546195",
})
```

Same call via the path form: `POST /v1/api/bilibili/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Bilibili User ID (UID).  |

## Details

Returns the public profile of a Bilibili user. It needs one input, the numeric `uid`. The response is a page-state object, and the profile sits under `space.info`.

### Use cases

- Look up a known creator's name, level, and bio for creator research.
- Check a creator's verification text and awards before a partnership.
- Find the user's live room ID and current live title.
- Confirm that a UID belongs to the expected account before you fetch that user's videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "546195"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Bilibili User ID (UID). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channel": {
    "channelConfig": [],
    "channelData": {},
    "serverFetched": null
  },
  "common": {
    "abtest": {
      "h5_resolution": "1"
    },
    "autoFallback": {
      "config": {
        "def": "",
        "dl": [],
        "fr": false,
        "hasSuffixesConfig": false,
        "suffixes": {}
      },
      "connectivities": {},
      "defDomain": "",
      "defFallbackThreshold": 5,
      "defUpdated": false,
      "hasSuffixesConfig": false,
      "on": false,
      "suffixConfigs": {},
      "wl": [],
      "x": 41
    },
    "browser": {
      "CMDC": false,
      "MicroMessenger": false,
      "QQLive": false,
      "Safari": false,
      "Youku": false,
      "android": true,
      "baidu": false,
      "baiduspider": false,
      "chrome": false,
      "harmonyOSNext": false,
      "iPad": false,
      "iPhone": false
    },
    "defDomain": "",
    "ipRegion": "",
    "isOversea": false,
    "isWxTagLaunch": false,
    "legalRegion": "",
    "noCallApp": false,
    "serverConfig": {
      "constants": {
        "newClipboard": false
      },
      "customChannel": {
        "bsource": [
          "OPPO_search"
        ]
      },
      "limitChannel": {
        "bsource": [
          "bilibili-toutiao"
        ],
        "referrer": [
          "(.)*\\.google.com"
        ],
        "ua": [
          "MicroMessenger"
        ]
      },
      "openappDialogConfig": {
        "autoOpenappLimit": 3,
        "commonOpenappFailedLimit": 3,
        "naturalSearchPlayerPauseOpenappLimit": 5,
        "naturalSearchPlayerPlayOpenappLimit": 3,
        "sharePlayerPauseOpenappLimit": 20,
        "sharePlayerPlayOpenappLimit": 10
      },
      "switch": {
        "search_h5_style": "column1"
      }
    },
    "switch": {
      "search_h5_style": "column1"
    },
    "ua": "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10)…"
  },
  "home": {
    "hotList": {
      "error": false,
      "extra": {},
      "noMore": false,
      "result": []
    }
  },
  "opus": {
    "detail": null,
    "fallback": {
      "id": "",
      "type": 0
    },
    "id": "",
    "isClient": false,
    "isTab3": false,
    "preview": null,
    "uniqueK": "",
    "verifyData": null
  },
  "playlist": {
    "forbidPreview": false,
    "hasMore": true,
    "isClient": false,
    "mediaData": {
      "mediaList": [],
      "noMore": false,
      "pn": 1,
      "ps": 20
    },
    "mediaId": "",
    "mediaList": [],
    "p": 1,
    "playEnd": false,
    "playMode": "order",
    "playSum": 0,
    "playUrl": [],
    "playlistType": 3
  },
  "route": {
    "from": {
      "fullPath": "/",
      "hash": "",
      "meta": {},
      "name": null,
      "params": {},
      "path": "/",
      "query": {}
    },
    "fullPath": "/space/546195",
    "hash": "",
    "meta": {},
    "name": "space",
    "params": {
      "id": "546195"
    },
    "path": "/space/546195",
    "query": {}
  },
  "search": {
    "blacklistArchive": [],
    "bsource": "",
    "isCustom": false,
    "keyword": "",
    "openAppDialog": true,
    "searchAllResult": {
      "click": {
        "noMore": false,
        "page": 0,
        "result": [],
        "total": 0
      },
      "dm": {
        "noMore": false,
        "page": 0,
        "result": [],
        "total": 0
      },
      "extra": {
        "count": {
          "bili_user": 0,
          "media_bangumi": 0,
          "media_ft": 0,
          "video": 0
        },
        "filmList": [],
        "pgcList": []
      },
      "pubdate": {
        "noMore": false,
        "page": 0,
        "result": [],
        "total": 0
      },
      "totalrank": {
        "noMore": false,
        "page": 0,
        "result": [],
        "total": 0
      }
    },
    "searchBangumiResult": {
      "noMore": false,
      "page": 0,
      "result": [],
      "total": 0
    },
    "searchFilmResult": {
      "noMore": false,
      "page": 0,
      "result": [],
      "total": 0
    },
    "searchUserResult": {
      "noMore": false,
      "page": 0,
      "result": [],
      "total": 0
    }
  },
  "space": {
    "feedList": {
      "error": false,
      "extra": {},
      "noMore": false,
      "result": []
    },
    "info": {
      "attestation": {
        "common_info": {
          "prefix": "bilibili UP主认证",
          "prefix_title": "bilibili UP主认证：2025百大UP主、2025年度商业影响力奖UP主、2022年度联合创作奖UP主",
          "title": "2025百大UP主、2025年度商业影响力奖UP主、2022年度联合创作奖UP主"
        },
        "desc": "",
        "icon": "https://i0.hdslb.com/bfs/activity-plat/static/20230828/e3b8ebec8e86f060b930a2c05…",
        "splice_info": {
          "title": "2025百大UP主、2025年度商业影响力奖UP主、2022年度联合创作奖UP主"
        },
        "type": 2
      },
      "birthday": "",
      "certificate_show": false,
      "coins": 0,
      "contract": null,
      "control": 0,
      "elec": {
        "show_info": {
          "icon": "https://i0.hdslb.com/bfs/garb/item/33e2e72d9a0c855f036b4cb55448f44af67a0635.png",
          "jump_url": "https://www.bilibili.com/h5/upower/index?mid=546195&navhide=1&oid=546195",
          "jump_url_web": "https://member.bilibili.com/mall/upower-pay?mid=546195",
          "list": [
            {
              "avatar": "https://i0.hdslb.com/bfs/face/77bc7841f08047c3a077186bc8de12cbee5ef5cc.jpg",
              "pay_mid": 3493077721287339,
              "rank": 1,
              "uname": "芝麻酱emu"
            }
          ],
          "long_title": "",
          "show": true,
          "state": 2,
          "title": "充电"
        }
      },
      "face": "http://i0.hdslb.com/bfs/face/bc5ca101313d4db223c395d64779e76eb3482d60.jpg",
      "face_nft": 0,
      "face_nft_type": 0,
      "fans_badge": true,
      "fans_medal": {
        "detail": null,
        "medal": null,
        "show": false,
        "wear": false
      }
    },
    "mid": 546195
  },
  "tag": {
    "tagInfo": {},
    "tagRelated": {
      "error": false,
      "extra": {},
      "result": [],
      "total": 0
    },
    "tagSimilar": []
  },
  "topic": {
    "activities": {},
    "ads": {},
    "headerTextColor": 0,
    "isExpanded": false,
    "relevantTopics": [],
    "topicDetail": {},
    "topicId": 0,
    "topicListResult": {
      "error": false,
      "extra": {},
      "no_more": false,
      "result": [],
      "total": 0
    }
  },
  "tribee": {
    "tribeeBaseInfo": {},
    "tribeeInviteDefer": null,
    "tribeeInviteInfo": null,
    "tribeeList": [],
    "tribeeListTotal": 0,
    "tribeeSteamHomeInfo": {}
  },
  "video": {
    "archiveConfigId": "",
    "archiveType": 0,
    "avid": 0,
    "breadcrumb": {},
    "bsource": "",
    "bvid": "",
    "elec": {},
    "error": 0,
    "eventConfig": {
      "bottomBannerImage": "",
      "bottomBannerUrl": {
        "searchKeyword": "",
        "type": "browser",
        "urlH5": ""
      },
      "mainCallButtonText": "",
      "relatedTabList": [],
      "relatedTabText": {
        "text": "",
        "videoListID": ""
      },
      "topBannerImage": "",
      "topButtonUrl": {
        "searchKeyword": "",
        "type": "browser",
        "urlH5": ""
      },
      "topSearchUrl": {
        "searchKeyword": "",
        "type": "browser",
        "urlH5": ""
      }
    },
    "gameMode": false,
    "hotSearchVideoList": [],
    "hotWord": ""
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `space.info.mid / space.mid` | The numeric user ID. It matches the `uid` you sent. |
| `space.info.name` | The display name of the account. |
| `space.info.sign` | The bio text the user wrote on their profile. |
| `space.info.level` | The account level shown on the profile. The sample value is `6`. |
| `space.info.face` | URL of the profile avatar image. |
| `space.info.official.title / space.info.attestation.common_info.title` | The verification text shown on the profile, such as creator awards. `official.role` and `attestation.type` give the verification type as numeric codes. |
| `space.info.live_room.roomid` | The ID of the user's live room. |
| `space.info.live_room.title / space.info.live_room.url / space.info.live_room.liveStatus` | The live room title, its web link, and a status code. `0` is the value in the sample. |
| `space.info.elec.show_info.list[].uname` | Names of top supporters shown in the charging (`充电`) section. Each row also has `rank`, `avatar` and `pay_mid`. |
| `space.info.top_photo_v2.l_img` | URL of the profile banner image. |

### Notes

- Pass `uid` as a string, for example `"546195"`. It is the same number used in the profile page path `/space/546195`.
- Most other top-level keys, such as `video`, `search`, `playlist` and `topic`, hold empty page-state defaults. Read the profile from `space.info`.
- Some fields come back empty or zero for this profile, such as `birthday`, `coins` and `jointime`. Do not rely on them.
- To get this user's videos next, call [Bilibili User Published Videos](/apis/bilibili/user-video-list) or [Bilibili User Post Videos](/apis/bilibili/web/user-post-videos) with the same UID.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/bilibili/user-detail.json`](../../../catalog/models/bilibili/user-detail.json) · Store page: https://www.sandbase.ai/model/bilibili/user-detail
