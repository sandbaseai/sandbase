# TikTok User Likes

`tiktok/web/user-like` · api · TikTok

Returns a list of videos liked by a specific TikTok profile based on their secUid. Supports pagination via cursor tokens and optional sort type settings.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-like", "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-like', {'secUid': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-like", {
  "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-like", sandbase.Params{
	"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-like` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default is 20, cannot be changed.  |
| `cursor` | integer |  | Page cursor  |
| `secUid` | string | yes | User secUid  |
| `coverFormat` | integer |  | Cover format  |
| `post_item_list_request_type` | integer |  | Sort type  |

## Details

Fetch videos liked by a TikTok account by supplying the target user's `secUid`. Paginate through past likes using the `cursor` parameter.

### Use cases

- Inspect public videos liked by a specific TikTok creator.
- Analyze content preferences and engagement trends of a target user.
- Collect user liked video records for audience research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-like" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page, default is 20, cannot be changed. |
| `cursor` | integer | No | Page cursor |
| `coverFormat` | integer | No | Cover format |
| `post_item_list_request_type` | integer | No | Sort type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "statusCode": 0,
  "status_code": 0
}
```

### Notes

- The `count` parameter defaults to 20 and cannot be changed.
- Use `cursor` for pagination across result pages.
- The target user's `secUid` is required.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-like.json`](../../../../catalog/models/tiktok/web/user-like.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-like
