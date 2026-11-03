# Lemon8 Discover Editor Picks API: pricing, parameters and code examples

`lemon8/app/discover-tab-information-tabs` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the Editor's Picks and discover tab information from the Lemon8 mobile app. Use this endpoint to inspect curated featured categories and discover sections.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/discover-tab-information-tabs"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/discover-tab-information-tabs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/discover-tab-information-tabs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/discover-tab-information-tabs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/lemon8/app/discover-tab-information-tabs` with the body above minus `model`.

## Details

Returns the Editor's Picks and discover tab sections shown in the Lemon8 mobile app. Each section carries a title, a banner image and a season of featured posts. The request takes no input parameters.

### Use cases

- List the current Lemon8 editor campaigns, such as `Weekly Trends` and `girltalk`, with their banner images.
- Collect featured posts and their authors from each campaign to see which creators Lemon8 promotes.
- Track how campaign hashtags and season subtitles change from one call to the next.
- Read the search phrases attached to featured posts to find topics tied to a campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/discover-tab-information-tabs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "impression_id": "7703843302294030605",
    "informations": [
      {
        "back_color": "",
        "banner_url": "https://p19-lemon8-va-sign.tiktokcdn-us.com/tos-maliva-i-tej9nj120t-us/7a69aeb45…",
        "has_more": true,
        "id": "7470802545074604087",
        "items": [],
        "offset": 10,
        "priority": 1062,
        "season": {
          "creator_intro": "",
          "creators": [],
          "has_more": true,
          "items": [
            {
              "abstract": "<p>Since grad season is upon us I thought I show some of the poses and locations…",
              "aggr_type": 0,
              "anchor_list": [
                {
                  "anchor_type": 2,
                  "biz_extra": "{\"word\":\"graduation photos ideas\",\"group_id\":\"950419280026140709\",\"score\":0.0038…",
                  "icon_type": "square",
                  "icon_url": "https://p16-lemon8-cross-sign.tiktokcdn-us.com/tos-alisg-i-2014-sg/10564e90b5d14…",
                  "log_extra": "{\"anchor_type\":\"search\",\"sar_query\":\"graduation photos ideas\"}",
                  "schema": "",
                  "show_in_folded": true,
                  "sub_title": "graduation photos ideas"
                }
              ],
              "app_transcode_rule": {},
              "article_class": "Gallery",
              "article_sub_class": "normal",
              "article_type": 0,
              "article_url": "https://www.lemon8-app.com/@swagis4eva/7501417544423703086?user_id=7262344915936…"
            }
          ],
          "offset": 10,
          "season_id": "7503609246219503621",
          "season_num": 7,
          "season_subtitle": "It’s your moment to shine! Whether you’re tossing your cap, striking a power pos…"
        },
        "sub_title": "#graduationpictures",
        "title": "Weekly Trends"
      }
    ]
  },
  "message": "success",
  "server_time": "1793691390.56"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.informations[].title / data.informations[].sub_title` | Name of the editor section and its hashtag, for example `Weekly Trends` with `#graduationpictures`. |
| `data.informations[].id` | ID of the section as a string. |
| `data.informations[].banner_url` | Banner image URL for the section. |
| `data.informations[].priority` | Number that sets the order of the sections. Lower values appear first in the sample. |
| `data.informations[].has_more / data.informations[].offset` | Show whether the section has more posts and the offset value returned for it. |
| `data.informations[].season.season_id / data.informations[].season.season_num` | ID and number of the current season of the campaign. |
| `data.informations[].season.season_subtitle` | Short text that describes the campaign and what creators should post. |
| `data.informations[].season.items[].article_url` | Link to a featured post on lemon8-app.com. The link holds the author handle and the post ID. |
| `data.informations[].season.items[].article_class` | Type of the post, such as `Gallery` or `Video`. |
| `data.informations[].season.items[].author.name / data.informations[].season.items[].author.user_unique_name` | Display name and handle of the post author. Author details such as `author_id` and `description` sit in the same object. |

### Notes

- The top-level `items` list in each section is empty in the sample. Read the featured posts from `season.items[]` instead.
- Some posts include `anchor_list[]`. Its `sub_title` holds a search phrase linked to the post.
- Pass a post ID from `article_url` to [Lemon8 Post Details](/apis/lemon8/app/post-detail) to get the full post.
- Pass a handle or author ID to [Lemon8 User Profile Details](/apis/lemon8/app/user-profile) to look at a creator.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Hot Search Keywords](/apis/lemon8/app/hot-search-keywords): Returns trending search keywords and topics currently popular on Lemon8.

---
Machine-readable: [`catalog/models/lemon8/app/discover-tab-information-tabs.json`](../../../../catalog/models/lemon8/app/discover-tab-information-tabs.json) · Store page: https://www.sandbase.ai/model/lemon8/app/discover-tab-information-tabs
