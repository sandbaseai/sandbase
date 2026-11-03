# Reddit User Public Trophies API: pricing, parameters and code examples

`reddit/app/user-trophies` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of public trophies and achievements for a specified Reddit account. Users can supply a username and optionally request cleaned, formatted data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-trophies", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-trophies', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-trophies", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-trophies", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-trophies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username (without u/ prefix)  |
| `need_format` | boolean |  | Whether to clean and format the data  |

## Details

Returns the public trophies shown on a Reddit user's profile. Each trophy has an ID, a name and an image URL. The only required input is the `username`, without the u/ prefix.

### Use cases

- Show a user's Reddit trophies and streak badges on an external profile page.
- Check which streak trophies an account holds, such as `700-Day Streak` or `600-Day Streak`.
- Collect trophy image URLs to display achievement icons in a dashboard.
- Compare the trophy names of several accounts when reviewing community members.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-trophies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username (without u/ prefix) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "redditorInfoByName": {
    "__typename": "Redditor",
    "trophyCase": {
      "categories": {
        "edges": [
          {
            "node": {
              "__typename": "AchievementTrophyCategory",
              "trophies": {
                "edges": [
                  {
                    "node": {
                      "__typename": "AchievementImageTrophy",
                      "id": "700-day-streak",
                      "image": {
                        "url": "https://preview.redd.it/h9a6sd4jhosf1.png?width=500&height=500&auto=webp&s=005d6…"
                      },
                      "name": "700-Day Streak"
                    }
                  }
                ]
              }
            }
          }
        ]
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `redditorInfoByName` | Root object for the Reddit user that matches the `username`. |
| `redditorInfoByName.trophyCase.categories.edges[].node.trophies.edges[]` | List of trophies in one trophy category. Each entry holds a `node` object with the trophy details. |
| `redditorInfoByName.trophyCase.categories.edges[].node.__typename` | Type of the trophy category, for example `AchievementTrophyCategory`. |
| `redditorInfoByName.trophyCase.categories.edges[].node.trophies.edges[].node.name` | Display name of the trophy, such as `Conversation Starter` or `700-Day Streak`. |
| `redditorInfoByName.trophyCase.categories.edges[].node.trophies.edges[].node.id` | Identifier of the trophy. Values can be a number string like `11` or a slug like `700-day-streak`. |
| `redditorInfoByName.trophyCase.categories.edges[].node.trophies.edges[].node.image.url` | URL of the trophy image. |
| `redditorInfoByName.trophyCase.categories.edges[].node.trophies.edges[].node.__typename` | Type of the trophy, for example `AchievementImageTrophy`. |

### Notes

- Pass the `username` without the u/ prefix, for example `spez`.
- Trophy IDs are strings. Some are numeric and some are slugs, so treat them as text.
- The response nests trophies under categories, so loop over the categories first and then over the trophies in each one.
- To look up more about the same account, call [Reddit App User Profile](/apis/reddit/app/user-profile) or [Reddit User Posts](/apis/reddit/app/user-posts).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-trophies.json`](../../../../catalog/models/reddit/app/user-trophies.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-trophies
