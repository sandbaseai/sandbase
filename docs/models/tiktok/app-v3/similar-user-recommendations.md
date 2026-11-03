# TikTok Similar User Recommendations API: pricing, parameters and code examples

`tiktok/app-v3/similar-user-recommendations` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended similar user profiles for a target TikTok account based on its secure user identifier, with support for cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
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

Returns a list of TikTok accounts that TikTok recommends as similar to a target account. The input is the target account's `sec_uid`. Each user object holds profile counts, avatar images and account settings.

### Use cases

- Find creators close to a known account to build a list of competitors in the same niche.
- Grow an influencer shortlist by starting from one strong creator and collecting the accounts TikTok suggests next to it.
- Compare `follower_count` across recommended accounts to sort lookalike creators by audience size.
- Map clusters of related accounts by calling the endpoint again with the `sec_uid` of each recommended user.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/similar-user-recommendations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid |
| `page_token` | string | No | Page token, not required for the first request, for subsequent requests, pass the next_page_token value from the previous response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_more": true,
  "next_page_token": "MzA=",
  "status_code": 0,
  "status_msg": "",
  "users": [
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
        "uri": "tos-useast5-avt-0068-tx/94f94830ec139c3b89320167da2acc60",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/94f94830ec139c3…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_300x300": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/94f94830ec139c3b89320167da2acc60",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/94f94830ec139c3…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_larger": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/94f94830ec139c3b89320167da2acc60",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/94f94830ec139c3…"
        ],
        "url_prefix": null,
        "width": 720
      },
      "avatar_medium": {
        "data_size": 0,
        "height": 720,
        "uri": "tos-useast5-avt-0068-tx/94f94830ec139c3b89320167da2acc60",
        "url_list": [
          "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/94f94830ec139c3…"
        ],
        "url_prefix": null,
        "width": 720
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of recommended accounts. Each item is one user profile. |
| `users[].follower_count` | Number of followers the recommended account has. |
| `users[].aweme_count` | Number of videos the account has posted. |
| `users[].favoriting_count` | Count of favorites on the account, as returned by TikTok. |
| `users[].create_time` | Account creation time as a Unix timestamp in seconds (for example `1581743982`). |
| `users[].custom_verify` | Verification label text for the account. It is an empty string when the account has no label. |
| `users[].avatar_larger / users[].avatar_medium / users[].avatar_thumb` | Avatar images in different sizes. Each has a `uri` and a `url_list` with several image URLs. |
| `users[].avatar_uri` | Identifier of the avatar image. |
| `has_more` | `true` when more recommended users can be fetched with another call. |
| `next_page_token` | Token to pass as `page_token` to get the next batch. |

### Notes

- Pass the target account's `sec_uid` in `sec_uid`. To get a `sec_uid` from a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- Leave `page_token` out on the first request. When `has_more` is `true`, send the `next_page_token` value as `page_token` in the next request.
- To read the full profile of a recommended account, call [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/similar-user-recommendations.json`](../../../../catalog/models/tiktok/app-v3/similar-user-recommendations.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/similar-user-recommendations
