# LinkedIn Group Posts API: pricing, parameters and code examples

`linkedin/group-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0026 per call · **Modes:** sync

List the posts in a LinkedIn group by group URL, newest first: full text, canonical link, publish date, author, engagement counts with a per-reaction breakdown, and attached media. One call returns a page of about 100 posts; pass page to go further back.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0026**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/group-posts", "url": "https://www.linkedin.com/groups/1898033"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/group-posts', {'url': 'https://www.linkedin.com/groups/1898033'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/group-posts", {
  "url": "https://www.linkedin.com/groups/1898033"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/group-posts", sandbase.Params{
	"url": "https://www.linkedin.com/groups/1898033",
})
```

Same call via the path form: `POST /v1/api/linkedin/group-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033).  |
| `page` | integer |  | Which page of about 100 posts to return, starting at 1 (default 1). Page 2 continues where page 1 ended, going further back in time. Each page is billed as one request. default `1`; range 1– |
| `postedLimit` | string |  | Only return posts published within this window (default any). The window is applied to the page, so a page can come back with fewer posts or none. one of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |

## Details

Returns a page of about 100 posts from a LinkedIn group, newest first. Each post has its text, link, publish time, author, engagement counts and attached media. The only required input is the group URL.

### Use cases

- Track what members of a sales or industry group discuss and which posts get the most reactions.
- Find active authors and group admins to study or contact.
- Collect shared articles and newsletters that circulate in a niche community.
- Monitor a group for new posts by pulling the first page on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/group-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/groups/1898033"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). |
| `page` | integer | No | Which page of about 100 posts to return, starting at 1 (default 1). Page 2 continues where page 1 ended, going further back in time. Each page is billed as one request. |
| `postedLimit` | string | No | Only return posts published within this window (default any). The window is applied to the page, so a page can come back with fewer posts or none. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "author": {
          "groupAdmin": true,
          "handle": "leesalz",
          "headline": "I architect sales strategies that make salespeople the reason buyers choose thei…",
          "id": "ACoAAADVAqYB4PzT526QoAz34ogYKSvUS-y_KMg",
          "image": "https://media.licdn.com/dms/image/v2/D5603AQGn5rWKhbQH8A/profile-displayphoto-cr…",
          "linkedinUrl": "https://www.linkedin.com/in/leesalz",
          "name": "Lee Salz",
          "type": "profile"
        },
        "contentAttributes": [
          {
            "hyperlink": null,
            "length": 24,
            "start": 551,
            "textLink": "https://lnkd.in/g8ci5eTN",
            "type": "TEXT_LINK"
          }
        ],
        "createdUtc": 1793383149,
        "edited": false,
        "engagement": {
          "comments": 0,
          "likes": 12,
          "reactions": [
            {
              "count": 11,
              "type": "LIKE"
            }
          ],
          "shares": 1
        },
        "id": "7521994118672261121",
        "pinned": true,
        "pollOptions": [],
        "postImages": [
          {
            "height": 1350,
            "url": "https://media.licdn.com/dms/image/v2/D5622AQHToSpcNczqcw/feedshare-image-high-re…",
            "width": 1080
          }
        ],
        "postVideo": null,
        "repostEngagement": {},
        "repostImages": []
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].id` | Post ID as a string of digits. |
| `data.items[].text` | Post text. Long posts may be cut in the response, and links in the text appear as short `lnkd.in` URLs. |
| `data.items[].url / data.items[].shareUrl` | Link to the post on LinkedIn. It contains the group ID and a `urn:li:groupPost` ID. |
| `data.items[].createdUtc` | Publish time as a Unix timestamp in seconds. |
| `data.items[].pinned` | `true` when the post is pinned in the group. |
| `data.items[].author.name / data.items[].author.headline` | Name and profile headline of the person who posted. |
| `data.items[].author.linkedinUrl / data.items[].author.handle` | Profile link and handle of the author. |
| `data.items[].author.groupAdmin` | `true` when the author is an admin of the group. |
| `data.items[].engagement.likes / data.items[].engagement.comments / data.items[].engagement.shares` | Counts of likes, comments and shares on the post. |
| `data.items[].engagement.reactions[]` | Breakdown of reactions. Each row has a `type` such as `LIKE`, `APPRECIATION` or `INTEREST`, and a `count`. |
| `data.items[].postImages[]` | Images attached to the post, with `url`, `width` and `height`. |
| `data.items[].articleTitle / data.items[].articleUrl` | Title and link of an article shared in the post. These keys appear only on posts that share an article. |

### Notes

- Pass the full group URL in `url`, for example `https://www.linkedin.com/groups/1898033`. Use [LinkedIn Group Search](/apis/linkedin/search-groups) to find groups.
- Set `page` to 2, 3 and so on to go further back in time. Each page holds about 100 posts.
- `postedLimit` filters the page after it is loaded, so a page can return fewer posts or none.
- Call [LinkedIn Post](/apis/linkedin/post) or [LinkedIn Post Comments](/apis/linkedin/post-comments) to look closer at a single post.

### Pricing

Billed at the actual cost of each call, about $0.0026 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/group-posts.json`](../../../catalog/models/linkedin/group-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/group-posts
