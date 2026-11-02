# DataForSEO Backlinks Referring Networks API: pricing, parameters and code examples

`dataforseo/v3/backlinks/referring_networks/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.02436 per call · **Modes:** sync

Referring IP addresses or subnets pointing to a target, with backlink counts per network.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.02436**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/referring_networks/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/referring_networks/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/referring_networks/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/referring_networks/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/referring_networks/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of networks to return.  |
| `target` | string |  | Domain, subdomain or page URL.  |
| `network_address_type` | string |  | Optional: "ip" or "subnet" (default "ip").  |

## Details

Referring IP addresses or subnets pointing to a target, with backlink counts per network.

Request fields follow the official DataForSEO `/v3/backlinks/referring_networks/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/referring_networks/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "limit": 10}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `target` | Domain, subdomain or page URL. |
| `network_address_type` | Optional: "ip" or "subnet" (default "ip"). |
| `limit` | Maximum number of networks to return. |

### Reference

- Official docs: https://docs.dataforseo.com/v3/backlinks/referring_networks/live/

### Pricing

Billed at the actual cost of each call, about $0.02436 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/referring_networks/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/referring_networks/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/referring_networks/live
