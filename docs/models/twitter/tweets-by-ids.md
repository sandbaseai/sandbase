# X (Twitter) Tweets by IDs API: pricing, parameters and code examples

`twitter/tweets-by-ids` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0075 per call · **Modes:** sync

Look up several tweets at once by a comma-separated list of tweet IDs, with text, author and engagement counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0075**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweets-by-ids", "tweet_ids": "1585341984679469056,1846987139428634858"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweets-by-ids', {'tweet_ids': '1585341984679469056,1846987139428634858'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweets-by-ids", {
  "tweet_ids": "1585341984679469056,1846987139428634858"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweets-by-ids", sandbase.Params{
	"tweet_ids": "1585341984679469056,1846987139428634858",
})
```

Same call via the path form: `POST /v1/api/twitter/tweets-by-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweet_ids` | string | yes | Comma-separated list of tweet IDs.  |

## Details

Returns details for several tweets in one call. You pass a comma-separated list of tweet IDs in `tweet_ids`, and the response has one entry per ID in `tweets` with the text, author, engagement counts and links.

### Use cases

- Refresh like, retweet and reply counts for a saved list of tweet IDs.
- Fetch the text and permalink of tweets collected from another source.
- Check which tweets in a batch are replies, quotes or retweets.
- Pull the author profile and media details for a set of known posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweets-by-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_ids": "1585341984679469056,1846987139428634858"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_ids` | string | Yes | Comma-separated list of tweet IDs. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "msg": "success",
  "status": "success",
  "tweets": [
    {
      "author": {
        "affiliatesHighlightedLabel": {
          "label": {
            "badge": {
              "url": "https://pbs.twimg.com/profile_images/1955359038532653056/OSHY3ewP_bigger.jpg"
            },
            "description": "X",
            "url": {
              "url": "https://twitter.com/X",
              "url_type": "DeepLink"
            },
            "user_label_display_type": "Badge",
            "user_label_type": "BusinessLabel"
          }
        },
        "automatedBy": null,
        "canDm": false,
        "canMediaTag": false,
        "coverPicture": "https://pbs.twimg.com/profile_banners/44196397/1774145451",
        "createdAt": "Tue Jun 02 20:12:29 +0000 2009",
        "description": "https://t.co/ZdBx5WABYx",
        "entities": {
          "description": {
            "urls": [
              {
                "display_url": "Terafab.AI",
                "expanded_url": "http://Terafab.AI",
                "indices": [
                  0
                ],
                "url": "https://t.co/ZdBx5WABYx"
              }
            ]
          }
        }
      },
      "bookmarkCount": 14034,
      "card": null,
      "communityInfo": null,
      "conversationId": "1585341984679469056",
      "createdAt": "Wed Oct 26 18:45:58 +0000 2022",
      "displayTextRange": [
        0
      ],
      "entities": {},
      "extendedEntities": {
        "media": [
          {
            "additional_media_info": {
              "monetizable": false
            },
            "display_url": "pic.x.com/D68z4K2wq7",
            "expanded_url": "https://x.com/elonmusk/status/1585341984679469056/video/1",
            "ext_master_playlist_only": [],
            "ext_media_availability": {
              "status": "Available"
            },
            "ext_playlists": [],
            "id_str": "1585341912877146112",
            "indices": [
              40
            ]
          }
        ]
      },
      "id": "1585341984679469056",
      "inReplyToId": "",
      "inReplyToUserId": ""
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tweets[]` | One entry per requested tweet ID. An entry with an empty `id` and empty `text` has no data. |
| `tweets[].id / tweets[].url / tweets[].twitterUrl` | The tweet ID and its links on x.com and twitter.com. |
| `tweets[].text` | The tweet text. Media links appear as short `t.co` URLs. |
| `tweets[].createdAt` | Posting time as a string such as `Wed Oct 26 18:45:58 +0000 2022`. |
| `tweets[].likeCount / tweets[].retweetCount / tweets[].replyCount / tweets[].quoteCount / tweets[].bookmarkCount` | Engagement counts for the tweet. |
| `tweets[].viewCount` | View count. The sample tweet shows `0`, so treat that value with care. |
| `tweets[].isReply / tweets[].isQuote / tweets[].isRetweet` | Flags that show what kind of tweet it is. |
| `tweets[].conversationId` | ID of the conversation the tweet belongs to. |
| `tweets[].author.createdAt / tweets[].author.description / tweets[].author.coverPicture` | When the author account was created, its bio text and its banner image URL. |
| `tweets[].extendedEntities.media[]` | Attached media items, with `expanded_url`, `display_url` and `id_str`. |

### Notes

- Separate tweet IDs with commas and no extra text, for example `1585341984679469056,1846987139428634858`.
- Tweet IDs are numeric strings. The ID is the last part of a tweet URL.
- The response has no pagination parameters. Each call returns the tweets for the IDs you send.
- To read replies or quotes of a tweet, call [Post Comments](/apis/twitter/post-comments) or [Tweet Quotes](/apis/twitter/tweet-quotes).

### Pricing

Billed at the actual cost of each call, about $0.0075 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweets-by-ids.json`](../../../catalog/models/twitter/tweets-by-ids.json) · Store page: https://www.sandbase.ai/model/twitter/tweets-by-ids
