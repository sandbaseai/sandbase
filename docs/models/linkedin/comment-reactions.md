# LinkedIn Comment Reactions

`linkedin/comment-reactions` · api · LinkedIn

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

List who reacted to a comment on a LinkedIn post - reactor name, profile URL, job title, and reaction type, 100 per page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/comment-reactions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/feed/update/urn:li:activity:7510715600319467520?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7510715600319467520%2C7510768837462745088%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510768837462745088%2Curn%3Ali%3Aactivity%3A7510715600319467520%29"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | LinkedIn comment URL, as returned in the url field of linkedin.post_comments or copied with "Copy link to comment" (a /feed/update/... link carrying commentUrn and dashCommentUrn). A post URL without dashCommentUrn, or a |
| `page` | integer | No | Which page of up to 100 reactions to return, starting at 1 (default 1). Each page is billed as one request; totalPages in the response says how many there are. |

### Pricing

Billed at the actual cost of each call, usually $0.0026 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/comment-reactions.json`](../../../catalog/models/linkedin/comment-reactions.json) · Store page: https://www.sandbase.ai/model/linkedin/comment-reactions
