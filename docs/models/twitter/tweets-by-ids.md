# X (Twitter) Tweets by IDs API: pricing, parameters and code examples

`twitter/tweets-by-ids` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0075 per call · **Modes:** sync

Look up several tweets at once by a comma-separated list of tweet IDs, with text, author and engagement counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0075**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/tweets-by-ids", "tweet_ids": "1585341984679469056,1846987139428634858"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/tweets-by-ids', {'tweet_ids': '1585341984679469056,1846987139428634858'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/tweets-by-ids", {
  "tweet_ids": "1585341984679469056,1846987139428634858"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/tweets-by-ids", sandbase.Params{
	"tweet_ids": "1585341984679469056,1846987139428634858",
})
```

Same call via the path form: `POST /v1/api/twitter/tweets-by-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweet_ids` | string | yes | Comma-separated list of tweet IDs.  |

## Details

Look up several tweets at once by a comma-separated list of tweet IDs, with text, author and engagement counts.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/tweets-by-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_ids": "1585341984679469056,1846987139428634858"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_ids` | string | No | Comma-separated list of tweet IDs. |

### Pricing

Billed at the actual cost of each call, about $0.0075 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/tweets-by-ids.json`](../../../catalog/models/twitter/tweets-by-ids.json) · Store page: https://www.sandbase.ai/model/twitter/tweets-by-ids
