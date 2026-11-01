# DataForSEO Backlinks History

`dataforseo/v3/backlinks/history/live` · api · DataForSEO

Monthly history of backlinks, referring domains and rank for a domain since 2019.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024324**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/history/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/history/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/history/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/history/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/history/live` with the body above minus `model`.

## Details

Monthly history of backlinks, referring domains and rank for a domain since 2019.

Request fields follow the official DataForSEO `/v3/backlinks/history/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/history/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target": "nike.com", "date_from": "2026-01-01"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `target` | Domain, e.g. "nike.com". |
| `date_from` | Optional start date, "yyyy-mm-dd". |
| `date_to` | Optional end date, "yyyy-mm-dd". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/backlinks/history/live/

### Pricing

Billed at the actual cost of each call, about $0.024324 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/history/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/history/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/history/live
