# LinkedIn Profile Posts (full) API: pricing, parameters and code examples

`linkedin/profile-posts-full` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Fetch recent public LinkedIn profile posts with enriched author, engagement, article, newsletter, media, annotation, repost, and social activity details.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/profile-posts-full", "url": "https://www.linkedin.com/in/williamhgates/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/profile-posts-full', {'url': 'https://www.linkedin.com/in/williamhgates/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/profile-posts-full", {
  "url": "https://www.linkedin.com/in/williamhgates/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/profile-posts-full", sandbase.Params{
	"url": "https://www.linkedin.com/in/williamhgates/",
})
```

Same call via the path form: `POST /v1/api/linkedin/profile-posts-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full URL of the public LinkedIn profile whose posts should be returned.  |
| `limit` | integer |  | Most posts to return (1-100, default 10). Ignored on sources that page: each call returns one full page of 50 posts; follow nextCursor for more. Sources that cannot page return up to `limit` posts in one call with no… default `10`; range 1–100 |
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `postedLimit` | string |  | Only return posts published within this relative time window. one of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |
| `contextCountry` | string |  | Regional LinkedIn context used when retrieving posts. one of: `any`, `US`, `GB`, `DE`, `FR` |
| `includeReposts` | boolean |  | Whether to include reposts that share content without added commentary. default `true` |
| `postedLimitDate` | string |  | Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string.  |
| `includeQuotePosts` | boolean |  | Whether to include quote posts that add commentary to shared content. default `true` |

## Details

Fetch recent public LinkedIn profile posts with enriched author, engagement, article, newsletter, media, annotation, repost, and social activity details.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/profile-posts-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/in/williamhgates/", "limit": 10}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full URL of the public LinkedIn profile whose posts should be returned. |
| `contextCountry` | string | No | Regional LinkedIn context used when retrieving posts. One of: `any`, `US`, `GB`, `DE`, `FR`. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |
| `includeQuotePosts` | boolean | No | Whether to include quote posts that add commentary to shared content. Default `true`. |
| `includeReposts` | boolean | No | Whether to include reposts that share content without added commentary. Default `true`. |
| `limit` | integer | No | Most posts to return (1-100, default 10). Ignored on sources that page: each call returns one full page of 50 posts; follow nextCursor for more. Sources that cannot page return up to `limit` posts in one call with no nex |
| `postedLimit` | string | No | Only return posts published within this relative time window. One of: `any`, `1h`, `24h`, `week`, `month`, `3months`, `6months`, `year`. |
| `postedLimitDate` | string | No | Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |

### Pricing

Billed at the actual cost of each call, usually $0.005 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/profile-posts-full.json`](../../../catalog/models/linkedin/profile-posts-full.json) · Store page: https://www.sandbase.ai/model/linkedin/profile-posts-full
