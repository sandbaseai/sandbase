# GetApp Blog Research API: pricing, parameters and code examples

`getapp/blog-research` · data API · GetApp · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Retrieve blog posts and software research guides from GetApp's resources section. Returns all published posts with metadata, topics, and content hubs.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "getapp/blog-research"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('getapp/blog-research', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("getapp/blog-research", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "getapp/blog-research", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/getapp/blog-research` with the body above minus `model`.

## Details

Returns the latest blog posts and software research guides from the GetApp resources section, plus the topic list and the featured content hubs. It takes no input. Send an empty JSON object.

### Use cases

- Track new GetApp buying guides in a software category such as pool service or music school software.
- Build a feed of GetApp articles with author names, publish dates and short summaries.
- Count how many posts GetApp has published under each topic to see which software areas get the most coverage.
- Collect the content hub links to find GetApp's long-form learning pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/getapp/blog-research" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "appData": {
      "_vercelExperimentsGa4": {},
      "_vercelFlags": {
        "getapp-ai-assistant": 0,
        "getapp-osano-cmp-primary": -1
      },
      "canShowLiveChat": true,
      "categories": [],
      "category": {},
      "compareBasketState": [],
      "countryCode": "US",
      "csrf": "",
      "experiments": {
        "currentPageActiveExperimentIds": [],
        "ga4": {
          "User_Information_GAExperimentId": null,
          "User_Information_GAExperimentUserId": "e05e334b-2e9c-45ac-a3b1-b249fc833153"
        },
        "variations": {}
      },
      "g2CompanyLookupApiKey": "pk_7874b…",
      "g2CompanyLookupUrl": "https://enrich.g2.com/quem",
      "g2EnrichHit": false
    },
    "contentHubs": [
      {
        "category": "LEARNING HUB",
        "content": "Shield your business from online threats and cybercriminals.",
        "image": {
          "url": "https://images.ctfassets.net/1nw0m35kh5t7/4eGH9eWLYmoKnZQzX8cwv6/92d3756b91e3a93…"
        },
        "title": "What is Cybersecurity?",
        "url": "https://www.getapp.com/knowledge-base/what-is-cybersecurity/"
      }
    ],
    "posts": {
      "items": [
        {
          "authors": {
            "items": [
              {
                "authorName": "Preksha Buttan",
                "authorTitle": "Content Writer",
                "avatar": {
                  "url": "https://images.ctfassets.net/1nw0m35kh5t7/701eMQxzFPfjdWSe36417R/068034ee3d830b1…"
                },
                "bio": "Preksha Buttan is a Writer at GetApp. She provides expert insights and helps sma…",
                "linkedInUrl": "https://www.linkedin.com/in/preksha-b-6661aa175/",
                "slug": "preksha-buttan",
                "twitterUrl": null
              }
            ],
            "total": 1
          },
          "contentfulMetadata": {
            "tags": []
          },
          "hasRedirect": null,
          "permalink": "best-mobile-pool-service-software",
          "publishDate": "2026-10-27T00:00:00.000-05:00",
          "redirectUrl": null,
          "shortDescription": "Learn what technicians can record at a stop, which phones and tablets each app s…",
          "slug": "best-mobile-pool-service-software"
        }
      ],
      "total": 834
    },
    "topics": {
      "items": [
        {
          "contentfulMetadata": {
            "tags": []
          },
          "linkedFrom": {
            "posts": {
              "total": 47
            }
          },
          "name": "Accounting & Finance",
          "slug": "accounting-and-finance",
          "sys": {
            "id": "1mesKpTa83u8DZq6nKoTip"
          }
        }
      ]
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts.total` | Total number of posts in the result set. |
| `data.posts.items[].slug / data.posts.items[].permalink` | URL slug of the post. In the sample, both fields hold the same value. |
| `data.posts.items[].shortDescription` | Short summary of the post. |
| `data.posts.items[].publishDate` | Publish date and time of the post as an ISO 8601 string with a UTC offset. |
| `data.posts.items[].authors.items[].authorName / data.posts.items[].authors.items[].authorTitle` | Name and job title of each post author. |
| `data.posts.items[].authors.items[].linkedInUrl / data.posts.items[].authors.items[].twitterUrl` | Author social profile links. A value is `null` when the author has no link. |
| `data.topics.items[].name / data.topics.items[].slug` | Display name and slug of a topic, for example `Accounting & Finance` and `accounting-and-finance`. |
| `data.topics.items[].linkedFrom.posts.total` | Number of posts linked to the topic. |
| `data.contentHubs[].title / data.contentHubs[].url` | Title and link of a content hub page, such as a knowledge-base guide. |
| `data.contentHubs[].category / data.contentHubs[].content` | Label of the hub (for example `LEARNING HUB`) and a one-line description. |

### Notes

- The request has no parameters, so the call always uses the empty body `{}`.
- `data.posts.items` holds only a sample of the posts, while `data.posts.total` shows the full count.
- The `data.appData` object holds page and session settings for the resources home page. Ignore it for content work.
- To research the software itself, call [GetApp List Categories](/apis/getapp/list-categories) or [GetApp Software Details](/apis/getapp/software-details).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/getapp/blog-research.json`](../../../catalog/models/getapp/blog-research.json) · Store page: https://www.sandbase.ai/model/getapp/blog-research
