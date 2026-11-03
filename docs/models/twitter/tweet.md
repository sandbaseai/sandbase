# X (Twitter) Twitter Tweet API: pricing, parameters and code examples

`twitter/tweet` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00022 per call · **Modes:** sync

Fetch a single Twitter/X tweet by URL with its full text and engagement counts (likes, retweets, replies, quotes, bookmarks, views).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00022**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweet", "url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweet', {'url': 'https://x.com/SpaceX/status/1732824684683784516'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweet", {
  "url": "https://x.com/SpaceX/status/1732824684683784516"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweet", sandbase.Params{
	"url": "https://x.com/SpaceX/status/1732824684683784516",
})
```

Same call via the path form: `POST /v1/api/twitter/tweet` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical x.com or twitter.com status URL with a numeric tweet ID, including /i/web/status and media-share variants.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoUrl` or `width`, and it is served only by a source that…  |

## Details

Returns one tweet from X (Twitter) as JSON: its text, author details, engagement counts, and attached media. It needs the tweet's `url` as input.

### Use cases

- Show a tweet's text and like, retweet and view counts in a dashboard or report.
- Track how a tweet's `likes`, `retweets` and `views` change by calling it on a schedule.
- Check whether a tweet is a reply and which conversation it belongs to.
- Pull the thumbnail and size of a tweet's video or image for a preview card.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweet" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical x.com or twitter.com status URL with a numeric tweet ID, including /i/web/status and media-share variants. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `videoUrl` or `width`, and it is served only by a source that returns  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "authorHandle": "SpaceX",
    "authorId": "34743251",
    "authorImage": "https://pbs.twimg.com/profile_images/1697749409851985920/HbrI04tM_normal.jpg",
    "authorName": "SpaceX",
    "authorVerified": true,
    "bookmarks": 1877,
    "conversationId": "1732824684683784516",
    "createdUtc": 1701972573,
    "id": "1732824684683784516",
    "inReplyToId": null,
    "lang": "en",
    "likes": 33783
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.text` | Full text of the tweet. Links appear as shortened `t.co` URLs. |
| `data.authorHandle / data.authorName` | Handle and display name of the account that posted the tweet. |
| `data.authorId` | Numeric ID of the author's account, as a string. |
| `data.authorVerified` | `true` if the author account is marked as verified. |
| `data.likes / data.retweets / data.replies / data.quotes / data.bookmarks` | Engagement counts for the tweet. |
| `data.views` | View count for the tweet. |
| `data.createdUtc` | Time the tweet was posted, as a Unix timestamp in seconds. |
| `data.conversationId / data.inReplyToId` | `conversationId` is the ID of the conversation the tweet belongs to. `inReplyToId` is `null` when the tweet is not a reply. |
| `data.media[].type / data.media[].url` | Type of each attached media item, such as `video`, and its image URL. For a video, the URL points to a thumbnail image. |
| `data.media[].width / data.media[].height` | Pixel size of the media item, as returned. |

### Notes

- Pass the full tweet link in `url`, for example `https://x.com/SpaceX/status/1732824684683784516`. The ID in the link matches `data.id`.
- Add `requireFields` with `videoUrl`, `width` or `height` if your code needs those fields. This can change which source serves the call and its price.
- If the tweet is not found, the call still succeeds and `found` is `false`.
- To fetch many tweets at once, use [Tweets by IDs](/apis/twitter/tweets-by-ids). To read the replies, use [Twitter Post Comments](/apis/twitter/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.00022 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweet.json`](../../../catalog/models/twitter/tweet.json) · Store page: https://www.sandbase.ai/model/twitter/tweet
