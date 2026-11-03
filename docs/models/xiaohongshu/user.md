# Xiaohongshu User Profile API: pricing, parameters and code examples

`xiaohongshu/user` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a Xiaohongshu (RedNote) user profile from a user ID or supported profile URL. Use it to support creator discovery, account research, and reviewing a known profile before related content analysis.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/user", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/user', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/user", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/user", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | A Xiaohongshu user ID or a profile URL containing /user/profile/.  |

## Details

Returns a Xiaohongshu (RedNote) user profile for one account. It needs a `userId`, which can be a user ID or a profile URL containing `/user/profile/`. The response includes the bio, follower and like totals, IP location, account type and live status.

### Use cases

- Check a creator's follower count and total likes before you plan a collaboration.
- Confirm that an account is an enterprise account and read its bio before you do account research.
- Check whether a known account is live right now and get its room ID.
- Track a profile's `fans`, `liked` and `collected` totals over time by calling it on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | A Xiaohongshu user ID or a profile URL containing /user/profile/. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "atme_notes_num": 1,
  "avatar_handle_entry_list": [],
  "avatar_like_status": false,
  "avatar_pendant": {
    "current_user_pendant": false,
    "current_user_pet": false
  },
  "banner_info": {
    "bg_color": "b8a1b3",
    "image": "http://sns-avatar-qc.rednotecdn.com/user_banner/1040g2k031qnj00er74005p5oj0ol6up…",
    "like_status": false
  },
  "block_view_from_user": false,
  "block_view_to_user": false,
  "blocked": false,
  "blocking": false,
  "brand_account_info": {
    "account_type_name": "企业账号",
    "conversions": [
      {
        "icon": "https://picasso-static.xiaohongshu.com/fe-platform/fb51da952d69f3cc44a174ff85dcc…",
        "id": "11",
        "is_red_shop": false,
        "is_shop": false,
        "link": "xhsdiscover://message/userPublicGroupList?user_id=64b898310000000014037b21&usern…",
        "name": "Group chat",
        "sub_title": "View details"
      }
    ],
    "trade_type_first_name": ""
  },
  "collected": 3152959,
  "collected_book_num": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `desc` | The profile bio text. Line breaks appear as `\n`. |
| `fans / follows` | The number of followers and the number of accounts this user follows. |
| `liked / collected` | Total likes and total saves this account has received on its content. |
| `interactions[]` | Summary counters shown on the profile. Each row has `type`, `name`, `count` and `is_private`. When `is_private` is `true`, the user has hidden that list from view. |
| `gender` | Numeric gender code. The sample value is `2`. The response does not define the codes. |
| `ip_location` | The location label shown on the profile, such as `湖南`. |
| `brand_account_info.account_type_name` | The account type label. The sample shows `企业账号` (enterprise account). |
| `images / imageb` | Avatar image URLs. `images` is the smaller version and `imageb` is the larger version. |
| `banner_info.image` | URL of the profile banner image. |
| `live.live_status / live.room_id / live.start_time` | The live stream state, the room ID, and the start time as a millisecond timestamp. |

### Notes

- Take `userId` from the profile URL, where it follows `/user/profile/`. You can also paste the full profile URL.
- To find a user ID by name, call [Xiaohongshu (RED) User Search](/apis/xiaohongshu/app-v2/search-users).
- To read this user's posts next, call [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes) with the same ID.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/user.json`](../../../catalog/models/xiaohongshu/user.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/user
