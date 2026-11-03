# Twitter User Profile API: pricing, parameters and code examples

`twitter/user-detail` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get an X (Twitter) user profile identified by its numeric Rest ID. Use it to review a known account before monitoring its posts or conducting creator and account research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/user-detail", "restId": "44196397"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/user-detail', {'restId': '44196397'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/user-detail", {
  "restId": "44196397"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/user-detail", sandbase.Params{
	"restId": "44196397",
})
```

Same call via the path form: `POST /v1/api/twitter/user-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `restId` | string | yes | The unique numeric identifier (Rest ID) for the X user.  |

## Details

Returns the public profile of one X (Twitter) account, including its handle, display name, follower count, post count and verification flags. It needs the account's numeric Rest ID in `restId`.

### Use cases

- Check an account's handle, name and status before you start monitoring its posts.
- Compare follower counts and post counts across creators during account research.
- Find the pinned post of an account by reading its post ID.
- Confirm whether an account is protected or still active before you pull data for it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/user-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"restId": "44196397"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `restId` | string | Yes | The unique numeric identifier (Rest ID) for the X user. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "affiliates": {
    "label": {
      "badge": {
        "url": "https://pbs.twimg.com/profile_images/1955359038532653056/OSHY3ewP_bigger.jpg"
      },
      "description": "X",
      "url": {
        "url": "https://twitter.com/X",
        "urlType": "DeepLink"
      },
      "userLabelDisplayType": "Badge",
      "userLabelType": "BusinessLabel"
    }
  },
  "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
  "blue_verified": true,
  "business_account": null,
  "created_at": "Tue Jun 02 20:12:29 +0000 2009",
  "desc": "https://t.co/ZdBx5WABYx",
  "friends": 1421,
  "header_image": "https://pbs.twimg.com/profile_banners/44196397/1774145451",
  "id": "44196397",
  "location": "",
  "media_count": 4756,
  "name": "Elon Musk"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `rest_id / id` | The numeric Rest ID of the account, returned as a string. Both fields hold the same value as the `restId` you sent. |
| `profile` | The account's handle, without the @ sign (for example `elonmusk`). |
| `name` | The display name shown on the profile. |
| `sub_count` | The follower count of the account. |
| `friends` | The number of accounts this user follows. |
| `statuses_count / media_count` | Total posts by the account, and the number of posts with media. |
| `created_at` | When the account was created, as a text timestamp such as `Tue Jun 02 20:12:29 +0000 2009`. |
| `blue_verified / verification_type` | `blue_verified` is a true or false flag for X Premium verification. `verification_type` is `null` when no other verification type is set. |
| `protected / status` | `protected` shows whether the account's posts are private. `status` shows the account state, such as `active`. |
| `pinned_tweet_ids_str[]` | IDs of the posts pinned to the profile. |
| `avatar / header_image` | URLs of the profile picture and the banner image. |
| `affiliates.label.description` | Name of the business or organization label shown on the profile, such as `X`. |

### Notes

- Pass the numeric Rest ID as a string in `restId`, for example `44196397`. The API does not accept a handle.
- Use the IDs in `pinned_tweet_ids_str[]` with [Twitter Tweets by IDs](/apis/twitter/tweets-by-ids) to load the pinned posts.
- Call [Twitter User Published Posts](/apis/twitter/user-posts) to read the account's posts, or [X / Twitter Followers](/apis/twitter/followers) to list its followers.
- The `desc` field can hold a shortened `t.co` link instead of the full bio text.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/user-detail.json`](../../../catalog/models/twitter/user-detail.json) · Store page: https://www.sandbase.ai/model/twitter/user-detail
