# Trade Company Search API: pricing, parameters and code examples

`tendata/company/search` · data API · Tendata · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0 per run, depending on parameters · **Modes:** async

Fuzzy-match a company name to trade company IDs, optionally filtered by ISO3 country code, for use in other customs trade queries.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0 |

Formula: `0`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tendata/company/search", "name": "apple", "pageNo": 1, "pageSize": 3}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tendata/company/search', {'name': 'apple', 'pageNo': 1, 'pageSize': 3})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tendata/company/search", {
  "name": "apple",
  "pageNo": 1,
  "pageSize": 3
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tendata/company/search", sandbase.Params{
	"name": "apple",
	"pageNo": 1,
	"pageSize": 3,
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/tendata/company/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | Company name keyword to match.  |
| `pageNo` | integer | yes | Page number, starting at 1. range 1–9007199254740991 |
| `pageSize` | integer | yes | Rows per page (1-20). Each returned row is billed, so this caps the cost of one call. range 1–20 |
| `countryCodes` | string |  | ISO3 country code(s), comma-separated (e.g. 'USA,TUR,ECU').  |

## Details

Fuzzy-match a company name to trade company IDs, optionally filtered by ISO3 country code, for use in other customs trade queries.

---
Machine-readable: [`catalog/models/tendata/company/search.json`](../../../../catalog/models/tendata/company/search.json) · Store page: https://www.sandbase.ai/model/tendata/company/search
