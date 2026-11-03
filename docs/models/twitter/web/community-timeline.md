# Twitter Community timeline API: pricing, parameters and code examples

`twitter/web/community-timeline` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get community timeline on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/community-timeline", "community_id": "1493290339532222469"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/community-timeline', {'community_id': '1493290339532222469'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/community-timeline", {
  "community_id": "1493290339532222469"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/community-timeline", sandbase.Params{
	"community_id": "1493290339532222469",
})
```

Same call via the path form: `POST /v1/api/twitter/web/community-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `ranking` | string |  | Ranking  |
| `community_id` | string | yes | Community ID  |

## Details

This API returns a page of posts from a Twitter Community timeline. It needs a `community_id` and returns each post with its text, author, engagement counts and attached media.

### Use cases

- Monitor what members of a crypto or niche community post each day.
- Collect posts with high `views` or `retweets` to find the most active topics in a community.
- Download video or photo URLs from community posts for archiving or review.
- Track which authors post most often in a community and whether they are `blue_verified`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/community-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"community_id": "1493290339532222469"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `community_id` | string | Yes | Community ID |
| `cursor` | string | No | Cursor |
| `ranking` | string | No | Ranking |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "DAAFCgABHWL0VND__-oLAAIAAADoRW1QQzZ3QUFBZlEvZ0dKTjB2R3AvQUFBQUJNZFlNZzdyWmRCRWgx…",
  "timeline": [
    {
      "author": {
        "avatar": null,
        "blue_verified": true,
        "name": "DPMF",
        "rest_id": "1452284866792464395",
        "screen_name": "DPMF_XDX"
      },
      "bookmarks": null,
      "created_at": "Mon Nov 02 12:56:30 +0000 2026",
      "favorites": 24,
      "lang": "en",
      "media": {
        "video": [
          {
            "aspect_ratio": [
              80
            ],
            "duration": 14280,
            "id": "2117239410529869824",
            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/2117239410529869824/img/9LrC8iqrcHuErv…",
            "original_info": {
              "focus_rects": [],
              "height": 976,
              "width": 1280
            },
            "variants": [
              {
                "content_type": "application/x-mpegURL",
                "url": "https://video.twimg.com/amplify_video/2117239410529869824/pl/1FzcdDBLNfg9eZzQ.m3…"
              }
            ]
          }
        ]
      },
      "quoted": {
        "author": {
          "avatar": null,
          "blue_verified": true,
          "name": "DPMF",
          "rest_id": "1452284866792464395",
          "screen_name": "DPMF_XDX"
        },
        "bookmarks": 9,
        "conversation_id": "2109604567742611954",
        "created_at": "Mon Oct 12 11:18:18 +0000 2026",
        "favorites": 40,
        "lang": "en",
        "media": {
          "video": [
            {
              "aspect_ratio": [
                9
              ],
              "duration": 26700,
              "id": "2109604322098941952",
              "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/2109604322098941952/img/7ITOFjzIw1zXzT…",
              "original_info": {
                "focus_rects": [],
                "height": 3840,
                "width": 2160
              },
              "variants": [
                {
                  "content_type": "application/x-mpegURL",
                  "url": "https://video.twimg.com/amplify_video/2109604322098941952/pl/ZRrfNz5avQmyKcBw.m3…"
                }
              ]
            }
          ]
        },
        "quotes": 3
      },
      "quotes": 1,
      "replies": 10,
      "retweets": 15,
      "screen_name": "DPMF_XDX",
      "source": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | List of posts in the community timeline. |
| `timeline[].tweet_id` | ID of the post. |
| `timeline[].text` | Text of the post. Long text may be cut. |
| `timeline[].created_at` | Post time as a string, for example `Mon Nov 02 12:56:30 +0000 2026`. |
| `timeline[].author.name / timeline[].author.screen_name / timeline[].author.rest_id` | Display name, handle and numeric user ID of the author. |
| `timeline[].author.blue_verified` | Whether the author has the blue verified badge. |
| `timeline[].favorites / timeline[].replies / timeline[].retweets / timeline[].quotes / timeline[].views` | Engagement counts for the post. `views` is returned as a string. |
| `timeline[].media.video[].variants[]` | Video files for the post. Each has a `url` and `content_type`. MP4 variants also have a `bitrate`. |
| `timeline[].media.photo[].media_url_https` | Image URL for a photo attached to the post. |
| `timeline[].quoted` | The post that this post quotes, with its own author, counts and media. It appears only on quote posts. |
| `cursor` | Value for the next page of the timeline. |

### Notes

- Pass the returned `cursor` value as the `cursor` parameter to get the next page.
- Find a `community_id` with [Twitter Search communities](/apis/twitter/web/search-communities). Use [Twitter Community info](/apis/twitter/web/community-info) for details about the community itself.
- Fields such as `bookmarks`, `source` and `avatar` can be `null`.
- Use the post `tweet_id` with [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) to get a single post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/community-timeline.json`](../../../../catalog/models/twitter/web/community-timeline.json) · Store page: https://www.sandbase.ai/model/twitter/web/community-timeline
