# Alibaba.com Search API: pricing, parameters and code examples

`alibaba/search` · data API · Alibaba.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00231 per call · **Modes:** sync

Search Alibaba by keyword and get up to 25 wholesale listings (title, price range, minimum order, and supplier) in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00231**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/search", "query": "bluetooth speaker"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('alibaba/search', {'query': 'bluetooth speaker'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("alibaba/search", {
  "query": "bluetooth speaker"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "alibaba/search", sandbase.Params{
	"query": "bluetooth speaker",
})
```

Same call via the path form: `POST /v1/api/alibaba/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. range 1–25 |
| `query` | string | yes | Keywords to search for on Alibaba (e.g. "bluetooth speaker wholesale").  |

## Details

Search Alibaba by keyword and get up to 25 wholesale listings (title, price range, minimum order, and supplier) in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "alibaba/search", "limit": 3, "query": "bluetooth speaker"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keywords to search for on Alibaba (e.g. "bluetooth speaker wholesale"). |
| `limit` | integer | No | Maximum number of results to return (1-25, default 25). You are billed per result returned, so a lower limit costs less. |

### Pricing

Billed at the actual cost of each call: about $0.00077 per result returned, up to $0.0193 per request (about $0.00231 for the request above). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/alibaba/search.json`](../../../catalog/models/alibaba/search.json) · Store page: https://www.sandbase.ai/model/alibaba/search
