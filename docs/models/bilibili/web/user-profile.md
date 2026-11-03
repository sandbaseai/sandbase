# Bilibili User Profile API: pricing, parameters and code examples

`bilibili/web/user-profile` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns profile details and charging sponsor information for a specified Bilibili account based on the provided user UID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/user-profile", "uid": "316183842"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/user-profile', {'uid': '316183842'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/user-profile", {
  "uid": "316183842"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/user-profile", sandbase.Params{
	"uid": "316183842",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

Returns the public profile of a Bilibili account, including name, avatar, level, verification title, live room and the top supporters in the charging (`elec`) list. It needs one input: the account's numeric `uid`.

### Use cases

- Show a creator's name, avatar, signature and verification title in a talent database.
- Read the `elec` ranking to see which accounts support a creator most through charging.
- Check whether a creator has a live room and whether it is live now.
- Pull the fan medal name and level to label a creator's fan community.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1437582453"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User UID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "attestation": {
      "common_info": {
        "prefix": "bilibili UP主认证",
        "prefix_title": "bilibili UP主认证：bilibili 知名虚拟UP主",
        "title": "bilibili 知名虚拟UP主"
      },
      "desc": "",
      "icon": "https://i0.hdslb.com/bfs/activity-plat/static/20230828/e3b8ebec8e86f060b930a2c05…",
      "splice_info": {
        "title": "bilibili 知名虚拟UP主"
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
        "jump_url": "https://www.bilibili.com/h5/upower/index?mid=1437582453&navhide=1&oid=1437582453",
        "jump_url_web": "https://member.bilibili.com/mall/upower-pay?mid=1437582453",
        "list": [
          {
            "avatar": "https://i2.hdslb.com/bfs/face/d7fcc7905f0b8142b450b7ba8db7fb48461abe96.jpg",
            "pay_mid": 592007747,
            "rank": 1,
            "uname": "蓮卫兵"
          }
        ],
        "long_title": "",
        "show": true,
        "state": 3,
        "title": "充电"
      }
    },
    "face": "https://i0.hdslb.com/bfs/face/55db91bff8585a806a0e5d3e7394b129afcafa50.jpg",
    "face_nft": 0,
    "face_nft_type": 0,
    "fans_badge": true,
    "fans_medal": {
      "detail": {
        "first_icon": "",
        "guard_level": 0,
        "level": 30,
        "medal_color": "#FFDDF0FB",
        "medal_color_border": "#FFDDF0FB",
        "medal_color_end": "#FFDDF0FB",
        "medal_color_level": "#FF7DB4DE",
        "medal_color_name": "#FF3F8DBA"
      },
      "medal": {
        "guard_level": 0,
        "level": 30,
        "medal_color": 2951253,
        "medal_color_border": 2951253,
        "medal_color_end": 10329087,
        "medal_color_start": 2951253,
        "medal_name": "棺人痴"
      },
      "show": true,
      "wear": true
    }
  },
  "message": "OK",
  "ttl": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.mid / data.name` | The account's numeric ID and display name. |
| `data.sign` | The profile signature text the user wrote. |
| `data.face` | URL of the avatar image. |
| `data.level` | The account's level number. |
| `data.official.title / data.attestation.common_info.title` | The verification title shown on the profile, such as a certified creator label. |
| `data.elec.show_info.list[].uname / data.elec.show_info.list[].rank / data.elec.show_info.list[].pay_mid` | Name, rank and numeric ID of each top charging supporter. Rank 1 is the top supporter. |
| `data.elec.show_info.jump_url_web` | Web link to the charging page of this account. |
| `data.live_room.roomid / data.live_room.title / data.live_room.url` | ID, title and link of the account's live room. |
| `data.live_room.liveStatus` | Live state flag of the room. The sample value is `0`. |
| `data.fans_medal.medal.medal_name / data.fans_medal.medal.level` | Name and level of the fan medal tied to this account. |

### Notes

- Pass `uid` as a string, for example `1437582453`. The same number comes back as `data.mid`.
- `data.elec.show_info.list[].pay_mid` is a supporter's account ID. You can pass it as `uid` to look up that supporter.
- Some fields can be `null` or empty, such as `data.contract`, `data.tags` and `data.birthday`.
- To get a creator's follower counts, call [Bilibili User Relation Statistics](/apis/bilibili/web/user-relation-stat). For their videos, call [Bilibili User Post Videos](/apis/bilibili/web/user-post-videos).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/user-profile.json`](../../../../catalog/models/bilibili/web/user-profile.json) · Store page: https://www.sandbase.ai/model/bilibili/web/user-profile
