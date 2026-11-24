# Tweet Search API: pricing, parameters and code examples

`twitter/bulk/tweet-search` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0006 per call · **Modes:** async

Scrape X (Twitter) tweets from search queries, profiles, lists, and tweet URLs at scale.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0006**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/bulk/tweet-search", "maxItems": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/bulk/tweet-search', {'maxItems': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/bulk/tweet-search", {
  "maxItems": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/bulk/tweet-search", sandbase.Params{
	"maxItems": 1,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/twitter/bulk/tweet-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | string |  | Returns tweets sent before the given date.  |
| `sort` | string |  | Sorts search results. If you are getting low results, try Top instead of Latest. Latest + Top runs both simultaneously to maximize results but may return some duplicate tweets. one of: `Top`, `Latest`, `Latest + Top` |
| `start` | string |  | Returns tweets sent after the given date.  |
| `author` | string |  | Returns tweets sent by the given user. It should be a Twitter (X) Handle.  |
| `geocode` | string |  | Returns tweets sent by users located within a given radius of the given latitude/longitude.  |
| `maxItems` | integer | yes | Maximum number of tweets to return (1-1000). Billed per returned tweet. range 1–1000 |
| `inReplyTo` | string |  | Returns tweets that are replies to the given user. It should be a Twitter (X) Handle.  |
| `onlyImage` | boolean |  | If selected, only returns tweets that contain images.  |
| `onlyQuote` | boolean |  | If selected, only returns tweets that are quotes.  |
| `onlyVideo` | boolean |  | If selected, only returns tweets that contain videos.  |
| `startUrls` | array |  | Twitter (X) URLs. Paste the URLs and get the results immediately. Tweet, Profile, Search or List URLs are supported.  |
| `mentioning` | string |  | Returns tweets mentioning the given user. It should be a Twitter (X) Handle.  |
| `searchTerms` | array |  | Search terms you want to search from Twitter (X). You can refer to https://github.com/igorbrigadir/twitter-advanced-search.  |
| `withinRadius` | string |  | Returns tweets sent within the given radius of the given location.  |
| `geotaggedNear` | string |  | Returns tweets sent near the given location.  |
| `placeObjectId` | string |  | Returns tweets tagged with the given place.  |
| `tweetLanguage` | string |  | Restricts tweets to the given language, given by an ISO 639-1 code. one of: `ab`, `aa`, `af`, `ak`, `sq`, `am`, `ar`, `an`, `hy`, `as`, `av`, `ae` … |
| `minimumReplies` | integer |  | Returns tweets with at least the given number of replies. range -9007199254740991–9007199254740991 |
| `twitterHandles` | array |  | Twitter handles that you want to search on Twitter (X)  |
| `conversationIds` | array |  | Conversation IDs that you want to search on Twitter (X)  |
| `minimumRetweets` | integer |  | Returns tweets with at least the given number of retweets. range -9007199254740991–9007199254740991 |
| `onlyTwitterBlue` | boolean |  | If selected, only returns tweets by users who are Twitter Blue subscribers.  |
| `minimumFavorites` | integer |  | Returns tweets with at least the given number of favorites. range -9007199254740991–9007199254740991 |
| `onlyVerifiedUsers` | boolean |  | If selected, only returns tweets by users who are verified.  |
| `includeSearchTerms` | boolean |  | If selected, a field will be added to each tweets about the search term that was used to find it.  |

## Details

Scrape X (Twitter) tweets from search queries, profiles, lists, and tweet URLs at scale.

### Pricing

- Inspect reference unit price: $0.0006 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/twitter/bulk/tweet-search.json`](../../../../catalog/models/twitter/bulk/tweet-search.json) · Store page: https://www.sandbase.ai/model/twitter/bulk/tweet-search
