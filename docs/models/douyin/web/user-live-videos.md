# Douyin User Webcast Video Records API: pricing, parameters and code examples

`douyin/web/user-live-videos` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves user broadcast video data from Douyin Web using a specific room identifier. Input the webcast ID to look up associated room records.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos", "webcast_id": "153857447459"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos', {'webcast_id': '153857447459'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos", {
  "webcast_id": "153857447459"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos", sandbase.Params{
	"webcast_id": "153857447459",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `webcast_id` | string | yes | Room webcast_id  |

## Details

This API returns the live room record for a Douyin room, looked up by `webcast_id`. The response includes the room ID, title, status, and basic details of the host account.

### Use cases

- Look up the current room ID and title for a Douyin live room when you only have its `webcast_id`.
- Check whether a room is live or ended by reading the room status fields.
- Get the host's `sec_uid` and nickname so you can call a user profile API for that account.
- Collect host avatar URLs for a dashboard that tracks Douyin live rooms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"webcast_id": "376034101029"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `webcast_id` | string | Yes | Room webcast_id |

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
        "id_str": "7703585232380857123",
        "like_count": 0,
        "linker_map": {}
      }
    ],
    "enter_mode": 0,
    "enter_room_id": "7703585232380857123",
    "partition_road_map": {},
    "qrcode_url": "",
    "room_status": 2,
    "shark_decision_conf": "",
    "similar_rooms": [],
    "user": {
      "avatar_thumb": {
        "url_list": [
          "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_3d5484c1ffb…"
        ]
      },
      "follow_info": {
        "follow_status": 0,
        "follow_status_str": "0"
      },
      "foreign_user": 0,
      "id_str": "1722258143337120",
      "nickname": "邓雨馨",
      "open_id_str": "",
      "sec_uid": "MS4wLjABAAAAfa6fIQF7wchh5UAYU6WgfR00rGeUCzBk5YBKsz-r4Ocza5JivsqLC0qild84a_pE"
    }
  },
  "extra": {
    "now": 1793691154095
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.enter_room_id` | ID of the room that matches the `webcast_id`. Use it as the room ID in other live room calls. |
| `data.room_status` | Numeric status of the room as a whole. The response gives no label for the values. |
| `data.data[].id_str` | Room ID as a string. In this response it equals `data.enter_room_id`. |
| `data.data[].title` | Title of the live room, as set by the host. |
| `data.data[].status / data.data[].status_str` | Numeric status of the room entry and the same value as a string. |
| `data.data[].user_count_str` | Viewer count for the room, given as a string. |
| `data.data[].like_count` | Like count for the room. |
| `data.data[].has_commerce_goods` | Shows `true` if the room has commerce goods attached, `false` if not. |
| `data.user.nickname` | Display name of the host. |
| `data.user.sec_uid` | Encrypted user ID of the host. Use it with APIs that take a `sec_user_id`. |
| `data.user.id_str` | Numeric ID of the host, as a string. |
| `data.user.avatar_thumb.url_list[]` | Image URLs for the host's small avatar (100x100). |

### Notes

- Send the room's `webcast_id` as a string. Use [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id) to pull it from live room links.
- Use `data.user.sec_uid` with [Douyin User Profile (Web)](/apis/douyin/web/user-profile) to load the host's profile.
- `extra.now` holds a numeric timestamp for the response, and `status_code` is `0` on success.
- Many fields in the sample, such as `admin_user_ids` and `similar_rooms`, are empty or zero.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos.json`](../../../../catalog/models/douyin/web/user-live-videos.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos
