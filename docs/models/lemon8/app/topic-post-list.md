# Lemon8 Topic Post List API: pricing, parameters and code examples

`lemon8/app/topic-post-list` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts under a specific topic or hashtag on Lemon8. Requires the topic category ID, category parameter, and hashtag name.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/topic-post-list", "category": "590", "category_parameter": "7174447913778593798", "hashtag_name": "lemon8christmas"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/topic-post-list', {'category': '590', 'category_parameter': '7174447913778593798', 'hashtag_name': 'lemon8christmas'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/topic-post-list", {
  "category": "590",
  "category_parameter": "7174447913778593798",
  "hashtag_name": "lemon8christmas"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/topic-post-list", sandbase.Params{
	"category": "590",
	"category_parameter": "7174447913778593798",
	"hashtag_name": "lemon8christmas",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/topic-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category` | string | yes | Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |
| `sort_type` | string |  | Sort type, 0 for default sort, currently only support default sort, please do not pass other values.  |
| `hashtag_name` | string | yes | Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |
| `max_behot_time` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests.  |
| `category_parameter` | string | yes | Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |

## Details

Returns a page of Lemon8 posts under one topic hashtag. Each post includes its author, engagement counts, link, and images. You need the topic `category`, `category_parameter`, and `hashtag_name` values.

### Use cases

- Track which posts and creators appear under a seasonal hashtag such as `lemon8christmas`.
- Compare `digg_count` and `comment_count` across posts to find the strongest content in a topic.
- Collect image URLs and captions from a hashtag for content research.
- Build a list of active creators in a topic from the `author` objects.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/topic-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "590", "category_parameter": "7174447913778593798", "hashtag_name": "lemon8christmas"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `category_parameter` | string | Yes | Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `hashtag_name` | string | Yes | Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `max_behot_time` | string | No | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests. |
| `sort_type` | string | No | Sort type, 0 for default sort, currently only support default sort, please do not pass other values. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "duration": 2,
    "has_more": true,
    "items": [
      {
        "activity_forum_list": [],
        "app_transcode_rule": {},
        "article_class": "Gallery",
        "article_selected": false,
        "article_sub_class": "normal",
        "article_tag_list": [],
        "article_type": 0,
        "article_url": "https://www.lemon8-app.com/@lemon8_us/7578989388068946487?user_id=72623449159366…",
        "author": {
          "author_id": 7233310269842719790,
          "avatar": {
            "height": 1,
            "log_extra": "{\"channel_id\":590,\"image_index\":0,\"image_type\":\"avatar\",\"impression_index\":0,\"mi…",
            "main_color": "",
            "mimetype": "",
            "origin_uri": "user-avatar-musically/af9910a9b88477e9a051741b7cc737f6",
            "thumb_uri": "thumb/user-avatar-musically/af9910a9b88477e9a051741b7cc737f6",
            "thumb_url_list": [],
            "uri": "https://p16-lemon8-va-sign.tiktokcdn-us.com/user-avatar-musically/af9910a9b88477…"
          },
          "description": "Lemon8 official account🍋\nNew Feature Notes is LIVE 🔥🍋",
          "link": "sslocal://user_profile?user_id=7233310269842719790",
          "name": "Lemon8 US",
          "rec_reason": "",
          "relation": 0,
          "user_auth_info": "{\"auth_type\":102,\"show_auth_symbol\":true}"
        },
        "avatar_clickable": false,
        "ban_comment": 0,
        "behot_time": 1793691394.999
      }
    ],
    "latency_info": {
      "gostream": 953685,
      "loader": 417090,
      "planner": 23,
      "provider": 525246,
      "stream_api": 1229507
    },
    "login_status": 1,
    "module_offset": 20,
    "session_impr_id": 7703845882646497549,
    "tip": "10 stories from TopBuzz",
    "total_number": 10
  },
  "message": "success",
  "server_time": "1793691395.48"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].item_id / data.items[].group_id` | Numeric ID of the post. Both fields hold the same value in the sample. Pass it to other post APIs. |
| `data.items[].article_url` | Public Lemon8 web link to the post. |
| `data.items[].article_class` | Type of post. The sample value is `Gallery`, an image post. |
| `data.items[].author.author_id / data.items[].author.name` | ID and display name of the creator who published the post. |
| `data.items[].author.description` | The creator's profile bio text. |
| `data.items[].digg_count / comment_count / favorite_count` | Counts of likes, comments, and saves for the post. Likes is the usual reading of `digg_count`, and saves of `favorite_count`. |
| `data.items[].abstract / article_description` | Caption text of the post as HTML. Not every post includes these fields. |
| `data.items[].gallery[].image.thumb_url_list[].url` | Thumbnail image URLs for each image in the post. |
| `data.items[].image_list[].image_multi_gears[].url_list[].url` | Larger image URLs for each image, with the size named in `gear` (for example `1080P`). |
| `data.items[].behot_time / display_time` | Timestamps of the post as Unix seconds with decimals. |
| `data.has_more` | Tells you whether more posts are available after this page. |

### Notes

- Get `category`, `category_parameter`, and `hashtag_name` from [Lemon8 Topic Information](/apis/lemon8/app/topic-info).
- Leave `max_behot_time` empty on the first call. For the next page, pass the `max_behot_time` value from the previous response, and stop when `data.has_more` is `false`.
- Pass `0` for `sort_type` or leave it out. Other values are not supported.
- Use [Lemon8 Post Details](/apis/lemon8/app/post-detail) or [Lemon8 Post Comments List](/apis/lemon8/app/post-comment-list) with an `item_id` to get more on one post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/topic-post-list.json`](../../../../catalog/models/lemon8/app/topic-post-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/topic-post-list
