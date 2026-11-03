# Lemon8 Topic Information API: pricing, parameters and code examples

`lemon8/app/topic-info` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information and background visual assets for a specific Lemon8 topic using its unique forum identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/topic-info", "forum_id": "7174447913778593798"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/topic-info', {'forum_id': '7174447913778593798'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/topic-info", {
  "forum_id": "7174447913778593798"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/topic-info", sandbase.Params{
	"forum_id": "7174447913778593798",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/topic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `forum_id` | string | yes | Topic ID, can be obtained from the following interfaces: Get information of specified post: `lemon8/app/post-detail`; Get Editor's Picks of discover page: `lemon8/app/discover-tab-information-tabs`; search hashtags:…  |

## Details

Returns details for one Lemon8 topic, including its name, description, follower and view counts, and background image URLs. It needs the topic's `forum_id`.

### Use cases

- Show a topic's name, description and background image on a custom topic page.
- Track `follower_count` and `views_count` for a campaign hashtag such as `lemon8christmas`.
- Build a share link for a topic from `share_url` to use in reports or outreach.
- Read the topic's feed tabs to see which sort orders Lemon8 offers for its posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/topic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"forum_id": "7174447913778593798"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `forum_id` | string | Yes | Topic ID, can be obtained from the following interfaces: Get information of specified post: `lemon8/app/post-detail`; Get Editor's Picks of discover page: `lemon8/app/discover-tab-information-tabs`; search hashtags: `lem |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "activity_icon_style": 0,
    "avatar": {
      "height": 0,
      "uri": "",
      "width": 0
    },
    "background": {
      "height": 1080,
      "origin_uri": "tos-maliva-i-tej9nj120t-us/4b46d07e128e4d369b65bb5c12a94f01",
      "thumb_uri": "tos-maliva-i-tej9nj120t-us/4b46d07e128e4d369b65bb5c12a94f01~tplv-tej9nj120t-cs:1…",
      "thumb_url_list": [
        {
          "url": "https://p16-lemon8-va-sign.tiktokcdn-us.com/tos-maliva-i-tej9nj120t-us/4b46d07e1…"
        }
      ],
      "uri": "tos-maliva-i-tej9nj120t-us/4b46d07e128e4d369b65bb5c12a94f01~tplv-tej9nj120t-cs:1…",
      "url": "https://p16-lemon8-va-sign.tiktokcdn-us.com/tos-maliva-i-tej9nj120t-us/4b46d07e1…",
      "url_list": [
        {
          "url": "https://p16-lemon8-va-sign.tiktokcdn-us.com/tos-maliva-i-tej9nj120t-us/4b46d07e1…"
        }
      ],
      "width": 1920
    },
    "bio_cover_image": {
      "height": 0,
      "uri": "",
      "width": 0
    },
    "bio_display_link": "",
    "bio_link": "sslocal://webview?url=https%3A%2F%2Fv.lemon8-app.com%2Foxygen%2Fpage%2Frelease%2…",
    "cold_start_default_follow": null,
    "color": "",
    "description": "Christmas GIVEAWAY is BACK!! Enter and unbox your Christmas gifts now!",
    "follower_count": 1343,
    "highlight": null,
    "id": 7174447913778593798
  },
  "message": "success",
  "rec_impr_id": 0,
  "server_time": "1793691394.01",
  "titlebar": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Topic name, for example `lemon8christmas`. |
| `data.description` | Short text that describes the topic. |
| `data.id` | Numeric topic ID. It matches the `forum_id` you sent. |
| `data.follower_count` | Number of followers of the topic. |
| `data.views_count` | Total view count of the topic. |
| `data.share_url` | Public Lemon8 web link to the topic. |
| `data.background.url / data.background.url_list[].url` | Full-size background image URL and its alternate hosts. The image is 1920 by 1080 pixels. |
| `data.background.thumb_url_list[].url` | Small thumbnail versions of the background image. |
| `data.stream_tab_list[].tab_name / data.stream_tab_list[].sort_type` | Name and sort type of each feed tab, such as `Popular` and `Recent`. The tab with `default_tab` set to `true` is the default. |
| `data.link` | In-app deep link to the topic detail screen. |

### Notes

- Get `forum_id` from [Lemon8 Post Details](/apis/lemon8/app/post-detail), [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs), or [Lemon8 Search](/apis/lemon8/app/search) with `search_tab` set to `hashtag`.
- To list the posts under a topic, call [Lemon8 Topic Post List](/apis/lemon8/app/topic-post-list).
- Some fields can be empty or zero for a topic, such as `data.avatar`, `data.talk_count` and `data.bio_display_link`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/topic-info.json`](../../../../catalog/models/lemon8/app/topic-info.json) · Store page: https://www.sandbase.ai/model/lemon8/app/topic-info
