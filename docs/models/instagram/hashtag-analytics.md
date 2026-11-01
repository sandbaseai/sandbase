# Instagram Hashtag Analytics

`instagram/hashtag-analytics` · api · Instagram

Get the total post count for any Instagram hashtag.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-analytics", "hashtag": "travel"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-analytics', {'hashtag': 'travel'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-analytics", {
  "hashtag": "travel"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-analytics", sandbase.Params{
	"hashtag": "travel",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-analytics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Deprecated. Has no effect. range 1–20 |
| `hashtag` | string | yes | The Instagram hashtag to analyze, with or without the # symbol (e.g. streetphotography).  |

## Details

Get the total post count for any Instagram hashtag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-analytics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "hashtag": "travel"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | The Instagram hashtag to analyze, with or without the # symbol (e.g. streetphotography). |
| `limit` | integer | No | Deprecated. Has no effect. |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/hashtag-analytics.json`](../../../catalog/models/instagram/hashtag-analytics.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-analytics
