# DataForSEO Backlinks Bulk Spam Score API: pricing, parameters and code examples

`dataforseo/v3/backlinks/bulk_spam_score/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024072 per call · **Modes:** sync

Backlink spam scores for up to 1,000 domains, subdomains or pages.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024072**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/backlinks/bulk_spam_score/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/backlinks/bulk_spam_score/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/backlinks/bulk_spam_score/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/backlinks/bulk_spam_score/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/backlinks/bulk_spam_score/live` with the body above minus `model`.

## Details

Backlink spam scores for up to 1,000 domains, subdomains or pages.

Request fields follow the official DataForSEO `/v3/backlinks/bulk_spam_score/live` task schema (one task per call). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/backlinks/bulk_spam_score/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"targets": ["nike.com", "adidas.com"]}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint. Main fields:

| Name | Description |
|---|---|
| `targets` | Array of domains, subdomains or page URLs (up to 1,000). |

### Reference

- Official docs: https://docs.dataforseo.com/v3/backlinks/bulk_spam_score/live/

### Pricing

Billed at the actual cost of each call, about $0.024072 for the request above. The cost grows with the number of rows, targets or tokens a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

---
Machine-readable: [`catalog/models/dataforseo/v3/backlinks/bulk_spam_score/live.json`](../../../../../../catalog/models/dataforseo/v3/backlinks/bulk_spam_score/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/backlinks/bulk_spam_score/live
