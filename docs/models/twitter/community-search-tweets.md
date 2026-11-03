# X (Twitter) Search Tweets Across Communities API: pricing, parameters and code examples

`twitter/community-search-tweets` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.003 per call · **Modes:** sync

Search tweets posted in all X Communities by keyword, sorted by Latest or Top.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.003**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community-search-tweets", "query": "AI", "queryType": "Latest"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community-search-tweets', {'query': 'AI', 'queryType': 'Latest'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community-search-tweets", {
  "query": "AI",
  "queryType": "Latest"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community-search-tweets", sandbase.Params{
	"query": "AI",
	"queryType": "Latest",
})
```

Same call via the path form: `POST /v1/api/twitter/community-search-tweets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query (e.g., keyword)  |
| `cursor` | string |  | Cursor for pagination  |
| `queryType` | string | yes | Query type (Latest or Top) one of: `Latest`, `Top`; default `"Latest"` |

## Details

This API searches tweets posted in X Communities by keyword. It needs a `query` and a `queryType` (`Latest` or `Top`). It returns a page of tweets with engagement counts, text, links and author data, plus a cursor for the next page.

### Use cases

- Track what people say about a topic such as `AI` inside X Communities.
- Pull the `Top` tweets for a keyword to find the most engaged community posts.
- Collect new community posts on a keyword with `Latest` for monitoring or alerts.
- Build a dataset of community tweets in different languages using the `lang` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community-search-tweets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "AI", "queryType": "Latest"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query (e.g., keyword) |
| `queryType` | string | Yes | Query type (Latest or Top) |
| `cursor` | string | No | Cursor for pagination |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_next_page": true,
  "next_cursor": "DAAHCgABHWL0Qjt__-QLAAIAAAAUV3pFM09UTTJPVEV5TnpBd01EQmQIAAMAAAACAAA",
  "tweets": [
    {
      "article": null,
      "author": {
        "affiliatesHighlightedLabel": {},
        "automatedBy": null,
        "canDm": true,
        "canMediaTag": false,
        "coverPicture": "",
        "createdAt": "Mon Jun 10 07:14:28 +0000 2024",
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
      "conversationId": "2117523188305531208",
      "createdAt": "Tue Nov 03 07:44:04 +0000 2026",
      "displayTextRange": [
        0
      ],
      "entities": {},
      "extendedEntities": {},
      "id": "2117523188305531208",
      "inReplyToId": null
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tweets[].id` | ID of the tweet, as a string. |
| `tweets[].text` | Text of the tweet. Long text may be cut off with an ellipsis. |
| `tweets[].url / tweets[].twitterUrl` | Links to the tweet on x.com and twitter.com. |
| `tweets[].createdAt` | Time the tweet was posted, in a format like `Tue Nov 03 07:43:59 +0000 2026`. |
| `tweets[].likeCount / tweets[].replyCount / tweets[].retweetCount / tweets[].quoteCount / tweets[].bookmarkCount / tweets[].viewCount` | Engagement counts for the tweet. |
| `tweets[].lang` | Language code of the tweet, such as `en`, `ja` or `vi`. |
| `tweets[].isReply / tweets[].inReplyToId` | Shows whether the tweet is a reply. When it is, `inReplyToId` holds the ID of the tweet it answers. |
| `tweets[].entities.user_mentions[]` | Accounts mentioned in the tweet, with `screen_name`, `name` and `id_str`. |
| `tweets[].author` | Profile data for the account that posted the tweet, such as `createdAt`, `coverPicture` and `canDm`. |
| `has_next_page / next_cursor` | `has_next_page` tells you if more results exist. `next_cursor` is the value to send as `cursor` to get them. |

### Notes

- Set `queryType` to `Latest` for newest tweets first or `Top` for the most relevant ones.
- To get the next page, pass the `next_cursor` value as `cursor` and repeat the same `query` and `queryType`.
- Tweet IDs are strings. Pass them to [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) or [X (Twitter) Tweets by IDs](/apis/twitter/tweets-by-ids) for more on a single tweet.
- To find communities by name rather than by tweet text, use [X / Twitter Community Search](/apis/twitter/search-communities).

### Pricing

Billed at the actual cost of each call, about $0.003 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community-search-tweets.json`](../../../catalog/models/twitter/community-search-tweets.json) · Store page: https://www.sandbase.ai/model/twitter/community-search-tweets
