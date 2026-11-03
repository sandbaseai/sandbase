# Reddit App Subreddit Info API: pricing, parameters and code examples

`reddit/app/subreddit-info` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a Reddit subreddit, such as rules, descriptions, and app installations. Look up data by subreddit name with optional response formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-info"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-info', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-info", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-info", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_name` | string |  | Subreddit name (without r/ prefix), e.g., "pics", "funny", "AskReddit" default `"pics"` |

## Details

Returns metadata for one Reddit subreddit, including its description, subscriber count, post settings, styling, and installed Devvit apps. It needs a subreddit name without the `r/` prefix, such as `pics`.

### Use cases

- Read `subscribersCount` and `communityStats` to compare the size and weekly activity of different subreddits.
- List the Devvit apps installed in a subreddit to see which moderation tools it uses.
- Check `allowedPostTypes`, `isNsfw` and `isPostingRestricted` before building a posting workflow for a subreddit.
- Pull the icon, banner and color values from `styles` to show a subreddit's branding in your own app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |
| `subreddit_name` | string | No | Subreddit name (without r/ prefix), e.g., "pics", "funny", "AskReddit" |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoByName": {
    "__typename": "Subreddit",
    "activeCount": 0,
    "allowedMediaInComments": [
      "GIPHY"
    ],
    "allowedPostTypes": [
      "LINK"
    ],
    "authorFlair": null,
    "authorFlairSettings": {
      "isEnabled": true,
      "isOwnFlairEnabled": false,
      "isSelfAssignable": false
    },
    "communityLeaderboard": {
      "isEnabled": false
    },
    "communityStats": {
      "weeklyActiveUsersCount": 3157928,
      "weeklyContributionsCount": 27065
    },
    "communityStatus": {
      "__typename": "SubredditCommunityStatus",
      "description": {
        "markdown": "📸",
        "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"t\":\"\\ud83d\\udcf8\"}],\"e\":\"par\"}]}"
      },
      "emoji": {
        "name": "upvote",
        "url": "https://emoji.redditmedia.com/ad1td4bx9ezz_t5_3nqvj/upvote"
      }
    },
    "createdAt": "2008-01-25T00:31:09.512000+0000",
    "description": {
      "markdown": "[Please read our rules in their entirety before participating.](/r/pics/wiki/ind…",
      "richtext": "{\"document\":[{\"c\":[{\"e\":\"link\",\"t\":\"Please read our rules in their entirety befo…"
    },
    "detectedLanguage": "en"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoByName.id / subredditInfoByName.name / subredditInfoByName.prefixedName` | The subreddit's ID (`t5_` format), its plain name, and its name with the `r/` prefix. |
| `subredditInfoByName.subscribersCount` | Number of subscribers to the subreddit. |
| `subredditInfoByName.communityStats.weeklyActiveUsersCount / subredditInfoByName.communityStats.weeklyContributionsCount` | Weekly active users and weekly contributions for the subreddit. |
| `subredditInfoByName.publicDescriptionText / subredditInfoByName.description.markdown` | A short public description, and the longer sidebar description in Markdown. The sidebar text holds the community rules and may be cut in long cases. |
| `subredditInfoByName.createdAt` | Creation time of the subreddit as an ISO 8601 timestamp. |
| `subredditInfoByName.allowedPostTypes / subredditInfoByName.allowedMediaInComments` | Post types the subreddit accepts, such as `LINK`, `IMAGE` and `GALLERY`, and media types allowed in comments. |
| `subredditInfoByName.isNsfw / subredditInfoByName.isQuarantined / subredditInfoByName.isPostingRestricted` | Flags for adult content, quarantine status, and whether posting is restricted. |
| `subredditInfoByName.devvit.installations[].app.name / subredditInfoByName.devvit.installations[].app.slug` | Name and slug of each Devvit app installed in the subreddit. |
| `subredditInfoByName.styles.icon / subredditInfoByName.styles.bannerBackgroundImage / subredditInfoByName.styles.primaryColor` | Image URLs for the icon and banner, and the primary color as a hex code. |
| `subredditInfoByName.taxonomy.taxonomyTopics[].displayCopy` | Ranking label for the subreddit within a topic, such as `#1 in Photography`. |

### Notes

- Pass `subreddit_name` without the `r/` prefix. The default value is `pics`.
- Set `need_format` to `true` to have the returned data cleaned and formatted.
- The `id` value starts with `t5_`. Use it with APIs that take a subreddit ID, such as [Reddit Community Highlights](/apis/reddit/app/community-highlights) or [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted).
- To read the posts in a subreddit, call [Reddit Subreddit Feed](/apis/reddit/app/subreddit-feed).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-info.json`](../../../../catalog/models/reddit/app/subreddit-info.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-info
