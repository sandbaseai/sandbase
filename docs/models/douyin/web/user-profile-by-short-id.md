# Douyin User Profile by Short ID API: pricing, parameters and code examples

`douyin/web/user-profile-by-short-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves Douyin web user profile details using an account short ID. Returns profile metadata, title information, and engagement counters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-profile-by-short-id", "short_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-profile-by-short-id', {'short_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-profile-by-short-id", {
  "short_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-profile-by-short-id", sandbase.Params{
	"short_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-profile-by-short-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `short_id` | string | yes | User Short ID  |

## Details

This API takes a Douyin account short ID and returns the live room data linked to that account, along with a short user block. The response includes the room title, room status, and the account's nickname and `sec_uid`.

### Use cases

- Resolve a Douyin short ID to the account's `sec_uid` so you can call other user endpoints.
- Check the nickname and avatar images of an account from its short ID.
- Read the current live room ID and title for an account.
- Check whether a live room is active by reading `room_status` and the room `status` value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-profile-by-short-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"short_id": "2941976066"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `short_id` | string | Yes | User Short ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "auth_cert_info": "",
    "data": [
      {
        "AnchorABMap": {},
        "admin_user_ids": [],
        "admin_user_ids_str": [],
        "admin_user_open_ids": [],
        "admin_user_open_ids_str": [],
        "fansclub_msg_style": 0,
        "follow_msg_style": 0,
        "gift_msg_style": 0,
        "has_commerce_goods": false,
        "id_str": "7561789775678769966",
        "like_count": 0,
        "linker_map": {}
      }
    ],
    "enter_mode": 0,
    "enter_room_id": "7561789775678769966",
    "partition_road_map": {},
    "qrcode_url": "",
    "room_status": 2,
    "shark_decision_conf": "",
    "similar_rooms": [],
    "user": {
      "avatar_thumb": {
        "url_list": [
          "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_3beaaeb52d3…"
        ]
      },
      "follow_info": {
        "follow_status": 0,
        "follow_status_str": "0"
      },
      "foreign_user": 0,
      "id_str": "92769419069",
      "nickname": "抖音作者助手",
      "open_id_str": "",
      "sec_uid": "MS4wLjABAAAA-hAqMwU4p1xu2AlQSM4R38D7DhTKGOk6d-zYU_o0LxY"
    }
  },
  "extra": {
    "now": 1793691154702
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user.nickname` | Display name of the account. |
| `data.user.sec_uid` | Encrypted user ID of the account. Other Douyin user endpoints accept this kind of ID. |
| `data.user.id_str` | Numeric user ID of the account, returned as a string. |
| `data.user.avatar_thumb.url_list[]` | Image URLs for the account's 100x100 avatar. Each entry points to a different image host. |
| `data.user.follow_info.follow_status` | Follow state between the request context and the account. It is `0` in this response. |
| `data.enter_room_id` | ID of the live room linked to the account. |
| `data.room_status` | Numeric status of the live room. It is `2` in this response. |
| `data.data[].title` | Title of the live room. |
| `data.data[].id_str` | ID of the live room, returned as a string. It matches `data.enter_room_id` here. |
| `data.data[].like_count / data.data[].user_count_str` | Like count and viewer count for the live room. Both are `0` in this response. |

### Notes

- Send `short_id` as a string, for example `2941976066`.
- The `data.user.sec_uid` value can be passed to [Douyin User Profile (Web)](/apis/douyin/web/user-profile) to get a fuller profile.
- Use [Douyin User Video Posts](/apis/douyin/web/user-post-videos) with `sec_uid` to list the account's videos.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-profile-by-short-id.json`](../../../../catalog/models/douyin/web/user-profile-by-short-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-profile-by-short-id
