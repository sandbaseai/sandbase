# Twitter List timeline API: pricing, parameters and code examples

`twitter/web/list-timeline` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get list timeline on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/list-timeline", "list_id": "84839422"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/list-timeline', {'list_id': '84839422'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/list-timeline", {
  "list_id": "84839422"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/list-timeline", sandbase.Params{
	"list_id": "84839422",
})
```

Same call via the path form: `POST /v1/api/twitter/web/list-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `list_id` | string | yes | List ID  |

## Details

Returns a page of recent tweets from a Twitter List as structured JSON. Each tweet includes its text, engagement counts, media and author details. The call needs a `list_id`.

### Use cases

- Monitor a curated list of accounts, such as sports reporters, and collect their newest tweets in one call.
- Track likes, retweets and views on tweets from a group of accounts.
- Archive media URLs from photos and videos that list members post.
- Feed a news or alert pipeline with fresh tweets from a hand-picked set of authors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/list-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"list_id": "84839422"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `list_id` | string | Yes | List ID |
| `cursor` | string | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": "DAABCgABHWL0VZH__5oKAAIdXYaf-dshfAgAAwAAAAIAAA",
  "timeline": [
    {
      "author": {
        "avatar": "https://pbs.twimg.com/profile_images/2079205452454248448/ew197Npq_normal.jpg",
        "blue_verified": true,
        "followers": 13821659,
        "name": "Sports",
        "rest_id": "300392950",
        "screen_name": "Sports"
      },
      "bookmarks": 2,
      "created_at": "Tue Nov 03 04:26:01 +0000 2026",
      "favorites": 122,
      "lang": "en",
      "media": {
        "photo": [
          {
            "id": "2117470280465674240",
            "media_url_https": "https://pbs.twimg.com/media/HWLEAFGacAAfdD8.jpg"
          }
        ]
      },
      "quotes": 1,
      "replies": 0,
      "retweets": 7,
      "screen_name": "Sports",
      "source": null,
      "text": "RELEASE THE LOCKER ROOM VIDEO 🗣️ https://t.co/4I8bZxDhpP"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | Tweets in the list timeline, one object per tweet. |
| `timeline[].tweet_id` | ID of the tweet, as a string. |
| `timeline[].text` | Text of the tweet. Links appear as short `t.co` URLs. |
| `timeline[].created_at` | Time the tweet was posted, in a format like `Tue Nov 03 04:26:01 +0000 2026`. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the tweet: likes, retweets, replies, quote tweets and bookmarks. |
| `timeline[].views` | View count for the tweet, returned as a string. |
| `timeline[].author.screen_name / timeline[].author.name / timeline[].author.rest_id` | Handle, display name and numeric user ID of the account that posted the tweet. |
| `timeline[].author.followers / timeline[].author.blue_verified` | Follower count of the author and whether the author has a blue verified badge. |
| `timeline[].media` | Attached media. It is an object with `photo` or `video` lists when media exists, and an empty list when there is none. Each item has an `id` and a `media_url_https`. |
| `timeline[].media.video[].variants[]` | Available video files. Each entry has a `url` and a `content_type`, and MP4 entries also have a `bitrate`. |
| `cursor` | Token that points to the next page of the timeline. |

### Notes

- Pass the `cursor` value from a response as the `cursor` parameter in the next request to get the following page.
- `list_id` is the numeric ID of a Twitter List, such as `84839422`.
- `media` is an object when a tweet has photos or video, but an empty list when it has none. Check the type before reading it.
- To see who belongs to the list, call [Twitter List members](/apis/twitter/web/list-members). To get full details for one tweet, call [Twitter Tweet Detail](/apis/twitter/web/tweet-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/list-timeline.json`](../../../../catalog/models/twitter/web/list-timeline.json) · Store page: https://www.sandbase.ai/model/twitter/web/list-timeline
