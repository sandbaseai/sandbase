# X / Twitter Community Search API: pricing, parameters and code examples

`twitter/search-communities` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search X (Twitter) communities by keyword and get their id, name, topic, and member count with cursor pagination. This is how you find a community URL to pass to twitter.community or twitter.community_tweets.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search-communities", "query": "artificial intelligence"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search-communities', {'query': 'artificial intelligence'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search-communities", {
  "query": "artificial intelligence"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search-communities", sandbase.Params{
	"query": "artificial intelligence",
})
```

Same call via the path form: `POST /v1/api/twitter/search-communities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to match against X (Twitter) community names and topics (e.g. artificial intelligence).  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of communities.  |

## Details

Search X (Twitter) communities by keyword and get their id, name, topic, and member count with cursor pagination. This is how you find a community URL to pass to twitter.community or twitter.community_tweets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search-communities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "artificial intelligence"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to match against X (Twitter) community names and topics (e.g. artificial intelligence). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of communities. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/search-communities.json`](../../../catalog/models/twitter/search-communities.json) · Store page: https://www.sandbase.ai/model/twitter/search-communities
