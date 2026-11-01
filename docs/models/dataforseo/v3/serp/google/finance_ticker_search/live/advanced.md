# DataForSEO Google Finance Ticker Search

`dataforseo/v3/serp/google/finance_ticker_search/live/advanced` · api · DataForSEO

Resolve a company or instrument name to Google Finance tickers. Google Finance search for a company or instrument name.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/finance_ticker_search/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/finance_ticker_search/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/finance_ticker_search/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/finance_ticker_search/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/finance_ticker_search/live/advanced` with the body above minus `model`.

## Details

Resolve a company or instrument name to Google Finance tickers.

Request fields follow the official DataForSEO `/v3/serp/google/finance_ticker_search/live/advanced` task schema (one task per call; send `{"tasks": [...]}` for several). The response is DataForSEO's original JSON; results are in `tasks[].result`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/finance_ticker_search/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "apple", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Reference

- Official docs: https://docs.dataforseo.com/v3/serp/google/finance_ticker_search/live/advanced/

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/finance_ticker_search/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/finance_ticker_search/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/finance_ticker_search/live/advanced
