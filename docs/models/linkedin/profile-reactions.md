# LinkedIn Profile Reactions API: pricing, parameters and code examples

`linkedin/profile-reactions` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List the posts a LinkedIn member has reacted to - the reaction, its timestamp, and the full post it was made on with author and engagement.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/profile-reactions", "url": "https://www.linkedin.com/in/williamhgates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/profile-reactions', {'url': 'https://www.linkedin.com/in/williamhgates'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/profile-reactions", {
  "url": "https://www.linkedin.com/in/williamhgates"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/profile-reactions", sandbase.Params{
	"url": "https://www.linkedin.com/in/williamhgates",
})
```

Same call via the path form: `POST /v1/api/linkedin/profile-reactions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the LinkedIn member profile whose reactions to list, for example https://www.linkedin.com/in/williamhgates.  |
| `limit` | integer |  | Maximum number of reactions to return. One page holds 100. default `100`; range 1–100 |

## Details

Returns the posts a LinkedIn member has reacted to. Each item has the reaction, its timestamp, and the post it was made on, including the post author and engagement counts. The input is the full LinkedIn profile URL of the member.

### Use cases

- List what a founder or executive reacts to, to see which topics and people they follow.
- Find which authors a target profile engages with most often.
- Track new reactions from a profile you monitor by comparing `createdUtc` values between calls.
- Collect posts that a group of members reacted to, along with each post's reaction and comment counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/profile-reactions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/williamhgates", "limit": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the LinkedIn member profile whose reactions to list, for example https://www.linkedin.com/in/williamhgates. |
| `limit` | integer | No | Maximum number of reactions to return. One page holds 100. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "action": "likes this",
        "actor": {
          "linkedinUrl": "https://www.linkedin.com/in/williamhgates"
        },
        "createdUtc": 1793328053,
        "id": "7521763026652368896",
        "post": {
          "author": {
            "headline": "Consultant Obstetrician & Gynaecologist | Reproductive Medicine & Fertility | Co…",
            "id": "ACoAACUvMyQBnhg-mScZ0mzZIAb7WC-yD4oBUrA",
            "image": "https://media.licdn.com/dms/image/v2/D4E03AQEYCk_qGeyb-Q/profile-displayphoto-cr…",
            "name": "Dr Yasmin Mulji",
            "profileUrl": "https://www.linkedin.com/in/yasmin-mulji",
            "publicIdentifier": "yasmin-mulji",
            "type": "profile"
          },
          "engagement": {
            "breakdown": [
              {
                "count": 154,
                "type": "LIKE"
              }
            ],
            "comments": 11,
            "reactions": 175,
            "reposts": 2
          },
          "id": "7520763761922744320",
          "postedUtc": 1793089809,
          "text": "What does a doctor say to a philanthropist who’s already given over $100bn to im…",
          "url": "https://www.linkedin.com/posts/yasmin-mulji_what-does-a-doctor-say-to-a-philanth…"
        },
        "url": "https://www.linkedin.com/feed/update/urn:li:activity:7521763026652368896"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].action` | Text describing the reaction, for example `likes this`. |
| `data.items[].createdUtc` | Time the member made the reaction. The value is a Unix timestamp. |
| `data.items[].id / data.items[].url` | ID of the reaction and its LinkedIn feed link. |
| `data.items[].actor.linkedinUrl` | Profile URL of the member who reacted. It matches the `url` you sent. |
| `data.items[].post.text` | Text of the post that was reacted to. Long text is cut in the sample. |
| `data.items[].post.url / data.items[].post.id` | Link to the post and its ID. |
| `data.items[].post.postedUtc` | Time the post was published, as a Unix timestamp. |
| `data.items[].post.author.name / data.items[].post.author.headline` | Name and headline of the person who wrote the post. |
| `data.items[].post.author.profileUrl / data.items[].post.author.publicIdentifier` | Profile link and public handle of the post author. |
| `data.items[].post.engagement.reactions / data.items[].post.engagement.comments / data.items[].post.engagement.reposts` | Total reaction, comment and repost counts on the post. |
| `data.items[].post.engagement.breakdown[]` | Reaction counts per type, such as `LIKE`, `PRAISE`, `EMPATHY` and `APPRECIATION`. Each row has `type` and `count`. |

### Notes

- Use the full profile URL in the form `https://www.linkedin.com/in/<handle>` for `url`.
- `limit` accepts 1 to 100 and defaults to 100.
- To read the full post that a reaction points to, call [LinkedIn Post](/apis/linkedin/post). To see who else reacted, call [LinkedIn Post Reactions](/apis/linkedin/post-reactions).
- To see the member's own comments instead of reactions, use [LinkedIn Profile Comments](/apis/linkedin/profile-comments).

### Pricing

Billed at the actual cost of each call, about $0.0029 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/profile-reactions.json`](../../../catalog/models/linkedin/profile-reactions.json) · Store page: https://www.sandbase.ai/model/linkedin/profile-reactions
