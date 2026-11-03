# X (Twitter) Tweet Quotes API: pricing, parameters and code examples

`twitter/tweet-quotes` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Quote tweets of a post by tweet ID, newest first, with optional time range and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweet-quotes", "tweetId": "1585341984679469056"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweet-quotes', {'tweetId': '1585341984679469056'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweet-quotes", {
  "tweetId": "1585341984679469056"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweet-quotes", sandbase.Params{
	"tweetId": "1585341984679469056",
})
```

Same call via the path form: `POST /v1/api/twitter/tweet-quotes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor for pagination.  |
| `tweetId` | string | yes | The tweet ID to get quotes for.  |
| `sinceTime` | integer |  | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `untilTime` | integer |  | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. range 0–9223372036854776000 |
| `includeReplies` | boolean |  | Whether to include replies in the results. Default is True. Provider reference (supplier schema): `{"default":true,"type":"boolean"}`.  |

## Details

Returns quote tweets of a post, newest first. Each item has the quoting tweet's text, engagement counts, author and a copy of the quoted tweet. It needs a `tweetId`.

### Use cases

- Find who is quoting a viral post and read what they say about it.
- Track reaction to a brand announcement by sorting quote tweets by `likeCount` or `viewCount`.
- Pull quotes posted inside a set time window using `sinceTime` and `untilTime`.
- Collect quoting authors for a tweet to review who amplifies it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweet-quotes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweetId": "1585341984679469056"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweetId` | string | Yes | The tweet ID to get quotes for. |
| `cursor` | string | No | Cursor for pagination. |
| `includeReplies` | boolean | No | Whether to include replies in the results. Default is True. Provider reference (supplier schema): `{"default":true,"type":"boolean"}`. |
| `sinceTime` | integer | No | On or after a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |
| `untilTime` | integer | No | Before a specified unix timestamp in seconds. Provider reference (supplier schema): `{"format":"int64","type":"integer"}`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next_page": true,
  "msg": "success",
  "next_cursor": "DAADDAABCgABHV-2mSOaQZoKAAIdWnCOlBtBRgAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUdYvRLOMAn…",
  "status": "success",
  "tweets": [
    {
      "article": null,
      "author": {
        "affiliatesHighlightedLabel": {},
        "automatedBy": null,
        "canDm": true,
        "canMediaTag": true,
        "coverPicture": "https://pbs.twimg.com/profile_banners/374202112/1747863953",
        "createdAt": "Thu Sep 15 21:57:34 +0000 2011",
        "description": "",
        "entities": {
          "description": {
            "urls": []
          },
          "url": {}
        }
      },
      "bookmarkCount": 0,
      "card": null,
      "communityInfo": null,
      "conversationId": "2116611118730985882",
      "createdAt": "Sat Oct 31 19:19:50 +0000 2026",
      "displayTextRange": [
        0
      ],
      "entities": {},
      "extendedEntities": {},
      "id": "2116611118730985882",
      "inReplyToId": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tweets[].id` | ID of the quote tweet, as a string. |
| `tweets[].text` | Text of the quote tweet. Long text may be cut in the sample. |
| `tweets[].url / tweets[].twitterUrl` | Links to the quote tweet on x.com and twitter.com. |
| `tweets[].createdAt` | When the quote tweet was posted, in a format like `Sat Oct 31 19:19:50 +0000 2026`. |
| `tweets[].likeCount / tweets[].replyCount / tweets[].retweetCount / tweets[].quoteCount / tweets[].bookmarkCount / tweets[].viewCount` | Engagement counts for the quote tweet. |
| `tweets[].author` | Profile of the account that wrote the quote, including `createdAt`, `coverPicture`, `canDm` and `description`. |
| `tweets[].quoted_tweet` | The original tweet that was quoted, with its own `author`, `bookmarkCount`, `conversationId` and `createdAt`. |
| `tweets[].isReply / tweets[].inReplyToId` | Show whether the quote tweet is also a reply, and which tweet it replies to. |
| `tweets[].entities.user_mentions[]` | Accounts mentioned in the quote tweet, with `screen_name`, `name` and `id_str`. |
| `has_next_page / next_cursor` | Show whether more results exist and give the cursor value for the next page. |

### Notes

- Take `tweetId` from the number at the end of a tweet URL, for example `1585341984679469056` in `https://x.com/<user>/status/1585341984679469056`.
- To get the next page, pass the `next_cursor` value as `cursor` while `has_next_page` is `true`.
- `sinceTime` and `untilTime` are unix timestamps in seconds. `createdAt` in the response uses a text date format instead.
- To read the original post itself, call [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) or [X (Twitter) Twitter Tweet](/apis/twitter/tweet).

### Pricing

Billed at the actual cost of each call, about $0.003 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweet-quotes.json`](../../../catalog/models/twitter/tweet-quotes.json) · Store page: https://www.sandbase.ai/model/twitter/tweet-quotes
