# LinkedIn Post Reactions API: pricing, parameters and code examples

`linkedin/post-reactions` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0029 per call · **Modes:** sync

List who reacted to a LinkedIn post - reactor name, profile URL, job title, and reaction type. Lead-gen grade.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0029**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/post-reactions", "url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/post-reactions', {'url': 'https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/post-reactions", {
  "url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/post-reactions", sandbase.Params{
	"url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG",
})
```

Same call via the path form: `POST /v1/api/linkedin/post-reactions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | URL of the LinkedIn post to list reactions for (a /posts/...-activity-... or /feed/update/urn:li:activity:... link).  |
| `limit` | integer |  | Maximum number of reactions to return (1-100, default 100). range 1–100 |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postId`, and it is served only by a source that returns every one…  |

## Details

Returns the people who reacted to a public LinkedIn post. Each row has the reactor's name, profile URL, headline and reaction type. It needs the post URL as input.

### Use cases

- Build a lead list from people who reacted to a competitor's or an executive's post.
- Check which job titles and industries engage with a post about your product.
- Count reaction types such as `LIKE` on a campaign post to compare posts.
- Find engaged profiles to review or enrich further.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/post-reactions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/posts/satyanadella_today-were-bringing-skills-to-copilot-for-activity-7475945433668694017--kvG", "limit": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | URL of the LinkedIn post to list reactions for (a /posts/...-activity-... or /feed/update/urn:li:activity:... link). |
| `limit` | integer | No | Maximum number of reactions to return (1-100, default 100). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `postId`, and it is served only by a source that returns every one of  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "actor": {
          "id": "ACoAAD4aAo0BsZ10crKCys0Pp0kbBjhn26OpGaA",
          "linkedinUrl": "https://www.linkedin.com/in/soundernarayanasamy/",
          "name": "Sounder Narayana Samy K",
          "pictureUrl": "https://media.licdn.com/dms/image/v2/D5603AQFqIDeCdph7Mg/profile-displayphoto-cr…",
          "position": "UI/UX Designer | Product Designer | E-commerce & AI SaaS | Figma to React/Next.j…"
        },
        "postId": null,
        "reactionType": "LIKE"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].actor.name` | Display name of the person who reacted. |
| `data.items[].actor.linkedinUrl` | Link to the reactor's LinkedIn profile. |
| `data.items[].actor.position` | Headline text from the reactor's profile. It often holds the job title plus other self-written text. |
| `data.items[].actor.id` | LinkedIn member ID of the reactor, in the `ACoAA...` format. |
| `data.items[].actor.pictureUrl` | Link to the reactor's profile photo. It is an empty string when there is no photo. |
| `data.items[].reactionType` | Type of reaction the person left, for example `LIKE`. |
| `data.items[].postId` | ID of the post. It can be `null` in the response. |
| `found` | `true` when the post was found. |

### Notes

- Copy `url` from the post's share link. It can be a `/posts/...-activity-...` link or a `/feed/update/urn:li:activity:...` link.
- Set `limit` between 1 and 100. The default is 100.
- `postId` was `null` in this response. Pass `requireFields: ["postId"]` to be served only by a source that returns it. This can raise the price.
- To read the comments on the same post, call [LinkedIn Post Comments](/apis/linkedin/post-comments).

### Pricing

Billed at the actual cost of each call, about $0.0029 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/post-reactions.json`](../../../catalog/models/linkedin/post-reactions.json) · Store page: https://www.sandbase.ai/model/linkedin/post-reactions
