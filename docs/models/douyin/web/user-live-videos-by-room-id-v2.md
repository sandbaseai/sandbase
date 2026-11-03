# Douyin Stream Data by Room ID (V2) API: pricing, parameters and code examples

`douyin/web/user-live-videos-by-room-id-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns stream data for a specified Douyin user using a room identifier. Provide a valid room ID to inspect stream metadata and broadcast details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos-by-room-id-v2", "room_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos-by-room-id-v2', {'room_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos-by-room-id-v2", {
  "room_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos-by-room-id-v2", sandbase.Params{
	"room_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos-by-room-id-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Room room_id  |

## Details

Returns the live room record for one Douyin room, looked up by `room_id`. The response holds cover image data, e-commerce flags, room settings and a map of anchor feature flags.

### Use cases

- Read the cover image URL and average color of a Douyin live room for display in a monitoring dashboard.
- Check whether a live room shows a shopping cart by reading the e-commerce settings.
- Inspect room-level flags such as virtual anchor status or geo block before further processing.
- Log the server timestamp of each lookup to track when a room record was fetched.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos-by-room-id-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7462723839303093032"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Room room_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "AnchorABMap": {
      "ab_admin_comment_on_wall": "0",
      "ab_friend_chat": "4",
      "admin_privilege_refine": "2",
      "allow_shared_to_fans": "false",
      "audience_linkmic_continue": "0",
      "audio_double_enlarge_enable": "1",
      "audio_room_subtitle_opt": "3",
      "battle_match_rebuild_anchor": "2",
      "big_party_enable_open_camera": "2",
      "chat_intercommunicate_multi_anchor": "2",
      "chat_intercommunicate_pk": "2",
      "double_enlarge_enable": "1"
    },
    "acquaintance_status": 0,
    "admin_user_ids": [],
    "admin_user_open_ids": [],
    "anchor_scheduled_time_text": "",
    "anchor_share_text": "",
    "anchor_tab_type": 0,
    "app_id": 0,
    "assist_label_list": [],
    "auth_city": "",
    "auto_cover": 0,
    "base_category": 0
  },
  "extra": {
    "now": 1793691152950
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.cover.url_list[]` | Cover image URLs for the room. Each entry is a signed link to the same image on a different host. |
| `data.cover.uri / data.cover.avg_color` | `uri` is the cover image identifier. `avg_color` is the average color of the image as a hex code. |
| `data.cover.width / data.cover.height` | Cover image size values. Both are `0` in the sample response. |
| `data.ecom_data.room_cart_v2.show_cart` | Numeric flag for the room shopping cart display. The sample value is `2`. |
| `data.extra.is_virtual_anchor` | Boolean that shows whether the anchor is a virtual anchor. |
| `data.extra.geo_block` | Numeric geo block flag for the room. The sample value is `0`. |
| `data.AnchorABMap` | Map of feature flag names to string values for the anchor. Use it to see which room features are set. |
| `data.admin_user_ids[]` | List of room admin user IDs. It is empty in the sample response. |
| `data.business_live / data.category / data.create_time` | Numeric room attributes. All are `0` in the sample response, so they carry no detail for this room. |
| `extra.now` | Timestamp of the response in milliseconds, as shown by the 13-digit value. |

### Notes

- Pass `room_id` as a string, for example `7462723839303093032`.
- To get a `room_id` from a live room link, call [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id) to get the webcast ID, then [Douyin Webcast ID to Room ID](/apis/douyin/web/webcast-id-2-room-id).
- A `status_code` of `0` appears in the sample response alongside the `data` object.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos-by-room-id-v2.json`](../../../../catalog/models/douyin/web/user-live-videos-by-room-id-v2.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos-by-room-id-v2
