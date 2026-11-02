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

List up to the 10 newest replies to a comment on a LinkedIn post - reply text, replier name/URL/job title, timestamps, and likes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510749329649725442%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510749329649725442%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A reply's URL returns the thread it bel |

### Pricing

Billed at the actual cost of each call, usually $0.0026 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/comment-replies.json`](../../../catalog/models/linkedin/comment-replies.json) · Store page: https://www.sandbase.ai/model/linkedin/comment-replies
