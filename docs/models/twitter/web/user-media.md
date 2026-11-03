# Twitter (X) User Media API: pricing, parameters and code examples

`twitter/web/user-media` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns media posts and timeline items for a specified user profile, queried by screen name or user ID. Supports cursor-based pagination for browsing past media posts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-media", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-media', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-media", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-media", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-media` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request  |
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns a page of media posts from a public Twitter (X) account, plus the account's profile details. It needs a `screen_name` or a numeric `rest_id`.

### Use cases

- Collect photo and video URLs posted by a brand or agency account.
- Compare `favorites`, `retweets` and `views` across an account's recent media posts.
- Download video files by picking a `variants` entry with the bitrate you want.
- Build a media archive for a profile by paging back through older posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-media" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the `next_cursor` in the last request |
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAABCgABHWL0W1z___0KAAIdXMz4Wdqw1ggAAwAAAAIAAA",
  "status": "ok",
  "timeline": [
    {
      "author": {
        "avatar": null,
        "blue_verified": true,
        "name": "NASA",
        "rest_id": "11348282",
        "screen_name": "NASA"
      },
      "bookmarks": 22,
      "conversation_id": "2117383753139925271",
      "created_at": "Mon Nov 02 22:30:00 +0000 2026",
      "favorites": 470,
      "lang": "en",
      "media": {
        "photo": [
          {
            "id": "2117375637358882816",
            "media_url_https": "https://pbs.twimg.com/media/HWJt7IDXsAAa7bN.jpg"
          }
        ]
      },
      "quotes": 6,
      "replies": 39,
      "retweets": 45,
      "sensitive": false,
      "source": null
    }
  ],
  "user": {
    "affiliates": [],
    "avatar": "https://pbs.twimg.com/profile_images/1321163587679784960/0ZxKlEKB_normal.jpg",
    "blue_verified": true,
    "business_account": {
      "affiliates_count": 85
    },
    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
    "desc": "Making the seemingly impossible, possible. ✨",
    "friends": 115,
    "header_image": "https://pbs.twimg.com/profile_banners/11348282/1788992290",
    "id": "11348282",
    "location": "Pale Blue Dot",
    "media_count": 28223,
    "name": "NASA"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[].tweet_id / timeline[].conversation_id` | ID of the post and ID of its conversation. They match for a standalone post. |
| `timeline[].text` | Post text. Long text may be shortened. |
| `timeline[].created_at` | Post time as a string such as `Mon Nov 02 22:30:00 +0000 2026`. |
| `timeline[].favorites / retweets / replies / quotes / bookmarks / views` | Engagement counts for the post. `views` is returned as a string. |
| `timeline[].media.photo[].media_url_https` | Image URL for each photo in the post. |
| `timeline[].media.video[].variants[]` | Available video files. MP4 entries carry a `bitrate` and `url`, and an HLS playlist entry has `content_type` `application/x-mpegURL`. |
| `timeline[].media.video[].duration / aspect_ratio` | Length of the video and its width-to-height ratio. `original_info` gives pixel `width` and `height`. |
| `timeline[].author.screen_name / rest_id` | Handle and numeric ID of the account that wrote the post. |
| `user.media_count / statuses_count / sub_count` | Number of media posts, number of posts, and subscriber count for the profile. `sub_count` is the follower-style total. |
| `next_cursor` | Cursor value for the next page of results. |

### Notes

- Take `screen_name` from the profile URL. In `https://twitter.com/NASA`, it is `NASA`.
- If you send `rest_id`, the API ignores `screen_name`. `rest_id` is an integer such as `44196397`.
- To get the next page, pass the `next_cursor` value from the last response as `cursor`.
- For the account's own posts, call [Twitter (X) User Posts](/apis/twitter/web/user-post-tweet). For one post, call [Twitter Tweet Detail](/apis/twitter/web/tweet-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-media.json`](../../../../catalog/models/twitter/web/user-media.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-media
