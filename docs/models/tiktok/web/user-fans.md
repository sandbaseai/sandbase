# TikTok User Followers API: pricing, parameters and code examples

`tiktok/web/user-fans` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified TikTok profile along with follower account stats. Supports pagination through cursor and count parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-fans", "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-fans', {'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-fans", {
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-fans", sandbase.Params{
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page  |
| `secUid` | string | yes | User secUid  |
| `maxCursor` | integer |  | Max cursor  |
| `minCursor` | integer |  | Min cursor  |

## Details

Retrieve followers for a specific TikTok profile by providing the account's `secUid`. Results can be paginated using `maxCursor`, `minCursor`, and `count`.

### Use cases

- Analyze the follower composition and engagement metrics of a TikTok creator.
- Inspect follower accounts for verification status and interaction counts.
- Export follower lists for audience research and influencer network mapping.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-fans" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page |
| `maxCursor` | integer | No | Max cursor |
| `minCursor` | integer | No | Min cursor |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "userList": [
    {
      "stats": {
        "diggCount": 317,
        "followerCount": 84,
        "followingCount": 222,
        "friendCount": 0,
        "heartCount": 0,
        "videoCount": 1
      },
      "statsV2": {
        "diggCount": "317",
        "followerCount": "84",
        "followingCount": "222",
        "friendCount": "0",
        "heartCount": "0",
        "videoCount": "1"
      },
      "user": {
        "id": "7683196544857965588",
        "nickname": "<user>",
        "privateAccount": false,
        "verified": false
      }
    }
  ]
}
```

### Notes

- Specify the target account using `secUid`.
- Paginate through results using `maxCursor`, `minCursor`, and `count`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-fans.json`](../../../../catalog/models/tiktok/web/user-fans.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-fans
