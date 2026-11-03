# Twitter Profiles by rest ids API: pricing, parameters and code examples

`twitter/web/user-profiles-by-rest-ids` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get profiles by rest ids on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-profiles-by-rest-ids", "rest_ids": "44196397,34743251"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-profiles-by-rest-ids', {'rest_ids': '44196397,34743251'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-profiles-by-rest-ids", {
  "rest_ids": "44196397,34743251"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-profiles-by-rest-ids", sandbase.Params{
	"rest_ids": "44196397,34743251",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-profiles-by-rest-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `rest_ids` | string | yes | User IDs, comma separated  |

## Details

Returns profile data for several Twitter accounts in one call. You pass a comma separated list of numeric user IDs (`rest_ids`) and get one entry per account in `users`.

### Use cases

- Resolve a list of stored Twitter user IDs into current handles and display names.
- Check whether a batch of accounts is still `active` or has `protected` tweets.
- Look up the account creation date and Blue verification status for a set of accounts.
- Collect avatar URLs and affiliation badges for accounts shown in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-profiles-by-rest-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"rest_ids": "44196397,34743251"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rest_ids` | string | Yes | User IDs, comma separated |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "users": [
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
      "can_dm": null,
      "created_at": "Tue Jun 02 20:12:29 +0000 2009",
      "desc": null,
      "favourites": null,
      "friends": null,
      "header_image": null,
      "id": "44196397",
      "location": ""
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[].rest_id / users[].id` | The numeric Twitter user ID as a string. Both keys hold the same value in the response. |
| `users[].profile` | The account handle (screen name) without the @ sign, such as `elonmusk`. |
| `users[].name` | The display name of the account. |
| `users[].created_at` | The account creation time as a text date, for example `Tue Jun 02 20:12:29 +0000 2009`. |
| `users[].blue_verified` | `true` when the account has Blue verification. |
| `users[].protected` | `true` when the account's tweets are protected. |
| `users[].status` | The account state. Both sample accounts return `active`. |
| `users[].avatar` | URL of the profile image. |
| `users[].location` | The location text from the profile. It can be an empty string. |
| `users[].affiliates.label.description` | Name of the organization shown in the affiliation badge, such as `X`. For accounts with no affiliation, `affiliates` is an empty list. |

### Notes

- Pass several IDs in `rest_ids` separated by commas, for example `44196397,34743251`.
- Fields such as `desc`, `friends`, `statuses_count` and `sub_count` came back as `null` in this sample. Call [Twitter (X) User Profile](/apis/twitter/web/user-profile) or [Twitter User about profile](/apis/twitter/web/user-about) for more account details.
- To get the posts of an account, use [Twitter (X) User Posts](/apis/twitter/web/user-post-tweet) with the same user ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/user-profiles-by-rest-ids.json`](../../../../catalog/models/twitter/web/user-profiles-by-rest-ids.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-profiles-by-rest-ids
