# X / Twitter User Search API: pricing, parameters and code examples

`twitter/search-users` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00054 per call · **Modes:** sync

Search X (Twitter) accounts by keyword - the People tab of X search. Matches handles, display names, and profile bios, and returns normalized profile records with follower, following, and post counts plus cursor pagination. Use twitter.search for posts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/search-users", "query": "ai agents"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/search-users', {'query': 'ai agents'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/search-users", {
  "query": "ai agents"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/search-users", sandbase.Params{
	"query": "ai agents",
})
```

Same call via the path form: `POST /v1/api/twitter/search-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to match against X (Twitter) handles, display names, and profile bios. This is the People tab of X search: pass a topic ('ai agents'), a name ('Elon Musk'), or a handle ('openai') and get back accounts, not…  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of accounts.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one…  |

## Details

Search X (Twitter) accounts by keyword - the People tab of X search. Matches handles, display names, and profile bios, and returns normalized profile records with follower, following, and post counts plus cursor pagination. Use twitter.search for posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/search-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ai agents"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to match against X (Twitter) handles, display names, and profile bios. This is the People tab of X search: pass a topic ('ai agents'), a name ('Elon Musk'), or a handle ('openai') and get back accounts, not posts |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of accounts. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `location`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, usually $0.00054 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/search-users.json`](../../../catalog/models/twitter/search-users.json) · Store page: https://www.sandbase.ai/model/twitter/search-users
