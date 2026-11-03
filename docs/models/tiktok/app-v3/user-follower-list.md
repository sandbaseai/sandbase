# TikTok User Follower List API: pricing, parameters and code examples

`tiktok/app-v3/user-follower-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the follower list for a specified TikTok profile. Supports paging with timestamp and token parameters, requiring either a numeric user ID or secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-follower-list", "count": 20, "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-follower-list', {'count': 20, 'sec_user_id': 'MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-follower-list", {
  "count": 20,
  "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-follower-list", sandbase.Params{
	"count": 20,
	"sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, do not exceed 20, keep it fixed.  |
| `user_id` | string |  | User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id)  |
| `min_time` | integer |  | Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests.  |
| `page_token` | string |  | Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests.  |
| `sec_user_id` | string |  | User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id)  |

## Details

Returns a page of followers for a TikTok profile. Each follower comes back as a user object with counts, avatar images and account settings. The input is either the numeric `user_id` or the `sec_user_id` of the profile.

### Use cases

- Sample the followers of a creator to see what kind of accounts follow them.
- Page through a follower list to build an audience research dataset.
- Compare follower account ages and sizes to spot accounts that look new or inactive.
- Collect follower profile details to feed into a lookup of each follower's videos or profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-follower-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "7486586574684881927", "sec_user_id": "MS4wLjABAAAA0lKrE0cVLLZCnVil-n-YEZlOoik9oeO3zOYQ08dqOEOw2pRSXWJdcSFw7lZeZcSP", "count": 20, "min_time": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, do not exceed 20, keep it fixed. |
| `min_time` | integer | No | Minimum time for paging, use default value 0 for the first request, and use the min_time value returned by the last request for subsequent requests. |
| `page_token` | string | No | Page token, use default value "" for the first request, and use the page_token value returned by the last request for subsequent requests. |
| `sec_user_id` | string | No | User sec_user_id, this is a mixed letter and number version ID (one of user_id and sec_user_id) |
| `user_id` | string | No | User ID, this is a pure numeric version of the user ID (one of user_id and sec_user_id) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074400C5EEACA4AB247225B1A3",
    "now": 1793691840000
  },
  "followers": [
    {
      "accept_private_policy": false,
      "account_labels": null,
      "account_region": "",
      "ad_cover_url": null,
      "advance_feature_item_order": null,
      "advanced_feature_info": null,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-maliva-avt-0068/7333682529319895046",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/7333682529319895046…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_300x300": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-maliva-avt-0068/7333682529319895046",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/7333682529319895046…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_larger": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-maliva-avt-0068/7333682529319895046",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/7333682529319895046…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_medium": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-maliva-avt-0068/7333682529319895046",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/7333682529319895046…"
        ],
        "url_prefix": null,
        "width": 720
      }
    }
  ],
  "has_more": true,
  "log_pb": {
    "impr_id": "20261103074400C5EEACA4AB247225B1A3"
  },
  "max_time": 1793691840,
  "min_time": 1793566415,
  "myself_user_id": "0",
  "next_page_token": "eyJtYXhf…",
  "offset": 0,
  "status_code": 0,
  "status_msg": "",
  "total": 52527
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followers[]` | One follower account per item. Each item is a full user object. |
| `followers[].follower_count` | Number of followers that this follower account has. |
| `followers[].aweme_count` | Number of videos posted by this follower account. |
| `followers[].favoriting_count` | Count of favorites on this follower account, as returned in the `favoriting_count` field. |
| `followers[].create_time` | Account creation time as a Unix timestamp in seconds. |
| `followers[].avatar_thumb / followers[].avatar_medium / followers[].avatar_larger` | Avatar image objects in different sizes. Each has a `url_list` of image links, plus `width` and `height`. |
| `followers[].avatar_uri` | Internal path of the follower's avatar image. |
| `followers[].follow_status / followers[].follower_status` | Relationship status flags for the follower account. Both are `0` in the sample. |
| `extra.now` | Server time of the response as a Unix timestamp in milliseconds. |
| `extra.logid` | Request log ID that you can quote when reporting a problem. |

### Notes

- Pass either `user_id` (numeric) or `sec_user_id` (letters, numbers, dashes). To find them from a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- Set `count` to 20 or less. For the first page, send `min_time` as `0` and `page_token` as an empty string.
- For the next page, send the `min_time` and `page_token` values returned by the previous call.
- To see who the account follows, call [TikTok User Following List](/apis/tiktok/app-v3/user-following-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-follower-list.json`](../../../../catalog/models/tiktok/app-v3/user-follower-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-follower-list
