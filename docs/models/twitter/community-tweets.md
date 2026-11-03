# X (Twitter) Twitter Community Tweets API: pricing, parameters and code examples

`twitter/community-tweets` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00045 per call · **Modes:** sync

List recent tweets posted in a Twitter/X community by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community-tweets", "url": "https://x.com/i/communities/1926186499399139650"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community-tweets', {'url': 'https://x.com/i/communities/1926186499399139650'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community-tweets", {
  "url": "https://x.com/i/communities/1926186499399139650"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community-tweets", sandbase.Params{
	"url": "https://x.com/i/communities/1926186499399139650",
})
```

Same call via the path form: `POST /v1/api/twitter/community-tweets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650).  |

## Details

Returns recent tweets posted in an X (Twitter) community. Each tweet includes the author, text, language, timestamp and engagement counts. The only input is the community `url`.

### Use cases

- Monitor a niche community for new posts about a topic or product.
- Rank community tweets by `views` or `favoriteCount` to find the posts that get the most reach.
- Collect author handles from a community to build a list of active members to follow up with.
- Track which verified accounts post in a community and how their posts perform.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community-tweets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "tweets": [
      {
        "authorHandle": "laksh_2705",
        "authorName": "Laksh Nijhawan",
        "authorVerified": false,
        "createdUtc": 1793418909,
        "favoriteCount": 4,
        "id": "2116378414223589764",
        "lang": "en",
        "quoteCount": 0,
        "replyCount": 3,
        "retweetCount": 0,
        "text": "racing to 200 \nlet's connect if you're into tech! https://t.co/80v46PiRNB",
        "views": 126
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.tweets[].id` | Tweet ID as a string. Pass it to other tweet APIs to fetch details. |
| `data.tweets[].text` | Text of the tweet. Links appear as shortened `t.co` URLs. |
| `data.tweets[].authorHandle / authorName` | Handle (without the @) and display name of the account that posted the tweet. |
| `data.tweets[].authorVerified` | `true` when the author account is marked as verified. |
| `data.tweets[].createdUtc` | Time the tweet was posted, as a Unix timestamp in seconds (UTC). |
| `data.tweets[].favoriteCount / replyCount / retweetCount / quoteCount` | Counts of likes, replies, retweets and quote tweets for the tweet. |
| `data.tweets[].views` | View count for the tweet. |
| `data.tweets[].lang` | Language code of the tweet, such as `en`. |
| `found` | `true` when the lookup returned a result. |

### Notes

- Copy the community URL from the browser. It has the form `https://x.com/i/communities/<id>`.
- The request has only the `url` parameter. This response shows no pagination field.
- To get details about the community itself, call [X (Twitter) Twitter Community](/apis/twitter/community).
- To fetch full data for a single tweet from the list, pass its `id` to [X (Twitter) Twitter Tweet](/apis/twitter/tweet).

### Pricing

Billed at the actual cost of each call, about $0.00045 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community-tweets.json`](../../../catalog/models/twitter/community-tweets.json) · Store page: https://www.sandbase.ai/model/twitter/community-tweets
