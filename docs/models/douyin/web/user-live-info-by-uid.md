# Douyin User Stream Information by UID API: pricing, parameters and code examples

`douyin/web/user-live-info-by-uid` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves stream session information and broadcast metadata for a Douyin user based on their unique identifier. Accepts a user UID to return stream scene and logging data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-info-by-uid", "uid": "7673500446660873006"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-info-by-uid', {'uid': '7673500446660873006'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-info-by-uid", {
  "uid": "7673500446660873006"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-info-by-uid", sandbase.Params{
	"uid": "7673500446660873006",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-info-by-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User UID  |

## Details

This API takes a Douyin user `uid` and returns a short record with stream session metadata. The response holds a `log_id`, a `scene_id` and a `user_live` list. In the sample response, `user_live` is empty.

### Use cases

- Check whether a Douyin account has any entries in `user_live` for a known `uid`.
- Store the `log_id` of each lookup to trace a specific request in your own logs.
- Run a quick check on a list of creator UIDs before calling heavier live-room APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-info-by-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "92769419069"}'
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
  "data": [
    {
      "log_id": "2026110315323230CB2D8E36B04148220A",
      "scene_id": 253,
      "user_live": []
    }
  ],
  "extra": {
    "now": 1793691152930
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | List of result objects for the requested `uid`. The sample holds one object. |
| `data[].user_live` | List of stream entries for the user. It is an empty list in the sample response, which means no stream entries came back for that `uid`. |
| `data[].log_id` | String that identifies this lookup. Its first 14 digits look like a date and time, but the time zone is not shown. |
| `data[].scene_id` | Number that labels the scene of the request. The sample value is `253`. |
| `extra.now` | Server time as a 13-digit number, which looks like a Unix timestamp in milliseconds. |
| `status_code` | Status of the call. `0` in the sample response. |

### Notes

- The `uid` is the numeric user ID as a string, for example `92769419069`.
- If you only have a `sec_user_id`, or need the reverse, use [Douyin UID to Sec User ID](/apis/douyin/web/encrypt-uid-to-sec-user-id) to convert IDs.
- To see profile details for the same `uid`, call [Douyin User Profile by UID](/apis/douyin/web/user-profile-by-uid).
- To get live room data once you have a room ID, call [Douyin Stream Data by Room ID (V2)](/apis/douyin/web/user-live-videos-by-room-id-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-info-by-uid.json`](../../../../catalog/models/douyin/web/user-live-info-by-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-info-by-uid
