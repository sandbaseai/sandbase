# LinkedIn Group Posts

`linkedin/group-posts` · api · LinkedIn

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

List the posts in a LinkedIn group by group URL, newest first: full text, canonical link, publish date, author, engagement counts with a per-reaction breakdown, and attached media. One call returns a page of about 100 posts; pass page to go further back.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/group-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/groups/1898033"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn group URL (e.g. https://www.linkedin.com/groups/1898033). |
| `page` | integer | No | Which page of about 100 posts to return, starting at 1 (default 1). Page 2 continues where page 1 ended, going further back in time. Each page is billed as one request. |
| `postedLimit` | string | No | Only return posts published within this window (default any). The window is applied to the page, so a page can come back with fewer posts or none. One of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |

### Pricing

Billed at the actual cost of each call, usually $0.0026 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/group-posts.json`](../../../catalog/models/linkedin/group-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/group-posts
