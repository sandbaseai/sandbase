# LinkedIn Comment Reactions API: pricing, parameters and code examples

`linkedin/comment-reactions` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0026 per call · **Modes:** sync

List who reacted to a comment on a LinkedIn post - reactor name, profile URL, job title, and reaction type, 100 per page.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0026**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/comment-reactions", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/comment-reactions', {'url': 'https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/comment-reactions", {
  "url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/comment-reactions", sandbase.Params{
	"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29",
})
```

Same call via the path form: `POST /v1/api/linkedin/comment-reactions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A post URL without dashCommentUrn, or…  |
| `page` | integer |  | Which page of up to 100 reactions to return, starting at 1 (default 1). Each page is billed as one request; totalPages in the response says how many there are. default `1`; range 1– |

## Details

Returns the people who reacted to a single LinkedIn comment. Each row has the reactor's name, profile URL, job title, and reaction type. It needs a LinkedIn comment URL and returns 100 reactions per page.

### Use cases

- Build a list of people who engaged with a high-performing comment for outreach or lead research.
- Filter reactors by job title to see which roles respond to a comment.
- Count reaction types such as `LIKE` and `EMPATHY` to measure how a comment landed.
- Export all reactors across pages to track engagement on a competitor's or customer's comment.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/comment-reactions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A post URL without dashCommentUrn, or a |
| `page` | integer | No | Which page of up to 100 reactions to return, starting at 1 (default 1). Each page is billed as one request; totalPages in the response says how many there are. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "actor": {
          "id": "ACoAAABuyR8B_XgmyiciUgrKJ4bFT4xocdOiFxA",
          "image": "https://media.licdn.com/dms/image/v2/C5603AQExZU_iRhfBDw/profile-displayphoto-sh…",
          "linkedinUrl": "https://www.linkedin.com/in/ACoAAABuyR8B_XgmyiciUgrKJ4bFT4xocdOiFxA",
          "name": "Gretchen Tuccy, PHR, SHRM-CP",
          "position": "Manager, HR Systems & Operations at DCS Corp"
        },
        "commentUrn": "urn:li:comment:(activity:7510715600319467520,7510768837462745088)",
        "id": "urn:li:fsd_reaction:(urn:li:fsd_profile:ACoAAABuyR8B_XgmyiciUgrKJ4bFT4xocdOiFxA,…",
        "reactionType": "LIKE"
      }
    ],
    "page": 1,
    "totalPages": 5,
    "totalResults": 490
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].actor.name` | Display name of the person who reacted. |
| `data.items[].actor.position` | Headline or job title text shown on the reactor's profile, such as a role and company. |
| `data.items[].actor.linkedinUrl` | URL of the reactor's LinkedIn profile. |
| `data.items[].actor.id` | LinkedIn profile ID of the reactor. It is also the last part of `linkedinUrl`. |
| `data.items[].actor.image` | URL of the reactor's profile photo. |
| `data.items[].reactionType` | Type of reaction, for example `LIKE` or `EMPATHY`. |
| `data.items[].commentUrn` | URN of the comment that was reacted to. It is the same on every row. |
| `data.items[].id` | Unique ID of the reaction, built from the reactor's profile URN and the comment URN. |
| `data.page / data.totalPages` | The page returned and the total number of pages available. |
| `data.totalResults` | Total number of reactions on the comment across all pages. |

### Notes

- Get the comment URL from the `url` field of [LinkedIn Post Comments](/apis/linkedin/post-comments), or use "Copy link to comment" on LinkedIn. The URL must carry `commentUrn` and `dashCommentUrn`.
- A post URL without `dashCommentUrn`, or a reply URL carrying `replyUrn`, is refused as invalid input.
- Set `page` to 2, 3, and so on to read further pages. Stop at `data.totalPages`.
- To see reactions on the post itself, call [LinkedIn Post Reactions](/apis/linkedin/post-reactions).

### Pricing

Billed at the actual cost of each call, about $0.0026 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/comment-reactions.json`](../../../catalog/models/linkedin/comment-reactions.json) · Store page: https://www.sandbase.ai/model/linkedin/comment-reactions
