# Twitter List followers API: pricing, parameters and code examples

`twitter/web/list-followers` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get list followers on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/list-followers", "list_id": "84839422"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/list-followers', {'list_id': '84839422'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/list-followers", {
  "list_id": "84839422"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/list-followers", sandbase.Params{
	"list_id": "84839422",
})
```

Same call via the path form: `POST /v1/api/twitter/web/list-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `list_id` | string | yes | List ID  |

## Details

Returns the users who follow a Twitter list, with profile details for each follower. It needs a `list_id`, and you can pass a `cursor` to get the next page.

### Use cases

- Build an audience list of accounts that follow a curated Twitter list.
- Check how large and how active the following of a topic list is.
- Collect new follower accounts of a list over time and compare them by `created_at`.
- Screen followers of a list for low-activity accounts using `statuses_count` and `followers_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/list-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"list_id": "84839422"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `list_id` | string | Yes | List ID |
| `cursor` | string | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "followers": [
    {
      "affiliates": [],
      "blue_verified": false,
      "business_account": null,
      "created_at": "Fri Jun 05 19:47:39 +0000 2026",
      "description": "",
      "followers_count": 0,
      "friends_count": 110,
      "location": "",
      "media_count": 0,
      "name": "بهاء عطيه",
      "profile_image": null,
      "screen_name": "nailom732gmail"
    }
  ],
  "more_users": true,
  "next_cursor": "1871166145375739390|2117523426632531946",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followers[].user_id` | ID of the follower account, as a string. |
| `followers[].screen_name / followers[].name` | The follower's handle and display name. |
| `followers[].description / followers[].location / followers[].website` | Profile bio, location text and website. These can be empty strings or `null`. |
| `followers[].followers_count / followers[].friends_count` | Number of accounts that follow this user, and number of accounts this user follows. |
| `followers[].statuses_count / followers[].media_count` | Number of posts and number of media posts on the account. |
| `followers[].created_at` | Date the account was created, in the format `Fri Jun 05 19:47:39 +0000 2026`. |
| `followers[].verified / followers[].blue_verified` | Whether the account is verified, and whether it has the Blue verified badge. |
| `more_users` | `true` when more followers are available on another page. |
| `next_cursor` | Value to send as `cursor` to get the next page. |

### Notes

- Send the `next_cursor` value from the response as `cursor` in the next request. Keep the same `list_id`.
- Stop paging when `more_users` is `false`.
- `user_id` is a numeric string. Use it with [Twitter (X) User Profile](/apis/twitter/web/user-profile) to look up a follower in more detail.
- To get the people who belong to the list instead of its followers, use [Twitter List members](/apis/twitter/web/list-members).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/list-followers.json`](../../../../catalog/models/twitter/web/list-followers.json) · Store page: https://www.sandbase.ai/model/twitter/web/list-followers
