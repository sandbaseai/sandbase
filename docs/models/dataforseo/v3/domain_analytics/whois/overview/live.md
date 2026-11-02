# DataForSEO Whois Overview with Site Metrics API: pricing, parameters and code examples

`dataforseo/v3/domain_analytics/whois/overview/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.1212 per call · **Modes:** sync

Whois records for domains matching filters, enriched with backlink and organic traffic metrics.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.1212**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/domain_analytics/whois/overview/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/domain_analytics/whois/overview/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/domain_analytics/whois/overview/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/domain_analytics/whois/overview/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/domain_analytics/whois/overview/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of domains to return.  |
| `filters` | array |  | Filter array, e.g. [["domain", "=", "nike.com"]].  |

## Details

Whois records for domains matching filters, enriched with backlink and organic traffic metrics.

Request fields follow the official DataForSEO `/v3/domain_analytics/whois/overview/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/domain_analytics/whois/overview/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"filters": [["domain", "=", "nike.com"]], "limit": 1}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `filters` | Filter array, e.g. [["domain", "=", "nike.com"]]. |
| `limit` | Maximum number of domains to return. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/domain_analytics/whois/overview/live/

### Pricing

Billed at the actual cost of each call, about $0.1212 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/domain_analytics/whois/overview/live.json`](../../../../../../../catalog/models/dataforseo/v3/domain_analytics/whois/overview/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/domain_analytics/whois/overview/live
