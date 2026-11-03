# X / Twitter Article API: pricing, parameters and code examples

`twitter/article` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00054 per call · **Modes:** sync

Get a public X long-form article from its wrapper post URL, including its author, engagement, cover image, and structured content blocks.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/article", "url": "https://x.com/Decentralisedco/status/1905545699552375179"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/article', {'url': 'https://x.com/Decentralisedco/status/1905545699552375179'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/article", {
  "url": "https://x.com/Decentralisedco/status/1905545699552375179"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/article", sandbase.Params{
	"url": "https://x.com/Decentralisedco/status/1905545699552375179",
})
```

Same call via the path form: `POST /v1/api/twitter/article` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical x.com or twitter.com URL of the public wrapper post for an X Article.  |

## Details

Returns a public X long-form article, including its title, author profile, engagement counts, cover image and content blocks. It needs one input: the `url` of the public wrapper post that carries the article.

### Use cases

- Archive the text and title of a crypto research article that a writer published on X.
- Track `views`, `likes`, `replies` and `quotes` on an article over repeated lookups.
- Check an author's follower count and verification status before citing their article.
- Convert the `contentBlocks` of an article into your own page or summary format.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/article" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/Decentralisedco/status/1905545699552375179"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical x.com or twitter.com URL of the public wrapper post for an X Article. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "author": {
      "avatarUrl": "https://pbs.twimg.com/profile_images/1766132688316973056/LB-8W7_d_normal.jpg",
      "bio": "Crypto Research and Investing",
      "blueVerified": true,
      "coverUrl": "https://pbs.twimg.com/profile_banners/1764631141926002689/1773416426",
      "createdUtc": 1709555838,
      "followers": 14176,
      "following": 465,
      "handle": "Decentralisedco",
      "id": "1764631141926002689",
      "location": "Writing →",
      "mediaCount": 520,
      "name": "DCo"
    },
    "contentBlocks": [
      {
        "entities": [],
        "inlineStyles": [
          {
            "length": 65,
            "offset": 0,
            "style": "Italic"
          }
        ],
        "text": "Breaking down how crypto protocols approach revenue and cash flow",
        "type": "unstyled"
      }
    ],
    "coverImage": "https://pbs.twimg.com/media/GnHXrznXUAEs-v5.jpg",
    "createdUtc": 1743152472,
    "id": "QXJ0aWNsZUVudGl0eToxOTA1NTQxMTM5MTQ0Mjk4NDk4",
    "likes": 156,
    "previewText": "Breaking down how crypto protocols approach revenue and cash flow\nThis is a summ…",
    "quotes": 8,
    "replies": 16,
    "title": "When Tokens Burn",
    "views": 44386
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Title of the article. |
| `data.previewText` | Short plain-text preview of the start of the article. The text is cut off with an ellipsis. |
| `data.contentBlocks[].text` | Text of one block of the article body. Blocks appear in reading order. |
| `data.contentBlocks[].type` | Block type, for example `unstyled` for a plain paragraph. |
| `data.contentBlocks[].inlineStyles[]` | Style ranges inside the block text. Each row has a `style` such as `Italic`, an `offset` and a `length`. |
| `data.contentBlocks[].entities[]` | Entity ranges inside the block text, with a `key`, an `offset` and a `length`. They mark spans of text such as links. |
| `data.views / data.likes / data.replies / data.quotes` | Engagement counts for the article. |
| `data.createdUtc` | Creation time of the article as a Unix timestamp in seconds. |
| `data.coverImage` | URL of the article cover image. |
| `data.author.handle / data.author.name / data.author.followers` | Handle, display name and follower count of the author. Other author fields include `bio`, `blueVerified`, `location` and `posts`. |

### Notes

- Pass the canonical x.com or twitter.com status URL of the wrapper post, not a link to the article body.
- The same `createdUtc` format (Unix seconds) is used for both the article and `data.author`.
- If the lookup finds nothing, the call still succeeds and returns `found: false`.
- To read the wrapper post itself, call [Twitter Post Detail](/apis/twitter/post-detail). To list the author's other posts, call [Twitter User Published Posts](/apis/twitter/user-posts).

### Pricing

Billed at the actual cost of each call, about $0.00054 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/article.json`](../../../catalog/models/twitter/article.json) · Store page: https://www.sandbase.ai/model/twitter/article
