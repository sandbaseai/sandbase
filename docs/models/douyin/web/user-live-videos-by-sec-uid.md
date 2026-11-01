# Douyin User Broadcast Videos

`douyin/web/user-live-videos-by-sec-uid` · api · Douyin

Returns broadcast video data for a specified Douyin user using their security identifier. Provide the account identifier to inspect streaming content and badge details.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/user-live-videos-by-sec-uid", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/user-live-videos-by-sec-uid', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/user-live-videos-by-sec-uid", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/user-live-videos-by-sec-uid", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/user-live-videos-by-sec-uid` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_uid, also called sec_user_id, can be found in the user's homepage link.  |

## Details

Retrieve broadcast video data for a specific user using their `sec_uid`. This endpoint inspects streaming records and related badge data from web profiles.

### Use cases

- Inspect broadcast video records for a target account.
- Monitor streamer profile activity and badge information.
- Gather streaming media details for creator analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/user-live-videos-by-sec-uid" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid, also called sec_user_id, can be found in the user's homepage link. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "badge_image_list": [
      {
        "image_type": 1,
        "content": {
          "alternative_text": "荣誉等级21级勋章"
        }
      }
    ]
  }
}
```

### Notes

- Find `sec_uid` (also referred to as sec_user_id) within the target user's homepage URL.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/model/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/model/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/model/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/user-live-videos-by-sec-uid.json`](../../../../catalog/models/douyin/web/user-live-videos-by-sec-uid.json) · Store page: https://www.sandbase.ai/model/douyin/web/user-live-videos-by-sec-uid
