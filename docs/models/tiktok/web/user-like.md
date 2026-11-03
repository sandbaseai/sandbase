# TikTok User Likes API: pricing, parameters and code examples

`tiktok/web/user-like` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of videos liked by a specific TikTok profile based on their secUid. Supports pagination via cursor tokens and optional sort type settings.

## Pricing

- **$0.001 per call** (USD)
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

Returns a page of videos liked by a TikTok profile. It needs the profile's `secUid` as input and returns a cursor for the next page.

### Use cases

- Check which public videos a specific TikTok creator has liked.
- Page through a user's like history to build a record of the content they engage with.
- Collect liked-video data for audience research on a target account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-like" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | Yes | User secUid |
| `count` | integer | No | Number per page, default is 20, cannot be changed. |
| `coverFormat` | integer | No | Cover format |
| `cursor` | integer | No | Page cursor |
| `post_item_list_request_type` | integer | No | Sort type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cookie": "tt_chain…",
  "cursor": "1791417327000",
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031544314BAB8FBD2CDB3104FCC3",
    "now": 1793691871000
  },
  "hasMore": true,
  "log_pb": {
    "impr_id": "202611031544314BAB8FBD2CDB3104FCC3"
  },
  "statusCode": 0,
  "status_code": 0,
  "status_msg": "",
  "tt_chain_token": "0k5cdiqY…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `cursor` | Cursor value for the next page. Pass it as `cursor` in the next request to continue. |
| `hasMore` | `true` when more liked videos remain after this page. |
| `statusCode / status_code` | Result code of the call. `0` means the request succeeded. |
| `status_msg` | Status message text. It is an empty string in this response. |
| `extra.fatal_item_ids` | List of item IDs that could not be returned. It is empty in this response. |
| `extra.now` | Server timestamp of the response, as a 13-digit number. |
| `extra.logid / log_pb.impr_id` | Request log identifier. Both fields hold the same value in this response. |

### Notes

- Get the `secUid` for a profile with [TikTok Profile Sec User ID](/apis/tiktok/web/sec-user-id), or from profile links with [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id).
- To fetch the next page, send the returned `cursor` value as the `cursor` parameter while `hasMore` is `true`.
- The `count` parameter defaults to 20 and cannot be changed.
- The trimmed response shown here does not include a video list. Check the full response for the liked video items.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-like.json`](../../../../catalog/models/tiktok/web/user-like.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-like
