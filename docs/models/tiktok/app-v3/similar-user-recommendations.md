# TikTok Similar User Recommendations

`tiktok/app-v3/similar-user-recommendations` · api · TikTok

Returns recommended similar user profiles for a target TikTok account based on its secure user identifier, with support for cursor-based pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/similar-user-recommendations", "sec_uid": "MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/similar-user-recommendations', {'sec_uid': 'MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/similar-user-recommendations", {
  "sec_uid": "MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/similar-user-recommendations", sandbase.Params{
	"sec_uid": "MS4wLjABAAAA2_YTgxz3kLb2XoyC3xOXnosim3gdiqMtFHnjRvckabZJFQ40XBOVttDCiB5cwa3b",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/similar-user-recommendations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_uid  |
| `page_token` | string |  | Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response.  |

## Details

Use this endpoint to look up accounts similar to a target TikTok profile using its `sec_uid` parameter. Subsequent batches can be retrieved by providing the `page_token`.

### Use cases

- Discover comparable creators within the same niche or topic.
- Expand influencer research by finding related TikTok accounts.
- Analyze audience overlap and creator recommendation clusters.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/similar-user-recommendations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid |
| `page_token` | string | No | Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "apple_account": 0,
      "authority_status": 0,
      "aweme_count": 448,
      "comment_filter_status": 0,
      "create_time": 1734207833,
      "favoriting_count": 1105,
      "fb_expire_time": 0,
      "follow_status": 0,
      "follower_count": 888639,
      "follower_status": 0,
      "matched_friend": {
        "face_cover_num": 0,
        "friend_relation_type": 0,
        "label_type": "5-0",
        "rec_type": "5-0",
        "relation_type": "43"
      },
      "original_musician": {
        "digg_count": 0,
        "music_count": 0,
        "music_used_count": 0
      }
    }
  ]
}
```

### Notes

- Requires the target user's `sec_uid`.
- For subsequent requests, pass the previous response's next page token into `page_token`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/similar-user-recommendations.json`](../../../../catalog/models/tiktok/app-v3/similar-user-recommendations.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/similar-user-recommendations
