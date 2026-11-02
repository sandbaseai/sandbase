# X / Twitter Trends API: pricing, parameters and code examples

`twitter/trends` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0001 per call · **Modes:** sync

Get current X (Twitter) trends for worldwide, a country, or a city in X ranking order, including the resolved location.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/trends"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/trends', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/trends", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/trends", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitter/trends` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of ranked trends to return (1-50, default 50). default `50`; range 1–50 |
| `location` | string |  | Country name, city name, or ISO country code. Omit for worldwide trends.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `promoted`, and it is served only by a source that returns every one…  |

## Details

Get current X (Twitter) trends for worldwide, a country, or a city in X ranking order, including the resolved location.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/trends" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10, "location": "US"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Maximum number of ranked trends to return (1-50, default 50). |
| `location` | string | No | Country name, city name, or ISO country code. Omit for worldwide trends. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `promoted`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, usually $0.0001 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/trends.json`](../../../catalog/models/twitter/trends.json) · Store page: https://www.sandbase.ai/model/twitter/trends
