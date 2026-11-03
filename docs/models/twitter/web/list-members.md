# Twitter List members API: pricing, parameters and code examples

`twitter/web/list-members` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get list members on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/list-members", "list_id": "84839422"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/list-members', {'list_id': '84839422'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/list-members", {
  "list_id": "84839422"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/list-members", sandbase.Params{
	"list_id": "84839422",
})
```

Same call via the path form: `POST /v1/api/twitter/web/list-members` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `list_id` | string | yes | List ID  |

## Details

Returns the members of a Twitter list as structured JSON. Each member includes profile details such as name, handle, follower count and account creation date. You need the `list_id` of the list.

### Use cases

- Export the accounts on a curated list to review who a list owner follows in a topic area.
- Compare follower counts across list members to rank the most influential accounts in a niche.
- Check which members of a list carry a verified badge or a business label.
- Page through a large list to build a full roster of its accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/list-members" \
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
  "members": [
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
      "blue_verified": true,
      "business_account": null,
      "created_at": "Wed Oct 21 22:04:47 +0000 2020",
      "description": "Empowering users to create a better-informed world.\n\nWe're open source and data …",
      "followers_count": 1191871,
      "friends_count": 0,
      "location": "",
      "media_count": 114,
      "name": "Community Notes",
      "profile_image": null,
      "screen_name": "CommunityNotes"
    }
  ],
  "more_users": true,
  "next_cursor": "4611686021428553846|2117523434526212074",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `members[]` | One entry per list member on the current page. |
| `members[].user_id` | Numeric ID of the account, returned as a string. |
| `members[].screen_name / members[].name` | The account handle and the display name. |
| `members[].description` | The profile bio text of the member. |
| `members[].followers_count / members[].friends_count` | Number of followers and number of accounts the member follows (`friends_count`). |
| `members[].statuses_count / members[].media_count` | Number of posts and number of media items counted on the account. |
| `members[].created_at` | When the account was created, in the format `Wed Oct 21 22:04:47 +0000 2020`. |
| `members[].blue_verified / members[].verified` | Flags for the paid verified badge and the legacy verified status. |
| `members[].affiliates.label.description` | Name of the organization shown in the business label badge. Accounts without a label return `affiliates` as an empty list. |
| `more_users / next_cursor` | `more_users` is `true` when more members remain. `next_cursor` holds the value to send as `cursor` for the next page. |

### Notes

- The `list_id` is the number at the end of a list URL, for example `84839422`.
- To get the next page, send the `next_cursor` value from the response as `cursor`, and repeat while `more_users` is `true`.
- Some fields can be `null` or empty, such as `profile_image`, `website` and `business_account`, so handle missing values.
- To read the posts of the same list, call [Twitter List timeline](/apis/twitter/web/list-timeline). To see who follows the list, call [Twitter List followers](/apis/twitter/web/list-followers).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/list-members.json`](../../../../catalog/models/twitter/web/list-members.json) · Store page: https://www.sandbase.ai/model/twitter/web/list-members
