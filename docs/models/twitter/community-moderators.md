# X (Twitter) Community Moderators API: pricing, parameters and code examples

`twitter/community-moderators` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0036 per call · **Modes:** sync

Moderators of an X Community by community ID, with profile details and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community-moderators", "community_id": "1493446837214187523"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community-moderators', {'community_id': '1493446837214187523'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community-moderators", {
  "community_id": "1493446837214187523"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community-moderators", sandbase.Params{
	"community_id": "1493446837214187523",
})
```

Same call via the path form: `POST /v1/api/twitter/community-moderators` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor for pagination  |
| `community_id` | string | yes | ID of the community  |

## Details

Returns the moderators of an X Community, with profile details for each moderator. It needs a `community_id` and supports cursor pagination.

### Use cases

- List who runs a community before you join it or contact its admins.
- Check follower counts of a community's moderators to judge how much reach the community has.
- Find moderators who accept direct messages by filtering on `can_dm`.
- Track changes in a community's moderator team by comparing `id` values over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community-moderators" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"community_id": "1493446837214187523"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `community_id` | string | Yes | ID of the community |
| `cursor` | string | No | Cursor for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next": false,
  "has_next_page": false,
  "moderators": [
    {
      "can_dm": true,
      "created_at": "Mon Jan 15 23:55:33 +0000 2007",
      "description": "🚧 https://t.co/aMZ4K3azU0 🏠 https://t.co/1KH3Ex4L2r 🤑 https://t.co/z2G662Uvhl 👀 …",
      "email": null,
      "favourites_count": 38120,
      "followers_count": 90269,
      "following_count": 977,
      "friends_count": 977,
      "id": "641633",
      "isBlueVerified": true,
      "location": "",
      "media_tweets_count": 4910
    }
  ],
  "msg": "success",
  "next_cursor": null,
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `moderators[].id` | Numeric ID of the moderator's X account, returned as a string. |
| `moderators[].screen_name / moderators[].name` | The moderator's @handle and display name. |
| `moderators[].description` | The profile bio text. Links appear as shortened `t.co` URLs. |
| `moderators[].followers_count / moderators[].following_count` | Number of accounts that follow the moderator, and number of accounts the moderator follows. |
| `moderators[].statuses_count / moderators[].media_tweets_count` | Total posts by the account, and the count of posts that contain media. |
| `moderators[].isBlueVerified / moderators[].verified` | Verification flags for the account. `isBlueVerified` can be `true` while `verified` is `false`. |
| `moderators[].can_dm` | Whether the account can receive direct messages, as a boolean. |
| `moderators[].created_at` | When the account was created, in a format like `Mon Jan 15 23:55:33 +0000 2007`. |
| `has_next / next_cursor` | Show whether more moderators exist. `next_cursor` is `null` when there are no more pages. |

### Notes

- Pass the `next_cursor` value as `cursor` in the next request to get the following page. Stop when `has_next` is `false`.
- The response also repeats the pagination flag as `has_next_page`.
- To find a `community_id`, try [X / Twitter Community Search](/apis/twitter/search-communities) or [X (Twitter) Twitter Community](/apis/twitter/community).
- To read what the community posts, call [X (Twitter) Twitter Community Tweets](/apis/twitter/community-tweets).

### Pricing

Billed at the actual cost of each call, about $0.0036 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community-moderators.json`](../../../catalog/models/twitter/community-moderators.json) · Store page: https://www.sandbase.ai/model/twitter/community-moderators
