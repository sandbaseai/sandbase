# Twitter Search Timeline API: pricing, parameters and code examples

`twitter/search` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search X (Twitter) by keyword across top, latest, media, people, or list result modes with cursor pagination. Use it to find public conversations, accounts, media, or lists related to a topic.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/twitter/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `keyword` | string | yes | Search keyword.  |
| `searchType` | string |  | Search result type. one of: `TOP`, `LATEST`, `MEDIA`, `PEOPLE`, `LISTS` |

## Details

This API searches X (Twitter) by keyword and returns a page of matching results in the `timeline` array. It needs a `keyword`. You can set `searchType` to `TOP`, `LATEST`, `MEDIA`, `PEOPLE`, or `LISTS`.

### Use cases

- Track public posts that mention a product name such as `iphone`.
- Rank posts about a topic by `views`, `favorites`, and `retweets` to find the ones that spread most.
- Collect video posts and their file URLs for a topic.
- Find large accounts that post about a topic using `user_info.followers_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |
| `searchType` | string | No | Search result type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAACCgACHWL0SvpAJxAKAAMdYvRK-j_Y8AgABAAAAAILAAUAAADwRW1QQzZ3QUFBZlEvZ0dKTjB2R3Av…",
  "prev_cursor": "DAACCgACHWL0SvpAJxAKAAMdYvRK-j_Y8AgABAAAAAELAAUAAADwRW1QQzZ3QUFBZlEvZ0dKTjB2R3Av…",
  "status": "ok",
  "timeline": [
    {
      "bookmarks": 254,
      "conversation_id": "2115181704403165431",
      "created_at": "Tue Oct 27 20:39:51 +0000 2026",
      "display_text_range": [
        0
      ],
      "entities": {
        "hashtags": [],
        "media": [
          {
            "additional_media_info": {
              "monetizable": false
            },
            "display_url": "pic.x.com/m7nyDKgKuU",
            "expanded_url": "https://x.com/TecnonautaTV/status/2115181704403165431/video/1",
            "ext_media_availability": {
              "status": "Available"
            },
            "id_str": "2115181241813147648",
            "indices": [
              205
            ],
            "media_key": "13_2115181241813147648",
            "media_results": {
              "result": {
                "media_key": "13_2115181241813147648"
              }
            }
          }
        ],
        "symbols": [],
        "timestamps": [],
        "urls": [],
        "user_mentions": []
      },
      "favorites": 1888,
      "lang": "es",
      "media": {
        "video": [
          {
            "aspect_ratio": [
              9
            ],
            "duration": 69300,
            "id": "2115181241813147648",
            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/2115181241813147648/img/Fi_52oJPz8Ji6Z…",
            "original_info": {
              "focus_rects": [],
              "height": 1920,
              "width": 1080
            },
            "variants": [
              {
                "content_type": "application/x-mpegURL",
                "url": "https://video.twimg.com/amplify_video/2115181241813147648/pl/_f3RJZ0z46BMZC3H.m3…"
              }
            ]
          }
        ]
      },
      "quotes": 16,
      "replies": 72,
      "retweets": 196,
      "screen_name": "TecnonautaTV"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | One search result per item. In this response each item is a post with `type` set to `tweet`. |
| `timeline[].tweet_id / timeline[].conversation_id` | ID of the post and ID of the conversation it belongs to. Both are strings. |
| `timeline[].text` | Text of the post. Long text may be cut. |
| `timeline[].created_at` | Time the post was created, in a format like `Tue Oct 27 20:39:51 +0000 2026`. |
| `timeline[].screen_name` | Handle of the account that wrote the post. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the post. |
| `timeline[].views` | View count of the post, returned as a string. |
| `timeline[].user_info.followers_count` | Follower count of the author. The `user_info` object also has `avatar`, `location`, and the account `created_at`. |
| `timeline[].media.video[].variants[]` | Video files for the post. Each has a `content_type` and `url`. MP4 variants also have a `bitrate`. |
| `timeline[].quoted.author.screen_name` | Handle of the author of a quoted post, present when the result quotes another post. |

### Notes

- For the next page, pass the response `next_cursor` as `cursor` in the next request. The response also returns `prev_cursor`.
- Keep `keyword` the same when you send a `cursor`.
- To read one post in full, call [Twitter Post Detail](/apis/twitter/post-detail). To read replies, call [Twitter Post Comments](/apis/twitter/post-comments).
- To search accounts only, see [X / Twitter User Search](/apis/twitter/search-users).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/search.json`](../../../catalog/models/twitter/search.json) · Store page: https://www.sandbase.ai/model/twitter/search
