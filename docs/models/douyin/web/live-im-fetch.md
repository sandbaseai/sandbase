# Douyin Room Danmaku Parameters API: pricing, parameters and code examples

`douyin/web/live-im-fetch` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves chat and danmaku parameters for a Douyin broadcast session. Requires the target room identifier and user unique identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/live-im-fetch", "room_id": "example", "user_unique_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/live-im-fetch', {'room_id': 'example', 'user_unique_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/live-im-fetch", {
  "room_id": "example",
  "user_unique_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/live-im-fetch", sandbase.Params{
	"room_id": "example",
	"user_unique_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/live-im-fetch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |
| `user_unique_id` | string | yes | User unique ID  |

## Details

Returns a batch of chat messages for a Douyin live room, plus cursor values in the `extra` object. It needs the `room_id` of the broadcast and a `user_unique_id`.

### Use cases

- Store the system and chat messages of a Douyin live room as they arrive.
- Use the `common.method` value of each message to separate room notices from other message types.
- Save the `extra.cursor` value from each call to track where a room's message stream stood.
- Use `common.create_time` to build a timeline of a broadcast.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/live-im-fetch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7382517534467115826", "user_unique_id": "7382524529011246630"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |
| `user_unique_id` | string | Yes | User unique ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "common": {
        "create_time": 1793691147063,
        "is_show_msg": true,
        "method": "WebcastRoomMessage",
        "msg_id": 7703844818881794276,
        "play_time": 0,
        "room_id": 7382517534467115826
      },
      "content": "欢迎来到直播间！抖音严禁未成年人直播或礼物消费。严禁违法违规、低俗色情、吸烟酗酒、人身伤害等直播内容。理性消费，如主播在直播中以不当方式诱导消费，请谨慎辨别。切…"
    }
  ],
  "extra": {
    "cursor": "r-1_d-1_u-1_h-1_t-1793691147079",
    "fetch_interval": 1000,
    "live_cursor": "u-1_d-1",
    "now": 1793691147079
  },
  "internal_ext": "internal_src:dim|wss_push_room_id:7382517534467115826|wss_push_did:7571816300415…",
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].common.method` | Message type name. The sample value is `WebcastRoomMessage`, a room notice. |
| `data[].common.msg_id` | Numeric ID of the message. |
| `data[].common.room_id` | ID of the live room the message belongs to. |
| `data[].common.create_time` | Time the message was created, as a 13-digit number that looks like a millisecond Unix timestamp. |
| `data[].common.is_show_msg` | Whether the message is meant to be shown in the chat. The sample value is `true`. |
| `data[].content` | Text of the message. In the sample it is the welcome and safety notice for the room, in Chinese. |
| `extra.cursor` | Cursor string for this batch. It ends with a `t-` value that matches `extra.now`. |
| `extra.live_cursor` | A second, shorter cursor string, `u-1_d-1` in the sample. |
| `extra.fetch_interval` | Fetch interval value. The sample value is `1000`. |
| `extra.now` | Time of the response as a 13-digit number that looks like a millisecond timestamp. |

### Notes

- `room_id` is a numeric ID such as `7382517534467115826`. To get it from a webcast ID, call [Douyin Webcast ID to Room ID](/apis/douyin/web/webcast-id-2-room-id).
- `status_code` is `0` in the sample response.
- `internal_ext` is a pipe-separated text string. In the sample it repeats the room ID and the fetch time.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/live-im-fetch.json`](../../../../catalog/models/douyin/web/live-im-fetch.json) · Store page: https://www.sandbase.ai/model/douyin/web/live-im-fetch
