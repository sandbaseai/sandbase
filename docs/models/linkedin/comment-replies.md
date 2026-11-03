# LinkedIn Comment Replies API: pricing, parameters and code examples

`linkedin/comment-replies` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0026 per call · **Modes:** sync

List up to the 10 newest replies to a comment on a LinkedIn post - reply text, replier name/URL/job title, timestamps, and likes.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0026**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/comment-replies", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/comment-replies', {'url': 'https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/comment-replies", {
  "url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/comment-replies", sandbase.Params{
	"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29",
})
```

Same call via the path form: `POST /v1/api/linkedin/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A reply's URL returns the thread it…  |

## Details

This API returns up to the 10 newest replies to one comment on a LinkedIn post. Each reply includes the text, the replier's name, profile URL and job title, a timestamp, and like counts. It needs a LinkedIn comment URL as input.

### Use cases

- Read the full thread under a high-traffic comment to see how people respond to it.
- Collect the profile URLs and job titles of people who reply to a comment, to build a list of engaged accounts.
- Track which replies draw likes and which reaction types they get.
- Find who is mentioned in each reply through the `contentAnnotations` entries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A reply's URL returns the thread it bel |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "actor": {
          "id": "ACoAAAEdHaIBq2zcPNMrJ_k-Z5E7LasZNFSRl7E",
          "linkedinUrl": "https://www.linkedin.com/in/kate-orloski-3423116",
          "name": "Kate Orloski",
          "position": "Marketing",
          "type": "profile"
        },
        "commentary": "Paul Linehan\nTo put a finer point on this, your earlier response, “My point was …",
        "contentAnnotations": [
          {
            "hyperlink": "https://www.linkedin.com/in/ACoAAAbqHRMBD_eyM7-R9_bqbQHjBhVCpmHRIq4",
            "length": 12,
            "profileFirstName": "Paul",
            "profileId": "ACoAAAbqHRMBD_eyM7-R9_bqbQHjBhVCpmHRIq4",
            "profileLastName": "Linehan",
            "profileUrl": "https://www.linkedin.com/in/ACoAAAbqHRMBD_eyM7-R9_bqbQHjBhVCpmHRIq4",
            "start": 0,
            "type": "PROFILE_MENTION"
          }
        ],
        "createdUtc": 1792813635,
        "edited": false,
        "engagement": {
          "likes": 0,
          "reactions": []
        },
        "id": "7519605402238476288",
        "postId": "activity:7510715600319467520",
        "url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?comment…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].commentary` | Text of the reply. In the sample it starts with the name of the person being replied to. |
| `data.items[].actor.name / data.items[].actor.position` | Display name and headline of the person who wrote the reply. |
| `data.items[].actor.linkedinUrl / data.items[].actor.id` | Profile URL and LinkedIn profile ID of the replier. The `image` field holds a profile photo URL when one is present. |
| `data.items[].createdUtc` | Time the reply was posted. The value is a Unix timestamp in seconds. |
| `data.items[].edited` | `true` if the reply was edited after posting. |
| `data.items[].engagement.likes` | Like count for the reply. |
| `data.items[].engagement.reactions[].type / data.items[].engagement.reactions[].count` | Reaction type, such as `LIKE` or `APPRECIATION`, and how many people gave it. |
| `data.items[].contentAnnotations[].profileUrl / data.items[].contentAnnotations[].type` | Profile link for each annotation in the reply text. A `PROFILE_MENTION` marks a mentioned person. |
| `data.items[].id / data.items[].postId` | ID of the reply and the ID of the post it belongs to, in the form `activity:<number>`. |
| `found` | `true` when the comment was found. |

### Notes

- Get the input `url` from the `url` field of [LinkedIn Post Comments](/apis/linkedin/post-comments), or copy it with "Copy link to comment" on LinkedIn.
- The URL must carry `commentUrn` and `dashCommentUrn`. A post URL without `dashCommentUrn` is refused as invalid input.
- A reply's URL returns the thread it belongs to.
- To see who reacted to a comment, call [LinkedIn Comment Reactions](/apis/linkedin/comment-reactions).

### Pricing

Billed at the actual cost of each call, about $0.0026 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/comment-replies.json`](../../../catalog/models/linkedin/comment-replies.json) · Store page: https://www.sandbase.ai/model/linkedin/comment-replies
