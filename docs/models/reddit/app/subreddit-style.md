# Reddit Subreddit Rules and Style Info API: pricing, parameters and code examples

`reddit/app/subreddit-style` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns rules, styling details, and moderator information for a designated Reddit subreddit. Accepts the subreddit name and an optional formatting toggle.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/subreddit-style"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/subreddit-style', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/subreddit-style", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/subreddit-style", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/reddit/app/subreddit-style` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |
| `subreddit_name` | string |  | Subreddit name default `"pics"` |

## Details

Returns the rules, visual styles, sidebar widgets and moderator list for one subreddit. It needs the subreddit name in `subreddit_name`, such as `pics`. Set `need_format` to `true` to get cleaned and formatted data.

### Use cases

- Copy a community's rule titles and full rule text into a moderation guide or a posting checklist.
- Read a subreddit's banner, icon and color settings to match its look in a custom viewer.
- Collect the user IDs of a subreddit's moderators to track who runs a community.
- Read the top bar menu links, such as wiki pages for title guidelines, to find a community's extra rule pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/subreddit-style" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |
| `subreddit_name` | string | No | Subreddit name |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "subredditInfoByName": {
    "__typename": "Subreddit",
    "id": "t5_2qh0u",
    "moderatorsInfo": {
      "edges": [
        {
          "node": {
            "id": "t2_2fpn"
          }
        }
      ]
    },
    "rules": [
      {
        "__typename": "SubredditRule",
        "content": {
          "__typename": "Content",
          "html": "<p><strong>No <a href=\"https://i.imgur.com/AtDiqpR.jpg\" target=\"_blank\">screensh…",
          "markdown": "**No [screenshots](https://i.imgur.com/AtDiqpR.jpg). No pictures wherein the onl…",
          "richtext": "{\"document\":[{\"c\":[{\"e\":\"text\",\"f\":[[1,0,3]],\"t\":\"No \"},{\"e\":\"link\",\"f\":[[1,0,11…",
          "typeHint": null
        },
        "id": "0783e9fa-9cb5-4fe4-a705-3f0d77111199",
        "name": "No screenshots, AI images, or pictures in which the focus is a screen.",
        "priority": 0,
        "violationReason": "Screenshot or AI-generated"
      }
    ],
    "styles": {
      "__typename": "SubredditStyles",
      "bannerBackgroundColor": "#5A74CC",
      "bannerBackgroundImage": "https://styles.redditmedia.com/t5_2qh0u/styles/bannerBackgroundImage_if1cbgj4mc7…",
      "bannerBackgroundImagePosition": null,
      "highlightColor": "#553200",
      "icon": "https://b.thumbs.redditmedia.com/VZX_KQLnI1DPhlEZ07bIcLzwR1Win808RIt7zm49VIQ.png",
      "mobileBannerImage": "https://styles.redditmedia.com/t5_2qh0u/styles/mobileBannerImage_b4mne1y5mc7b1.j…",
      "postDownvoteCountColor": null,
      "postDownvoteIconActive": null,
      "postDownvoteIconInactive": null,
      "postPlaceholderImage": null,
      "postPlaceholderImagePosition": null
    },
    "widgets": {
      "orderedSidebarWidgets": [
        {
          "__typename": "SubredditRulesWidget",
          "display": "full",
          "id": "widget_rules-2qh0u",
          "shortName": "Subreddit Rules"
        }
      ],
      "orderedTopbarWidgets": [
        {
          "__typename": "MenuWidget",
          "id": "widget_10n9nqieach4y",
          "isWikiShown": false,
          "menus": [
            {
              "children": null,
              "text": "Rules",
              "url": "https://new.reddit.com/r/pics/wiki/index"
            }
          ],
          "shortName": null
        }
      ]
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `subredditInfoByName.id` | Subreddit ID in the `t5_` format. |
| `subredditInfoByName.rules[].name / subredditInfoByName.rules[].violationReason` | Short rule title, and the reason text shown when a post breaks that rule. |
| `subredditInfoByName.rules[].content.markdown / subredditInfoByName.rules[].content.html` | Full rule text in Markdown and in HTML. Long rules may carry links to example images. |
| `subredditInfoByName.rules[].priority` | Rule order. The first rule has `priority` `0`. |
| `subredditInfoByName.moderatorsInfo.edges[].node.id` | Moderator user ID in the `t2_` format. |
| `subredditInfoByName.styles.primaryColor / subredditInfoByName.styles.highlightColor / subredditInfoByName.styles.bannerBackgroundColor` | Hex color codes for the community theme. |
| `subredditInfoByName.styles.icon / subredditInfoByName.styles.bannerBackgroundImage / subredditInfoByName.styles.mobileBannerImage` | Image URLs for the community icon and the desktop and mobile banners. |
| `subredditInfoByName.widgets.orderedSidebarWidgets[].moderators[].redditor.name` | Moderator username, listed in the moderator sidebar widget. |
| `subredditInfoByName.widgets.orderedSidebarWidgets[].moderators[].flair.text` | Flair text shown next to a moderator. It is `null` when the moderator has no flair. |
| `subredditInfoByName.widgets.orderedTopbarWidgets[].menus[].text / subredditInfoByName.widgets.orderedTopbarWidgets[].menus[].url` | Label and link of each top bar menu item, such as wiki pages. |

### Notes

- Style fields such as the vote icon and sidebar widget colors can be `null` when the subreddit has not set them.
- Moderator names appear only in the moderator widget. The `moderatorsInfo` list holds IDs only.
- For other community data, try [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info) or [Reddit App Subreddit Settings](/apis/reddit/app/subreddit-settings).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/subreddit-style.json`](../../../../catalog/models/reddit/app/subreddit-style.json) · Store page: https://www.sandbase.ai/model/reddit/app/subreddit-style
