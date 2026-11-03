# Reddit App Trending Searches API: pricing, parameters and code examples

`reddit/app/trending-searches` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns currently trending search queries and topics from the Reddit mobile application, with an option to clean and format the output data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/trending-searches", "need_format": true}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/trending-searches', {'need_format': True})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/trending-searches", {
  "need_format": true
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/trending-searches", sandbase.Params{
	"need_format": true,
})
```

Same call via the path form: `POST /v1/api/reddit/app/trending-searches` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Returns the list of search queries currently trending in the Reddit mobile app. The only input is the optional `need_format` flag, so you can call it with an empty body.

### Use cases

- Show a live list of trending Reddit topics on a dashboard or newsletter.
- Spot new events, product launches and earnings talk that Reddit users are searching for.
- Feed trending query text into a keyword search to collect the posts behind each topic.
- Compare the trending list across repeated calls to see which topics enter or leave it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/trending-searches" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "trendingQueries": [
    {
      "displayQuery": "Sephora Rouge Fall 2026 Savings Event Code",
      "id": "Sephora Rouge Fall 2026 Savings Event Code",
      "rawQuery": "Sephora Rouge Fall 2026 Savings Event Code",
      "trendingIcon": ""
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `trendingQueries` | List of the trending search queries. Each item is one query. |
| `trendingQueries[].displayQuery` | The query text as shown to app users. Use this for display. |
| `trendingQueries[].rawQuery` | The query text to use when you run a search for this topic. |
| `trendingQueries[].id` | Identifier for the query. In this response it has the same value as the query text. |
| `trendingQueries[].trendingIcon` | Icon value for the query. It is an empty string in this response. |

### Notes

- The request needs no input. Send `{}` to get the default output, or set `need_format` to `true` to ask for cleaned and formatted data.
- Pass a `rawQuery` value to [Reddit Keyword Search](/apis/reddit/search) or [Reddit Search](/apis/reddit/app/dynamic-search) to get the posts for a trending topic.
- To get partial matches while a user types, use [Reddit App Search Typeahead](/apis/reddit/app/search-typeahead).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/trending-searches.json`](../../../../catalog/models/reddit/app/trending-searches.json) · Store page: https://www.sandbase.ai/model/reddit/app/trending-searches
