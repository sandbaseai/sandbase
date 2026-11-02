# Similarweb Audience Overlap API: pricing, parameters and code examples

`similarweb/audience-overlap` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Compare the audiences of up to 5 websites: unique visitors per site, overlapping visitors and the combined audience.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.15 * Math.max(1.0, Math.min(5.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/audience-overlap", "domains": "cnn.com,bbc.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/audience-overlap', {'domains': 'cnn.com,bbc.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/audience-overlap", {
  "domains": "cnn.com,bbc.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/audience-overlap", sandbase.Params{
	"domains": "cnn.com,bbc.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/audience-overlap` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `domains` | string | yes | domains  |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |

## Details

Compare the audiences of up to 5 websites: unique visitors per site, overlapping visitors and the combined audience.

The response is the official Similarweb API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/audience-overlap" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domains": "cnn.com,bbc.com", "granularity": "monthly"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `domains` | string | Yes | domains |
| `end_date` | string | Yes | end_date |
| `granularity` | string | No | granularity |
| `start_date` | string | Yes | start_date |

### Pricing

$0.15 per returned row (2 Similarweb credits), up to 5 rows; billed on rows returned. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/audience-overlap.json`](../../../catalog/models/similarweb/audience-overlap.json) · Store page: https://www.sandbase.ai/model/similarweb/audience-overlap
