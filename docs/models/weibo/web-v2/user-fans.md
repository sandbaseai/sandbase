# Weibo User Follower List API: pricing, parameters and code examples

`weibo/web-v2/user-fans` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a paginated list of accounts following a specified Weibo user profile by ID, including follower metrics and profile summaries.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-fans", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-fans', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-fans", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-fans", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 0 (default 0)  |

## Details

Returns a page of accounts that follow a given Weibo user, with a profile summary and counts for each follower. It needs the target user's `uid` and takes an optional `page` number.

### Use cases

- Pull the follower profiles of a brand or influencer account to review who follows it.
- Check follower accounts for verification status, follower counts and profile descriptions.
- Page through the follower list of a Weibo account to build an audience sample.
- Compare the follower counts of the accounts that follow a profile to find large or influential followers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-fans" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 0 (default 0) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "display_total_number": 1,
  "display_total_number_str": "1",
  "fill_material": 0,
  "has_filtered_attentions": false,
  "has_filtered_fans": false,
  "next_cursor": 0,
  "ok": 1,
  "previous_cursor": 0,
  "screenName": "用户8431518763",
  "show_related_topic": false,
  "show_unread": false,
  "sort_type": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of follower accounts on this page. Each item is one Weibo user profile. |
| `users[].description` | Profile bio text of the follower. |
| `users[].created_at` | Account creation time as a text date, for example `Wed Mar 21 10:31:42 +0800 2012`. |
| `users[].followers_count / users[].followers_count_str` | Number of followers of this follower account. The `_str` field gives a short display form such as `1.65亿`. |
| `users[].friends_count / users[].favourites_count / users[].bi_followers_count` | Counts of accounts this user follows, posts this user favorited, and mutual follow relationships. |
| `users[].auth_status / users[].credit_score` | Verification status flag and the credit score shown on the profile. |
| `users[].avatar_hd / users[].avatar_large` | Image URLs for the follower's profile picture in high and large sizes. |
| `users[].follow_me / users[].following` | Flags for whether this user follows the requester and whether the requester follows this user. |
| `total_number / display_total_number_str` | Total follower count reported for the list, and its display string. |
| `next_cursor / previous_cursor` | Cursor values for the neighboring pages. Both are `0` in this response. |

### Notes

- `uid` is a numeric user ID passed as a string, for example `8431518763`. Look it up with [Weibo User Search](/apis/weibo/web-v2/user-search).
- `page` starts at 0. Increase it to read later pages.
- To see the accounts a user follows instead, call [Weibo User Following List](/apis/weibo/web-v2/user-following).
- Avatar URLs in the response carry `Expires` and `ssig` query parameters.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-fans.json`](../../../../catalog/models/weibo/web-v2/user-fans.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-fans
