# Reddit App Subreddit Settings API: pricing, parameters and code examples

`reddit/app/subreddit-settings` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns settings and configuration details for a specified Reddit subreddit, including posting rules, flair settings, and moderation configurations.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-settings", "need_format": false, "subreddit_id": "t5_2qh0u"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-settings', {'need_format': False, 'subreddit_id': 't5_2qh0u'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-settings", {
  "need_format": false,
  "subreddit_id": "t5_2qh0u"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-settings", sandbase.Params{
	"need_format": false,
	"subreddit_id": "t5_2qh0u",
})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-settings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_id` | string | yes | Subreddit ID with format starting with t5_, e.g., "t5_2qh0u" (can be obtained from the fetch_subreddit_info endpoint)  |

## Details

Returns settings for one Reddit subreddit, such as allowed post types, flair settings, comment media types and channel options. It needs a `subreddit_id` that starts with `t5_`.

### Use cases

- Check which post types (`LINK`, `IMAGE`, `GALLERY`) a subreddit accepts before you build a posting tool.
- Find out whether post flair and user flair are turned on and whether users can assign them to themselves.
- Compare discovery and top listing settings across a list of subreddits.
- Check which comment media types a community allows, such as GIPHY or static images.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-settings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit_id": "t5_2qh0u"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit_id` | string | Yes | Subreddit ID with format starting with t5_, e.g., "t5_2qh0u" (can be obtained from the fetch_subreddit_info endpoint) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoById": {
    "__typename": "Subreddit",
    "allAllowedPostTypes": [
      "LINK"
    ],
    "amaSettings": {
      "postPermissions": "OFF"
    },
    "authorFlairSettings": {
      "isEnabled": true,
      "isSelfAssignable": false
    },
    "commentContributionSettings": {
      "allowedMediaTypes": [
        "GIPHY"
      ]
    },
    "countrySiteSettings": {
      "countryCode": "",
      "isCountrySiteEditable": true,
      "languageCode": "",
      "modMigrationAt": "2023-07-03T16:04:00.000000+0000"
    },
    "id": "t5_2qh0u",
    "isArchivePostsEnabled": true,
    "isDiscoveryAllowed": true,
    "isSubredditChannelsEnabled": {
      "isChatEnabled": false,
      "isPostEnabled": true
    },
    "isTopListingAllowed": true,
    "language": "en"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoById.id` | The subreddit ID, in the same `t5_` format as the input. |
| `subredditInfoById.allAllowedPostTypes[]` | The post types the subreddit accepts, such as `LINK`, `IMAGE` and `GALLERY`. |
| `subredditInfoById.postFlairSettings.isEnabled / subredditInfoById.authorFlairSettings.isEnabled` | Whether post flair and author flair are enabled in this subreddit. |
| `subredditInfoById.postFlairSettings.isSelfAssignable / subredditInfoById.authorFlairSettings.isSelfAssignable` | Whether users can assign the flair to themselves. |
| `subredditInfoById.commentContributionSettings.allowedMediaTypes[]` | The media types allowed in comments, such as `GIPHY`, `STATIC` and `EXPRESSION`. |
| `subredditInfoById.isSubredditChannelsEnabled.isChatEnabled / subredditInfoById.isSubredditChannelsEnabled.isPostEnabled` | Whether chat channels and post channels are enabled for the subreddit. |
| `subredditInfoById.isDiscoveryAllowed / subredditInfoById.isTopListingAllowed` | Whether the subreddit may appear in discovery and in top listings. |
| `subredditInfoById.isArchivePostsEnabled` | Whether archiving of posts is enabled. |
| `subredditInfoById.language` | The language code set for the subreddit, such as `en`. |
| `subredditInfoById.amaSettings.postPermissions` | The AMA post permission setting. The value `OFF` is returned in this example. |

### Notes

- Get the `subreddit_id` from the [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info) API. The ID starts with `t5_`, for example `t5_2qh0u`.
- Set `need_format` to `true` to clean and format the data. The default is `false`.
- For the rules and style of a subreddit, call [Reddit Subreddit Rules and Style Info](/apis/reddit/app/subreddit-style).
- `countrySiteSettings.modMigrationAt` is an ISO 8601 timestamp in UTC.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-settings.json`](../../../../catalog/models/reddit/app/subreddit-settings.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-settings
