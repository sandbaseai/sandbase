# X / Twitter Tweet Thread API: pricing, parameters and code examples

`twitter/thread` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00269 per call · **Modes:** sync

Resolve the linear self-thread containing an X (Twitter) post, from its root through the author's linked continuations. This excludes replies from other users.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00269**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/thread", "url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/thread', {'url': 'https://x.com/SpaceX/status/1732824684683784516'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/thread", {
  "url": "https://x.com/SpaceX/status/1732824684683784516"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/thread", sandbase.Params{
	"url": "https://x.com/SpaceX/status/1732824684683784516",
})
```

Same call via the path form: `POST /v1/api/twitter/thread` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical x.com or twitter.com status URL with a numeric tweet ID. Any tweet in the self-thread can be supplied; the provider resolves the thread root.  |

## Details

Returns the self-thread that contains an X (Twitter) post, from the root tweet through the author's own continuations. It needs one input, the `url` of any tweet in the thread. The response includes the author profile and each tweet with its text, media and engagement counts.

### Use cases

- Archive a full multi-tweet announcement from a single tweet link.
- Read a long thread as one ordered list of tweets for summarizing or translating.
- Track likes, reposts and views across every tweet in an author's thread.
- Collect video and image URLs from all tweets in a thread.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/thread" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical x.com or twitter.com status URL with a numeric tweet ID. Any tweet in the self-thread can be supplied; the provider resolves the thread root. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "author": {
      "avatarUrl": "https://pbs.twimg.com/profile_images/1697749409851985920/HbrI04tM_normal.jpg",
      "bio": "SpaceX designs, manufactures and launches the world’s most advanced rockets and …",
      "blueVerified": true,
      "coverUrl": "https://pbs.twimg.com/profile_banners/34743251/1681251194",
      "createdUtc": 1240523610,
      "followers": 41933559,
      "following": 127,
      "handle": "SpaceX",
      "id": "34743251",
      "location": "Earth",
      "name": "SpaceX",
      "url": "https://x.com/SpaceX"
    },
    "complete": true,
    "conversationId": "1732824684683784516",
    "threadLength": 1,
    "tweets": [
      {
        "authorHandle": "SpaceX",
        "authorId": "34743251",
        "authorName": "SpaceX",
        "bookmarkCount": 1877,
        "conversationId": "1732824684683784516",
        "createdUtc": 1701972573,
        "id": "1732824684683784516",
        "inReplyToId": null,
        "isReply": false,
        "lang": "en",
        "likeCount": 33783,
        "media": [
          {
            "type": "video",
            "url": "https://pbs.twimg.com/ext_tw_video_thumb/1732820284301058052/pu/img/A-6jgWgxmMJ4…",
            "videoUrl": "https://video.twimg.com/ext_tw_video/1732820284301058052/pu/vid/avc1/1920x1080/K…"
          }
        ]
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the thread was resolved. A lookup that finds nothing returns `false`. |
| `data.complete` | Whether the full thread was returned. |
| `data.threadLength` | Number of tweets in the thread. |
| `data.author.handle / data.author.name / data.author.id` | The thread author's `@` handle, display name and numeric user ID. |
| `data.author.followers / data.author.following` | Follower count and following count for the author. |
| `data.tweets[].id` | Numeric ID of the tweet. |
| `data.tweets[].text` | Text of the tweet. Links appear as shortened `t.co` URLs. |
| `data.tweets[].createdUtc` | Tweet creation time as a Unix timestamp in seconds. |
| `data.tweets[].likeCount / data.tweets[].repostCount / data.tweets[].replyCount / data.tweets[].quoteCount / data.tweets[].bookmarkCount / data.tweets[].viewCount` | Engagement counts for each tweet. |
| `data.tweets[].media[]` | Media attached to the tweet. Each item has a `type`, a preview image `url` and, for video, a `videoUrl`. |

### Notes

- Pass any tweet URL from the thread in `url`. The root is resolved for you.
- The `url` must contain a numeric tweet ID, for example `https://x.com/SpaceX/status/1732824684683784516`.
- Replies from other users are not included. To read them, call [Twitter Post Comments](/apis/twitter/post-comments).
- For a single tweet without thread logic, use [Twitter Tweet Detail](/apis/twitter/web/tweet-detail).

### Pricing

Billed at the actual cost of each call, about $0.00269 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/thread.json`](../../../catalog/models/twitter/thread.json) · Store page: https://www.sandbase.ai/model/twitter/thread
