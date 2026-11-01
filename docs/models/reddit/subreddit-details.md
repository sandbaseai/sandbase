# Reddit Subreddit Details

`reddit/subreddit-details` · api · Reddit

Fetch a subreddit's metadata (weekly active users, description, and category).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-details", "subreddit": "programming"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-details', {'subreddit': 'programming'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-details", {
  "subreddit": "programming"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-details", sandbase.Params{
	"subreddit": "programming",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subreddit` | string | yes | Subreddit name without the r/ prefix. Case-sensitive (e.g. "AskReddit", not "askreddit").  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `weeklyActiveUsers` or `advertiserCategory`, and it is served only…  |

## Details

Fetch a subreddit's metadata (weekly active users, description, and category).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit": "programming"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the r/ prefix. Case-sensitive (e.g. "AskReddit", not "askreddit"). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `weeklyActiveUsers` or `advertiserCategory`, and it is served only by  |

### Pricing

Billed at the actual cost of each call, usually $0.00038 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/subreddit-details.json`](../../../catalog/models/reddit/subreddit-details.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-details
